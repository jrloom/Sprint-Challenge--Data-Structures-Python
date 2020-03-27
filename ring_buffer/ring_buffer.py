from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # print(f"cap: {self.capacity} | store: {self.storage.length} | item: {item}")

        # this fails
        # if at cap
        # if self.storage.length > self.capacity:
        #     # set new val to current
        #     self.current.value = item
        #     # move current
        #     self.current = self.current.next
        # # if not at cap
        # else:
        #     # add item
        #     self.storage.add_to_tail(item)
        #     # move older items
        #     self.storage.head.prev = self.storage.tail
        #     self.storage.tail.next = self.storage.head
        #     # set current item to head
        #     self.current = self.storage.head

        # if not at cap
        if self.storage.length < self.capacity:
            # add item
            self.storage.add_to_tail(item)
            # move older items
            self.storage.head.prev = self.storage.tail
            self.storage.tail.next = self.storage.head
            # set current item to head
            self.current = self.storage.head
        # if at cap
        else:
            # set new val to current
            self.current.value = item
            # move current
            self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        current = self.storage.head

        while True:
            if current.value is not None:
                list_buffer_contents.append(current.value)

            if current is self.storage.tail:
                break

            current = current.next

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
