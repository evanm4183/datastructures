from linkedlist.listnode import ListNode

class LinkedList():
    head = None

    def __init__(self, vals):
        self.insert_list(vals)

    def insert_node(self, val):
        if self.head is None:
            self.head = ListNode(val)
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = ListNode(val)

    def insert_list(self, vals):
        for val in vals:
            self.insert_node(val)

    def print(self):
        curr = self.head

        while curr is not None:
            print(f'{curr.val} -> ', end ='')
            curr = curr.next

        print('')
