string= "I love eden".split(" ")
print(string)

string= "I love eden".split("e")
print(string)

string= "I love eden".partition("e")
print(string)

string= "I love eden".split("f")
print(string)

string= "I love eden".partition("f")
print(string)
#will always partition into three

string= "I love eden".partition(" ")
print(string)

string = "I love eden"
a, b, c = "I love eden".split(" ")
print(b)