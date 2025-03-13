
import pytest

from gendiff.logic_gendiff import generate_diff


@pytest.fixture
def expected_result():
    return """
Property 'Alex' was removed
Property 'check' was removed
Property 'foo' was removed
Property 'setting2' was added with value: 200
Property 'setting3' was updated. From null to true
Property 'setting4' was removed
"""


def test_generate_diff_with_plain(expected_result):
    
    assert generate_diff('tests/fixtures/file1.json',
                        'tests/fixtures/file2.json', 'plain').strip() == expected_result.strip()


