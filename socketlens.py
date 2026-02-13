import core.logger
import core.banner
from modules.lens_web import lens_web
from modules.lens_port import lens_port

def main():
    core.logger.setup_logger()
    log = core.logger.get_logger()
    log.info("SocketLens started.")
    core.banner.print_banner()
    print("Welcome to SocketLens!")
    print("What would you like to do?")
    print("1. Check HTTPS accessibility and Server header")
    print("2. Scan open ports on a host")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        log.info("User selected option 1: Check HTTPS accessibility and Server header.")
        url = input("Enter the URL to check (include https:// or http://): ")
        if not url.startswith("https://") and not url.startswith("http://"):
            print("Please enter a valid URL.")
            exit()
        toFile = input("Do you want to save the results to a file? (y/n): ")
        if toFile.lower() == "y":
            file_name = input("Enter the file name to save the results: ")
            lens_web(url, file_name)
        else:
            lens_web(url)
    elif choice == "2":
        log.info("User selected option 2: Scan open ports on a host.")
        ip = input("Enter the IP address to scan: ")
        if not ip:
            print("Please enter a valid IP address.")
            log.warning("User did not enter a valid IP address.")
            exit()
        port = input("Enter the ports to scan (comma-separated or range): ")
        ports = []
        for p in port.split(","):
            p = p.strip()
            if "-" in p:
                parts = p.split("-")
                if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                    start, end = int(parts[0]), int(parts[1])
                    if start > end or start < 1 or end > 65535:
                        print(f"Invalid port range: {p}. Skipping.")
                        log.warning(f"User entered an invalid port range: {p}.")
                    else:
                        ports.extend(range(start, end + 1))
            else:
                if p.isdigit():
                    if 1 <= int(p) <= 65535:
                        ports.append(int(p))
                    else:
                        print(f"Invalid port number: {p}. Skipping.")
                        log.warning(f"User entered an invalid port number: {p}.")
        ports = list(set(ports))
        ports.sort()
        if not ports:
            print("No valid ports to scan. Exiting.")
            log.warning("User did not enter any valid ports to scan.")
            exit()
        toFile = input("Do you want to save the results to a file? (y/n): ")
        if toFile.lower() == "y":
            file_name = input("Enter the file name to save the results: ")
            lens_port(ip, ports, file_name)
        else:
            lens_port(ip, ports)
    else:
        print("Invalid choice. Please enter 1 or 2.")
        log.warning("User entered an invalid choice.")

if __name__ == "__main__":
    main()