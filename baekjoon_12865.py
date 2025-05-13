n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

# DP 테이블 초기화 (최대 무게 k까지)
dp = [0] * (k + 1)

# 각 아이템에 대해 반복
for weight, value in items:
    # 뒤에서부터 무게를 체크 (중복 방지) : 같은 아이템이 한 번 이상 사용되는 잘못된 상황 방지 하기 위해서
    for j in range(k, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[k])
