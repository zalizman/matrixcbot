from matrixcbot.core import simple_spread_filter


def test_simple_spread_filter():
    assert simple_spread_filter(1.1000, 1.1002, 0.0003) is True
    assert simple_spread_filter(1.1000, 1.1005, 0.0003) is False
