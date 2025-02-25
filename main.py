import Coder
import Decoder


text = input("Enter text to encrypt: ")

print("Coder:   ___________________________________________")
encrypted_text = Coder.encrypt(text)
print("Cryptogram: "+encrypted_text)

print("Decoder: ___________________________________________")
decrypted_text = Decoder.decrypt(encrypted_text)
print("Decoded cryptogram: "+decrypted_text)

#
if text == decrypted_text:
    print("Algorithm work well")
else: print("Something went wrong")