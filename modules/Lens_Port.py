import socket

def lens_port(ip, ports):
    try:
        ip = socket.gethostbyname(ip)
    except socket.gaierror:
        print("Hostname could not be resolved.")
        exit()
    for p in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, p))
            if result == 0:
                print(f"Port {p} of {ip} is open")
            else:
                print(f"Port {p} of {ip} is closed")

            sock.close()
        except socket.error:
            print(f"Could not connect to port {p} of {ip}")

def lens_port_to_file(ip, ports, file):
    try:
        ip = socket.gethostbyname(ip)
    except socket.gaierror:
        print("Hostname could not be resolved.")
        exit()
    with open(file, "a") as file:
        file.write(f"Host to be scanned {ip}\n")
        for p in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, p))
                if result == 0:
                    print(f"Port {p} of {ip} is open")
                    file.write(f"Port {p} of {ip} is open\n")
                else:
                    print(f"Port {p} of {ip} is closed")
                    file.write(f"Port {p} of {ip} is closed\n")
                sock.close()
            except socket.error:
                print(f"Could not connect to port {p} of {ip}")
        file.write("\n")