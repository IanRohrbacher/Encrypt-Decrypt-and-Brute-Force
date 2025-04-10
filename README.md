# Encrypt, Decrypt, and Brute Force
The program `base64code.py` uses XOR bitwise operations combined with Base64 encoding for encryption and decryption. The `crack.py` script allows brute-forcing attempts the encryption by guessing the key.

## Details
This project provides tools to:
- Encrypt plaintext using a key and save the result as Base64-encoded ciphertext.
- Decrypt Base64-encoded ciphertext using the correct key.
- Brute-force the decryption by guessing the key until the correct one is found.

The encryption process involves XORing the plaintext with a key, followed by Base64 encoding. Decryption reverses this process using the same key.

## Getting Started

### Installing
1. Clone the repository or download the project files.
2. Install the required Python dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

### Running
#### Encrypting a Message
1. Create a file named `plaintext.txt` containing the message you want to encrypt.
2. Create a file named `key.txt` containing the encryption key.
3. Run the `base64code.py` script and choose the `(e)ncode` option:
   ```bash
   python base64code.py
   ```
4. The encrypted message will be saved to `output.txt`.

#### Decrypting a Message
1. Create a file named `ciphertext.txt` containing the Base64-encoded ciphertext.
2. Create a file named `key.txt` containing the decryption key.
3. Run the `base64code.py` script and choose the `(d)ecode` option:
   ```bash
   python base64code.py
   ```
4. The decrypted message will be saved to `output.txt`.

#### Brute-Forcing the Key
1. Create a file named `ciphertext.txt` containing the Base64-encoded ciphertext.
2. Create a file named `key.txt` containing the correct key for verification.
3. Create a file named `guess_key.txt` containing the guessed key.
4. Run the `crack.py` script and follow the prompts to guess the key:
   ```bash
   python crack.py
   ```
5. If the guessed key matches the correct key, the script will display the decoded message.

## Features
- **Encryption**: XOR-based encryption with Base64 encoding.
- **Decryption**: Decodes Base64 ciphertext and reverses the XOR operation.
- **Brute Force**: Allows guessing the key to decrypt the message.

## Licensing
The code in this project is licensed under the MIT license.
