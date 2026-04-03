def solution(m, n, puddles):
    road = [[0] * (m + 1) for _ in range(n + 1)]
    
    for x, y in puddles:
        road[y][x] = -1 
        
    road[1][1] = 1 
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i == 1 and j == 1) or road[i][j] == -1:
                continue
                
            from_top = road[i-1][j] if road[i-1][j] != -1 else 0
            from_left = road[i][j-1] if road[i][j-1] != -1 else 0
            
            road[i][j] = (from_top + from_left) % 1_000_000_007
    
    return road[n][m]