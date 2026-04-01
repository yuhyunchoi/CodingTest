from itertools import permutations

def solution(numbers):
    answer = 0
    
    num_list = list(numbers) # 예: "17" -> ['1', '7']
    all_cases = set() # 중복 제거를 위한 셋
    
    # 1. 1장 뽑기부터 n장 뽑기까지 모든 순열 생성
    for i in range(1, len(numbers) + 1):
        # permutations는 튜플을 반환하므로 join으로 합쳐줌
        for p in permutations(num_list, i):
            num = int("".join(p))
            all_cases.add(num)
            
    # 2. 소수 판별
    for case in all_cases:
        if is_prime(case):
            answer += 1
            
    return answer

def is_prime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    