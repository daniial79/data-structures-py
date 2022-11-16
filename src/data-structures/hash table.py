class HashTable:
    def __init__(self, size = 11):
        self.data_map = [None] * size

    def __hash(self, key):
        hash_base = 0
        for letter in key:
            hash_base = (hash_base + ord(letter) * 23) % len(self.data_map)
        return hash_base

    def set_item(self, key, value):
        bucket_index = self.__hash(key)
        if self.data_map[bucket_index] is None:
            self.data_map[bucket_index] = []
        self.data_map[bucket_index].append((key, value))
        return True

    def get_item(self, key):
        bucket_index = self.__hash(key)
        for pair in self.data_map[bucket_index]:
            if pair[0] == key:
                return pair[1]
        return None

    def print_keys(self):
        for index, bucket in enumerate(self.data_map):
            if bucket is None:
                print(index, " : ", None)
            else:
                for pair in bucket:

                    print(index, " : ", pair[0])
    
    def keys(self):
        all_keys = []
        for bucket in self.data_map:
            if bucket is not None:
                for pair in bucket:
                    all_keys.append(pair[0])
        return all_keys