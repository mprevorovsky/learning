class MyArray:-
    def __init__(self, values=[10, 20, 30]):
        self.my_array = values

    def print(self):
        print(self.my_array)

    def add_item(self, new_value):
        self.my_array.append(new_value)

    def remove_item(self, index):
        self.my_array.pop(index)


z = MyArray(values=[20, 30, 40])
z.print()
z.add_item(9)
z.print()
z.remove_item(1)