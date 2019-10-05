s = input()
q = int(input())
for i in range(0, q):
    args = input().split()
    if args[0] == "print":
        print(s[int(args[1]): int(args[2]) + 1])
    elif args[0] == "reverse":
        tmp = s[0: int(args[1])]
        tmp += s[int(args[1]): int(args[2]) + 1][::-1]
        tmp += s[int(args[2]) + 1:]
        s = tmp
    elif args[0] == "replace":
        s = s[0:int(args[1])] + args[3] + s[int(args[2]) + 1:]
