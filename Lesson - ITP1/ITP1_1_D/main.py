S = int(input())
hour = S // 3600
minute = (S % 3600) // 60
secound = (S % 3600) % 60
print(hour, minute, secound, sep=':')
