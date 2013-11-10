holiday
~~~~~~~

Use this library (and please contribute to it) when your Python code needs to
know the holiday dates for certain years and parts of the world.

The code is hosted at https://github.com/nandoflorestan/holiday

The library is tested on Python 2.6, 2.7, 3.2 and 3.3.

For documentation on each module, please refer to its own docstrings.

This version was published with `releaser <https://pypi.python.org/pypi/releaser>`_.


The need for this library
=========================

Enumerating the holidays of a certain place and a certain year is not as simple
as one might think. Some holidays are fixed, others need to be calculated.
This kind of query also depends on some kind of scope -- for instance, the
stock and futures markets may have different holidays.

This library tries to take care of all that -- but it needs your help: please implement your location(s) and make a pull request!

This version only contains (incomplete) holiday information from:

* Brazil
* Poland
* United Kingdom


Getting started
===============


Installation
------------

    easy_install -UZ holiday


Usage
-----

Suppose you want to get the holidays for 2014 in the city of São Paulo,
state of São Paulo, Brazil. You would do this::

    from holiday import get_holidays
    adict = get_holidays(year=2013, place='Sri Lanka')
    assert adict is None  # We don't have information on Sri Lanka yet.

    adict = get_holidays(year=2014, place='Brazil/SP/São Paulo',
                         scope='legal')
    print(adict)

    {datetime.date(2014, 1, 1): 'Confraternização Universal',
     datetime.date(2014, 1, 25): 'Aniversário da Cidade de São Paulo',
     datetime.date(2014, 3, 4): 'Carnaval',
     datetime.date(2014, 4, 18): 'Sexta-feira da Paixão',
     datetime.date(2014, 4, 20): 'Páscoa',
     datetime.date(2014, 4, 21): 'Tiradentes',
     datetime.date(2014, 5, 1): 'Dia do trabalhador',
     datetime.date(2014, 6, 19): 'Corpus Christi',
     datetime.date(2014, 7, 9): 'Revolução Constitucionalista de 1932',
     datetime.date(2014, 9, 7): 'Dia da Independência',
     datetime.date(2014, 10, 12): 'Nossa Senhora Aparecida',
     datetime.date(2014, 11, 2): 'Finados',
     datetime.date(2014, 11, 15): 'Proclamação da República',
     datetime.date(2014, 11, 20): 'Dia da Consciência Negra',
     datetime.date(2014, 12, 25): 'Natal'}

We don't currently help calculations involving business days; maybe we should.
But many approaches are possible. See, for instance,
http://pandas.pydata.org/pandas-docs/stable/timeseries.html#custom-business-days-experimental
