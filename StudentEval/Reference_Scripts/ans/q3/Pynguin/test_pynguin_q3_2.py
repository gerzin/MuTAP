import q3 as module_0
def test_case_1():
    dict_0 = {}
    list_0 = [dict_0, dict_0]
    var_0 = module_0.remove_extras(list_0)
    assert var_0 == [{}]
    tuple_0 = ()
    var_1 = module_0.remove_extras(tuple_0)
