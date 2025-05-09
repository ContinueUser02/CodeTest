import sys
from queue import PriorityQueue

input = sys.stdin.readline

n,m = map(int,input().split())

pq = PriorityQueue()

parent = [0] * (n+1) #n+1을 한 이유는 인덱스 번호와 노드 번호를 일치시키기 위해 노드0은 안 쓸 예정

for i in range(n+1):
    parent[i] = i #여기서 parent[] 배열을 0 1 2 3으로 세팅한거임 여기선 아무 작업도 안했으니 부모 노드가 곧 자기 자신임

for i in range(m):
    s,e,w = map(int,input().split())
    pq.put((w,s,e))


def find_root(node):
    while node != parent[node]:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return node
    
def union(node_a, node_b):
    root_a = find_root(node_a)
    root_b = find_root(node_b)

    if root_a != root_b:
        parent[root_b] = root_a

result = 0
useEdge = 0

while useEdge < n-1:
    w,s,e = pq.get()
    if find_root(s) != find_root(e):
        union(s,e)
        result += w
        useEdge += 1

print(result)




