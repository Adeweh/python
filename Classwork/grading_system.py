score = int(input("Enter a Score: "))
if 70 <= score <= 100:
    print('A')
if 60 <= score <= 69:
    print('B')
if 50 <= score <= 59:
    print('C')
if 45 <= score <= 49:
    print('D')
if 40 <= score <= 44:
    print('E')
if score < 40:
    print('F')


if 70 <= score <= 100:
    print('A')
elif 60 <= score <= 69:
    print('B')
elif 50 <= score <= 59:
    print('C')
elif 45 <= score <= 49:
    print('D')
elif 40 <= score <= 44:
    print('E')
else:
    print('F')

