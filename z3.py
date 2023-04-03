tekst = input("Введите текст: ")
words = tekst.split()
repeated_word = {}
for word in words:
    if word in repeated_word:
        repeated_word[word] += 1
    else:
        repeated_word[word] = 1
longest_word = max(words, key=len)
most_repeated_word = max(repeated_word, key=repeated_word.get)
print("Самое длинное слово:", longest_word)
print("Наиболее часто встречающееся слово:", most_repeated_word)
