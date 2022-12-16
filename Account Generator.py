import threading
import random
import string
import requests
import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
file_path = os.path.join(desktop, 'accounts.txt')

def generate_email():
  # Generate a random email address using one of the top 5 most popular email domains
  email_domains = ["gmail.com", "yahoo.com", "outlook.com", "aol.com", "hotmail.com"]
  domain = random.choice(email_domains)
  return f"{generate_username()}@{domain}"

def generate_password():
  # Generate a random password using a combination of lowercase letters, uppercase letters, digits, and special characters
  special_characters = "!@#$%^&*()"
  characters = string.ascii_letters + string.digits + special_characters
  return ''.join(random.choices(characters, k=8))

def generate_username():
  # Generate a more human-like username by using a combination of
  # a random name and a random number
  names = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Greta", "Hannah", "Ivy", "Jake"]
  name = random.choice(names)
  number = random.randint(10000, 10000000)
  return f"{name}{number}"

def send_request():
  # Generate the payload
  email = generate_email()
  password = generate_password()
  username = generate_username()
  payload = {
          "user": username,
          "pwd": password,
          "cpwd": password,
          "email": email,
          "terms": "acc",
          "Register": "Register",
          "action": "register"
      }

  # Send the POST request
  response = requests.post("http://www.hacker-project.com/index.php", data=payload)
  
  # Save the username, password, and email to the file
  with open(file_path, 'a') as f:
      f.write(f"Username: {username} Password: {password} Email: {email}\n")
    
  # Print the generated username, password, and email
  print(f"Username: {username} Password: {password} Email: {email}")

def create_accounts():
  while True:
    send_request()

# Create threads
threads = []
for i in range(1300):
  t = threading.Thread(target=create_accounts)
  threads.append(t)
  t.start()