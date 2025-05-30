
import socket
import os
import sys
import time

import port_scanner
import brute_forcer


def run_port_scanner() -> None:
    """Run the port-scanner workflow."""
    try:
        target = input("Enter target IP or domain: ").strip()
        start_port = int(input("Enter starting port: "))
        end_port   = int(input("Enter ending port: "))

        # Resolve domain → IP so user sees what is scanned
        target_ip = socket.gethostbyname(target)
        print(f"Resolved target to IP: {target_ip}")

        t0 = time.time()
        open_ports = port_scanner.scan_ports(target_ip, start_port, end_port)
        elapsed = time.time() - t0

        print("\n==== Scan Results ====")
        if open_ports:
            for port, service in open_ports:
                print(f"[OPEN] Port {port} ({service})")
        else:
            print("No open ports found.")
        print(f"\nScan completed in {elapsed:.2f} seconds.\n")

    except socket.gaierror:
        print("[ERROR] Hostname could not be resolved.\n")
    except ValueError:
        print("[ERROR] Invalid port number.\n")
    except KeyboardInterrupt:
        print("\n[!] Scan cancelled by user.")
        sys.exit()


def run_brute_forcer() -> None:
    """Run the brute-forcer workflow."""
    try:
        url           = input("Enter the login URL: ").strip()
        username      = input("Enter the username: ").strip()
        password_file = input("Enter path to password list file: ").strip()
        success_key   = input("Enter success keyword from response (e.g., 'Login successful'): ").strip()
        delay_input   = input("Delay between requests in seconds (optional): ").strip()
        delay         = float(delay_input) if delay_input else 0.0

        if not os.path.exists(password_file):
            print("[ERROR] Password list file not found.\n")
            return

        with open(password_file, "r", encoding="utf-8", errors="ignore") as fh:
            passwords = [line.strip() for line in fh]

        brute_forcer.brute_force_login(
            url,
            username,
            passwords,
            success_key,
            delay
        )

    except FileNotFoundError:
        print(f"[ERROR] Password list file not found: {password_file}\n")
    except KeyboardInterrupt:
        print("\n[!] Brute force interrupted by user.")
        sys.exit()


def main() -> None:
    print("==== Penetration Testing Toolkit ====")
    print("1. Port Scanner")
    print("2. Brute Forcer")
    choice = input("Choose a tool to use (1/2): ").strip()

    if choice == "1":
        run_port_scanner()
    elif choice == "2":
        run_brute_forcer()
    else:
        print("[ERROR] Invalid choice. Please enter 1 or 2.\n")


if __name__ == "__main__":
    main()
