"""
This module provides a python data structure that handles the comments on
tables and rows.
"""

from typing import Iterable, Mapping, TypeVar

JSON = TypeVar('JSON', str, int, Iterable['JSON'], Mapping[str, 'JSON'])

class TableComment:
    def __init__(self, name: str, source: str, collection_date, orig_file: str,
                 spat_resolution: Iterable[str],
                 fields: Iterable[FieldDescription], licence: str,
                 proper_use: Iterable[str], description: str=""):
        self.name = name
        self.source = source
        self.collection_data = collection_date
        self.orig_file = orig_file
        self.spat_resolution = spat_resolution
        self.fields = list(fields)
        self.licence = licence
        self.proper_use = proper_use
        self.description = description

class FieldDescription:
    def __init__(self, name, description, unit=None):
        self.name = name
        self.description = description
        self.unit = unit

class RowComment:
    """
    This class handles the basic cell comments in conformance to
    http://wiki.openmod-initiative.org/wiki/DatabaseRules#Comments_on_Rows

    Attributes
        origin: str
            Describes the actual source the data of this row comes from
        method: str
            Describes the method that was used to generate the data in this row
        assumption: list of Assumption
            Specifies the assumptions that were made to achieve a full
            non-redundant row of data
    """

    def __init__(self, origin: str, method: str,
                 assumptions: Iterable[Assumption] = None):
        self.origin = origin
        self.method = method
        self.assumptions = list(assumptions) if assumptions else []


class Assumption:
    """
    Handler for multiplicity assumptions.

    These may be used, if a simulation or calculation resulted in several
    possible value.

    Attributes:
        type: str
            Stores the type of assumption e.g. gap or multiplicity
        begin: str
            Name of the first column the assumption concerns
        end: str
            Name of the last column the assumption concerns
        solution: str
            Description of the solution to create the final data
    """

    def __init__(self, assumption_type: str, begin: str, end: str,
                 solution: str):
        self.type = assumption_type
        self.begin = begin
        self.end = end
        self.solution = solution

    def to_json(self):
        """
        Translates the assumption to a json string that can be stored in the
        oedb
        :return: JSON string
        """
        return {'type': self.type,
                'begin': self.begin,
                'end': self.end,
                'solution': self.solution}


class Multiplicity(Assumption):
    """
    Handler for multiplicity assumptions. These may be used, if a simulation
    or calculation resulted in several possible value.

    Attributes:
        values: A dictionary that maps column names to the corresponding possible
    """

    def __init__(self, begin: int, end: int, solution: str,
                 values: Mapping[str, JSON]):
        super(Multiplicity, self).__init__('multiplicity', begin, end, solution)
        self.values = dict(values)

    def to_json(self):
        dic = super(Multiplicity, self).to_json()
        dic['values'] = self.values
        return dic
