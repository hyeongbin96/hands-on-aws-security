# generator expression
from typing import Generator
import psutil
import os
import csv

CSV_NAME = "test.csv"

# 현재 메모리 사용량 출력 함수 (Current memory usage output function)
def memory_usage(message: str = "debug"):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2**20  # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.3f} MB")


def create_test_csv(name):
    fp = open(name, "w")
    w = csv.writer(fp)
    for _ in range(0, 10000000):
        w.writerow([1, 2, 3, 4])


if not os.path.exists(CSV_NAME):
    create_test_csv(CSV_NAME)


# ###############################################
# # 1. List Comprehension vs Generator Expression
# ###############################################
memory_usage("평소 메모리 사용량")

# # list_comp = [i for i in range(0, 10000000)]
# # memory_usage("List Comprehension")
# # 리스트 컴프렌션 기능을 사용하면 읽는 데이터에 비례하게 메모리 사용률이 올라간다. 
# # 만약 매우 큰 데이터를 읽어야 되면 파이썬이 매우 느려진다. 이때 제너레이션 익스프레션을 사용한다.

# # print(list_comp[-1])  # 인덱싱 가능 (indexable)

# gen_exp: Generator[int, None, None] = (i for i in range(0, 10000000))
# memory_usage("Generator Expression")
# # 리스트 컴프랜션과 다르게 초기 메모리랑 거의 차이가 없다.
# # 리스트 컴프랜션같은 경우엔 전부 메모리에 올리는 반면, 제네레이션 같은 경우엔 어떤 표현식을 만든 것이다.
# # 10000000000000을 바로 메모리에 올리는게 아니라 만들 수 있는 공식만 저장해 둔 것이다.
# # for i in gen_exp : 
# #     print(i) 
# # 이렇게 gen_exp를 돌때 메모리에서 어떤 공식을 통해 계산을 하여 특정 값을 가져와 출력하는 것이기 때문에 메모리 사용률이 굉장히 낮다.

# print(gen_exp[-1]) # 인덱싱 불가능 (Unable to index)
# # 메모리에 올라간게 아닌 바로바로 값을 가져오는거기 때문에 인덱싱을 통해 값을 바로 가져오는게 불가능하다.

###############################################
# 2. Read a file
###############################################
fp = open(CSV_NAME)
r = csv.reader(fp)
# list_comp = [i for i in r]  # type: ignore
# list_comp = [tuple(i) for i in r]  # type: ignore
# memory_usage("List Comprehension(Read a File)")

gen_exp = (i for i in r)  # type: ignore
for i in gen_exp:
    print(i)
    break
memory_usage("Generator Expression(Read a File)")

memory_usage("END")