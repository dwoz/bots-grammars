from bots.botsconfig import *
from records004051 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RO',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B1', MIN: 1, MAX: 1},
    {ID: 'Y6', MIN: 0, MAX: 2},
    {ID: 'Y5', MIN: 1, MAX: 1},
    {ID: 'V9', MIN: 0, MAX: 10},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
