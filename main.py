import random
from random import randint
a = random.randrange(1,10)
random_list_of_nums = []

for i in range(a):
    random_list_of_nums.append(randint(1,99))
print(random_list_of_nums, "- начальное яблоко")

for i in range(a-1):
    for j in range(a-i-1):
        if random_list_of_nums[j] > random_list_of_nums[j + 1]:
            random_list_of_nums[j], random_list_of_nums[j+1] = random_list_of_nums[j+1], random_list_of_nums[j]

print(random_list_of_nums, "- конечное яблоко")
print("Наименьшее число:", random_list_of_nums[0])
print("Наибольшее число:", random_list_of_nums[-1])