import socket


def pinger(host: str, port: int) -> bool:
    """Проверяет, что порт на указанном хосту доступен для подключения.

    :return: TRUE если порт доступен, FALSE если не доступен.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    sock.close()

    return result == 0


def test_port():
    host = "127.0.0.1"
    ports = {
        "SSH": 2222,
        "GDB": 7777,
    }

    for name, port in ports.items():
        print(f"Проверка {port}({name})")
        res = pinger(host, port)

        if res:
            text_res = "доступен"
        else:
            text_res = "не доступен"
        print(f"{name}: {text_res}")


if __name__ == "__main__":
    print("TODO: пока не готово")
    test_port()
