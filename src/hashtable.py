# '''
# Linked List hash table key/value pair
# '''

# helpful resource:
# http://linebylinecode.com/2017/11/24/how-to-implement-a-hash-table-in-python
# https://medium.com/@quinstonpimenta/implementing-a-hash-table-in-python-ff6e73bb0f94
class LinkedPair:
    def __init__(self, key, value):

        # linked list node
        self.key = key
        self.value = value
        self.next = None # this is the linked list part :)

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        # how much is initially allocated, whether in use or not
        self.capacity = capacity  # Number of buckets in the hash table

        # buckets is the internal array, storing each inserted value in a
        # a storage bucket based on the provided key
        self.buckets = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.

        Python's built in hash function! It is not deterministic.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.

        Insert (can go at any index) vs. append (only at end)

        '''
        # first, compute the index of the key using the hash_mod function
        # this returns an int
        index = self._hash_mod(key)

        # go to node pointing to the hash
        current_node = self.buckets[index]
        last_node = None

        # before putting anything in the bucket, which is a whole linked list
        # need to check that the same key does not already exist in the linked list
        while current_node != None and current_node.key != key:
            last_node = current_node
            current_node = last_node.next

        # if it does exist, need to update the key with the new value
        if current_node != None:
            current_node.value = value

        # if it doesn't exist, append the key-value pair at the end of the linked list
        else:
            new_node = LinkedPair(key, value)
            new_node.next = self.buckets[index]
            self.buckets[index] = new_node

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # first, compute the index of the key using the hash_mod function
        # this returns an int
        index = self._hash_mod(key)

        # go to node pointing to the hash
        current_node = self.buckets[index]
        last_node = None

        # before putting anything in the bucket, which is a whole linked list
        # need to check that the same key does not already exist in the linked list
        while current_node != None and current_node.key != key:
            last_node = current_node
            current_node = last_node.next

        # if it does not exist, i.e. key not found
        if current_node == None:
            print("Error")

        # if it does exist, i.e. key found
        else:
            if last_node == None:
                self.buckets[index] = current_node.next
            else:

                last_node.next = current_node.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # first, compute the index of the key using the hash_mod function
        # this returns an int
        index = self._hash_mod(key)

        # go to node pointing to the hash
        current_node = self.buckets[index]

        while current_node != None:
            if current_node.key == key:
                return current_node.value
            else:
                current_node = current_node.next

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # duplicate first
        old_buckets = self.buckets

        # double capacity of the hash table
        # this is an int
        self.capacity = 2 * self.capacity

        # create new buckets storage
        self.buckets = [None] * self.capacity

        current_node = None

        for item in old_buckets:
            current_node = item

            while current_node != None:
                # re-insert
                self.insert(current_node.key, current_node.value)
                current_node = current_node.next 



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.buckets)
    ht.resize()
    new_capacity = len(ht.buckets)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
