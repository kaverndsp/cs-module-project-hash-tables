from linkedlist import Node, LinkedList


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [LinkedList()] * capacity
        self.count = 0
        self.resizeWhenLoadFactorGreaterThan = 0.7

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        hval = 0x811c9dc5
        fnv_32_prime = 0x01000193
        for s in key:
            hval = hval ^ ord(s)
            hval = (hval * fnv_32_prime) % self.capacity
        return hval

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        for index in self.storage:
            node_with_key = self.__find_node_with_key_in_ll(index, key)
            if node_with_key is not None:
                node_with_key.value.value = value
                return

        if self.get_load_factor() > self.resizeWhenLoadFactorGreaterThan:
            self.resize(self.capacity * 2)

        node = Node(HashTableEntry(key, value))
        index = self.fnv1(key)
        self.storage[index].insert_at_head(node)

        self.count += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] == None:
            return
        else:
            self.storage[index] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # index = self.hash_index(key)
        # value = self.storage[index]
        # return value
        hash = 0
        for char in str(key):
            hash += ord(char)
            if char is None:
                return None
        return hash % self.capacity

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """

        self.capacity = new_capacity

        new_data = []

        for ll_at_index in self.data:
            cur = ll_at_index.head
            while cur is not None:
                kv = {}
                kv["key"] = cur.value.key
                kv["value"] = cur.value.value
                new_data.append(kv)
                cur = cur.next

        self.data = [LinkedList()] * self.capacity
        for kv in new_data:
            self.put(kv["key"], kv["value"])

     def __find_node_with_key_in_ll(self, linkedlist, key): 
        cur = linkedlist.head
        while cur is not None:
            if cur.value.key == key:
                return cur
            cur = cur.next
        return None


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
