import pytest

from gendiff.logic_gendiff import gen_diff


@pytest.fixture
def test_result():
    return """{
  - Alex: Neishchenko
  - check: null
    follow: false
  - foo: bar
    host: hexlet.io
    proxy: 123.234.53.22
    setting1: Value 1
  + setting2: 200
  - setting3: null
  + setting3: true
  - setting4: blah blah
    timeout: 50
}"""


def test_logic_gendiff(test_result):
    assert gen_diff('tests/files/file1.json', 'tests/files/file2.json') == test_result
















