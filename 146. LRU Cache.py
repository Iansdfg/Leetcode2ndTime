class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = []
        self.Dic = dict()
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.Dic:
            return -1
        self.cache.remove(key)
        self.cache.append(key)
        return self.Dic[key]
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.Dic[key] = value
            self.cache.remove(key)
            self.cache.append(key)
        else:
            if len(self.cache) == self.capacity:
                del_key = self.cache[0]
                self.cache = self.cache[1:]
                del self.Dic[del_key]
            self.cache.append(key)
            self.Dic[key] = value
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
