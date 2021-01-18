from app import read_files


def test_read_files():
    result = read_files.get_report()
    assert isinstance(result, list)
    assert len(result) == 19
    assert result[0][5] < result[18][5]
