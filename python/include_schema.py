# Auto generated from include_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-09 18:01
# Schema: include_schema
#
# id: https://w3id.org/include_schema
# description: INCLUDE Schema prototype
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
from . include_core import NamedThing, NamedThingId
from linkml.utils.metamodelcore import XSDDate
from linkml_model.types import Date, Integer, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
INCLUDE_SCHEMA = CurieNamespace('include_schema', 'https://w3id.org/mixs/include_schema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = INCLUDE_SCHEMA


# Types

# Class references
class PersonId(NamedThingId):
    pass


class SubjectId(PersonId):
    pass


class SampleId(NamedThingId):
    pass


class VisitId(NamedThingId):
    pass


@dataclass
class Person(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE_SCHEMA.Person
    class_class_curie: ClassVar[str] = "include_schema:Person"
    class_name: ClassVar[str] = "person"
    class_model_uri: ClassVar[URIRef] = INCLUDE_SCHEMA.Person

    id: Union[str, PersonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Subject(Person):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE_SCHEMA.Subject
    class_class_curie: ClassVar[str] = "include_schema:Subject"
    class_name: ClassVar[str] = "subject"
    class_model_uri: ClassVar[URIRef] = INCLUDE_SCHEMA.Subject

    id: Union[str, SubjectId] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    dob: Optional[Union[str, XSDDate]] = None
    birth_month: Optional[int] = None
    birth_year: Optional[int] = None
    birth_city: Optional[str] = None
    birth_country: Optional[str] = None
    sex: Optional[Union[str, "GenderEnum"]] = None
    race: Optional[Union[str, "RaceEnum"]] = None
    ethnicity: Optional[Union[str, "EthnicityEnum"]] = None
    handedness: Optional[Union[str, "HandednessEnum"]] = None
    primary_language: Optional[Union[str, "LanguageEnum"]] = None
    other_language: Optional[Union[str, "LanguageEnum"]] = None
    residence: Optional[Union[str, "ResidenceEnum"]] = None
    age_of_mother_at_birth: Optional[int] = None
    age_of_father_at_birth: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SubjectId):
            self.id = SubjectId(self.id)

        if self.first_name is not None and not isinstance(self.first_name, str):
            self.first_name = str(self.first_name)

        if self.middle_name is not None and not isinstance(self.middle_name, str):
            self.middle_name = str(self.middle_name)

        if self.last_name is not None and not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

        if self.dob is not None and not isinstance(self.dob, XSDDate):
            self.dob = XSDDate(self.dob)

        if self.birth_month is not None and not isinstance(self.birth_month, int):
            self.birth_month = int(self.birth_month)

        if self.birth_year is not None and not isinstance(self.birth_year, int):
            self.birth_year = int(self.birth_year)

        if self.birth_city is not None and not isinstance(self.birth_city, str):
            self.birth_city = str(self.birth_city)

        if self.birth_country is not None and not isinstance(self.birth_country, str):
            self.birth_country = str(self.birth_country)

        if self.sex is not None and not isinstance(self.sex, GenderEnum):
            self.sex = GenderEnum(self.sex)

        if self.race is not None and not isinstance(self.race, RaceEnum):
            self.race = RaceEnum(self.race)

        if self.ethnicity is not None and not isinstance(self.ethnicity, EthnicityEnum):
            self.ethnicity = EthnicityEnum(self.ethnicity)

        if self.handedness is not None and not isinstance(self.handedness, HandednessEnum):
            self.handedness = HandednessEnum(self.handedness)

        if self.primary_language is not None and not isinstance(self.primary_language, LanguageEnum):
            self.primary_language = LanguageEnum(self.primary_language)

        if self.other_language is not None and not isinstance(self.other_language, LanguageEnum):
            self.other_language = LanguageEnum(self.other_language)

        if self.residence is not None and not isinstance(self.residence, ResidenceEnum):
            self.residence = ResidenceEnum(self.residence)

        if self.age_of_mother_at_birth is not None and not isinstance(self.age_of_mother_at_birth, int):
            self.age_of_mother_at_birth = int(self.age_of_mother_at_birth)

        if self.age_of_father_at_birth is not None and not isinstance(self.age_of_father_at_birth, int):
            self.age_of_father_at_birth = int(self.age_of_father_at_birth)

        super().__post_init__(**kwargs)


@dataclass
class Sample(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE_SCHEMA.Sample
    class_class_curie: ClassVar[str] = "include_schema:Sample"
    class_name: ClassVar[str] = "sample"
    class_model_uri: ClassVar[URIRef] = INCLUDE_SCHEMA.Sample

    id: Union[str, SampleId] = None
    subject: Union[str, SubjectId] = None
    sample_date: Optional[Union[str, XSDDate]] = None
    parent_sample: Optional[Union[str, SampleId]] = None
    sample_type: Optional[Union[str, "SampleEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SubjectId):
            self.subject = SubjectId(self.subject)

        if self.sample_date is not None and not isinstance(self.sample_date, XSDDate):
            self.sample_date = XSDDate(self.sample_date)

        if self.parent_sample is not None and not isinstance(self.parent_sample, SampleId):
            self.parent_sample = SampleId(self.parent_sample)

        if self.sample_type is not None and not isinstance(self.sample_type, SampleEnum):
            self.sample_type = SampleEnum(self.sample_type)

        super().__post_init__(**kwargs)


@dataclass
class Visit(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE_SCHEMA.Visit
    class_class_curie: ClassVar[str] = "include_schema:Visit"
    class_name: ClassVar[str] = "visit"
    class_model_uri: ClassVar[URIRef] = INCLUDE_SCHEMA.Visit

    id: Union[str, VisitId] = None
    subject: Union[str, SubjectId] = None
    sample: Optional[Union[str, List[str]]] = empty_list()
    visit_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VisitId):
            self.id = VisitId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SubjectId):
            self.subject = SubjectId(self.subject)

        if self.sample is None:
            self.sample = []
        if not isinstance(self.sample, list):
            self.sample = [self.sample]
        self.sample = [v if isinstance(v, str) else str(v) for v in self.sample]

        if self.visit_date is not None and not isinstance(self.visit_date, XSDDate):
            self.visit_date = XSDDate(self.visit_date)

        super().__post_init__(**kwargs)


# Enumerations
class GenderEnum(EnumDefinitionImpl):
    """
    Gender of something
    """
    _defn = EnumDefinition(
        name="GenderEnum",
        description="Gender of something",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 description="Male gender") )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 description="Female gender") )
        setattr(cls, "8",
                PermissibleValue(text="8",
                                 description="Nonbinary gender") )

class RaceEnum(EnumDefinitionImpl):
    """
    Race of something
    """
    _defn = EnumDefinition(
        name="RaceEnum",
        description="Race of something",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 description="American Indian or Alaska Native") )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 description="Asian") )
        setattr(cls, "2",
                PermissibleValue(text="2",
                                 description="Black or African-American") )
        setattr(cls, "3",
                PermissibleValue(text="3",
                                 description="Native Hawaiian or Other Pacific Islander") )
        setattr(cls, "4",
                PermissibleValue(text="4",
                                 description="White") )
        setattr(cls, "5",
                PermissibleValue(text="5",
                                 description="More than one race") )
        setattr(cls, "6",
                PermissibleValue(text="6",
                                 description="Other") )
        setattr(cls, "7",
                PermissibleValue(text="7",
                                 description="Decline to answer") )

