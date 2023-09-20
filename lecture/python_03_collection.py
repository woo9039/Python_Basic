# 컬렉션 타입
#  - 변수 하나에 값을 여러개 저장
#  - 실질적으로 변수에 컬렉션 1개가 저장
#  - 리스트(List), 튜플(Tuple), 딕트(Dictionary), 세트(Set)

# 1. 리스트(List)
#  - 시퀀스 자료형(연속 된 값 저장)
#  - 정렬 가능
#  - mutable(생성 된 후 변경 가능)
#  - index사용(slicing 가능)
#  - paking과 unpaking 가능
#  - 멤버함수: append(), extend(), insert(), remove(), pop(), index(), sorted(), 등등
# * 2차원 리스트는 표(table)과 동일한 형태

# 리스트 초기화(생성)
list_a = [1, 2, 3]
list_b = []
list_c = ["chosun", 98, 3.14, [1, 2, 3]]

print(list_c[0])   # 리스트에서 단일 값 추출
print(list_c[1:3])  # 리스트 슬라이싱

# 패킹과 언패킹
list_d = ["A", "B", "c"]  #패킹
a, b, c = list_d  #언패킹
#  a = list_d[0]

# append(): 리스트 맨 마지막에 값 추가!
a = [1, 2, 3, 4, 5]
a.append(10)
print(a)

# insert(): 원하는 인덱스에 값 추가!
a.insert(1, "A")  # (인덱스, 값)
print(a)