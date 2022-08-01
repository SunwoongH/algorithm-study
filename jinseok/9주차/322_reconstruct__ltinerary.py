
import collections


def findItinerary(tickets):
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a,b in sorted(tickets):
        graph[a].append(b)
    print(graph)
    route = []
    def dfs(a):
        # 첫 번째 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop(0))
            
        route.append(a)

    dfs('JFK')
    # 다시 뒤집어 어휘 순 결과로
    return route[::-1]

t = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(findItinerary(t))