class EthnicityEnum(EnumDefinitionImpl):
    """
    Ethnicity of something
    """
    _defn = EnumDefinition(
        name="EthnicityEnum",
        description="Ethnicity of something",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 description="Hispanic or latino") )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 description="Not Hispanic or Latino") )
        setattr(cls, "2",
                PermissibleValue(text="2",
                                 description="Unsure") )
        setattr(cls, "3",
                PermissibleValue(text="3",
                                 description="Decline to answer") )

class HandednessEnum(EnumDefinitionImpl):
    """
    Side of dominant hand of a person
    """
    _defn = EnumDefinition(
        name="HandednessEnum",
        description="Side of dominant hand of a person",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 description="Right handed") )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 description="Left handed") )
        setattr(cls, "2",
                PermissibleValue(text="2",
                                 description="Ambidextrous") )

class LanguageEnum(EnumDefinitionImpl):
    """
    Human language
    """
    _defn = EnumDefinition(
        name="LanguageEnum",
        description="Human language",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 description="English") )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 description="Spanish") )
        setattr(cls, "2",
                PermissibleValue(text="2",
                                 description="Other") )

class ResidenceEnum(EnumDefinitionImpl):
    """
    A living arrangement
    """
    _defn = EnumDefinition(
        name="ResidenceEnum",
        description="A living arrangement",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 description="With family/caregiver") )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 description="Group home") )
        setattr(cls, "2",
                PermissibleValue(text="2",
                                 description="Independent living") )
        setattr(cls, "3",
                PermissibleValue(text="3",
                                 description="Facility") )

