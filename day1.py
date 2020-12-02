with open('inputs/day1_input.txt') as f:
    nums = f.read().split()
nums = list(map(int, nums))

# 2 nums that sum to 2020
found = False
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 2020:
            print(nums[i] * nums[j])
            found = True
            break
    if found:
        break

# 3 nums that sum to 2020
found = False
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] > 2020:
            continue
        for k in range(j + 1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 2020:
                print(nums[i] * nums[j] * nums[k])
                found = True
                break
        if found:
            break
    if found:
        break
