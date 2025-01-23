
def all_variants(text):
    j = len(text)
    for start in range(j):
        for end in range(start + 1, j + 1):
            yield text[start:end]

a = all_variants("abc")
for i in a:
    print(i)