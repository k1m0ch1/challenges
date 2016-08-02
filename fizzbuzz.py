def main():
	for x in range(1, 21):
		hasil = ""
		hasil += "fizz" if x%3==0 else ""
		hasil += "buzz" if x%5==0 else ""
		hasil = x if hasil=="" else hasil

		print hasil
	return;

main()