import pytest

import roster


def test_fetch_semester_year():

    expected = 'AU26'
    setup = {'semester': 'AU26'}

    result = roster.fetch_semester_year(setup)

    assert expected == result

