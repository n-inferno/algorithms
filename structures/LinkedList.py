class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return self.val


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.last = None
        if nodes:
            self.last = Node(nodes.pop(0))
            self.head = self.last
            for item in nodes:
                self.last.next = Node(item)
                self.last = self.last.next

    def __repr__(self):
        node = self.head
        represent = ''
        while node:
            represent += str(node.val)
            node = node.next
            if node:
                represent += ' -> '
        if not represent:
            return 'LinkedList()'
        return represent

    def to_list(self):
        result = []
        node = self.head
        while node:
            result.append(node.val)
            node = node.next
        return result

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

    def append(self, item):
        if not self.last:
            self.head = Node(item)
            self.last = self.head
        else:
            self.last.next = Node(item)
            self.last = self.last.next
        return self

    def extend(self, items):
        for item in items:
            self.append(item)
        return self

    def insert(self, pos, val):
        curr_pos = 0
        if pos == curr_pos:
            temp = self.head
            self.head = Node(val)
            self.head.next = temp
        else:
            node = self.head
            while node and node.next:
                if curr_pos + 1 == pos:
                    temp = node.next
                    node.next = Node(val)
                    node.next.next = temp
                    break
                node = node.next
                curr_pos += 1
            else:
                self.append(val)
        return self

    def remove(self, val):
        if not self.head:
            raise ValueError(f'{val} not in linked list {self}')
        node = self.head
        if node.val == val:
            self.head = self.head.next
            return self
        while node.next:
            if node.next.val == val:
                if node.next.next:
                    node.next = node.next.next
                else:
                    node.next = None
                break
            node = node.next
        else:
            raise ValueError(f'{val} not in linked list {self}')
        return self

    def maximum(self):
        if not self.head:
            return None
        maxi = self.head.val
        node = self.head
        while node:
            if node.val > maxi:
                maxi = node.val
            node = node.next
        return maxi

    def minimum(self):
        if not self.head:
            return None
        mini = self.head.val
        node = self.head
        while node:
            if node.val < mini:
                mini = node.val
            node = node.next
        return mini

    def is_sorted(self):
        node = self.head
        if not node or not node.next:
            return True
        while node.next:
            if node.val > node.next.val:
                return False
            node = node.next
        return True
