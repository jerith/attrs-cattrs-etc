import cattr
import yaml

import import_ipynb
from part_4_nested_config import Config

def parse_config():
    cfg = yaml.safe_load(open("part_4_example_config.yaml"))
    return cattr.structure(cfg, Config)

parse_config()

#########
# hooks

from part_4_nested_config import SOURCE_MAP, Source

def structure_source(src, _type):
    cls = SOURCE_MAP[src.pop("type")]
    return cattr.structure(src, cls)

def parse_config():
    cfg = yaml.safe_load(open("part_4_example_config.yaml"))
    conv = cattr.Converter()
    conv.register_structure_hook(Source, structure_source)
    return conv.structure(cfg, Config)

parse_config()

#########
# autodetection by field

def parse_config():
    cfg = yaml.safe_load(open("part_4_example_config.yaml"))
    for src in cfg["sources"]:
        src.pop("type")
    return cattr.structure(cfg, Config)

parse_config()

#########
# pretty

import attr

attr.asdict(parse_config())
