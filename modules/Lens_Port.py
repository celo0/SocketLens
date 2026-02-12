import socket
import core.logger

def lens_port(ip, ports, file=None):
    log = core.logger.logging.getLogger()
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
                messages.append(f"Port {p} is open")
            else:
                messages.append(f"Port {p} is closed")

            sock.close()
        except socket.error:
            messages.append(f"Could not connect to port {p}")
            log.error(f"Could not connect to port {p} on {ip}")

    output = "\n".join(messages)
    print(output)

    if file:
        with open(file, "a") as f:
            f.write(f"{output}\n\n")