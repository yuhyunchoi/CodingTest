def solution(N, number):
    if N == number:
        return 1
    
    s = [set() for _ in range(9)]
    
    for i in range(1,9):
        s[i].add(int(str(N)*i))
        
    cnt = 0
    
    for i in range(1,9):
        for j in range(1, i):
            for op1 in s[j]:
                for op2 in s[i-j]:
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    if op2 != 0:
                        s[i].add(op1//op2)
                    cnt += 1
                    
        if number in s[i]:
            return i
    
    
    return -1