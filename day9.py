# starting on 26, find the first number that is not the sum of 2 previous
with open('inputs/day9_input.txt') as f:
    s = f.read().strip()

nums = list(map(int, s.split()))

for i in range(26, len(nums)):
    valid = False
    for j in range(i-25, i):
        for k in range(j+1, i):
            if k == j:
                continue
            if nums[j] + nums[k] == nums[i]:
                valid = True
                break
        if valid==True:
            break
    if not valid:
        print(nums[i])
        break



for i in range(len(nums)):
    for j in range(i, len(nums)):
        contig = [nums[x] for x in range(i, j)]
        if sum(contig) == 14144619:
            print(min(contig) + max(contig))
            break