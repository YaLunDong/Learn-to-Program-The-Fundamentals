def mystery(s):
    i = 0
    result = ''
    while not s[i].isdigit():
        result = result + s[i]
        i = i + 1

    return result

mystery('123')

ans = 0
for i in range(524,10509,2):
    ans = ans + i

print(ans)