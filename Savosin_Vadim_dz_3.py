class List_valid(Exception):
    def __init__(self):
        self.my_list = []
        self.validation()
    def validation(self):
        while True:
            try:
                a = input()
                if a == 'stop':
                    print(self.my_list)
                    break
                a = int(a)
                self.my_list.append(a)
            except ValueError:
                print(f"Введенное значение {a} - не число")
list1 = List_valid()
