chars = []
def hash_map(string, k):
    HM = { }
    for char in string:
        if char in HM:
            HM[char] += 1
        else:
            HM[char] = 1
    for char in HM:
        if HM[char] == k:
            chars.append(char)
    return chars

s = "ajgljdsflajlasjfo"
k = 2
print(hash_map(s,k))