import requests
import core.logger

def lens_web(url, file=None):
    log = core.logger.get_logger()
    messages = []
    try:
        response = requests.get(url, timeout=5)
        log.info(f"Checked URL: {url} - Status Code: {response.status_code}")
        if response.url.startswith("https://"):
            messages.append(f"The URL {url} is accessible over HTTPS.")
        else:
            messages.append(f"The URL {url} is not accessible over HTTPS.")
        server = response.headers.get("Server")
        if server:            
            messages.append(f"Server header found: {server}")
            messages.append("Header is exposed! Security vulnerability!")
            if any(char.isdigit() for char in server):
                messages.append("Server version is exposed, security vulnerability!")
        else:
            messages.append("Header is not exposed, no security vulnerability!")
        output = "\n".join(messages)
        print(output)
        if file:
            with open(file, "a") as f:
                f.write(f"Checking URL: {url}\n")
                f.write(f"{output}\n\n")
    except requests.exceptions.RequestException as e:
        error_msg = f"An error occurred: {e}"
        print(error_msg)
        log.error(error_msg)