import random
import string
import requests
import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
file_path = os.path.join(desktop, 'accounts.txt')

def generate_email():
  # Generate a random email address
  username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
  domain = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
  return f"{username}@{domain}.com"

def generate_password():
  # Generate a random password
  return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def generate_username():
  # Generate a random username
  return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

while True:
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
  
  # Save the username and password to the file
  with open(file_path, 'a') as f:
      f.write(f"Username: {username} Password: {password}\n\n")
    
  # Print the generated username and password
  print(f"Username: {username} Password: {password}")