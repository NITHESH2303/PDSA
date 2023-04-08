def reverse(root):
    if root.isEmpty:
        return root
    temp = root
    prev = None
    while temp:
        nxt, temp.next = temp.next, prev
        prev, temp = temp, nxt
    return prev