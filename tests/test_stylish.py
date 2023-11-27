import pytest
from gendiff import generate_diff


@pytest.mark.parametrize('file1, file2, file_res', [
    ('tests/fixtures/file3.json', 'tests/fixtures/file4.json',
     'tests/fixtures/stylish.txt'),
    ('tests/fixtures/file3.yml', 'tests/fixtures/file4.yml',
     'tests/fixtures/stylish.txt'),
    ('tests/fixtures/empty.json', 'tests/fixtures/empty.json',
     'tests/fixtures/empty.txt'),
    ('tests/fixtures/empty.yml', 'tests/fixtures/empty.yml',
     'tests/fixtures/empty.txt')
])
def test_diff(file1, file2, file_res):
    with open(file_res, 'r') as result:
        res = result.read()
    diff = generate_diff(file1, file2)
    assert diff == res
