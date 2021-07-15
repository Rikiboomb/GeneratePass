import string

PLAIN_TEXT = string.ascii_letters
CIPHER_TEXT = 'kWFUsDYeAxolSLTwChgNJtaMvQIzRZVrPEyfiKXGcdBunbqHjpOm'

CIPHER_TABLE = str.maketrans(PLAIN_TEXT, CIPHER_TEXT)
PLAIN_TABLE = str.maketrans(CIPHER_TEXT, PLAIN_TEXT)

def main():
    while True:
        choice = input('Шифровать или дешифровать? (En/De) ').lower()
        if choice:
            if 'en'.startswith(choice):
                process_text(CIPHER_TABLE)
                continue
            if 'de'.startswith(choice):
                process_text(PLAIN_TABLE)
                continue
        print('Пожалуйста, попробуйте снова')

def process_text(table):
    buffer = []
    while True:
        line = input('> ')
        if not line:
            break
        buffer.append(line.translate(table))
    print('\n'.join(buffer))

if __name__ == '__main__':
    main()
