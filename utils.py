from cryptography.fernet import Fernet
import os

def generate_key():
    
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("-> New key generated and saved as key.key")

def load_key():

    if not os.path.exists("key.key"):
        raise FileNotFoundError("The key file (key.key) was not found. Please generate a key first.")
    with open("key.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(input_filename, output_filename):
    
    try:
        key = load_key()
        fernet = Fernet(key)

        
        with open(input_filename, "r", encoding="utf-8") as file:
            file_data = file.read()

        
        encrypted_data = fernet.encrypt(file_data.encode("utf-8"))

        
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

        
        with open(input_filename, "rb") as file:
            encrypted_data = file.read()

        
        decrypted_data = fernet.decrypt(encrypted_data)

    
        with open(output_filename, "w", encoding="utf-8") as file:
            file.write(decrypted_data.decode("utf-8"))
        print(f"\n[SUCCESS] File decrypted and saved to {output_filename}")

    except FileNotFoundError:
        print(f"\n[ERROR] The file '{input_filename}' could not be found.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred. Ensure your key and file are valid: {e}")