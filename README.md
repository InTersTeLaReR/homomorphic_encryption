# Homomorphic Encryption for Financial Data

This project implements homomorphic encryption to securely encrypt and decrypt financial transactions using the Paillier cryptosystem. It is built with Streamlit, allowing users to submit transaction data that is securely encrypted and visible only to the admin with the proper access code.

## Features

- **Data Encryption:** Encrypts financial data on the client-side using the Paillier encryption scheme.
- **Decryption for Admin:** Allows an admin to decrypt and view the transaction data securely.
- **Streamlit Web App:** A user-friendly interface built with Streamlit to submit financial transactions and view results in real-time.
- **Admin Panel:** A secure admin panel to view the decrypted financial data, accessible only with an admin password.

## Tech Stack

- **Python 3.x**
- **Streamlit** - for building the interactive web app.
- **Paillier Homomorphic Encryption** - implemented using the `phe` library for secure data encryption and decryption.
- **Git** - version control system to manage the project.

## Installation

Follow these steps to set up the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/homomorphic_encryption.git
cd homomorphic_encryption
