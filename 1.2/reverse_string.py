def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print("Реверс рядка:", reverse_string("hello"))
