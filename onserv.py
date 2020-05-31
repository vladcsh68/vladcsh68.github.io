import socket

SERVER_ADDRESS = ('192.168.42.28', 8125)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(SERVER_ADDRESS)
clients = []
members = {}
print("Server is running")

#ТУТ БОЛЬШАЯ ФУНКЦИЯ "РЕГИСТРАЦИИ"
#С ВВОДОМ ИМЕНИ, ПОДТВЕРЖДЕНИЕМ, ПАРОЛЕМ
def register_on_chat(port_address):
    register_data = 'Необходимо пройти регистрацию, введите свой ник: '
    server_socket.sendto(register_data.encode('utf-8'), address)

    def confirm_nickname(port_address):
        name, address = server_socket.recvfrom(1024)
        registration_data = f"Ваш ник {name.decode('utf-8')}? Введите Уes или No."
        server_socket.sendto(registration_data.encode('utf-8'), address)
        append_to_list(name, port_address)

    def new_nickmane(address):
        registration_data = 'Введите свой ник: '
        server_socket.sendto(registration_data.encode('utf-8'), address)
        confirm_nickname(address)

    def append_to_list(name, port_address):
        data, address = server_socket.recvfrom(1024)
        if data.decode('utf-8') == 'Yes':
            get_pass(name)
        elif data.decode('utf-8') == 'No':
            new_nickmane(port_address)

    def get_pass(name):
        pass_data_1 = f"Привет {name.decode('utf-8')} Введите пароль для своего ника: "
        server_socket.sendto(pass_data_1.encode('utf-8'), address)
        password_1, adr= server_socket.recvfrom(1024)
        pass_data_2 = "Повтори пароль"
        server_socket.sendto(pass_data_2.encode('utf-8'), address)
        password_2, adr = server_socket.recvfrom(1024)

        if password_1 == password_2:
            members[name.decode('utf-8')] = password_1.decode('utf-8')
            pass_data_3 = "Отлично, регистрация прошла успешно"
            server_socket.sendto(pass_data_3.encode('utf-8'), address)
            print(members)
        else:
            pass_data_4 = "Давай-ка попробуем снова"
            server_socket.sendto(pass_data_4.encode('utf-8'), address)
            get_pass(name)

    confirm_nickname(port_address)


while True:
    data, address = server_socket.recvfrom(1024)
    print(address[0], address[1])
    if address not in clients:
        clients.append(address)
        register_on_chat(address)
        text = "Регистрация прошла успешно. Добро пожаловать в чат!"
        server_socket.sendto(text.encode('utf-8'), address)

    for client in clients:

        if client == address:
            text_from_client = data.decode('utf-8')
            print(text_from_client)

            continue

        server_socket.sendto(data, client)