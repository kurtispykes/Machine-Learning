from calculate_age import get_age

def test_get_age():
    # Given
    yyyy, m, d = map(int, "1996/9/11".split("/"))
    # When
    age = get_age(yyyy, m, d)
    # Then
    assert age == 25
