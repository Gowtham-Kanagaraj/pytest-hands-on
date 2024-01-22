import square_root

def test_square():
    assert square_root.square(5) == 25


import pytest

@pytest.mark.parametrize(
    ('input_n', 'expected'),
    (
        (5, 25),
        (3, 9)
    )
)


def test_s(input_n, expected):
    assert square_root.square(input_n) == expected