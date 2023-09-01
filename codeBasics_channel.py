##https://www.youtube.com/watch?v=ea8BRGxGmlA
"""This codes will help to know how the dictionaries in python works internally. Also to get a better idea how the
hashtable works """


##to get the array location of the parcticular
class HashTable:
    def __init__(self):
        self.MAX = 10000
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))
       # self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        return None  # Key not found

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][index]


t = HashTable()
t['march 6'] = 138
t['march 6'] = 835
t['march 3'] = 55
t['jujne 8'] = 878
t['march 17'] = 2
t['UDACITY'] = 559
print(t.get_hash('UDACITY'))

print(t.arr)
