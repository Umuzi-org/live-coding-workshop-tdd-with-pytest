
def add(numbers):    #1\n2,3
    if numbers == "":
        return 0

    # individual_numbers = numbers.split(',')  # ['1\n2','3']
    individual_numbers = special_split(numbers)
    result = 0
    for number in individual_numbers:
        result += int(number)
    return result


def special_split(string_to_split):  # "1,2\n3"
    """this will split a string by multiple characters, eg: 1,2\n3 => [1,2,3]"""
    first_list = string_to_split.split(',') # ["1","2\n3"]
    result = []

    for part in first_list:
        part_list = part.split("\n")
        result.extend(part_list)
    return result
