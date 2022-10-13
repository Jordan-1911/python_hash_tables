# class to represent an empty bucket
class EmptyBucket:
   pass

# HashTable class definition using linear probing
class LinearProbingHashTable:

    # Constructor with optional initial capacity. All buckets are
    # assigned with an  EmptyBucket() instance called self.EMPTY_SINCE_START.
    def __init__(self, initial_capacity=10):

        # Special constants to be used as the two types of empty buckets.
        self.EMPTY_SINCE_START = EmptyBucket()
        self.EMPTY_AFTER_REMOVAL = EmptyBucket()

        # Initialize all the table buckets to be EMPTY_SINCE_START.
        self.table = [self.EMPTY_SINCE_START] * initial_capacity


    def insert(self, item):
        collisions = 0
        bucket = hash(item) % len(self.table)
        buckets_probed = 0
        while buckets_probed < len(self.table):
        # if the bucket is empty, the item can be inserted at that index.
            if type(self.table[bucket]) is EmptyBucket:
                self.table[bucket] = item
                collisions += 1
                return True, collisions 
     
        # the bucket was occupied, continue probing to next index in table.
            bucket = (bucket + 1) % len(self.table)
            buckets_probed = buckets_probed + 1

        # the entire table was full and the key could not be inserted.
        return False

    # Removes an item with a matching key from the hash table.
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        buckets_probed = 0
        while self.table[bucket] is not self.EMPTY_SINCE_START and buckets_probed < len(self.table):
            if self.table[bucket] == key:
                self.table[bucket] = self.EMPTY_AFTER_REMOVAL
        
            # the bucket was occupied (now or previously), so continue probing.
            bucket = (bucket + 1) % len(self.table)
            buckets_probed = buckets_probed + 1

    # Searches for an item with a matching key in the hash table. Returns the
    # item if found, or None if not found.
    def search(self, key):
        bucket = hash(key) % len(self.table)
        buckets_probed = 0
        while self.table[bucket] is not self.EMPTY_SINCE_START and buckets_probed < len(self.table):
            if self.table[bucket] == key:
                return self.table[bucket]
        
            # the bucket was occupied (now or previously), so continue probing.
            bucket = (bucket + 1) % len(self.table)
            buckets_probed = buckets_probed + 1

        # the entire table was probed or an empty cell was found.
        return None