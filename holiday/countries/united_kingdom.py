# -*- coding: utf-8 -*-

'''Holiday information for the United Kingdom. Adapted from
https://gist.github.com/chokosabe/5023154
'''

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from datetime import date, timedelta
from dateutil import easter
from dateutil.relativedelta import relativedelta, MO


def get_holidays(year, place=['United Kingdom', None, None], scope='legal',
                 _=str):
    """Returns UK holiday dates (legally considered non-working days)."""
    easter_sunday = easter.easter(year)
    return {
        date(year, 1, 1): _('New Year'),
        easter_sunday - timedelta(days=2): _('Good Friday'),
        easter_sunday: _('Easter Sunday'),
        easter_sunday + timedelta(days=1): _('Easter Monday'),
        date(year, 5, 1) + relativedelta(weekday=MO):
        _('Early May Bank Holiday'),  # First Monday of May
        date(year, 5, 31) + relativedelta(weekday=MO(-1)):
        _('Spring Bank Holiday'),  # Last Monday of May
        date(year, 8, 31) + relativedelta(weekday=MO(-1)):
        _('Summer Bank Holiday'),  # Last Monday of August
        date(year, 12, 25): _('Christmas Day'),
        date(year, 12, 26): _('Boxing Day'),
        }  # What the hell, you don't celebrate B. Britten's birthday???


if __name__ == "__main__":
    from pprint import pprint
    pprint(get_holidays(2014))
