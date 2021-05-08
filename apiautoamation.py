# import requests
#
# response = requests.get("http://216.10.245.166/Library/GetBook.php?AuthorName=RahulShetty")
# print(type(response.headers))
a = [0, 1, 2, 3, 4, 5]
b = []
m = 1
n = m
for i in a: #range(1,len(a)+1)
    b.append(a[m])
    m = m + 1
    if m == len(a):
        break
for j in range(n):
    b.append(a[j])
print(b)
