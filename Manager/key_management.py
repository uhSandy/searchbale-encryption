import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding as symmetric_padding
import os
import json



def utf8(s: bytes):
    return str(s, 'utf-8')

def generate_random_symmetric_key():
    # Generate a random symmetric key for encryption
    return os.urandom(32)  # 32 bytes for AES-256

def generate_random_iv():
    # Generate a random initialization vector (IV)
    return os.urandom(16)  # 16 bytes for AES block size


def encrypt_symmetric_key(symmetric_key, public_key):
    # Encrypt the symmetric key using the public key
    encrypted_key = public_key.encrypt(
        symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_key

def decrypt_symmetric_key(encrypted_key, private_key):
    # Decrypt the symmetric key using the private key
    symmetric_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return symmetric_key

def generatekeys():
    # Generate sender's and recipient's RSA key pairs
    sender_private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    recipient_private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

    sender_public_key = sender_private_key.public_key()
    recipient_public_key = recipient_private_key.public_key()

    print("sender_public_key", type(sender_public_key))
    print("recipient_public_key:", recipient_public_key)

    # -----------------------------------sender_private_key
    # Convert the public key to the PEM format
    pem_data1 = sender_private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Write the PEM-encoded public key to a file
    with open('../keys/sender_private_key.pem', 'wb') as file:
        file.write(pem_data1)

    # -----------------------------------sender_public_key
    # Convert the public key to the PEM format
    pem_data2 = sender_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Write the PEM-encoded public key to a file
    with open('../keys/sender_public_key.pem', 'wb') as file:
        file.write(pem_data2)

    # -----------------------------------recipient_private_key
    # Convert the public key to the PEM format
    pem_data3 = recipient_private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Write the PEM-encoded public key to a file
    with open('../keys/recipient_private_key.pem', 'wb') as file:
        file.write(pem_data3)

    # -----------------------------------recipient_public_key
    # Convert the public key to the PEM format
    pem_data4 = recipient_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Write the PEM-encoded public key to a file
    with open('../keys/recipient_public_key.pem', 'wb') as file:
        file.write(pem_data4)

    print("******************END of key generation*************************************")

def tempkeygeneration():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open('../keys/private_key.pem', 'wb') as f:
        f.write(private_pem)

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open('../keys/public_key.pem', 'wb') as f:
        f.write(public_pem)

    with open("../keys/private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )