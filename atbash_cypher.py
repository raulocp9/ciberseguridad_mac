import sys
import argparse

# Python program to implement Atbash Cipher

# This script uses dictionaries to lookup various alphabets
lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
		'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
		'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
		'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
		'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}

def atbash(message):
	cipher = ''
	for letter in message:
		# checks for space
		if(letter != ' '):
			#adds the corresponding letter from the lookup_table
			cipher += lookup_table[letter]
		else:
			# adds space
			cipher += ' '

	return cipher

# Driver function to run the program
def main():
	
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="encrypts the message given by command line using the atbash cipher", type=str)
    args = parser.parse_args()
    message = args.n

	#encrypt the given message
    #print('\t\t This program implement the atbash cypher\n\n')
    #print('Enter a message to encrypt')
    #message = input()
    print(atbash(message.upper()))
	
	#decrypt the given message
    #message = 'TVVPH ULI TVVPH'
    #print(atbash(message.upper()))


# Exhecutes the main function
if __name__ == '__main__':
	main()
