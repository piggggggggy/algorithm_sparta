# 스파르타 알고리즘 강의 4주차 DFS 문제
# Q. 인접 리스트가 주어질 때, 모든 노드를 DFS 순서대로 방문하시오.

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_stack(adjacent_graph, start_node):
    # 구현해보세요!
    visited = []
    stack = []
    stack.append(start_node)
    while len(stack) > 0:
        lst = adjacent_graph[stack[-1]]
        visited.append(stack.pop())
        for i in lst:
            if i not in visited:
                stack.append(i)
    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!