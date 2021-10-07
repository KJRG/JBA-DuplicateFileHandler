#  You can experiment here, it won’t be checked
import argparse


CIPHER_OFFSET = 13


def decode_caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print(text)


parser = argparse.ArgumentParser()
parser.add_argument("--file")
args = parser.parse_args()
filename = args.file
opened_file = open(filename)
encoded_text = opened_file.read()  # read the file into a string
opened_file.close()  # always close the files you've opened
decode_caesar_cipher(encoded_text, -CIPHER_OFFSET)
