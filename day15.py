n = [0, 13, 16, 17, 1, 10, 6]
last_num = 6
visited_nums = {a: b for a, b in zip(n[:-1], range(len(n)-1))}
for i in range(6, 30000000-1):
    previous_index = visited_nums.get(last_num, i)
    visited_nums[last_num] = i
    last_num = i - previous_index
print(last_num)
