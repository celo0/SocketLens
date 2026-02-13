import socket
import core.logger


def banner_grabber(sock, port):
    log = core.logger.get_logger()
    sock.settimeout(2)
    try:
        if port in [80, 8080, 8000]:
            sock.send(b"GET / HTTP/1.0\r\n\r\n")
            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
            if banner:
                lines = banner.split("\n")
                for line in lines:
                    if 'Server' in line:
                        return line.strip()
            return "HTTP/HTTPS Service"
        elif port == 443:
            return "HTTPS (encrypted)"
        else:    
            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
            if banner:
                log.info(f"Banner grabbed from port {port}: {banner}")
                return banner
    except Exception as e:
        log.debug(f"No banner from port {port}: {e}")
        pass
    return None

def lens_port(ip, ports, file=None):
    log = core.logger.get_logger()
    messages = []
    try:
        ip = socket.gethostbyname(ip)
    except socket.gaierror:
        error_msg = "Hostname could not be resolved."
        print(error_msg)
        log.error(error_msg)
        exit()
    
    messages.append(f"Scanning Host: {ip}")
    log.info(f"Starting port scan on {ip} for ports: {ports}")
    for p in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, p))
            if result == 0:
                messages.append(f"Port {p} is open - Service: {banner_grabber(sock, p)}")
            else:
                messages.append(f"Port {p} is closed - Service: {banner_grabber(sock, p)}")

            sock.close()
        except socket.error:
            messages.append(f"Could not connect to port {p}")
            log.error(f"Could not connect to port {p} on {ip}")

    output = "\n".join(messages)
    print(output)

    if file:
        with open(file, "a") as f:
            f.write(f"{output}\n\n")