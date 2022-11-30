# File for testing any of the classes

from linkedlist.linkedlist import LinkedList
from linkedlist.listnode import ListNode

blank_list = LinkedList()
ll = LinkedList()
ll.print()

ll.insert_list([1, 2, 3])
ll.print()

ll.insert_list([4, 5, 6])
ll.print()

ll.insert_before(2, 0)
ll.print()

blank_list.insert_list([1, 2])
blank_list.print()

blank_list.insert_before(3, 0)
blank_list.print()
