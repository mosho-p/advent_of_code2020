import math


with open('inputs/day10_input.txt') as f:
    s = f.read().strip()

l = s.split()
l = sorted(list(map(int, l)))
l = [0] + l + [max(l)+3]
# l_diff = [l2-l1 for l1, l2 in zip(l[:-1], l[1:])]

# print((len([x for x in l_diff if x==1])) * (len([x for x in l_diff if x==3])))
#
# # take the diff of diff and the diff of diff diff, then find n! where n = len(diff<3) + len(diffdiff<3)
#
# l_d2 = [l2+l1 for l1, l2 in zip(l_diff[:-1], l_diff[1:])]
# l_d3 = [l2+l1+l3 for l3, l1, l2 in zip(l_diff[:-2], l_diff[1:-1], l_diff[2:])]
#
# print(math.factorial(len([x for x in l_d2 if x <= 3])) + math.factorial(len([x for x in l_d3 if x <= 4]))+1)
#
# n = len([x for x in l_d2 if x <= 3])
# m = len([x for x in l_d3 if x <= 3])
# ld4 = [l2+l1+l3+l4 for l3, l1, l2, l4 in zip(l_diff[:-3], l_diff[1:-2], l_diff[2:-1], l_diff[3:])]
# o = len([x for x in ld4 if x<=4])
# answer = 0
# for x in range(0, m-len(o)):
#     answer += math.factorial(n - (2*x)) * (m - x)
#
# print(answer)
l = sorted([28,
     33,
     18,
     42,
     31,
     14,
     46,
     20,
     48,
     47,
     24,
     23,
     49,
     45,
     19,
     38,
     39,
     11,
     1,
     32,
     25,
     35,
     8,
     17,
     7,
     9,
     4,
     2,
     34,
     10,
     3, 0, 52])
l_diff = [l2-l1 for l1, l2 in zip(l[:-1], l[1:])]
twos = [l2+l1 for l1, l2 in zip(l_diff[:-1], l_diff[1:])]
fours = [l2+l1 for l1, l2 in zip(twos[:-1], twos[1:])]
eights = [l2+l1 for l1, l2 in zip(fours[:-1], fours[1:])]
sixteens = [l2+l1 for l1, l2 in zip(eights[:-1], eights[1:])]
look_ahead_2 = [l2-l1 for l1, l2 in zip(l[:-2], l[2:])]
look_ahead_3 = [l2-l1 for l1, l2 in zip(l[:-3], l[3:])]

n = len([x for x in twos if x <= 3])
tris = len([x for x in eights if x==8])
quads = len([x for x in sixteens if x==16])

ahead_2 = len([x for x in look_ahead_2 if x <=3])
ahead_3 = len([x for x in look_ahead_3 if x<=3])

# print(2**n - tris*(2**(n-3)))
# dupes = (2**(tris))*(2**(n-3-tris+1))
dupes = sum([(tris-q) * 2**(n-3*(q+1)) for q in range(tris)])/(2**tris-1)
print(2**n - dupes)

a = 2**(n-tris*3)
print(a*(n-a)**(tris))

orderings = 1
skip = False
for x, y in zip(look_ahead_2, look_ahead_3 + [9]):
     if y <= 3:
          orderings *= 7
          skip = True
          continue
     elif x <= 3 and not skip:
          orderings *= 2
     skip = False
print(orderings)
