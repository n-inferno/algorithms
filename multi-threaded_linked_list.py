class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return self.val


class LinkedList:
    def __init__(self, **threads):
        self.objects = set()
        for i in threads.values():
            self.objects.update(i)
        self.objects = list(self.objects)
        self.threads = []
        for k, v in threads.items():
            self.threads.append(k)
            self.__setattr__(k, Node(self.objects[self.objects.index(v.pop(0))]))
            node = self.__getattribute__(k)
            for i in range(len(v)):
                node.next = Node(self.objects[self.objects.index(v[i])])
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

    def __str__(self, threads=None):
        return self.__repr__(threads)

