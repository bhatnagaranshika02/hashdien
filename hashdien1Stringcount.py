str = input()
word=input()
ans = 999
flag=True
for i in word:
    s = str.count(i)
    if word.count(i) == s:
        ans = min(s,ans)
    else:
        flag = False
        break

if flag == True:
    print(ans)
else:
    print(0)
