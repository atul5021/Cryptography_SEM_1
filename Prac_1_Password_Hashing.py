import bcrypt
pwd = input('Enter the password: ')
falsePwd = "falsepassword"
bytePwd = pwd.encode('utf-8')
byteFalsepwd = falsePwd.encode('utf-8')

# Generate salt
mySalt = bcrypt.gensalt()

# Hash password
hash = bcrypt.hashpw(bytePwd, mySalt)
print('Hashed password : ', hash)
print('Matching hashed password with entered password : ' ,bcrypt.checkpw(bytePwd, hash))
print('Matching hashed password with false password : ' ,bcrypt.checkpw(byteFalsepwd, hash))
