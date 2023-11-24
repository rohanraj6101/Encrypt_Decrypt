# Encrypt_Decrypt

# Description:
This Python script demonstrates text and image encryption/decryption using the Fernet symmetric key cryptography library. 
The Fernet library provides a secure and straightforward way to encrypt and decrypt data.

# How to use for text
* Text Encryption/Decryption:
Run the first part of the script to generate a new key and encrypt/decrypt sample text.
* Predefined Text Decryption:
Uncomment the section for predefined text decryption and run the corresponding code.

# How to use for image
* Image Encryption/Decryption:
Run the section for image encryption to encrypt an image (kli.jpg).
The encrypted image will be saved as encrypted_123.jpg, and the key will be saved in encryption_key.key.

* Predefined Image Decryption:
Uncomment the section for predefined image decryption and run the corresponding code.

# Important Note
-Ensure you have the cryptography library installed (pip install cryptography).
-Customize the file names and paths according to your preferences.

# Detail view
* Text Encryption/Decryption:
Generates a new Fernet key for text encryption.
Encrypts a sample text using the generated key.
Decrypts the encrypted text back to its original form.
The key is printed to the console for reference.

* Predefined Text Decryption:
Uses a predefined Fernet key for text decryption.
Decrypts a sample encrypted text using the predefined key.
The decrypted text is printed to the console.

* Image Encryption/Decryption:
Generates a new Fernet key for image encryption.
Reads an image file (kli.jpg) and encrypts its binary data using the generated key.
Writes the encrypted image data to a new file (encrypted_123.jpg).
Writes the generated key to a separate file (encryption_key.key).
Prints a success message for image encryption.

* Predefined Image Decryption:
Reads the predefined key from the encryption_key.key file.
Reads the encrypted image data from encrypted_123.jpg.
Decrypts the encrypted image data using the predefined key.
Writes the decrypted image data to a new file (decrypted_123.jpg).
Prints a success message for image decryption.

