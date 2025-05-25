def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            print(f"Підрядок знайдено на позиції {i}")

text = "ababababakg"
pattern = "bab"
naive_search(text, pattern)
