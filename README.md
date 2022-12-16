# Account Generation Script
This script is used to generate new accounts with randomly generated username, password, and email. The generated account information is saved to a file on the desktop and printed to the console.

## How to use
Clone the repository to your local machine
Install the required libraries: pip install requests
Run the script: python main.py
The script will create 10 threads, each running in a loop to generate a new account. The generated account information will be saved to a file called accounts.txt on the desktop and printed to the console.

## Customization
You can customize the number of threads by adjusting the value in the range function on line 45. For example, to create 1000 threads, change range(1000) to range(100).

You can also customize the payload data for the POST request on line 24. This can be useful if you want to use the script to generate accounts on a different website that requires different form data.

## Disclaimer
This script is for educational purposes only. Use it at your own risk. I am not responsible for any consequences of using this script.
