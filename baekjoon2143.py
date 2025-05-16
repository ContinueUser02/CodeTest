import sys

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
na = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
ma = list(map(int, sys.stdin.readline().split()))

n_sa = []
m_sb = []

for i in range(n):
    total = 0
    for j in range(i,n):
        total += na[j]
        n_sa.append(total)

for i in range(m):
    total = 0
    for j in range(i,m):
        total += ma[j]
        m_sb.append(total)

m_sb.sort()

def lower_bound(sb_arr, target):
    left, right = 0, len(sb_arr)
    while left < right:
        mid = (left + right) // 2
        if sb_arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(sb_arr, target):
    left, right = 0, len(sb_arr)
    while left < right:
        mid = (left + right) // 2
        if sb_arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

answer = 0

for k in n_sa:
    target = t - k
    left = lower_bound(m_sb, target)
    right = upper_bound(m_sb, target)
    answer += (right - left)

print(answer)


