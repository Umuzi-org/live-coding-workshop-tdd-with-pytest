from stuff import add,special_split

def test_add_returns_0_for_empty_strings():
    result = add("")
    assert result==0

def test_add_single_number():
    """ passing in a single number as a string should result in an integer"""
    result = add("5")
    assert result == 5

    result = add("0")
    assert result == 0

    result = add("555")
    assert result == 555

def test_add_multiple_numbers():
    result = add("1,2")
    assert result == 3

    result= add("5,7")
    assert result==12

    result= add("5,7,100")
    assert result==112

    result= add("5,7,2000")
    assert result==2012

def test_works_with_newline():
    result = add("1\n2")
    assert result == 3

    result = add("1\n2,3")
    assert result == 6

def test_special_split():
    result = special_split("1,2\n3")
    assert result == ['1','2','3']

    result = special_split("11,22\n33,8")
    assert result == ['11','22','33','8']

