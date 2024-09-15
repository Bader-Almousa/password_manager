# password_manager

**Password Manager** is a simple, secure, and open-source tool to manage your passwords safely using encryption. This tool allows you to store, retrieve, and manage passwords for different services securely on your local machine.

## Features

- **Secure Storage**: Passwords are encrypted using a generated encryption key before being stored.
- **Easy to Use**: Simple command-line interface to add and view passwords.
- **Local Storage**: All data is stored locally, providing an added layer of security.
- **Open Source**: Fully customizable and extendable by the community.

## Installation

To use the Password Manager tool, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/bader-almousa/password_manager.git

2. **Navigate to the project directory:

cd password_manager

3. **Install the required dependencies:

You need to have Python installed on your machine. Install the dependencies using pip:
pip install -r requirements.txt

4. **Run the tool:
python password_manager.py

## How to Use
Once the tool is running, you can perform the following actions:

** Add a New Password
To add a new password for a service:

Run the tool by executing python password_manager.py.
Select option 1 to add a new password.
Enter the name of the service (e.g., "Snapchat").
Enter the password for the service.
Example:

Password Manager
1. Add a new password
2. View all passwords
3. Quit
Enter your choice: 1
Enter the service name: Snapchat
Enter the password: mySnapchatPassword123!
Password for Snapchat added successfully!

** View All Passwords
To view all stored passwords:

Run the tool by executing python password_manager.py.
Select option 2 to view all passwords.
The tool will display a list of all services with their decrypted passwords.
Example:

Password Manager
1. Add a new password
2. View all passwords
3. Quit
Enter your choice: 2
Service: Snapchat, Password: mySnapchatPassword123!

## Benefits
Enhanced Security: By encrypting passwords using the cryptography library, it ensures that even if someone accesses the password file, they won't be able to read the passwords without the encryption key.
Local and Private: Unlike other password managers that store data on the cloud, this tool keeps all information local to your machine, reducing the risk of data breaches.
Open Source and Customizable: You can customize the tool according to your needs, add more features, or integrate it with other tools.
No Need for a Master Password: The tool uses an encryption key saved locally instead of a master password, providing a different layer of security.
Contributing
This project is open source, and contributions are welcome! If you have suggestions for improvement or want to add new features, feel free to fork the repository and submit a pull request.

# Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.
License
This project is licensed under the MIT License. You are free to use, modify, and distribute this project as you wish.

# Contact
For more information, suggestions, or inquiries, feel free to contact me or visit my GitHub profile: Bader-almousa.

Feel free to use and modify this tool. Enjoy managing your passwords securely!
