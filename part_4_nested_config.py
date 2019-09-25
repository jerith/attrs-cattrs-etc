from typing import Dict, List, Optional, Union

import attr


@attr.s(frozen=True)
class SourceBase:
    "Base class: ad-hoc interface and some common behaviour."

    name: str = attr.ib()
    # We strip the type field out of the source dict during parsing. This
    # attrib puts it back during serialization so we can read what we wrote.
    type: str = attr.ib(init=False)

    @type.default
    def _type_default(self):
        return self._source_type

    _logger = None

    @property
    def displayname(self):
        return f"{self._source_type}:{self.name}"

    @property
    def logger(self):
        if self._logger is None:
            # Because we (and all our subclasses) are frozen, we need to cheat.
            logger = _sources_logger.child(self.displayname)
            object.__setattr__(self, "_logger", logger)
        return self._logger

    async def fetch(self, dest_dir):
        raise NotImplementedError()


@attr.s(frozen=True)
class Manifest(SourceBase):
    "Fetch a file that is assumed to contain YAML."

    _source_type = "manifest"

    url: str = attr.ib()

    async def fetch(self, dest_dir):
        pass


@attr.s(frozen=True)
class HelmChartReleaseVars:
    "Things helm wnats that aren't template variables."

    name: Optional[str] = attr.ib(default=None)
    namespace: Optional[str] = attr.ib(default=None)

    def helm_template_args(self) -> List[str]:
        pass


@attr.s(frozen=True)
class HelmChart(SourceBase):
    "Fetch a helm chart and render it to a single YAML file."

    _source_type = "chart"

    repo: str = attr.ib()
    version: str = attr.ib()
    templatevars: Dict[str, str] = attr.ib(factory=dict)
    releasevars: HelmChartReleaseVars = attr.ib(factory=HelmChartReleaseVars)

    async def fetch(self, dest_dir):
        pass


@attr.s(frozen=True)
class ArchivePath:
    "Complicated path glob matcher."

    path: str = attr.ib()
    dest: str = attr.ib(default="")

    @path.validator
    def _path_validator(self, attribute, value):
        for seg in value.split("/")[:-1]:
            if seg == "**":
                raise ValueError("** may only appear at the end of a path")

    def match(self, path) -> Optional[str]:
        pass


@attr.s(frozen=True)
class Archive(SourceBase):
    "Fetch an archive and extracts a subset of the files within it."

    _source_type = "archive"

    url: str = attr.ib()
    paths: List[ArchivePath] = attr.ib(factory=list)

    async def fetch(self, dest_dir):
        pass


SOURCE_MAP = {"chart": HelmChart, "manifest": Manifest, "archive": Archive}

Source = Union[HelmChart, Manifest, Archive]


@attr.s(frozen=True)
class Config:
    "Structured config object parsed populated from YAML file."

    sources: List[Source] = attr.ib()
