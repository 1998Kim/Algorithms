def bfs(start_node, graph, line_check):
    visit = [True] * len(graph)
    visit[start_node] = False
    queue = [start_node]
    lines = 0

    while queue:
        now_node = queue.pop(0)
        
        for next_node in graph[now_node]:
            if visit[next_node] == True and line_check[now_node][next_node] == True:
                queue.append(next_node)
                visit[next_node] = False
                lines += 1
        
    return lines
    
def solution(n, wires):
    answer = n
    
    graph = [[] for _ in range(n+1)]
    for node_a, node_b in wires:
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)

    line_check = [[True] * (n+1) for _ in range(n+1)]
        
    for node_a, node_b in wires:
        line_check[node_a][node_b] = False
        line_check[node_b][node_a] = False
        
        cnt_a = bfs(node_a, graph, line_check)
        cnt_b = bfs(node_b, graph, line_check)
        
        line_check[node_a][node_b] = True
        line_check[node_b][node_a] = True
        
        answer = min(answer, abs(cnt_a - cnt_b))
        
    return answer