class SampleEnum(EnumDefinitionImpl):
    """
    Type of material sample
    """
    _defn = EnumDefinition(
        name="SampleEnum",
        description="Type of material sample",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 description="Blood") )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 description="Urine") )
        setattr(cls, "2",
                PermissibleValue(text="2",
                                 description="Stool") )

# Slots
class slots:
    pass

slots.name = Slot(uri=INCLUDE_SCHEMA.name, name="name", curie=INCLUDE_SCHEMA.curie('name'),
                   model_uri=INCLUDE_SCHEMA.name, domain=None, range=Optional[str])

slots.first_name = Slot(uri=INCLUDE_SCHEMA.first_name, name="first name", curie=INCLUDE_SCHEMA.curie('first_name'),
                   model_uri=INCLUDE_SCHEMA.first_name, domain=None, range=Optional[str])

slots.middle_name = Slot(uri=INCLUDE_SCHEMA.middle_name, name="middle name", curie=INCLUDE_SCHEMA.curie('middle_name'),
                   model_uri=INCLUDE_SCHEMA.middle_name, domain=None, range=Optional[str])

slots.last_name = Slot(uri=INCLUDE_SCHEMA.last_name, name="last name", curie=INCLUDE_SCHEMA.curie('last_name'),
                   model_uri=INCLUDE_SCHEMA.last_name, domain=None, range=Optional[str])

slots.dob = Slot(uri=INCLUDE_SCHEMA.dob, name="dob", curie=INCLUDE_SCHEMA.curie('dob'),
                   model_uri=INCLUDE_SCHEMA.dob, domain=None, range=Optional[Union[str, XSDDate]])

slots.birth_month = Slot(uri=INCLUDE_SCHEMA.birth_month, name="birth month", curie=INCLUDE_SCHEMA.curie('birth_month'),
                   model_uri=INCLUDE_SCHEMA.birth_month, domain=None, range=Optional[int])

slots.birth_year = Slot(uri=INCLUDE_SCHEMA.birth_year, name="birth year", curie=INCLUDE_SCHEMA.curie('birth_year'),
                   model_uri=INCLUDE_SCHEMA.birth_year, domain=None, range=Optional[int])

slots.birth_city = Slot(uri=INCLUDE_SCHEMA.birth_city, name="birth city", curie=INCLUDE_SCHEMA.curie('birth_city'),
                   model_uri=INCLUDE_SCHEMA.birth_city, domain=None, range=Optional[str])

slots.birth_country = Slot(uri=INCLUDE_SCHEMA.birth_country, name="birth country", curie=INCLUDE_SCHEMA.curie('birth_country'),
                   model_uri=INCLUDE_SCHEMA.birth_country, domain=None, range=Optional[str])

slots.sex = Slot(uri=INCLUDE_SCHEMA.sex, name="sex", curie=INCLUDE_SCHEMA.curie('sex'),
                   model_uri=INCLUDE_SCHEMA.sex, domain=None, range=Optional[Union[str, "GenderEnum"]])

slots.race = Slot(uri=INCLUDE_SCHEMA.race, name="race", curie=INCLUDE_SCHEMA.curie('race'),
                   model_uri=INCLUDE_SCHEMA.race, domain=None, range=Optional[Union[str, "RaceEnum"]])

slots.ethnicity = Slot(uri=INCLUDE_SCHEMA.ethnicity, name="ethnicity", curie=INCLUDE_SCHEMA.curie('ethnicity'),
                   model_uri=INCLUDE_SCHEMA.ethnicity, domain=None, range=Optional[Union[str, "EthnicityEnum"]])

