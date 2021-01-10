class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return self.val


class LinkedList:
    def __init__(self, **threads):
        self.threads = []
        for k, v in threads.items():
            self.threads.append(k)
            self.__setattr__(k, Node(v.pop(0)))
            node = self.__getattribute__(k)
            for i in range(len(v)):
                node.next = Node(v[i])
                node = node.next

    def __repr__(self, threads=None):
        if not threads:
            threads = self.threads
        else:
            for i in threads:
                if i not in self.threads:
                    raise ValueError(f"Thread {i} is not initialised")
        representations = []
        for i in range(len(threads)):
            node = self.__getattribute__(threads[i])
            representations.append(f'{threads[i]} : ')
            while node:
                representations[i] = representations[i] + str(node.val)
                node = node.next
                if node:
                    representations[i] += ' -> '
        return '\n'.join(representations)

if __name__ == '__main__':
    a = LinkedList(**{'distance': [1,2,3,4,5], 'size': [5,4,3,2,1], 'khaotic': [2,4,3,5,1]})
    print(a)

