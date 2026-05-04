from cryptography.fernet import Fernet
import os

def generate_key():
    """Generates and saves a new encryption key."""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("-> New key generated and saved as key.key")

def load_key():
    """Loads the existing key from the project directory."""
    if not os.path.exists("key.key"):
        raise FileNotFoundError("The key file (key.key) was not found. Please generate a key first.")
    with open("key.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(input_filename, output_filename):
    """Encrypts a file and saves the encrypted version."""
    try:
        key = load_key()
        fernet = Fernet(key)

        # 1. Read the input file as text
        with open(input_filename, "r", encoding="utf-8") as file:
            file_data = file.read()

        # 2. Encrypt the data
        encrypted_data = fernet.encrypt(file_data.encode("utf-8"))

        # 3. Write the encrypted data to the output file (in binary mode)
        with open(output_filename, "wb") as file:
            file.write(encrypted_data)
        print(f"\n[SUCCESS] File encrypted and saved to {output_filename}")

    except FileNotFoundError:
        print(f"\n[ERROR] The file '{input_filename}' could not be found.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")

def decrypt_file(input_filename, output_filename):
    """Decrypts an encrypted file and saves the decrypted text."""
    try:
        key = load_key()
        fernet = Fernet(key)

        # 1. Read the encrypted file
        with open(input_filename, "rb") as file:
            encrypted_data = file.read()

        # 2. Decrypt the data
        decrypted_data = fernet.decrypt(encrypted_data)

        # 3. Save the decrypted data as plain text
        with open(output_filename, "w", encoding="utf-8") as file:
            file.write(decrypted_data.decode("utf-8"))
        print(f"\n[SUCCESS] File decrypted and saved to {output_filename}")

    except FileNotFoundError:
        print(f"\n[ERROR] The file '{input_filename}' could not be found.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred. Ensure your key and file are valid: {e}")