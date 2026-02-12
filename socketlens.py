import core.logger
import core.banner
import modules.lens_web
import modules.lens_port

def main():
    core.logger.setup_logger()
    log = core.logger.logging.getLogger()
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
            modules.lens_web.lens_web(url, file_name)
        else:
            modules.lens_web.lens_web(url)
    elif choice == "2":
        log.info("User selected option 2: Scan open ports on a host.")
        ip = input("Enter the IP address to scan: ")
        port = input("Enter the ports to scan (comma-separated): ")
        ports = [int(p.strip()) for p in port.split(",") if p.strip().isdigit()]
        toFile = input("Do you want to save the results to a file? (y/n): ")
        if toFile.lower() == "y":
            file_name = input("Enter the file name to save the results: ")
            modules.lens_port.lens_port(ip, ports, file_name)
        else:
            modules.lens_port.lens_port(ip, ports)
    else:
        print("Invalid choice. Please enter 1 or 2.")
        log.warning("User entered an invalid choice.")

if __name__ == "__main__":
    main()