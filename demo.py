# Write a python code for the string operation.


def string_operations(input_string):
    length = len(input_string)

    lower_case = input_string.lower()

    upper_case = input_string.upper()

    count_a = input_string.count('a')

    replaced_string = input_string.replace("test", "exam")

    reversed_string = input_string[::-1]

    split_string = input_string.split()

    joined_string = '-'.join(split_string)

    return {
        "Length": length,
        "Lower Case": lower_case,
        "Upper Case": upper_case,
        "Count of 'a'": count_a,
        "Replaced String": replaced_string,
        "Reversed String": reversed_string,
        "Split String": split_string,
        "Joined String": joined_string
    }


input_string = "Hello, this is a test string."
result = string_operations(input_string)
for key, value in result.items():
    print(f"{key}: {value}")


# List operation and create function
def list_operations(input_list, new_items):
    length = len(input_list)

    input_list.append(new_items)

    sorted_list = sorted(input_list)

    reversed_list = input_list[::-1]

    max_value = max(input_list)
    min_value = min(input_list)

    count_item = input_list.count(3)

    unique_items = list(set(input_list))

    return {
        "Original List": input_list,
        "Length of List": length,
        "Sorted List": sorted_list,
        "Reversed List": reversed_list,
        "Max Value": max_value,
        "Min Value": min_value,
        "Count of 3": count_item,
        "Unique Items": unique_items
    }


input_list = [12, 5, 9, 34, 3, 12, 3, 9]
new_item = 18
result = list_operations(input_list, new_item)

for key, value in result.items():
    print(f"{key}: {value}")
