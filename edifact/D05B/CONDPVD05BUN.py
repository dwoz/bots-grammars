#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD05BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'AUT', MIN: 0, MAX: 2},
    {ID: 'FTX', MIN: 0, MAX: 5},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 25},
        {ID: 'FII', MIN: 0, MAX: 5},
        {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
        {ID: 'DOC', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'CUX', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
    ]},
    {ID: 'IND', MIN: 0, MAX: 100, LEVEL: [
        {ID: 'RFF', MIN: 1, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'BII', MIN: 0, MAX: 1000, LEVEL: [
        {ID: 'RCS', MIN: 0, MAX: 1},
        {ID: 'PAI', MIN: 0, MAX: 1},
        {ID: 'PYT', MIN: 0, MAX: 1},
        {ID: 'APR', MIN: 0, MAX: 2, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
        {ID: 'ARD', MIN: 1, MAX: 100, LEVEL: [
            {ID: 'MOA', MIN: 1, MAX: 6},
            {ID: 'FTX', MIN: 0, MAX: 10},
            {ID: 'TAX', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 1},
                {ID: 'LOC', MIN: 0, MAX: 5},
            ]},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 20, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 25},
            {ID: 'FII', MIN: 0, MAX: 5},
            {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 5},
            ]},
            {ID: 'DOC', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 5},
            ]},
            {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 5},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]