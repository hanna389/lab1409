import re
from collections import Counter


def main():
    print("Hello from lab1409!")

    with open ("./text.txt", mode="r", encoding="utf-8") as file:
        text = file.read()

    words = re.findall(r"\b\w+\b", text.lower())

    words_count = {}
    total_words = len(words)

    for word in words:
        if word in words_count:
            words_count[word] = words_count[word] + 1/total_words
        else:
            words_count[word] = 1/total_words

    print("\nЧастота вживання слів у %:")
    for word, frequency in words_count.items():
        print(f"{word}: {frequency*100:.2f}%")
    
    min_len = len(min(words, key=len))
    shortest_words = set(list(word for word in words if len(word) == min_len))
    print(f"\nНайкоротші слова: {shortest_words}")

    max_len = len(max(words, key=len))
    longest_words = set(list(word for word in words if len(word) == max_len))
    print(f"\nНайдовші слова: {longest_words}")

    unique_count = len(words_count)
    print("\nКількість унікальних слів:")
    print(unique_count)

    print("\nКількість слів:")
    print(len(words))

    all_letters = "".join(words)
    letter_counts = Counter(all_letters)
    print(f"\nЛітери, що використовувалися у тексті: {sorted(list(letter_counts.keys()))}")

    if all_letters:
        most_common_letter = letter_counts.most_common(1)
        print(f"\nЛітера, що зустрічалася найчастіше: {most_common_letter}")


if __name__ == "__main__":
    main()
