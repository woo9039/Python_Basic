# 버블정렬
# A = [5, 3, 29, 215, 82]
# for i in range (0, 5):
#     for j in range (0, 4-i):
#         if A[j] < A[j+1]:
#             temp = A[j]
#             A[j] = A[j+1]
#             A[j+1] = temp
# print(A)

# 1. 사용자가 입력한 단수를 출력하는 코드
# n = int(input())
# for i in range(1,10):
#     print(f"{n} * {i} = {n*i}")

# 2. 2단부터 9단까지 출력
# for i in range(2,10):
#     for j in range(1,10):
#         print(f"{i} * {j} = {i*j}")
#     print("\n")

# 3. list a의 평균 값을 계산하세요.
# a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
# sum = 0
# for i in range(len(a)):
#     sum += a[i]
# ave = sum/len(a)
# print(ave)

# 4. list b에서 최소값 찾기
# b = [22, 1, 4, 7, 98]
# min = b[0]
# for i in range(len(b)):
#     if min > b[i]:
#         min = b[i]
# print(min)

# 5. list c의 최소값, 최대값 찾기
# c = [2, 5, 7, 1, 8]
# min = c[0]
# max = c[0]
# for i in range(len(c)):
#     if min > c[i]:
#         min = c[i]
#     if max < c[i]:
#         max = c[i]
# print(min)
# print(max)

# 6. 로그인(pw) -> 3번 이상 암호를 틀리면 프로그램 종료
# pw = 1234
# count = 0
# while(True):
#     n = int(input("비밀번호를 입력하세요: "))
#     if n == pw:
#         print("정답입니다!")
#         break;
#     count += 1
#     if count == 3:
#         print("잠김")
#         break

# 7. 1~100까지 더해서 총합 계산
# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

# 8.계산기 만들기
# 함수: 덧셈 뺄셈, 메인
# def plus (x, y):
#     return x + y
# def minus (x, y):
#     return x - y
# def mul(x, y):
#     return x*y
# def div(x, y):
#     return x/y
#
# n1 = int(input("숫자를 입력하시오: "))
# n2 = int(input("숫자를 입력하시오: "))
# ch = str(input("기호를 입력하시오: "))
#
# if ch == "+":
#     print(plus(n1, n2))
# if ch == "-":
#     print(minus(n1, n2))
# if ch == "*":
#     print(mul(n1, n2))
# if ch == "/":
#     print(div(n1, n2))


# n = int(input())
#
# for i in range(int(n/2 + 1)):
#     for j in range(int(n- i)):
#         print(' ',end="")
#     for j in range(int(2 * i + 1)):
#         print("*",end="")
#     print("")


count = 0
while(1):
    if count == 10:
        break
    print(count)
    count += 1
