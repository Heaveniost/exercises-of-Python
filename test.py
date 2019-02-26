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
