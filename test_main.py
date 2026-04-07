import main
import pytest


@pytest.mark.parametrize(
    ('input_x', 'input_y', 'expected'),
    (
        (0, 0, 1),
        (1, 0, 1),
        (0, 1, 1),
        (1, 1, 2)
    )
)
def test_foo(input_x, input_y, expected):
    assert main.foo(input_x, input_y) == expected


@pytest.mark.parametrize(
    ('input_u', 'input_v', 'answer'),
    (
        (0, 0, 0),
        (1, 0, 1),
        (0, 1, 1),
        (1, 1, 2)
    )
)
def test_bar(input_u, input_v, answer):
    assert main.bar(input_u, input_v) == answer
