word_list = "dictionary.txt"
word = input("Enter word: ").lower()

def is_anagram(str1, str2):
	return sorted(str1) == sorted(str2)

with open(word_list, "r") as word_list:
	for w in word_list:
		if is_anagram(word, w.replace("\n", "")):
			if w.strip() != word.strip(): print(w)
		