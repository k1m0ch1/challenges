def main():
	for x in range(1, 16):
		print fizzorbuzz(x)
	return;

def fizzorbuzz(angka):
	hasil = angka;
	if angka%3==0:
		hasil = "fizz";
	elif angka%5==0:
		hasil = "buzz";

	return hasil;

main()