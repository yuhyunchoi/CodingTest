def solution(participant, completion):
    answer = ''
    dict = {}
    
    for p in participant:
        if p in dict:
            dict[p] += 1
        else: # dict[p] not in participant
            dict[p] = 1
            
    for c in completion:
        dict[c] -= 1
        
    for k, v in dict.items():
        if v > 0:
            answer = k
    
    
    return answer