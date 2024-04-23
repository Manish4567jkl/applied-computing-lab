ListNode = tuple[int, 'ListNode']

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    flag, p, q, current = (0, None), list1, list2, (0, None)
    while p and q:
        current = (p[0], current) if p[0] < q[0] else (q[0], current)
        p, q = (p[1], q) if p[0] < q[0] else (p, q[1])
    current = (p if p else q, current)
    result = []
    while current[1]:
        result.append(current[0])
        current = current[1]
    return result[::-1]

list1 = (1, (2, (4, None)))
list2 = (1, (3, (4, None)))
merged_list = mergeTwoLists(list1, list2)
print("Merged List:", merged_list)
