import time

users = {
    "admin": "admin"
}


login_attempts = {}
blocked_users = {}

def is_blocked(username):
    if username in blocked_users:
        block_time = blocked_users[username]
        if time.time() < block_time:
            return True, int(block_time - time.time())
        else:
            del blocked_users[username]
    return False, 0

def login():
    
   while True:
        username = input("Username: ")
        password = input("Password: ")

        blocked, remaining = is_blocked(username)
        if blocked:
            print(f"Blocked! Try again in {remaining} seconds.")
            continue

        if users.get(username) == password:
            print("Login successful!")
            return True
        else:
            login_attempts[username] = login_attempts.get(username, 0) + 1
            if login_attempts[username] >= 3:
                blocked_users[username] = time.time() + 300
                print("Too many attempts. Blocked for 5 minutes.")
            else:
                print("Incorrect credentials.")