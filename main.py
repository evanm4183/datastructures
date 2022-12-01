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

ll.reverse()
ll.print()

ll2 = LinkedList()
ll2.insert_list([1, 2])
ll2.print()

ll2.reverse()
ll2.print()

