# -*- coding: utf-8 -*-

'''Holiday information for Brazil.'''

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from datetime import date, timedelta
from dateutil import easter


def _carnival(easter):
    return easter - timedelta(days=47)


def get_holidays(year, place=['Brazil', None, None], scope='legal', _=str):
    """Returns Brazilian holiday dates. Election dates are also considered
    holidays and they always happen on Sundays.
    """
    adict = {
        date(year,  1,  1): 'Confraternização Universal',
        date(year,  4, 21): 'Tiradentes',
        date(year,  5,  1): 'Dia do trabalhador',
        date(year,  9,  7): 'Dia da Independência',
        date(year, 10, 12): 'Nossa Senhora Aparecida',
        date(year, 11,  2): 'Finados',
        date(year, 11, 15): 'Proclamação da República',
        date(year, 12, 25): 'Natal',
        }  # These are the *national* holidays.

    if place[1] in ('SP', 'São Paulo'):  # State of São Paulo
        adict[date(year, 7, 9)] = 'Revolução Constitucionalista de 1932'

    if place[2] == 'São Paulo':  # City of São Paulo
        eastr = easter.easter(year)
        adict[date(year, 1, 25)] = 'Aniversário da Cidade de São Paulo'
        adict[_carnival(eastr)] = 'Carnaval'
        adict[date(year, 11, 20)] = 'Dia da Consciência Negra'
        adict[eastr - timedelta(days=2)] = 'Sexta-feira da Paixão'
        adict[eastr] = 'Páscoa'
        adict[eastr + timedelta(days=60)] = 'Corpus Christi'
    return adict  # What? You don't celebrate Villa-Lobos' birthday???


if __name__ == "__main__":
    from pprint import pprint
    pprint(get_holidays(2014, place=['Brazil', 'SP', 'São Paulo']))
