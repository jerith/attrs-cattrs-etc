import yaml

import import_ipynb
from part_4b_nested_config_validated import Config

def parse_config():
    cfg = yaml.safe_load(open("part_4_example_config.yaml"))
    return Config(**cfg)

parse_config()

#########
# build sources

from part_4b_nested_config_validated import SOURCE_MAP

def dict_to_source(src):
    cls = SOURCE_MAP[src.pop("type")]
    return cls(**src)

def parse_config():
    cfg = yaml.safe_load(open("part_4_example_config.yaml"))
    cfg["sources"] = [dict_to_source(src) for src in cfg["sources"]]
    return Config(**cfg)

parse_config()

#########
# build source fields

from part_4b_nested_config_validated import ArchivePath, HelmChartReleaseVars

def dict_to_source(src):
    src_type = src.pop("type")
    cls = SOURCE_MAP[src_type]
    if src_type == "archive":
        if "paths" in src:
            src["paths"] = [ArchivePath(**path) for path in src["paths"]]
    elif src_type == "chart":
        if "releasevars" in src:
            src["releasevars"] = HelmChartReleaseVars(**src["releasevars"])
    return cls(**src)

def parse_config():
    cfg = yaml.safe_load(open("part_4_example_config.yaml"))
    cfg["sources"] = [dict_to_source(src) for src in cfg["sources"]]
    return Config(**cfg)

parse_config()

#########
# pretty

import attr

attr.asdict(parse_config())
