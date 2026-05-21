import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items
    
    def add_item_to_cheque(self,name):
        try:
            if len(name) == 0 or len(name) > 40:
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
            elif name not in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')
            else:
                self.__name_items.append(name)
                self.__number_items = self.__number_items + 1
        except ValueError as e:
            print(e)
        except NameError as e:
            print(e)
        return self.__name_items, self.__number_items

    def delete_item_from_check(self, name):
        try:
            if name not in self.__name_items:
                raise NameError('Позиция отсутствует в чеке')
            else:
                self.__name_items.remove(name)
                self.__number_items = self.__number_items - 1
        except NameError as e:
            print(e)
        return self.__name_items, self.__number_items

    def check_amount(self):
        total  = []
        total = list(map(self.__item_price.get, filter(self.__item_price.__contains__, self.__name_items)))
        if len(total) > 10:
            return sum(total) * 0.9
        else:
            return sum(total)

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        for key, value in self.__tax_rate.items():
            if value == 20:
                twenty_percent_tax.append(key)
        total = []
        for item in self.__name_items:
            if item in twenty_percent_tax:
                for key, value in self.__item_price.items():
                    if key == item:
                        total.append(value)
        if len(total) > 10:
            tax20 = sum(total) * 0.9 * 0.2
        else:
            tax20 = sum(total) * 0.2
        return tax20

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        for key, value in self.__tax_rate.items():
            if value == 10:
                ten_percent_tax.append(key)
        total = []
        for item in self.__name_items:
            if item in ten_percent_tax:
                for key, value in self.__item_price.items():
                    if key == item:
                        total.append(value)
        if len(total) > 10:
            tax10 = sum(total) * 0.9 * 0.1
        else:
            tax10 = sum(total) * 0.1
        return tax10

    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    def get_telephone_number(self, telephone_number):
        try:
            if not isinstance(telephone_number, int):
                raise ValueError('Необходимо ввести цифры')
            elif len(str(telephone_number)) > 10:
                raise ValueError('Необходимо ввести 10 цифр после "+7"')  
            else:
                result =  f'+7{telephone_number}'
        except ValueError as e:
            #print(e)
            result = e
        return result
            
collector = OnlineSalesRegisterCollector()

#Проверки
print(collector.add_item_to_cheque("чипсы")) 
print(collector.add_item_to_cheque("кола")) 
print(collector.add_item_to_cheque("молоко"))
print(collector.add_item_to_cheque(""))
print(collector.add_item_to_cheque("овощовощовощовощовощовощовощовощовощовощовощ"))
print(collector.add_item_to_cheque("фрукт"))
print(collector.delete_item_from_check("чипсы"))
print(collector.delete_item_from_check("банан"))
print(collector.check_amount())
print(collector.twenty_percent_tax_calculation())
print(collector.ten_percent_tax_calculation())
print(collector.total_tax())
print(collector.get_telephone_number("1234567891"))
print(collector.get_telephone_number(9211111111))
print(collector.get_telephone_number(92111111112))