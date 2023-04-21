from script_27_cp_few_shot import flip_case


def test_flip_case():
    assert flip_case('') == ''
    assert flip_case('a') == 'A'
    assert flip_case('A') == 'a'
    assert flip_case('abc') == 'ABC'
    assert flip_case('ABC') == 'abc'
    assert flip_case('aBc') == 'AbC'
    assert flip_case('AbC') == 'aBc'
    assert flip_case('aBc123') == 'AbC123'
    assert flip_case('AbC123') == 'aBc123'
    assert flip_case('aBc123!') == 'AbC123!'
    assert flip_case('AbC123!') == 'aBc123!'
    assert flip_case('aBc123!@#') == 'AbC123!@#'
    assert flip_case('AbC123!@#') == 'aBc123!@#'
    assert flip_case('aBc123!@#_') == 'AbC123!@#_'
    assert flip_case('AbC123!@#_') == 'aBc123!@#_'
    assert flip_case('aBc123!@#_ ') == 'AbC123!@#_ '
    assert flip_case('AbC123!@#_ ') == 'aBc123!@#_ '
    assert flip_case('aBc123!@#_  ') == 'AbC123!@#_  '
    assert flip_case('AbC123!@#_  ') == 'aBc123!@#_  '
    assert flip_case('aBc123!@#_   ') == 'AbC123!@#_   '
    assert flip_case('AbC123!@#_   ') == 'aBc123!@#_   '
    assert flip_case('aBc123!@#_    ') == 'AbC123!@#_    '
    assert flip_case('AbC123!@#_    ') == 'aBc123!@#_    '
    assert flip_case('aBc123!@#_     ') == 'AbC123!@#_     '



