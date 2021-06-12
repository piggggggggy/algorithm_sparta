# hash

class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        idx = hash(key) % len(self.items)
        self.items[idx] = value

    def get(self, key):
        return self.items[hash(key)%len(self.items)]

my_dict = Dict()
my_dict.put("cat",'ben')
print(my_dict.get("cat"))
