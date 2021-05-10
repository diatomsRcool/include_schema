# Auto generated from include_core.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-09 18:01
# Schema: include_core
#
# id: https://w3id.org/include_core
# description: This is an example of an imported module
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml.utils.slot import Slot
from linkml.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml.utils.formatutils import camelcase, underscore, sfx
from linkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml.utils.curienamespace import CurieNamespace
from linkml_model.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
INCLUDE_CORE = CurieNamespace('include_core', 'https://w3id.org/mixs/include_core/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = INCLUDE_CORE


# Types

# Class references
class NamedThingId(extended_str):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    root class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE_CORE.NamedThing
    class_class_curie: ClassVar[str] = "include_core:NamedThing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = INCLUDE_CORE.NamedThing

    id: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=INCLUDE_CORE.id, name="id", curie=INCLUDE_CORE.curie('id'),
                   model_uri=INCLUDE_CORE.id, domain=None, range=URIRef)
