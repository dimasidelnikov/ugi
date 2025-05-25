def analyze_text(text):
    symbols = len(text)
    words = len(text.split())
    sentences = text.count('.') + text.count('!') + text.count('?')
    paragraphs = text.count('\n') + 1 if text else 0

    return {
        "Символів": symbols,
        "Слів": words,
        "Речень": sentences,
        "Абзаців": paragraphs
    }

if __name__ == "__main__":
    print("📝 Введіть текст для аналізу (завершіть введення двома ентерами):")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = "\n".join(lines)
    result = analyze_text(text)

    print("\n📊 Результат аналізу:")
    for k, v in result.items():
        print(f"{k}: {v}")
