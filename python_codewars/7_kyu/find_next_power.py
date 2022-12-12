
def find_next_power(val, pow_):
    for i in range(val):
        mult = i ** pow_
        if mult > val:
            return mult



print(find_next_power(12385, 3))
print(find_next_power(1245678, 5))
print(find_next_power(1245678, 6))
