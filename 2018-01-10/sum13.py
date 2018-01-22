def sum13(nums):
    total = 0
    for index in range(len(nums)):
        num = nums[index]
        if num == 13:
            pass
        elif nums[index - 1] == 13 and index != 0:
            pass
        else:
            total += num
    return total


tests = [
    [1, 13, 2],
    [1, 13, 2, 13],
    [13, 13, 13, 13],
    [13, 2, 6, 7],
    []
]

for test in tests:
    print(sum13(test))
