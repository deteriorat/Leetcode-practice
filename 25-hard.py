
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup( head: Optional[ListNode], k: int) -> Optional[ListNode]:
    PreNode = ListNode(0, head)
    left = PreNode
    cur = head
    while cur != None:
        i = 0
        right = cur
        while i < k :
            right = right.next
            i += 1
            if right is None:
                return PreNode.next
        tmp = right.next
        left.next = right
        right = right.next

        for i in range(k):
            nextnode = cur.next
            cur.next = right
            right = cur
            cur = nextnode
            print("dealinhg with ", i, " ", cur.val)
        
    return PreNode.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

cur = head
while cur != None:
    print(cur.val)
    cur = cur.next
print("=====")
head = reverseKGroup(head=head, k=2)

cur = head
while cur != None:
    print(cur.val)
    cur = cur.next