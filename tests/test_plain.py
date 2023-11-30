import pytest
from gendiff import generate_diff


@pytest.mark.parametrize('file1, file2, file_res, form', [
    ('tests/fixtures/file3.json', 'tests/fixtures/file4.json',
     'tests/fixtures/plain.txt', 'PLAIN'),
    ('tests/fixtures/file3.yml', 'tests/fixtures/file4.yml',
     'tests/fixtures/plain.txt', 'PLAIN'),
    ('tests/fixtures/empty.json', 'tests/fixtures/file4.json',
     'tests/fixtures/half_plain.txt', 'PLAIN')
])
def test_diff(file1, file2, file_res, form):
    with open(file_res, 'r') as result:
        res = result.read()
    diff = generate_diff(file1, file2, form)
    assert diff == res
