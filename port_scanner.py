import socket
import concurrent.futures
import sys
import time

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"
                return (port, service)
    except Exception:
        return None
    return None

def scan_ports(target, start_port, end_port):
    print(f"\n[+] Scanning {target} from port {start_port} to {end_port}...\n")
    open_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, target, port) for port in range(start_port, end_port + 1)]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                open_ports.append(result)
    
    return sorted(open_ports)

if __name__ == "__main__":
    try:
        print("==== Simple Port Scanner ====")
        target = input("Enter target IP or domain: ").strip()
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        # Resolve hostname to IP
        target_ip = socket.gethostbyname(target)
        print(f"Resolved target to IP: {target_ip}")

        start_time = time.time()
        open_ports = scan_ports(target_ip, start_port, end_port)
        duration = time.time() - start_time

        print("\n==== Scan Results ====")
        if open_ports:
            for port, service in open_ports:
                print(f"[OPEN] Port {port} ({service})")
        else:
            print("No open ports found.")
        print(f"\nScan completed in {duration:.2f} seconds.")

    except socket.gaierror:
        print("[ERROR] Hostname could not be resolved.")
    except ValueError:
        print("[ERROR] Invalid port number.")
    except KeyboardInterrupt:
        print("\n[!] Scan cancelled by user.")
        sys.exit()
