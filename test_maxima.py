import numpy as np

from maxima import find_maxima

def test_simple_sequence_two_maxima():
    inp = [0, 1, 2, 1, 2, 1, 0]
    out = find_maxima(inp)
    exp = [2, 4]
    assert exp == out


def test_simple_sequence_one_maximum():
    inp = [-i**2 for i in range(-3, 4)]
    out = find_maxima(inp)
    exp = [3]
    assert exp == out


def test_sine_wave():
    inp = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    out = find_maxima(inp)
    exp = [16,78]
    assert exp == out


def test_max_on_both_borders():
    inp = [4, 2, 1, 3, 1, 2]
    out = find_maxima(inp)
    exp = [0,3,5]
    assert exp == out


def test_max_on_both_borders2():
    inp = [4, 2, 1, 3, 1, 5]
    out = find_maxima(inp)
    exp = [0,3,5]
    assert exp == out


def test_max_on_both_borders3():
    inp = [4, 2, 1, 3, 1]
    out = find_maxima(inp)
    exp = [0,3]
    assert exp == out


def test_saddle_plateau():
    inp = [1, 2, 2, 1]
    out = find_maxima(inp)
    exp = [1, 2]
    assert exp == out


def test_saddle_rise_right():
    inp = [1, 2, 2, 3, 1]
    out = find_maxima(inp)
    exp = [3]
    assert exp == out


def test_saddle_rise_left():
    inp = [1, 3, 2, 2, 1]
    out = find_maxima(inp)
    exp = [1]
    assert exp == out


def test_saddle_rise_both():
    inp = [3, 2, 2, 3]
    out = find_maxima(inp)
    exp = [0, 3]
    assert exp == out


def test_saddle_open_right():
    inp = [1, 2, 2, 2]
    out = find_maxima(inp)
    exp = [1, 2, 3]
    assert exp == out


def test_saddle_open_left():
    inp = [2, 2, 2, 1]
    out = find_maxima(inp)
    exp = [0, 1, 2]
    assert exp == out


def test_saddle_just_plateau():
    inp = [2, 2, 2, 2]
    out = find_maxima(inp)
    exp = [0, 1, 2, 3]
    assert exp == out

def test_saddle_two_plateaus():
    inp = [2, 2, 2, 1, 2, 2, 2]
    out = find_maxima(inp)
    exp = [0, 1, 2, 4, 5, 6]
    assert exp == out
# additional tests for
# - max on both borders
#   x = [4, 2, 1, 3, 1, 2]
# - max on both borders, absolute max on right border
#   x = [4, 2, 1, 3, 1, 5]
# - one max (absolute) on left border
#   x = [4, 2, 1, 3, 1]
# - plateau
#   x = [1, 2, 2, 1]
#   (decide for a sensible output in this case)
# - test cases for plateau
#   x = [1, 2, 2, 3, 1]
#   x = [1, 3, 2, 2, 1]
#   x = [3, 2, 2, 3]
