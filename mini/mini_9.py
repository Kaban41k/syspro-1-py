class LRUCache:
    def __init__(self, capaсity=3):
        self.capaсity = capaсity
        self.cache = {}
        self.keys = []

    def put(self, key, value):
        if len(self.keys) == self.capaсity:
            self.cache.pop(self.keys[-1])
            self.keys[-1] = key
        else:
            self.keys.append(key)

        self.cache[key] = value

    def get(self, key):
        if key not in self.keys:
            return None

        self.keys.remove(key)
        self.keys.insert(0, key)

        return self.cache[key]


cache = LRUCache()

cache.put(1, 2)
cache.put(2, 3)
# 1 2
print(cache.get(1))
cache.put(3, 4)
# 1 2 3
print(cache.get(3))
cache.put(4, 5)
# 1 3 4
print(cache.get(1))
print(cache.get(2))
cache.put(5, 6)
# 1 3 5

"""
output:
2
4
2
None
"""
