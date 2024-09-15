# password_manager.py
import os
import json
from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
# You must keep this key safe. Anyone who gets this key
# can decrypt your passwords
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the key from the current directory named `key.key`
def load_key():
    return open("key.key", "rb").read()

# Encrypt the password
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Decrypt the password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Add a new password
def add_password(service, password, key):
    encrypted_password = encrypt_password(password, key)
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
    else:
        passwords = {}

    passwords[service] = encrypted_password.decode()
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)
    print(f"Password for {service} added successfully!")

# View all passwords
def view_passwords(key):
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
            for service, encrypted_password in passwords.items():
                print(f"Service: {service}, Password: {decrypt_password(encrypted_password.encode(), key)}")
    else:
        print("No passwords stored yet!")

# Main function to interact with the user
def main():
    if not os.path.exists("key.key"):
        print("Key not found. Generating a new key...")
        generate_key()

    key = load_key()

    while True:
        print("\nPassword Manager")
        print("1. Add a new password")
        print("2. View all passwords")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            service = input("Enter the service name: ")
            password = input("Enter the password: ")
            add_password(service, password, key)
        elif choice == "2":
            view_passwords(key)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
