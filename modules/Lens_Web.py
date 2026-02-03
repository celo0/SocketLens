import requests

def lens_web(url):
    try:
        response = requests.get(url, timeout=5)
        if response.url.startswith("https://"):
            print(f"The URL {url} is accessible over HTTPS.")
        else:
            print(f"The URL {url} is not accessible over HTTPS.")
        server = response.headers.get("Server")
        if server:
            print(f"Server header found: {server}")
            print("Header is exposed! Security vulnerability!")
            if any(char.isdigit() for char in server):
                print("Server version is exposed, security vulnerability!")
        else:
            print("Header is not exposed, no security vulnerability!")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def lens_web_to_file(url, file):
    with open(file, "a") as file:
        file.write(f"Checking URL: {url}\n")
        try:
            response = requests.get(url, timeout=5)
            if response.url.startswith("https://"):
                print(f"The URL {url} is accessible over HTTPS.")
            else:
                print(f"The URL {url} is not accessible over HTTPS.")
            server = response.headers.get("Server")
            if server:
                print(f"Server header found: {server}")
                print("Header is exposed! Security vulnerability!")
                if any(char.isdigit() for char in server):
                    print("Server version is exposed, security vulnerability!")
            else:
                print("Header is not exposed, no security vulnerability!")
            file.write(f"Server header: {server}\n\n")
            file.write(f"HTTPS accessibility: {response.url.startswith('https://')}\n")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        