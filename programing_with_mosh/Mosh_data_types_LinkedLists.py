class Node():
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def change_value(self, value):
        self.value = value

    def change_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, values):
        self.nodes = []
        for i in range(len(values)):
            self.nodes[i] = Node(values[i])
            if i > 0:
                self.nodes[i-1].change_next_node(self.nodes[i].next_node)


            self.first = Node(value)
            self.last = self.first


test_list = LinkedList([1, 4, 6])

test_node = Node(14)
print(test_node.value)
print(test_node.next_node)
test_node.change_value(20)
print(test_node.value)
