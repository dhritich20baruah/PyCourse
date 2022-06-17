    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None