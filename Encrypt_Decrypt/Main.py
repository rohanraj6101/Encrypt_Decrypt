# Encryption of Text

from cryptography.fernet import Fernet

key=Fernet.generate_key()
print(key)
print()
cipher_suite=Fernet(key)

text="this is not done, until i am Dead...!"

encrypted_text=cipher_suite.encrypt(text.encode())
print('encrypted: ',encrypted_text)

decrypted_text=cipher_suite.decrypt(encrypted_text).decode()
print('Decrypted: ',decrypted_text)


#Decryption  of Text

from cryptography.fernet import Fernet
key = b'PLf1AoMC5aDp0irsbwZNMotK0g98TV5K9AFdYzQbvqg='
cipher_suite = Fernet(key)
encrypted_text =   b'gAAAAABlYMPgDcgYMOQ10hg0w-VpXHg8H-2IkX7LybU21jy5qfVfUyJ7Qf1kbxgGS8tpoQvgD8HrjMaG7gWNZavN5mUaIrsuTZgzrSoCG3PmWnaJvcn0ZTqUDJdn-E3rIzMz-0TKIGMJ'

decrypted_text = cipher_suite.decrypt(encrypted_text).decode()

print('Decrypted:', decrypted_text)






# # Encryption of Image

from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
print()
cipher_suite = Fernet(key)

with open('kli.jpg', 'rb') as file:
    image_data = file.read()
encrypted_image_data = cipher_suite.encrypt(image_data)
with open('encrypted_123.jpg', 'wb') as file:
    file.write(encrypted_image_data)
with open('encryption_key.key', 'wb') as key_file:
    key_file.write(key)
print('Image encrypted successfully!')



# #Decryption of image

from cryptography.fernet import Fernet
with open('encryption_key.key', 'rb') as key_file:
    key = key_file.read()
cipher_suite = Fernet(key)
with open('encrypted_123.jpg', 'rb') as file:
    encrypted_image_data = file.read()

decrypted_image_data = cipher_suite.decrypt(encrypted_image_data)

with open('decrypted_123.jpg', 'wb') as file:
    file.write(decrypted_image_data)

print('Image decrypted successfully!')



