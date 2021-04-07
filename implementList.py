
class arraylist():

    array = [None] * 16
    size = 0
    capacity = 16

    def size():
        return size
    
    def capacity():
        return capacity

    def is_empty():
        return size == 0

    def at(index):
        if index >= size:
            raise Exception("IndexOutOfBounds")
        return array[index]

    def push(item):
        insert(size, item)

    def insert(index, item):
        if size == capacity:
            resize(capacity*2)
        for i in range(size, index, -1):
            array[i] = array[i-1]
        array[index] = item
        size += 1

    def prepend(item):
        insert(item, 0)

    def pop():
        delete(size-1)

    def delete(index):
        for i in range(index, size-1):
            array[i] = array[i+1]
        array[size] = None
        size -= 1
        if size <= capacity/4:
            resize(capacity/2)

    def remove(item):
        for i in range(size):
            if array[i] == item:
                delete(i)

    def find(item):
        for i in range(size):
            if array[i] == item:
                return i
        return -1

    def __resize(new_capacity):
        newArray = [None] * new_capacity
        for i in range(size):
            newArray[i] = array[i]
        array = newArray
        capacity = new_capacity
