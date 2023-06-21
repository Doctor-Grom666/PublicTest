class Clients:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance

    def get_guests(self):
        return f'{self.first_name} {self.second_name}, {self.city}'


client_1 = Clients('Иван', 'Петров', 'Москва', 50)
client_2 = Clients('Олег', 'Сергеев', 'Волгоград', 100)
client_3 = Clients('Василий', 'Еремеев', 'Краснодар', 70)

guests_list = [client_1, client_2, client_3]
for guest in guests_list:
    print(guest.get_guests())