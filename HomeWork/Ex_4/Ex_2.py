# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

nums = [4, 4, 5, 5, 5, 7, 8, 2, 0]
new_num = []
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1
        if count == 1:
            new_num.append(nums[i])
print(nums)
print(new_num)
