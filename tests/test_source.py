from calculate.source import reverse_str


def test_should_reverse_string_with_digits():
    assert reverse_str('123') == '321'


def test_should_not_reverse_string():
    assert reverse_str('abc') == 'abc'
