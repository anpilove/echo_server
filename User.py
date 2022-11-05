import socket
import logging
import time


def user(host='localhost', port=7671):
    logging.basicConfig(filename='user.log', filemode='w',format='%(filename)s - %(asctime)s - %(message)s', level=logging.INFO)
    try:
        with socket.socket() as s:
            logging.info('Соединение с сервером')
            print('Соединение с сервером')
            try:
                s.connect((host, port))
            except OSError:
                logging.info("Соединение не установлено")
                print("Соединение не установлено")



            while True:
                inp = input(">>> Input: ")
                if inp == "exit":
                    s.close()
                    logging.info("Разрыв соединения с сервером")
                    print("Разрыв соединения с сервером")
                    break
                logging.info("Отправка данных серверу")
                print("Отправка данных серверу")
                s.send(inp.encode())
                logging.info("Прием данных от сервера")
                print("Прием данных от сервера")
                data = s.recv(1024)
                logging.info(f">>> Echoing:  {data.decode()}")
                print('>>> Echoing: ', data.decode())

    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    host = input("Введите называние host: ")
    port = int(input("Введите port: "))
    user(host,port)
