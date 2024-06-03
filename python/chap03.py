# 함수
def print_is_two(number):
    if number == 2:
        print(number)
    else:
        print("none")


print_is_two(1)
print_is_two(2)

# 예외 처리
# 1 / 0   > ZeroDivisionError: division by zero
# int("ASDF")  > ValueError: invalid literal for int() with base 10: 'ASDF'
try:
    1 / 0  # type: ignore
except ZeroDivisionError as e:
    print(e)

try:
    int("!@#")
except ValueError as e:
    print(e)

try:
    int("ASDF")
except Exception as e:  # 거의 모든 예외를 추적
    print(e)


# Exception은 편리한만큼 조심히 사용해야 한다.
# def del_user():
#     try:
#         delete_user(name="rex")
#     except NoSuchUserException as e:
#         return True
#     except Exception as e:
#         return False


def convert_str_to_int(value):
    try:
        int(value)
        return value
    except ValueError:
        raise Exception(f"{value}는 숫자 변환이 불가능합니다.")


print(convert_str_to_int("123"))
print(convert_str_to_int("ASD"))
