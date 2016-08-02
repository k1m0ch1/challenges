def main():
	for x in range(1, 21):
		print fizzorbuzz(x)
	return;

def fizzorbuzz(angka):
	hasil = "";
	if angka%3==0:
		hasil += "fizz"
	if angka%5==0:
		hasil += "buzz"
	if hasil=="":
		hasil = angka

	return hasil;

main()