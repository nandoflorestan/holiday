# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from nine import basestring, str


def get_holidays(year, place, scope='legal', _=str):
    '''The ``place`` argument may be a sequence of 3 unicode strings
    (country, state, city), or a single unicode string separated by slashes:
    'Brazil/RJ/Rio de Janeiro'.
    '''
    if isinstance(place, basestring):
        place = [p.strip() for p in place.split('/')]
    if len(place) == 1:
        place.append(None)
    if len(place) == 2:
        place.append(None)
    assert len(place) == 3
    # Import the module for the country in question
    module_name = 'holiday.countries.' + place[0].lower().replace(' ', '_')
    try:
        module = __import__(module_name, fromlist=['holiday', 'countries'],
                            level=0)
    except ImportError:
        return None  # We don't know about the requested country
    # Call the get_holidays() function in that module
    return module.get_holidays(year, place, scope, _=_)
