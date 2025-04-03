import pytest

from gendiff.logic_gendiff import generate_diff


@pytest.fixture
def expected_result():
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


def test_logic_gendiff(expected_result):
    assert generate_diff('tests/fixtures/file1.json', 
                         'tests/fixtures/file2.json') == expected_result





















