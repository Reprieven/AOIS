from src.rus_to_int import rus_to_int
from src.row import Row
class HashTable():
    def __init__(self, size: int):
        self.size = size
        self.table = [None]*size
    
    def find_v(self, key: str):
        char_num = 2
        v_value = 0
        if len(key) < char_num:
            raise ValueError("Размер ключа меньше количества необходимых значений")
        for i in range(char_num):
            char_int = rus_to_int(key[i])
            v_value+= char_int*33**(char_num-i-1)
        return v_value
    
    def hash(self, key: str):
        return self.find_v(key) % self.size
    
    def insert(self, key:str, value: str):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = Row(key, value)
        else:
            current = self.table[index]
            while current.next is not None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next

            if current.key == key:
                current.value = value
            else:
                current.next = Row(key, value)

    def search(self, key: str):
        index = self.hash(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def delete(self, key: str):
        index = self.hash(key)
        current = self.table[index]
        prev = self.table[index]
        if current is None:
            return
        if current.key == key:
            self.table[index] = current.next
            return
        current = current.next
        while current is not None:
            if current.key == key:
                prev.next = current.next
                return
            prev, current = current, current.next


        
        