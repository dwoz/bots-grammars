from bots.botsconfig import *
from records005010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'DI',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'N1', MIN: 1, MAX: 1},
    {ID: 'N2', MIN: 0, MAX: 99},
    {ID: 'N3', MIN: 0, MAX: 2},
    {ID: 'N4', MIN: 0, MAX: 1},
    {ID: 'DN', MIN: 0, MAX: 7},
    {ID: 'R9', MIN: 0, MAX: 50},
    {ID: 'DH', MIN: 0, MAX: 28},
    {ID: 'PER', MIN: 0, MAX: 1},
    {ID: 'K1', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
