# -*- coding: utf-8 -*-

'''Holiday information for Poland. Adapted from
https://gist.github.com/sebzur/1810707
'''

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from datetime import date, timedelta
from dateutil import easter
from dateutil.relativedelta import relativedelta, SU, TH


def get_holidays(year, place=['Poland', None, None], scope='legal', _=str):
    """Returns Polish holiday dates (legally considered non-working days)."""
    easter_sunday = easter.easter(year)
    return {
        date(year, 1, 1): _('New Year'),
        date(year, 1, 6): _('Trzech Kroli'),
        easter_sunday: _('Easter Sunday'),
        easter_sunday + timedelta(days=1): _('Easter Monday'),
        date(year, 5, 1): _('Labor Day'),
        date(year, 5, 3): _('Constitution Day'),
        # 7th Sunday after Easter
        # (notice days+1 - this is 7th Sunday excluding Easter Sunday
        easter_sunday + relativedelta(days=+1, weekday=SU(+7)):
        _('Pentecost Sunday'),
        # 9th Thursday after Easter
        easter_sunday + relativedelta(weekday=TH(+9)):
        _('Corpus Christi'),
        date(year, 8, 15): _('Assumption of the Blessed Virgin Mary'),
        date(year, 11, 1): _("All Saints' Day"),
        date(year, 11, 11): _('Independence Day'),
        date(year, 12, 25): _('Christmas Day'),
        date(year, 12, 26): _('Boxing Day'),
        }  # What the hell, you don't celebrate Chopin's birthday???


if __name__ == "__main__":
    from pprint import pprint
    pprint(get_holidays(2014))
