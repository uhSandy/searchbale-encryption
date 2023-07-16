from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding as symmetric_padding
import os
import Manager.key_management
import json


def ind_kga_game(encryption_scheme, public_key):
    # Generate two different messages
    message1 = "Message 1"
    message2 = "Message 2"

    # Encrypt the messages with the same key
    symmetric_key = Manager.key_management.generate_random_symmetric_key()

    # Encrypt the symmetric key using the public key
    encrypted_key = Manager.key_management.encrypt_symmetric_key(symmetric_key, public_key)

    # Generate a random initialization vector (IV)
    iv = Manager.key_management.generate_random_iv()

    # Encrypt the data using the symmetric key and IV
    cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = symmetric_padding.PKCS7(128).padder()
    padded_data = padder.update(message1) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    print("encrypted data:", encrypted_data)

    #ciphertext1 = encryption_scheme.encrypt(key, message1)
    #ciphertext2 = encryption_scheme.encrypt(key, message2)

    #return ciphertext1, ciphertext2


def ind_cka_game(encryption_scheme, key, keyword):
    # Generate two different messages containing the keyword
    message1 = f"Message with keyword: {keyword}"
    message2 = f"Another message with keyword: {keyword}"

    # Encrypt the messages with the same key
    ciphertext1 = encryption_scheme.encrypt(key, message1)
    ciphertext2 = encryption_scheme.encrypt(key, message2)

    return ciphertext1, ciphertext2


# Usage example
# encryption_scheme = MyEncryptionScheme()  # Replace with your encryption scheme implementation
# key = "Secret Key"
# keyword = "important"
#
# # Test IND-KGA game
# ciphertexts_kga = ind_kga_game(encryption_scheme, key)
# print("Ciphertexts (IND-KGA):", ciphertexts_kga)
#
# # Test IND-CKA game
# ciphertexts_cka = ind_cka_game(encryption_scheme, key, keyword)
# print("Ciphertexts (IND-CKA):", ciphertexts_cka)

def tst():
    my_dictionary = {
        "apple": {"color": "red", "taste": "sweet"},
        "banana": {"color": "yellow", "taste": "sweet"},
        "orange": {"color": "orange", "taste": "sour"},
        "mango": {"color": "yellow", "taste": "sweet"}
    }

    with open("../keys/recipient_public_key.pem", "rb") as key_file:
        recipient_public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    dict_str = json.dumps(my_dictionary)
    bytes_data = dict_str.encode('utf-8')
    ind_kga_game(recipient_public_key)
    #encrypted_key, iv, encrypted_data = encrypt_large_data(bytes_data, recipient_public_key)

from __future__ import annotations

from typing import Any

def default_backend() -> Any:
    from cryptography.hazmat.backends.openssl.backend import backend

    return backend