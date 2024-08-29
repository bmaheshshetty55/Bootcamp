def remove_duplicates(arr):
    if not arr:
        return []

    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            result.append(arr[i])

    return result


input_array = [1, 1, 2, 3, 3, 4]
output_array = remove_duplicates(input_array)
print(output_array) 