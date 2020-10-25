import hashlib
email = 'pumpkintime84@gmail.com'
hash_email = hashlib.md5(email.encode('utf-8').lower()).hexdigest()

print(hash_email)

# https://www.gravatar.com/avatar/95a53b19c1598b4ab14b7303c6fa6014