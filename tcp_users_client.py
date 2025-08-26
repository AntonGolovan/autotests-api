import socket

# Создаем TCP-сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Отправляем сообщение серверу
message = input("Введите сообщение: ")
client_socket.send(message.encode('utf-8', errors='replace'))

# Получаем ответ от сервера
response = client_socket.recv(1024).decode('utf-8')
print(response)

# Закрываем соединение
client_socket.close()
