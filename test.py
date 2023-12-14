class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # A simple hash function using the length of the key
        return len(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        # If the index is empty, create a list to store key-value pairs
        if self.table[index] is None:
            self.table[index] = []

        # Check if the key already exists and update the value
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        # Add a new key-value pair
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)

        # If the index is empty, key does not exist
        if self.table[index] is None:
            return None

        # Search for the key in the list at the computed index
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        # Key not found
        return None


# Example usage
hash_table = HashTable(size=10)

hash_table.insert("name", "John")
hash_table.insert("age", 25)

print("Name:", hash_table.get("name"))
print("Age:", hash_table.get("age"))
print("City:", hash_table.get("city"))  # Should print None as "city" is not in the hash table
