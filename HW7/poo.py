# s = "python rocks"
# print(s[1] * s.index("n"))


s = "python rocks"
for idx in range(len(s)):
    if idx % 2 == 0:
        print(s[idx])