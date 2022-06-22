num = int(input("Enter a number: "))
num_sq = num ** 2
converted_num = str(num)
converted_num_sq = str(num_sq)

anagram_find = converted_num_sq.rfind(converted_num)
if anagram_find:
    print(converted_num, "is an anagram of", converted_num_sq)
else:
    print(converted_num, "is not an anagram of", converted_num_sq)
