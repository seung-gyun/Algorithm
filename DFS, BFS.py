from collections import deque
n, m, start = map(int, input().split()) # n = 노드, m = 에지, start = 노드의 시작점
A = [[] for i in range(n+1)] # 노드의 개수를 기준으로 맨 앞에는 배열을 비워두는 것이다. 계산하기 편함

for j in range(m):
    s, e = map(int, input().split())
    A[s].append(e) # 무방향 에지 연결 
    A[e].append(s) # 무방향 에지 연결


# for i in range(n+1):
#     A[i].sort() #작은 노드부터 방문하기 위한 정렬


# def DFS(v):
#     print(v, end= '')
#     visited[v] = True # 들어왔다는 건 v에 관한 곳은 True
#     for i in A[v]:
#         if not visited[i]: # false라는 것은 아직 탐색을 하지 않은 것
#             DFS(i)


# visited = [False] * (n+1) # 방문 리스트
# DFS(start)

# def BFS(v):
#     queue = deque()
#     queue.append(v)
#     visited[v] = True # A[v] 번째는 탐색 자체를 시작하므로 그 구간은 true가 된다.
#     while queue:
#         now_Node = queue.popleft()
#         print(now_Node, end= '')
#         for i in A[now_Node]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)

# print()
# visited = [False] * (n+1) # Global변수 이기 때문에 초기화
# BFS(start)



def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

visited = [False] * (n+1)
DFS(start)

print()

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:        #queue가 계속 있으면
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

visited = [False] * (n+1)
BFS(start)