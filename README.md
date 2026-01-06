# Encrypt, Decrypt, and Brute Force
Spring 2025 — CS 32301: Human Interface Computing — Class Assignment <br>
Python scripts for simple XOR encryption/decryption with Base64 encoding, plus a brute-force key guessing tool.


## Overview
This project provides tools to:
- Encrypt plaintext using a key and save the result as Base64-encoded ciphertext
- Decrypt Base64-encoded ciphertext using the correct key
- Brute-force the decryption by guessing the key

Encryption uses XOR with a key, then Base64 encoding. Decryption reverses this process.


## How to Use
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Encrypt a Message
1. Put your message in `plaintext.txt` and your key in `key.txt`.
2. Run:
   ```
   python base64code.py
   ```
3. Choose `(e)ncode` when prompted. Output is saved to `output.txt`.

### Decrypt a Message
1. Put the Base64 ciphertext in `ciphertext.txt` and the key in `key.txt`.
2. Run:
   ```
   python base64code.py
   ```
3. Choose `(d)ecode` when prompted. Output is saved to `output.txt`.

### Brute-Force the Key
1. Put the ciphertext in `ciphertext.txt`, the correct key in `key.txt`, and your guess in `guess_key.txt`.
2. Run:
   ```
   python crack.py
   ```
3. If the guess is correct, the decoded message is shown.


## Features
- XOR-based encryption with Base64 encoding
- Decryption and brute-force guessing


---
> **PERSONAL TOOL:** This is a simple Python project for learning and experimentation. Not actively maintained.
---


## License
The code in this project is licensed under the MIT license.

