import base64
from rich import print

#XOR the data with the provided key.
def xor_with_key(data: bytes, key: str) -> bytes:
    key_bytes = key.encode('utf8')
    return bytes([data[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(data))])

# Ask the user if they want to encode or decode a message
print("[bright_magenta]Do you want to encode or decode a message? [yellow][bold](e)[not bold]ncode/[bold](d)[not bold]ecode")
response = input().strip().lower()

# Ask the user for a key file
print("[bright_magenta]Enter a key file for encryption/decryption: [yellow]default is [bold]'key.txt'")
key_file = input().strip()
if key_file == "":
    key_file = "key.txt"
try:
    # Read the key from the specified file
    with open(key_file, 'r') as keyfile:
        key = keyfile.read().strip()
    if key == "":
        print("[bright_red]Key file is empty. Exiting.")
        exit(1)
except FileNotFoundError:
    print(f"[bright_red]Key file '{key_file}' not found. Exiting.")
    exit(1)
except Exception as e:
    print(f"[bright_red]An error occurred while reading the key file: {e}")
    exit(1)

match response:
    case "encode" | "e":
        try:
            # Read the plaintext message from a file
            with open('plaintext.txt', 'r') as plaintextfile:
                plaintext = plaintextfile.read()
            
            # XOR the plaintext with the key
            xor_result = xor_with_key(plaintext.encode('utf8'), key)
            
            # Encode the XORed result using Base64
            ciphertext_message = base64.b64encode(xor_result).decode('utf8')
            
            # Save the ciphertext message to a file
            with open('output.txt', 'w') as output_file:
                output_file.write(ciphertext_message)
            
            print("[bright_green]Message encoded and saved to [bold]'output.txt'.")
        except FileNotFoundError:
            print("[bright_red]'plaintext.txt' not found. Please create the file with the message to encode.")
            exit(1)
        except Exception as e:
            print(f"[bright_red]An error occurred during encoding: {e}")
            exit(1)

    case "decode" | "d":
        try:
            # Read the Base64 ciphertext message from a file
            with open('ciphertext.txt', 'r') as ciphertext_file:
                ciphertext_message = ciphertext_file.read()
            
            # Decode the Base64 message
            decoded_base64 = base64.b64decode(ciphertext_message.encode('utf8'))

            # XOR the decoded Base64 result with the key
            decoded_message = xor_with_key(decoded_base64, key).decode('utf8')
            
            # Save the decoded message to a file
            with open('output.txt', 'w') as output_file:
                output_file.write(decoded_message)
            
            print("[bright_green]Message decoded and saved to [bold]'output.txt'.")
        except FileNotFoundError:
            print("[bright_red]'ciphertext.txt' not found. Please ensure the file exists for decoding.")
            exit(1)
        except base64.binascii.Error:
            print("[bright_red]Decoding failed. The ciphertext message may be corrupted or invalid.")
            exit(1)
        except Exception as e:
            print(f"[bright_red]An error occurred during decoding: {e}")
            exit(1)

    case _:
        print("[bright_red]Invalid response. Please enter [bold]'(e)ncode' [not bold]or [bold]'(d)ecode'.")
        exit(1)