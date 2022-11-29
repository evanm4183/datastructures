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

ll.insert_at_beginning(0)
ll.print()

ll.insert_at_end(7)
ll.print()

ll.insert_after(2, 7)
ll.print()

ll.insert_after(7, 100)
ll.print()
