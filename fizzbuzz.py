def main():
	for x in range(1, 21):
		hasil = ""
		if x%3==0:
			hasil += "fizz"
		if x%5==0:
			hasil += "buzz"
		if hasil == "":
			hasil = x

		print hasil
	return;

main()