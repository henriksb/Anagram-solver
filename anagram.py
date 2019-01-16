import argparse

def arguments():
	parser = argparse.ArgumentParser(description="Extremely simple python script to find anagrams.")
	parser.add_argument("-d", "--dictionary", help="Dictionary (wordlist) to search for anagrams", required=True)
	parser.add_argument("-w", "--word", help="Input word to find anagrams with", required=True)
	
	return vars(parser.parse_args())


def is_anagram(str1, str2):
	return sorted(str1) == sorted(str2)

		
if __name__ == "__main__":
	args = arguments()
	
	dictionary = args["dictionary"]
	word = args["word"].lower()
	
	with open(dictionary, "r") as word_list:
		for w in word_list:
			if is_anagram(word, w.replace("\n", "")):
				if w.strip() != word.strip(): print(w.replace("\n", ""))
