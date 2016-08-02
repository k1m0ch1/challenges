def main():
	print occurences("What The Fuck was happen?!?!?!..")
	return;

#this only count small letter
#no-big-letter
#unicode characte un-supported
def occurences(word):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	hasil = ""
	for x in alphabet:
		hasil += str(x) + "," + str(word.count(x)) + "\n" if word.count(x)>0 else ""
	return hasil

main()