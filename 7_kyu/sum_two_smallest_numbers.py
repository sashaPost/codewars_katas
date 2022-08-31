
def sum_two_smallest_numbers(numbers):
    first_num = min(numbers)
    numbers.remove(first_num)
    second_num = min(numbers)
    numbers.remove(second_num)
    return (first_num + second_num)
    #return numbers


    
print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))
print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))
