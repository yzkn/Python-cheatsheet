import random
import string
from aes_cipher import AESCipher


key_text = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(32)])
plain_text = 'test message.'


cipher = AESCipher(key_text)

encrypted = cipher.encrypt(plain_text)
print(encrypted)

decrypted = cipher.decrypt(encrypted)
print(decrypted)
print(decrypted == plain_text)
