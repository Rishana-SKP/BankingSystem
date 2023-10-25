#BANKING SYSTEM

Link to my Video Representation on Google Drive: https://drive.google.com/file/d/1iQqVlqdNDS-zdhTQQGVTEzNBmEyYW-k3/view?usp=sharing



This Python program is a simple banking system simulation that allows users to create accounts, log in, deposit and withdraw money, and perform basic banking operations. Here's a breakdown of the key components and functionality of the program:

Bank Class: The Bank class is the core of the banking system. It has methods to create accounts, log in, deposit, and withdraw money.

create_account: Generates a random account number and creates a new account with the provided name, password, and initial balance.

login: Allows users to log in using their account number and password. If the provided credentials match an existing account, it returns the account information; otherwise, it returns None.

deposit: Allows users to deposit money into their accounts. It updates the account balance and provides feedback on the transaction.

withdraw: Allows users to withdraw money from their accounts, provided they have sufficient balance. It updates the account balance and provides feedback on the transaction.

Main Function: The main function is where the program execution begins. It creates an instance of the Bank class and initializes it with a list of customer information.

Customer Data: The customerlist contains pre-defined customer data, including account numbers, names, passwords, and initial balances.

User Interaction: The program presents a menu to the user with three options: creating a new account, logging into an existing account, and exiting the system.

If the user selects option 1, they can create a new account by providing their name, password, and initial balance. The system generates a random account number and informs the user.

If the user selects option 2, they can log in using their account number and password. After successful login, they can choose to deposit, withdraw, or log out. The user can repeat these operations until they decide to log out.

If the user selects option 3, the program terminates, ending the banking session.

Invalid choices and unsuccessful login attempts are handled with appropriate error messages.

This program provides a simplified simulation of a banking system and is designed for educational purposes. It helps users understand basic account management and interaction with a Python-based banking system.
