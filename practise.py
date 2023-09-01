def calculate_hash_value(string):
    """Helper function to calculate a
    hash value from a string."""
    h = 0
    for char in string:
        h += ord(char)
    return h % 10000   #Assuming self.MAX is 10000

hash_value = calculate_hash_value('march 6')
print(hash_value)
