def value_exists(input: dict[str, int], x: int) -> bool:
    for item in input:
        if input[item] == x:
            return True
    return False

test_dict : dict [ str , int ] = { " a " : 2 , " b " : 4 , " c " : 7 , " d " : 1}
test_val : int = 4
print(value_exists(test_dict ,test_val ))
print(value_exists(test_dict, 5))