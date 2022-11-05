import socket


def server(host='localhost', port=7671):
    try:
        print(">>> Запуск сервера")
        with socket.socket() as s:

            s.bind((host, port))
            print(">>> Начало прослушивания порта")
            while True:
                s.listen(0)
                print(">>> Подключение клиента")
                conn, addr = s.accept()
                while True:
                    print(">>> Приём данных у клиента")
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(">>> Отправка данных клиенту")
                    conn.send(data)
                print(">>> Отключение клиента")
                conn.close()
            print(">>> Отключение сервера")

    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    server()
