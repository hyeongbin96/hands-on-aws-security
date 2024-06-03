# 기본 자료형
# number, string, boolean, list, dictionary, tuple, none
a = "string test"
a.find("str")
a.startswith("string")
a.endswith("test")

a = []  # 리스트 선언
b = {}  # 딕셔너리 선언
c = ()  # 튜플 선언

# 출력 포맷팅
print("test")
s = "test"
print(s, "test")
print("%s" % "test")
print("%s %d" % ("test", 1))  # s는 문자열, d는 정수, f는 실수, x는 16진수
print("{} {}".format("test", 123))
e = "test"
print(f"{e}")

# 타입 변환
print(type(None))
print(type(1))
print(int(1))
print(str(123))
print(tuple([]))
print(list(()))
print(list({1: 2, 3: 4}))  # 각 키값만 추출해서 리스트로 변환
