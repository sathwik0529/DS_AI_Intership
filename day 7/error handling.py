def power(base, exp):
    return base ** exp

def average(numbers_list):
    return sum(numbers_list) / len(numbers_list)

result_power = power(2, 10)
result_average = average([10, 20, 30, 40])

print(f"2^10 = {result_power}")
print(f"Average = {result_average}")