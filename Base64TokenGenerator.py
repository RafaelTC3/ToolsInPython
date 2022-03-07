import base64


def create_basic_auth(user: str, password: str) -> str:
    message = f"{user}:{password}"
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode("ascii")

    return base64_message


def simple_encoding(value: str) -> str:
    message_bytes = value.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode("ascii")

    return base64_message


def base64_decode(value: str) -> str:
    value_bytes = value.encode("ascii")
    base64_bytes = base64.b64decode(value_bytes)
    message = base64_bytes.decode("ascii")

    return message


def select_action():
    print(
        "Chose an option\n 1- Base 64 encode an basic auth\n 2- Base 64 message encoding \n 3- Base 64 message "
        "decoding"
    )
    option = input()
    if option == "1":
        print("Insert username")
        user = input()
        print("Insert password")
        password = input()
        print(create_basic_auth(user, password))
    elif option == "2":
        print("Insert value to be encoded")
        value = input()
        print(simple_encoding(value))
    else:
        print("Insert value to be decoded")
        value = input()
        print(base64_decode(value))
