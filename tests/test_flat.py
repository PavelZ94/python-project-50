import pytest
from gendiff import generate_diff


@pytest.mark.parametrize('file1, file2, file_res', [
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'tests/fixtures/flat.txt'),
    ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'tests/fixtures/flat.txt'),
    ('tests/fixtures/empty.json', 'tests/fixtures/empty.json', 'tests/fixtures/empty.txt'),
    ('tests/fixtures/empty.yml', 'tests/fixtures/empty.yml', 'tests/fixtures/empty.txt'),
    ('tests/fixtures/empty.json', 'tests/fixtures/file2.json', 'tests/fixtures/half.txt'),
    ('tests/fixtures/empty.yml', 'tests/fixtures/file2.yml', 'tests/fixtures/half.txt')
])
def test_diff(file1, file2, file_res):
    with open(file_res, 'r') as result:
        res = result.read()
    diff = generate_diff(file1, file2)
    assert diff == res
