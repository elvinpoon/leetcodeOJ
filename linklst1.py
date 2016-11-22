class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return
        la = 1
        ptr = headA
        while(ptr.next != None):
            la += 1
            ptr = ptr.next
        lb = 1
        ptr = headB
        while(ptr.next != None):
            lb += 1
            ptr = ptr.next
        ptra = headA
        ptrb = headB
        if la > lb:
            step = la - lb
            for i in range(step):
                ptra = ptra.next
        else:
            step = lb - la
            for i in range(step):
                ptrb = ptrb.next
        while(ptra.next != None):
            if ptra.val == ptrb.val:
                return ptra
            else:
                ptra = ptra.next
                ptrb = ptrb.next
        if ptra.val == ptrb.val:
                return ptra
        else:
            return None

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node5.next = node1
node1.next = node3
node2.next = node3
node3.next = node4
m = Solution()
print m.getIntersectionNode(node5,node2).val