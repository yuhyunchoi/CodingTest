from collections import * 

def solution(n, wires):
    answer = n
    
    for i in range(len(wires)):
        adj = [[] for _ in range(n+1)]
        
        for j, (v1, v2) in enumerate(wires):
            if i == j: continue
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        group1_count = count_node(wires[i][0],n,adj)
        group2_count = n - group1_count
        
        answer = min(answer, abs(group1_count - group2_count))
        
    
    return answer

def count_node(start_node, n, adj):
    visited = [False]*(n+1)
    queue = deque([start_node])
    visited[start_node] = True
    
    count = 1
    
    while queue:
        curr = queue.popleft()
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
                
    return count
        
        