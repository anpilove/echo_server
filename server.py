import socket
import logging


def server(host='localhost', port=7669):
    logging.basicConfig(filename='server.log', filemode='w',format='%(filename)s - %(asctime)s - %(message)s', level=logging.INFO)

    try:
        logging.info("Запуск сервера")
        print(">>> Запуск сервера")
        with socket.socket() as s:

            s.bind((host, port))
            logging.info("Начало прослушивания порта")
            print(">>> Начало прослушивания порта")
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
