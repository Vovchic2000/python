n = int(input())
n %= 86400
print(n // 3600 , (n // 60) % 60 , n % 60 , sep = ':')
