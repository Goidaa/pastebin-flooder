import time
import random
import requests

API_KEY = "ABCDEFGabcdefg1234567890" # Api key here ( pastebin.com/doc_api )

def create_paste(paste_text, paste_title):
    payload = {
        'api_dev_key': API_KEY,
        'api_option': 'paste',
        'api_paste_code': paste_text,
        'api_paste_name': paste_title,
        'api_paste_expire_date': '10M',
        'api_paste_private': 0,  # 0 = public, 1 = unknown, 2 = private
    }

    response = requests.post("https://pastebin.com/api/api_post.php", data=payload)
    return response

def generate_random_suffix(length=3):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789' # Random chars
    return ''.join(random.choice(characters) for _ in range(length))


print(f'https://github.com/Goidaa/pastebin-flooder/
paste_title_base = input("Enter title: ")
paste_text = input("Enter text: ")

i = 1
while i <= 10:  # Paste limit per sec
    paste_title = f"{paste_title_base} {generate_random_suffix()}" 
    
    response = create_paste(paste_text, paste_title)
    
    if response.status_code == 200:
        print(f"Created paste {i}: {response.text}")
    else:
        print(f"Error: {response.status_code}, {response.text}")
    
    i += 1
    time.sleep(7)  # Delay
