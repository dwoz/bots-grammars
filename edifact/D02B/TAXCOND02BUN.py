#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD02BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 5},
    {ID: 'RFF', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'DOC', MIN: 1, MAX: 9, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'CNT', MIN: 1, MAX: 1},
            {ID: 'TAX', MIN: 1, MAX: 9, LEVEL: [
                {ID: 'MOA', MIN: 1, MAX: 3},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]
