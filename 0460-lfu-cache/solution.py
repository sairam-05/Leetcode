from collections import defaultdict, OrderedDict
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.val = {}                    # key -> value
        self.freq = {}                   # key -> frequency
        self.group = defaultdict(OrderedDict)  # freq -> keys
        self.minfreq = 0
    def get(self, key: int) -> int:
        if key not in self.val:
            return -1
        f = self.freq[key]
        del self.group[f][key]
        if not self.group[f]:
            del self.group[f]
            if self.minfreq == f:
                self.minfreq += 1
        self.freq[key] = f + 1
        self.group[f + 1][key] = 1
        return self.val[key]
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.val:
            self.val[key] = value
            self.get(key)
            return
        if len(self.val) == self.capacity:
            old_key,_ = self.group[self.minfreq].popitem(last=False)
            del self.val[old_key]
            del self.freq[old_key]
        self.val[key] = value
        self.freq[key] = 1
        self.group[1][key] = 1
        self.minfreq = 1
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
#460 lfu cache
