# Учитывая массив целых чисел nums и целочисленную цель, верните индексы двух чисел так, чтобы их сумма составляла цель.
# Вы можете предположить, что каждый вход будет иметь ровно одно решение, и вы не можете использовать один и тот же элемент дважды.
# Вы можете вернуть ответ в любом порядке.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

def func(nums, target):
    rezault = []
    for i in nums:
        for b in nums:
            if i + b == target: 
                rezault.append(enumerate())            