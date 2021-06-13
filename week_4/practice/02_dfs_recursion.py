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
visited = []


def dfs_recursion(adjacent_graph, cur_node, visited_array):
    # 구현해보세요!
    visited_array.append(cur_node)
    cur_lst = adjacent_graph[cur_node]
    for idx in cur_lst:
        if idx not in visited_array:
            cur_node = idx
            dfs_recursion(adjacent_graph,cur_node,visited_array)

    return visited_array


dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!