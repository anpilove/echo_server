import socket
import logging
import random


def server(host='localhost', port=7669):
    logging.basicConfig(filename='server.log', filemode='w',format='%(filename)s - %(asctime)s - %(message)s', level=logging.INFO)

    try:
        logging.info("Запуск сервера")
        print(">>> Запуск сервера")
        with socket.socket() as s:
            while True:
                try:
                    s.bind((host, port))
                    print(f"Подключение к порту {port}")
                    logging.info("Начало прослушивания порта")
                    print(">>> Начало прослушивания порта")
                    break
                except OSError:
                    logging.info(f"Не получилось подключиться к порту {port}")
                    print(f"Не получилось подключиться к порту {port}")

                host = "localhost"
                port = random.randint(1111,9999)

            while True:
                s.listen(0)
                logging.info("Подключение клиента")
                print(">>> Подключение клиента")
                conn, addr = s.accept()
                while True:
                    logging.info("Приём данных у клиента")
                    print(">>> Приём данных у клиента")
                    data = conn.recv(1024)
                    if not data:
                        break
                    logging.info("Отправка данных клиенту")
                    print(">>> Отправка данных клиенту")
                    conn.send(data)
                logging.info("Отключение клиента")
                print(">>> Отключение клиента")
                conn.close()
            logging.info("Отключение сервера")
            print(">>> Отключение сервера")

    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    server()
