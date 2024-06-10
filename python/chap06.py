# multi thread
# 멀티 스레드는 멀티 프로세스와 달리 싱글 코어에서 동작한다. 그렇기에 어떤 연산과 같은 작업을 할 땐 멀티 스레드를 쓰는 의미가 없다.
# 하지만 클라우드 api와 같은 경우처럼 네트워크 통신이 주된 작업인 경우, cpu를 사용하는게 아니기 때문에 멀티 스레드를 사용하면 더 효율적으로 작업을 할 수 있다.

from concurrent.futures import ThreadPoolExecutor, as_completed
from botocore.config import Config
from pprint import pprint

import boto3
import time

# client : https://boto3.amazonaws.com/v1/documentation/api/latest/guide/clients.html
# resource, session : https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html?highlight=multithreading#multithreading-or-multiprocessing-with-resources
def get_role_last_used_date(iam, role_name):
    role = iam.get_role(RoleName=role_name)["Role"]
    return role_name, role["RoleLastUsed"].get('LastUsedDate')


if __name__ == "__main__":
    start_time = time.time()
    print(start_time)

    iam = boto3.client("iam", config=Config(max_pool_connections=1000))
    roles = iam.list_roles()["Roles"]


    ###############################################
    # No MultiThreads
    ###############################################
    # for role in roles:
    #     r = iam.get_role(RoleName=role["RoleName"])["Role"]
    #     print(r["RoleName"], r["RoleLastUsed"].get('LastUsedDate'))

    # print(f"ELAPSED TIME: {time.time() - start_time:.3f}s")
    

    ###############################################
    # Yes MultiThreads
    ###############################################
    # threads = []
    # pool = ThreadPoolExecutor(max_workers=len(roles))

    # for role in roles:
    #     #threads.append(pool.submit(get_role_last_used_date, iam, role["RoleName"]))
    #     threads.append(pool.submit(get_role_last_used_date, iam, role["RoleName"]))

    # for future in as_completed(threads):
    #     name, last_used_date = future.result()
    #     print(name, last_used_date)

    # print(f"ELAPSED TIME: {time.time() - start_time:.3f}s")