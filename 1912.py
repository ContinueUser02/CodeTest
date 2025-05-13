import sys

sys.setrecursionlimit(1000000)  # 재귀 한도 높임

def max_subarray(arr, left, right):
    if left == right:
        return arr[left]
    
    mid = (left + right) // 2

    # 좌측 최대 부분합
    left_max = max_subarray(arr, left, mid)
    # 우측 최대 부분합
    right_max = max_subarray(arr, mid+1, right)
    
    # 가운데를 걸치는 최대 부분합
    left_sum = -float('inf')
    temp = 0
    for i in range(mid, left-1, -1):
        temp += arr[i]
        left_sum = max(left_sum, temp)

    right_sum = -float('inf')
    temp = 0
    for i in range(mid+1, right+1):
        temp += arr[i]
        right_sum = max(right_sum, temp)
    
    cross_max = left_sum + right_sum

    return max(left_max, right_max, cross_max)

# 입력
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 실행 및 출력
result = max_subarray(arr, 0, n-1)
print(result)
