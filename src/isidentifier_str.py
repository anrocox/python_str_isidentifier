#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 15, 2014

@author: anroco

How to check if a string is a valid identifier in python?

¿Como determinar si un string es un identificador valido en python?
'''

#create a str
s = 'name_field'
print(s)

#verify if the string is a valid identifier according to the language
#definition. Return True or False. The uppercase and lowercase letters A
#through Z, the underscore _ and, except for the first character, the digits
#0 through 9.
#
#https://docs.python.org/3/reference/lexical_analysis.html#identifiers
#PEP-3131 -> http://legacy.python.org/dev/peps/pep-3131/
#
print(s.isidentifier())

#create a str
s = 'name field'
print(s)

#whitespace is not valid as identifier in python.
print(s.isidentifier())

#create a str
s = '1_name_field'
print(s)

#A digit can not start the identifier in python
print(s.isidentifier())
