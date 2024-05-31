class Node: # This class is the Node class which will have date and pointer to the next list data.
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # Inserting at the begining of the Linked List
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    # Inserting at the End
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    # Utility function to print The Linked List
    def print(self):
        if self.head is None:
            print('Linked List is Empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)
        

if __name__ == '__main__':
    ll = LinkedList()
    for i in range(10):
        if i % 2 == 0:
            ll.insert_at_begining(i)

    for i in range(10):
        if i % 2 != 0:
            ll.insert_at_end(i)
    ll.print()