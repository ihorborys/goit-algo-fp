class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

def reverse_linked_list(linked_list):
    prev = None
    curr = linked_list.head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    linked_list.head = prev

def merge_sort_linked_list(head):
    if not head or not head.next:
        return head

    # Розділити список на дві половини
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(next_to_middle)

    # Злиття відсортованих списків
    sorted_list = sorted_merge(left, right)
    return sorted_list

def get_middle(head):
    if not head:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def sorted_merge(a, b):
    if not a:
        return b
    if not b:
        return a

    if a.data <= b.data:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)
    return result

def merge_two_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    else:
        tail.next = list2

    return dummy.next

# Створення та додавання елементів у список
llist = LinkedList()
llist.append(3)
llist.append(1)
llist.append(2)

print("Original List:")
llist.print_list()

# Реверсування списку
reverse_linked_list(llist)
print("Reversed List:")
llist.print_list()

# Сортування списку методом злиття
llist.head = merge_sort_linked_list(llist.head)
print("Sorted List:")
llist.print_list()

# Об'єднання двох відсортованих списків
llist2 = LinkedList()
llist2.append(0)
llist2.append(4)
merged_head = merge_two_sorted_lists(llist.head, llist2.head)

# Виведення об'єднаного списку
merged_list = LinkedList()
merged_list.head = merged_head
print("Merged Sorted List:")
merged_list.print_list()