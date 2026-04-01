from collections import deque

def solution(progresses, speeds):
    answer = []
    
    n = len(progresses)
    queue = deque()
    
    
    for i in range(n):
        current = progresses[i]
        day = 0
        
        while current < 100:
            current += speeds[i]
            day += 1
        
        queue.append(day)
        
    
    while queue:
        current_max = queue.popleft()
        cnt = 1
        
        while queue and current_max >= queue[0]:
            queue.popleft()
            cnt += 1

        answer.append(cnt)
        
    return answer