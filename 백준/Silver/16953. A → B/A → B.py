from collections import deque

def convert_A_to_B(A, B):
    queue = deque([(A, 0)])

    while queue:
        current, count = queue.popleft()

        if current == B:
            return count + 1

        # 2를 곱하는 경우
        next_double = current * 2
        if next_double <= B:
            queue.append((next_double, count + 1))

        # 1을 수의 가장 오른쪽에 추가하는 경우
        next_append = current * 10 + 1
        if next_append <= B:
            queue.append((next_append, count + 1))

    # B로 바꿀 수 없는 경우
    return -1

# 입력
A, B = map(int, input().split())

# 결과 출력
result = convert_A_to_B(A, B)
print(result)
