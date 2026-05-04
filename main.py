import os
from utils import generate_key, encrypt_file, decrypt_file

def main():
    
    os.makedirs("data", exist_ok=True)
    
    while True:
        print("\n===========================================")
        print("   PYTHON FILE ENCRYPTION / DECRYPTION     ")
        print("===========================================")
        print("1. Generate new Encryption Key")
        print("2. Encrypt a File")
        print("3. Decrypt a File")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            generate_key()
            
        elif choice == '2':
            print("\n--- Encrypting File ---")
            input_file = input("Enter input path (e.g., data/original.txt): ").strip()
            output_file = input("Enter output path (e.g., data/encrypted.txt): ").strip()
            encrypt_file(input_file, output_file)
            
        elif choice == '3':
            print("\n--- Decrypting File ---")
            input_file = input("Enter input path (e.g., data/encrypted.txt): ").strip()
            output_file = input("Enter output path (e.g., data/decrypted.txt): ").strip()
            decrypt_file(input_file, output_file)
            
        elif choice == '4':
            print("\nExiting program. Goodbye!")
            break
            
        else:
            print("\n[INVALID INPUT] Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()