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

num_min = b[0]  # 최소값 담을 공간
for x in b:  # 5번 반복
    if x < num_min:
        num_min = x

print(num_min)  # 1 출력

# 문제5) list c의 최소값, 최대값 찾기
c = [2, 5, 7, 1, 8]

num_min = c[0]
num_max = c[1]
for x in c:
    if x < num_min:
        num_min = x
    if x > num_max:
        num_max = x

print(num_min)  # 1 출력
print(num_max)  # 8 출력

# 문제6)
print("=" * 100)
# 사용자가 입력한 값 1, 2, 3 통과
# 아닌 경우 다시 입력하도록

# count = 0  #틀린 횟수
# while True:
#     if count >= 4:
#         print("프로그램을 사용할 수 없습니다.")
#         break
#     num = int(input("값: "))
#     # if 4 > num > 0:  # num = 1, 2, 3
#     if num in [1, 2, 3]:
#         print(f"{num}을 입력하셨습니다.")
#         break
#     else:
#         print("1, 2, 3의 값만 입력해주세요")
#         count += 1

# 문제7) 1부터 100까지 총합을 출력하는 코드
# - for문으로 작성
# - while문으로 작성

sum = 0
for i in range(1, 101):
    sum += i
print(sum)

i =1
sum =0
while i <= 100:
    sum += i
    i += 1
print(sum)
