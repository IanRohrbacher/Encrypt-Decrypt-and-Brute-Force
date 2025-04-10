import base64
from rich import print

# XOR the data with the provided key.
def xor_with_key(data: bytes, key: str) -> bytes:
    key_bytes = key.encode('utf8')
    return bytes([data[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(data))])

READ_KEY = 'g'
QUIT_KEY = 'q'

CORRECT_KEY_FILE = "key.txt"

# Ask the user for a input file
print("[bright_magenta]Enter a file to read ciphertext from: [yellow]default is [bold]'ciphertext.txt'")
ciphertext_file = input().strip()
if ciphertext_file == "":
    INPUT_FILE = "ciphertext.txt"
else:
    INPUT_FILE = ciphertext_file

# Ask the user for a key file
print("[bright_magenta]Enter a file to read a guessing key from: [yellow]default is [bold]'guess_key.txt'")
guessing_file = input().strip()
if guessing_file == "":
    GUESS_KEY_FILE = "guess_key.txt"
else:
    GUESS_KEY_FILE = guessing_file

print(f"[italic dark_sea_green2]Input:'{INPUT_FILE}' Key:'{GUESS_KEY_FILE}'")


print(f"[bright_magenta]Try to Guess the Key! [bold yellow]'{QUIT_KEY}'[not bold bright_magenta] to quit, [bold yellow]'{READ_KEY}'[not bold bright_magenta] to guess!")
while(True):

    # records user input
    response = input().strip().lower()
    if response == QUIT_KEY:
        print("[bright_red]Exiting...")
        exit(0)
    elif response == READ_KEY:

        # decrypt the message with the guessed key
        try:
            # Read the Base64 ciphertext message from a file
            with open(INPUT_FILE, 'r') as input_file:
                input_message = input_file.read()
            
            # Read the guessed key from the file
            with open(GUESS_KEY_FILE, 'r') as guess_key_file:
                guessed_key = guess_key_file.read().strip()
            
            # Decode the Base64 message
            guess_decoded_base64 = base64.b64decode(input_message.encode('utf8'))
            # XOR the decoded Base64 result with the guessed key
            guess_decoded_message = xor_with_key(guess_decoded_base64, guessed_key).decode('utf8')

        except FileNotFoundError:
            print(f"[bright_red]'{INPUT_FILE}' or '{GUESS_KEY_FILE}' not found. Please ensure the files exist for decoding.")
            exit(1)
        except base64.binascii.Error:
            print(f"[bright_red]Decoding failed. {INPUT_FILE}'s message may be corrupted or invalid.")
            exit(1)
        except Exception as e:
            print(f"[bright_red]An error occurred during decoding: {e}")
            exit(1)
        
        # decrypt the message with the correct key
        try:
            # Read the Base64 ciphertext message from a file
            with open(INPUT_FILE, 'r') as correct_input_file:
                correct_message = correct_input_file.read()
            
            # Read the correct key from the file
            with open(CORRECT_KEY_FILE, 'r') as correct_key_file:
                correct_key = correct_key_file.read().strip()
            
            # Decode the Base64 message
            correct_decoded_base64 = base64.b64decode(correct_message.encode('utf8'))
            # XOR the decoded Base64 result with the correct key
            correct_decoded_message = xor_with_key(correct_decoded_base64, correct_key).decode('utf8')

        except FileNotFoundError:
            print(f"[bright_red]'{CORRECT_KEY_FILE}' not found. Please ensure the file exists for decoding.")
            exit(1)
        except base64.binascii.Error:
            print(f"[bright_red]Decoding failed. {CORRECT_KEY_FILE}'s message may be corrupted or invalid.")
            exit(1)
        except Exception as e:
            print(f"[bright_red]An error occurred during decoding: {e}")
            exit(1)

        # print(correct_decoded_message)
        # print("[bright_magenta]-------------------------------------")
        # print(guess_decoded_message)

        if correct_decoded_message == guess_decoded_message:
            with open(GUESS_KEY_FILE, 'r') as guess_file:
                print(f"[bold bright_green]Correct Key! [reset]{guess_file.read()}")
            print(f"[bold bright_green]Decoded message: [reset]{correct_decoded_message}")
            break
        else:
            with open(GUESS_KEY_FILE, 'r') as guess_file:
                print(f"[bold bright_red]Incorrect Key! [reset]{guess_file.read()}")
            print(f"[bold bright_red]Decoded message: [reset]{guess_decoded_message}")
            print(f"[bright_magenta]Try Again to Guess the Key! [bold yellow]'{QUIT_KEY}'[not bold bright_magenta] to quit, [bold yellow]'{READ_KEY}'[not bold bright_magenta] to guess!\n")
    else:
        print("[bright_red]Invalid input. [bright_magenta]Please enter [bold yellow]'g'[not bold bright_magenta] to guess the key or [bold yellow]'q'[not bold bright_magenta] to quit.")
