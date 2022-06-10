morse_code= {'A': '.-', 'B': '-...',
           	   'C': '-.-.', 'D': '-..', 'E': '.',
           	   'F': '..-.', 'G': '--.', 'H': '....',
           	   'I': '..', 'J': '.---', 'K': '-.-',
           	   'L': '.-..', 'M': '--', 'N': '-.',
           	   'O': '---', 'P': '.--.', 'Q': '--.-',
           	   'R': '.-.', 'S': '...', 'T': '-',
           	   'U': '..-', 'V': '...-', 'W': '.--',
           	   'X': '-..-', 'Y': '-.--', 'Z': '--..',
           	   '1': '.----', '2': '..---', '3': '...--',
           	   '4': '....-', '5': '.....', '6': '-....',
           	   '7': '--...', '8': '---..', '9': '----.',
           	   '0': '-----', ',': '--..--', '.': '.-.-.-',
           	   '?': '..--..', ' ': '/', '-': '-....-',
           	   '(': '-.--.', ')': '-.--.-'
           }
reverse_dict={
    morse_code[key]: key for key in morse_code
}
def encrypt(data):
    result=''
    for ch in data.upper():
        result += morse_code.get(ch , ch)
        result += ' '
    return result.strip()
def decrypt(data):
    result=''
    for ch in data.split():
         result += reverse_dict.get(ch , ch)
    return result

data="hii bro ."
encrypted=encrypt(data)
decrypted=decrypt(encrypted)
print(encrypted)
print(decrypted)


