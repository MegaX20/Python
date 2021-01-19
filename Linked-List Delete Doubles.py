class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
    
    def insert_node(self, data):
        """
        :param data: Node data
        :return: None
        """
        node = Node(data)
        node.next = self.head
        self.head = node

    def display_list(self):

        current = self.head
        while current:
            print(current.value, end="->")
            current = current.next

ll = LinkedList()
ll.insert_node(25)
ll.insert_node(35)
ll.insert_node(15)
ll.insert_node(32)
ll.insert_node(25)
ll.insert_node(80)
ll.insert_node(15)
ll.display_list()
print("\n")
prev = None
curr = ll.head
double_dict = dict()
while curr:
    if curr.value not in double_dict:
        double_dict[curr.value] = None
        prev = curr
    else:
        prev.next = curr.next
    curr=prev.next

ll.display_list()