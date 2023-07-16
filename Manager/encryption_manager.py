
import base64
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding as symmetric_padding
import os
import Manager.key_management
import json


def encrypt_file_content(data, filename):
    print("encryption started")

    with open("../keys/recipient_public_key.pem", "rb") as key_file:
        recipient_public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    # Encrypt data using sender's public key
    dict_str = json.dumps(data)
    bytes_data = dict_str.encode('utf-8')
    encrypted_key, iv, encrypted_data = encrypt_large_data(bytes_data, recipient_public_key)

    # save one time encrypted key
    with open('../keys/encrypted_key.bin', 'wb') as file:
        file.write(encrypted_key)
    # save one time iv
    with open('../keys/iv.bin', 'wb') as file:
        file.write(iv)

    # Save encrypted files
    with open(f"../data/{filename}_encrypted.bin", 'wb') as file:
        file.write(encrypted_data)

    print("file encrypted successfully")


def encrypt_file(filePath):
    print("encryption started")
    with open(filePath, 'rb') as file:
        file_content = file.read()
        #print(file_content)
        file_name = os.path.splitext(os.path.basename(filePath))[0]

        # Load public key
        with open("../keys/public_key.pem", "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )

        # Encrypt the file content
        encrypted_content = public_key.encrypt(
            file_content,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # Save encrypted files
        with open(f"../documents/{file_name}_encrypted.bin", 'wb') as file:
            file.write(encrypted_content)

        print("file encrypted successfully")

#encrypt_file_content("../documents/Book1.csv")

def decryptFile(filePath, secretKey):

    with open('../keys/iv.bin', 'rb') as file:
        byte_dataiv = file.read()
    #print(byte_dataiv)

    # Open the file in write mode ('w') and write the new data
    with open('../keys/encrypted_key.bin', 'rb') as file:
        byte_dataencrypted_key = file.read()

    with open("../keys/recipient_private_key.pem", "rb") as key_file:
        recipient_private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    # Read the encrypted data from the file
    with open(filePath, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = decrypt_large_data(byte_dataencrypted_key, byte_dataiv, encrypted_data, recipient_private_key)
    #print("Decrypted data:", decrypted_data)

    return decrypted_data
    # with open("../keys/private_key.pem", "rb") as key_file:
    #     private_key = serialization.load_pem_public_key(
    #         key_file.read(),
    #         backend=default_backend()
    #     )
    #
    # # Read the encrypted data from the file
    # with open(filePath, 'rb') as file:
    #     encrypted_data = file.read()
    #
    # decrypted = private_key.decrypt(
    #     base64.b64decode(encrypted_data),
    #     padding.OAEP(
    #         mgf=padding.MGF1(algorithm=hashes.SHA256()),
    #         algorithm=hashes.SHA256(),
    #         label=None
    #     )
    # )
    #
    # decrypted_text = decrypted.decode('utf-8')
    #
    # # Print the decrypted text
    # print("decrypted data received successfully")
    # print(decrypted_text)
    # return decrypted_text

def encrypt_large_data(data, public_key):
    # Generate a random symmetric key
    symmetric_key = Manager.key_management.generate_random_symmetric_key()

    # Encrypt the symmetric key using the public key
    encrypted_key = Manager.key_management.encrypt_symmetric_key(symmetric_key, public_key)

    # Generate a random initialization vector (IV)
    iv = Manager.key_management.generate_random_iv()

    # Encrypt the data using the symmetric key and IV
    cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = symmetric_padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    #print("encrypted data:", encrypted_data)
    return encrypted_key, iv, encrypted_data

def decrypt_large_data(encrypted_key, iv, encrypted_data, private_key):
    #print("Decrypt data started")
    # Decrypt the symmetric key using the private key
    symmetric_key = Manager.key_management.decrypt_symmetric_key(encrypted_key, private_key)

    # Decrypt the data using the symmetric key and IV
    cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = symmetric_padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return unpadded_data
#print(decryptFile("../documents/index_encrypted.bin", ''))
# plaintext = b'this is the correct plaintext!'
# print(f'plaintext: \033[1;33m{utf8(plaintext)}\033[0m')
# encrypted = base64.b64encode(public_key.encrypt(
#     plaintext,
#     padding.OAEP(
#         mgf=padding.MGF1(algorithm=hashes.SHA256()),
#         algorithm=hashes.SHA256(),
#         label=None
#     )
# ))
# print(f'encrypted: \033[1;32m{utf8(encrypted)}\033[0m')
#
#
# decrypted = private_key.decrypt(
#     base64.b64decode(encrypted),
#     padding.OAEP(
#         mgf=padding.MGF1(algorithm=hashes.SHA256()),
#         algorithm=hashes.SHA256(),
#         label=None
#     )
# )
# print(f'decrypted: \033[1;31m{utf8(decrypted)}\033[0m')