slots.handedness = Slot(uri=INCLUDE_SCHEMA.handedness, name="handedness", curie=INCLUDE_SCHEMA.curie('handedness'),
                   model_uri=INCLUDE_SCHEMA.handedness, domain=None, range=Optional[Union[str, "HandednessEnum"]])

slots.primary_language = Slot(uri=INCLUDE_SCHEMA.primary_language, name="primary language", curie=INCLUDE_SCHEMA.curie('primary_language'),
                   model_uri=INCLUDE_SCHEMA.primary_language, domain=None, range=Optional[Union[str, "LanguageEnum"]])

slots.other_language = Slot(uri=INCLUDE_SCHEMA.other_language, name="other language", curie=INCLUDE_SCHEMA.curie('other_language'),
                   model_uri=INCLUDE_SCHEMA.other_language, domain=None, range=Optional[Union[str, "LanguageEnum"]])

slots.residence = Slot(uri=INCLUDE_SCHEMA.residence, name="residence", curie=INCLUDE_SCHEMA.curie('residence'),
                   model_uri=INCLUDE_SCHEMA.residence, domain=None, range=Optional[Union[str, "ResidenceEnum"]])

slots.age_of_mother_at_birth = Slot(uri=INCLUDE_SCHEMA.age_of_mother_at_birth, name="age of mother at birth", curie=INCLUDE_SCHEMA.curie('age_of_mother_at_birth'),
                   model_uri=INCLUDE_SCHEMA.age_of_mother_at_birth, domain=None, range=Optional[int])

slots.age_of_father_at_birth = Slot(uri=INCLUDE_SCHEMA.age_of_father_at_birth, name="age of father at birth", curie=INCLUDE_SCHEMA.curie('age_of_father_at_birth'),
                   model_uri=INCLUDE_SCHEMA.age_of_father_at_birth, domain=None, range=Optional[int])

slots.sample = Slot(uri=INCLUDE_SCHEMA.sample, name="sample", curie=INCLUDE_SCHEMA.curie('sample'),
                   model_uri=INCLUDE_SCHEMA.sample, domain=None, range=Optional[Union[str, List[str]]])

slots.subject = Slot(uri=INCLUDE_SCHEMA.subject, name="subject", curie=INCLUDE_SCHEMA.curie('subject'),
                   model_uri=INCLUDE_SCHEMA.subject, domain=None, range=Optional[Union[str, SubjectId]])

slots.sample_date = Slot(uri=INCLUDE_SCHEMA.sample_date, name="sample date", curie=INCLUDE_SCHEMA.curie('sample_date'),
                   model_uri=INCLUDE_SCHEMA.sample_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.visit_date = Slot(uri=INCLUDE_SCHEMA.visit_date, name="visit date", curie=INCLUDE_SCHEMA.curie('visit_date'),
                   model_uri=INCLUDE_SCHEMA.visit_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.parent_sample = Slot(uri=INCLUDE_SCHEMA.parent_sample, name="parent sample", curie=INCLUDE_SCHEMA.curie('parent_sample'),
                   model_uri=INCLUDE_SCHEMA.parent_sample, domain=None, range=Optional[Union[str, SampleId]])

slots.sample_type = Slot(uri=INCLUDE_SCHEMA.sample_type, name="sample type", curie=INCLUDE_SCHEMA.curie('sample_type'),
                   model_uri=INCLUDE_SCHEMA.sample_type, domain=None, range=Optional[Union[str, "SampleEnum"]])

slots.sample_subject = Slot(uri=INCLUDE_SCHEMA.subject, name="sample_subject", curie=INCLUDE_SCHEMA.curie('subject'),
                   model_uri=INCLUDE_SCHEMA.sample_subject, domain=Sample, range=Union[str, SubjectId])

slots.visit_subject = Slot(uri=INCLUDE_SCHEMA.subject, name="visit_subject", curie=INCLUDE_SCHEMA.curie('subject'),
                   model_uri=INCLUDE_SCHEMA.visit_subject, domain=Visit, range=Union[str, SubjectId])
