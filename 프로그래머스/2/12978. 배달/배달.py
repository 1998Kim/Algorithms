import heapq

def process(N, graph, start_node):
    dists = [float("INF")] * (N+1)
    dists[start_node] = 0

    queue = []
    heapq.heappush(queue, [start_node, dists[start_node]])
    
    while queue:
        now_node, now_dist = heapq.heappop(queue)
        if now_dist > dists[now_node]:
            continue
        for new_node, new_dist in graph[now_node]:
            dist = now_dist + new_dist
            if dist < dists[new_node]:
                dists[new_node] = dist
                heapq.heappush(queue, [new_node, dists[new_node]])
    return dists
    
def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N+1)]
    
    for a, b, time in road:
        graph[a].append((b, time))
        graph[b].append((a, time))
    
    dists = process(N, graph, 1)
    for dist in dists:
        if dist <= K:
            answer += 1
    return answer