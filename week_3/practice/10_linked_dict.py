# hash

class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8)
            self.items.append(LinkedTuple())

    def put(self, key, value):
        idx = hash(key)%8
        self.items[idx].add(key, value)
        return

    def get(self, key):
        idx = hash(key) % 8
        return


my_dict = Dict()
my_dict.put("cat",'ben')
print(my_dict.get("cat"))
