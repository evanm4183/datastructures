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

    # inserts a node after the first instance of a value in the linked list
    def insert_after(self, list_val, insert_val):
        if self.head is None:
            print('ERROR: Cannot insert after a value because list is empty')
            return

        curr = self.head
        while curr.next is not None and curr.val != list_val:
            curr = curr.next

        if curr.next is None and curr.val != list_val:
            print(f'ERROR: {list_val} does not exist within the linked list')
        elif curr.next is None:
            self.insert_at_end(insert_val)
        else:
            temp = curr.next
            curr.next = ListNode(insert_val)
            curr.next.next = temp

    # inserts a node before the first instance of a value in the linked list
    def insert_before(self, list_val, insert_val):
        if self.head is None:
            print('ERROR: Cannot insert before a value because list is empty')
            return

        if self.head.val == list_val:
            self.insert_at_beginning(insert_val)
        else:
            curr = self.head
            while curr.next is not None and curr.next.val != list_val:
                curr = curr.next
            
            # curr is the tail, therefore the value was not found within the list
            if curr.next is None:
                print(f'ERROR: {list_val} does not exist within the linked list')
            else:
                node = ListNode(insert_val)
                temp = curr.next
                curr.next = node
                node.next = temp

    # removes the first instance of a value in the linked list
    def remove(self, val):
        if self.head is None:
            print('ERROR: Cannot remove any values because the list is empty')
            return

        if self.head.val == val:
            self.head = self.head.next
        else:
            curr = self.head
            while curr.next is not None and curr.next.val != val:
                curr = curr.next

            if curr.next is None:
                print(f'ERROR: {val} does not exist within the linked list')
            elif curr.next.next is None:
                curr.next = None
                self.tail = curr
            else:
                curr.next = curr.next.next

    # reverses the linked list in place
    def reverse(self):
        if self.head is not None and self.head.next is not None:
            prev = None
            curr = self.head

            while curr is not None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = self.head
            self.head = self.tail
            self.tail = temp

        
    # gets the length of the linked list
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
