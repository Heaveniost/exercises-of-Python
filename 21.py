# import os, base64
# from hashlib import sha256
# from hmac import HMAC


# def encrypt_password(password, salt=None):
#     """Hash password on the fly."""
#     if salt is None:
#         salt = os.urandom(8)  # 64 bits.

#     assert 8 == len(salt)
#     assert isinstance(salt, bytes)
#     assert isinstance(password, str)
    
#     if isinstance(password, str):
#         password = password.encode('UTF-8')

#     assert isinstance(password, bytes)

#     result = password
#     for i in range(10):
#         result = HMAC(result, salt, sha256).digest()

#     return salt + result


# def validate_password(hashed, input_password):
#     return hashed == encrypt_password(input_password, salt=hashed[:8])


# if __name__ == "__main__":
#     hashed = encrypt_password('secret password')
#     assert validate_password(hashed, 'secret password')
#     print (hashed)
#     print (base64.b64encode(hashed))
#     print (base64.b64decode(base64.b64encode(hashed)))

import hashlib, random 

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def store_password(password):
    salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
    pswd = get_md5(password + salt)
    return pswd 

if __name__ == '__main__':
    password = input('Input Password: ')
    encrypted_password = store_password(password)
    print(encrypted_password)
