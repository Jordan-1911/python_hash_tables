# Jordan Washburn
# CSC 506-1 Algorithms - Module 5

# Class to represent an empty bucket
class EmptyBucket:
    pass

# HashTable class definition using linear probing
class QuadraticProbingHashTable:
    
    # Constructor with optional c1 and c2 values, as well as an optional initial
    # capacity. All buckets are assigned with an EmptyBucket() instance called
    # self.EMPTY_SINCE_START.
    def __init__(self, c1 = 1, c2 = 1, get_key_function = None, initial_capacity = 11):
        self.c1 = c1
        self.c2 = c2
        
        if get_key_function == None:
            # By default, the key of an element is itself
            self.get_key = lambda el: el
        else:
            self.get_key = get_key_function
        
        # Special constants to be used as the two types of empty buckets.
        self.EMPTY_SINCE_START = EmptyBucket()
        self.EMPTY_AFTER_REMOVAL = EmptyBucket()
        
        # Initialize all the table buckets to be EMPTY_SINCE_START.
        self.table = [self.EMPTY_SINCE_START] * initial_capacity

    def insert(self, item):
        # Get the item's key
        key = self.get_key(item)

        # Ensure that the key doesn't already exist in the table
        if self.search(key) != None:
            return False
        
        for i in range(len(self.table)):
            # Compute the bucket index
            bucket = (hash(key) + self.c1 * i + self.c2 * i * i) % len(self.table)
            
            # The item can be inserted into either type of empty bucket
            if type(self.table[bucket]) is EmptyBucket:
                self.table[bucket] = item
                return True
        
        # N buckets were probed and the item could not be inserted
        return False

    # Removes an item with a matching key from the hash table
    def remove(self, key):
        for i in range(len(self.table)):
            # Compute the bucket index
            bucket = (hash(key) + self.c1 * i + self.c2 * i * i) % len(self.table)
            
            # An empty-since-start bucket stops the search
            if self.table[bucket] is self.EMPTY_SINCE_START:
                break
            
            if self.table[bucket] is not self.EMPTY_AFTER_REMOVAL:
                if self.get_key(self.table[bucket]) == key:
                    # Remove item by setting bucket to EMPTY_AFTER_REMOVAL
                    self.table[bucket] = self.EMPTY_AFTER_REMOVAL
                    return True
        
        # An item with the specified key was not found
        return False
            
    # Searches for an item with a matching key in the hash table. Returns the
    # item if found, or None if not found.
    def search(self, key):
        for i in range(len(self.table)):
            # Compute the bucket index
            bucket = (hash(key) + self.c1 * i + self.c2 * i * i) % len(self.table)
        
            # An empty-since-start bucket stops the search
            if self.table[bucket] is self.EMPTY_SINCE_START:
                break

            if self.table[bucket] is not self.EMPTY_AFTER_REMOVAL:
                if self.get_key(self.table[bucket]) == key:
                    # Found item with matching key. Return item.
                    return self.table[bucket]
        
        # An item with the specified key was not found
        return None