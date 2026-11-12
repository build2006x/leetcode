class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Convert Python list [1, 2, 3] -> Linked List
def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# Print Linked List nicely in terminal
def show(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals) + " -> None")

# Test it out:
head = build_linked_list([10, 20, 30, 40])
show(head)  # Output: 10 -> 20 -> 30 -> 40 -> None