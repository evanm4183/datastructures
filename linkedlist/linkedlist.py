from linkedlist.listnode import ListNode

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __populate_empty_list(self, node):
        self.head = node
        self.tail = node

    # inserts a list of values at the end of the linked list
    def insert_list(self, vals):
        if len(vals) == 0:
            print('ERROR: Cannot insert an empty list')
            return

        if self.head is None:
            node = ListNode(vals.pop(0))
            self.__populate_empty_list(node)

        curr = self.tail
        for val in vals:
            curr.next = ListNode(val)
            curr = curr.next
        self.tail = curr

    # inserts a node at the beginning of the list
    def insert_at_beginning(self, val):
        node = ListNode(val)

        if self.head is None:
            self.__populate_empty_list(node)
        else:
            node.next = self.head
            self.head = node

    # inserts a node at the end of the list
    def insert_at_end(self, val):
        node = ListNode(val)

        if self.tail is None:
            self.__populate_empty_list(node)
        else:
            self.tail.next = node
            self.tail = node

    def get_length(self):
        count = 0
        curr = self.head
        
        while curr is not None:
            count += 1
            curr = curr.next

        return count

    # prints the list
    def print(self):
        if self.head is None:
            print('List is empty')
            print('------------------------------------')
            return

        print(f'head: {self.head.val} | tail {self.tail.val}')

        curr = self.head
        while curr is not None:
            print(f'{curr.val} -> ', end ='')
            curr = curr.next

        print('\n------------------------------------')
