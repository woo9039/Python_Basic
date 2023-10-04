# 문제2)
# 2단 9단까지 출력 => 중첩 for
# 2x1=2
# 2x2=4
# ...
# 3x1=3
# ...
# 9x9=81

for i in range(2, 10):
    for j in range(1, 10):

        print(f"{i}x{j}={i*j}")

# 문제3) list a의 평균값을 계산하세요.
print("=" * 100)
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
# total => 총합
total = 0
for num in a:
    total += num
length = len(a)
result = total / length
print(round(result, 2))

# 문제4) list b에서 최소값 찾기!
b = [22, 1, 4, 7, 98]

print(num_min)  # 1 출력
