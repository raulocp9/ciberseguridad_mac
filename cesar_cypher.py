import sys
import argparse

def encrypt(text,s):

	result = ""
   # transverse the plain text
	for i in range(len(text)):
		char = text[i]
      # Encrypt uppercase characters in plain text

		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
		if (char.islower()):
			result += chr((ord(char) + s - 97) % 26 + 97)
		#else:
			#ord(char)+32
         #   pass
	return result

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='encripts the message given by command line using cesar cipher')
    parser.add_argument("message", help="message to encrypt", type=str)
    parser.add_argument('key', help='key (int)', type=int)
    args = parser.parse_args()
    message = args.message
    key = args.key

    print("Plain Text : " + message)
    print("Shift pattern : " + str(key))
    encrypted = encrypt(message, key)
    print("Cypher: " + encrypted)
    print("Decipher: " + encrypt(encrypted, 26-key))
