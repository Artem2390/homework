class MyList:
    def __init__(self, initial_list):
        self.data = initial_list

    def clear(self):
        self.data = []

    def add_element(self, element, index):
        self.data.insert(index, element)

    def remove_last_element(self):
        if self.data:
            self.data.pop()

    def remove_element_at_index(self, index):
        if index < len(self.data):
            del self.data[index]

    def display(self):
        print(self.data)


# Приклад використання
initial_list = [1, 2, 3, 4, 5]
my_list = MyList(initial_list)

my_list.display()

my_list.clear()
my_list.display()

my_list.add_element(10, 0)
my_list.display()

my_list.remove_last_element()
my_list.display()

my_list.remove_element_at_index(1)
my_list.display()
