# pip3 install boto3
# pip3 install boto3-stubs

from pprint import pprint
import boto3

####### 1. boto3 라이브러리로 aws 계정 정보 확인
client = boto3.client("sts")
res = client.get_caller_identity()

pprint(res)
print(res["Account"], res["Arn"], res["ResponseMetadata"]["HTTPStatusCode"], sep="\n")

if res["Arn"].endswith("root"):
    print("루트 계정입니다.")

####### 2. boto3 라이브러리로 유저 생성 및 삭제
client = boto3.client("iam")
username = input("사용자 이름 입력 : ")

try:  # 유저 생성
    client.create_user(UserName=username)
    print(f"{username} 사용자가 생성되었습니다.")
except client.exceptions.EntityAlreadyExistsException:
    print(f"{username} 사용자는 이미 존재합니다.")


try:  # 유저 삭제
    client.delete_user(UserName=username)
    print(f"{username} 사용자가 삭제되었습니다.")
except client.exceptions.NoSuchEntityException:
    print(f"{username}은 존재하는않는 사용자입니다.")


def Del_user(client, username):  # 함수로 변환
    if not username:
        raise Exception(f"{username} 잘못된 사용자 이름입니다.")
    try:
        client.delete_user(UserName=username)
        print((f"{username} 사용자가 삭제되었습니다."))
        return True
    except client.exceptions.NoSuchEntityException:
        print((f"{username}은 존재하지 않는 사용자입니다."))
        return True, None
    except Exception as e:
        return False, e

print(Del_user(client, username))

####### 3. 역할 조회
from datetime import datetime, timezone, timedelta

now = datetime.now(timezone.utc)

roles = client.list_roles()["Roles"]

# for role in roles: # 출력 시 boto3 문서에 예시에 나온 tags, rolelastused는 나오지 않는다. 문서에 보면 해당 값들은 getrole을 사용해야 얻을 수 있다고 명시돼있음
#     pprint(role["RoleName"])

for role in roles:  # role을 돌며 rolename을 name 변수에 넣고 get_role 함수의 전달
    name = role["RoleName"]
    r = client.get_role(RoleName=name)["Role"]
    # if r["RoleLastUsed"]:
    #     last_used_date = r["RoleLastUsed"]["LastUsedDate"]
    #     print(name, last_used_date)
    # else:
    #     last_used_date = "none"
    #     print(name, last_used_date)
    last_used_date = r["RoleLastUsed"].get("LastUsedDate")  # .get을 사용하면 위처럼 if else로 필터링하지 않아도 된다.

    if not last_used_date:
        print(name, "400일 내 사용 기록 없음")
    elif (now - last_used_date) > timedelta(days=90):
        print(name, f"90일 내 사용 기록 없음 | {last_used_date}")
    else:
        print(name, f"90일 내 사용 기록 있음 | {last_used_date}")

# 리스트 계열의 api 사용 시 주의점
# MaxItems란 파라미터를 사용하지 않으면 기본적으로 100개만 출력되고, 넘어가는 값들에 대해선 마커 등을 사용하여 다시 받아야 하는 불편함이 있다.
# > paginator 함수를 사용하면 이 부분을 편리하게 사용할 수 있다.