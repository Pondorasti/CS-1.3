#!python

from LinkedList import LinkedList


class HashTable(object):

    def __init__(self, num_buckets=8):
        """Initialize this hash table with the given initial size."""
        self.numBuckets = num_buckets
        self.buckets = [LinkedList() for i in range(num_buckets)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.a"""
        numEntries = 0
        for bucket in self.buckets:
          numEntries += bucket.length()

        return numEntries / self.numBuckets

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table."""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Best case running time: O(1)
        Worst case running time: O(n)
        """
        # Find the bucket the given key belongs in
        bucketIndex = abs(hash(key)) % self.numBuckets
    
        # Find the entry with the given key in that bucket, if one exists
        return self.buckets[bucketIndex].find(key)

    def set(self, key, value):
        """Insert the given key with its associated value.
        Best case running time: O(1)
        Worst case running time: open
        """
        # Find the bucket the given key belongs in
        bucketIndex = abs(hash(key)) % self.numBuckets
        
        # Insert the new key-value entry into the bucket 
        if self.buckets[bucketIndex].find(key) is None:
          self.buckets[bucketIndex].append((key, value))
        else:
          self.buckets[bucketIndex].update(key, value)
        
        # resize based on load factor rating
        if self.load_factor() > 0.75:
          self._resize()

    def delete(self, key):
        """Delete the given key and its associated value, or raise KeyError.
        Best case running time: O(1)
        Worst case running time: O(n)
        """
        # Find the bucket the given key belongs in
        bucketIndex = abs(hash(key)) % self.numBuckets
        
        # Find the entry with the given key in that bucket, if one exists
        self.buckets[bucketIndex].delete(key)

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key)."""
        oldItems = self.items()
        self.buckets = [LinkedList() for i in range(self.numBuckets * 2)]
        self.numBuckets *= 2 
        for key, value in oldItems:
          self.set(key, value)
          



def test_hash_table():
    ht = HashTable(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
 
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
  
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
   
 
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

