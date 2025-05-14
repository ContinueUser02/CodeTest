n = int(input())
a = list(map(int, input().split()))

cost = 0

for i in range(n - 2):
    # 먼저 i+1 > i+2 상황 처리
    if a[i + 1] > a[i + 2]:
        min_2 = min(a[i], a[i + 1] - a[i + 2])
        a[i] -= min_2
        a[i + 1] -= min_2
        cost += min_2 * 5
    
    # 이제 i, i+1, i+2에서 3개 사기
    min_3 = min(a[i], a[i + 1], a[i + 2])
    a[i] -= min_3
    a[i + 1] -= min_3
    a[i + 2] -= min_3
    cost += min_3 * 7

for i in range(n - 1):
    min_2 = min(a[i], a[i + 1])
    a[i] -= min_2
    a[i + 1] -= min_2
    cost += min_2 * 5

for i in range(n):
    cost += a[i] * 3

print(cost)


'''
문제 읽고 '가장 싸게 사는 방법'만 생각한다
방법3: (i,i+1,i+2) -> 7원 -> 가장 쌈
방법2: (i,i+1) -> 5원 -> 중간
방법1: (i) ->3원 가장 비쌈

핵심 관점: 최대한 많은 구간을 방법 3으로 사야함
나머지는 방법2로 최대한 처리
진짜 남는건 방법1로 처리

그리디 함정 파악(i+1 > i+2 케이스)
만약 i+1이 i+2보다 많으면?
방법 3을 먼저 쓰면 i+1이 많이 남고 결국 방법1,방법2로 비싸게 사야하므로
->이 때는 먼저 i,i+1에서 방법2로 처리해서 i+1을 줄이고 -> 방법3 쓰는게 이득

for i in range(N - 2):
    if a[i+1] > a[i+2]: 먼저 i, i+1 방법2 처리
    그 다음 i, i+1, i+2 방법3 최대 처리

for i in range(N - 1):
    i, i+1 방법2 최대 처리

for i in range(N):
    i 방법1 처리
'''
