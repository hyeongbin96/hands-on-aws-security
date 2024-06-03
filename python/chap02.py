# 반복문 (while, for)
while True:
    print(1)
    break

a = 5
while a >= 1:
    a -= 1
    print(a)

for i in [1, 2, 3, 4, 5, 6]:
    print(i)

for i in range(1, 10):
    for j in range(1, 10):
        # continue
        print(f"{i} * {j} = {i * j}")
    # continue
    # break

# 조건문 (if)
test = "asdf"
if test == "asdf":
    print("true")
elif test == "asdfg":
    print("false")
else:
    print("else")

# list comprehension
a = [1, 2, 3, 4]
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
print(b)

b = [
    i for i in a if i % 2 == 0
]  # 리스트 컴프랜션으로 리스트 내에 반복문or조건문을 사용하여 코드를 간결하게 만들 수 있음

# Assignment Expression (Walrus expression)
l = [1, 2, 3, 4, 5, 6]
c = len(l)
if (c := len(l)) > 5:  # 리스트의 길이를 c라는 변수에 저장한다는 의미
    print(c)

# while True :
#     data = f.read(128)
#     if not data :
#         break
#     print(data)

# while data := f.read(128) :
#     print(data)
