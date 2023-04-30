import requests

with open('open_554.txt', 'r') as f:
    ips = f.read().splitlines()

for ip in ips:
    try:
        response = requests.get('http://' + ip, timeout=5)
        if response.status_code == 200:
            # print(ip + ' is up and running!')
            if "Honeywell" in response.text:
                print(f"Honeywell camera found: {ip}")
                with open("honeywell", "a") as file:
                    file.write(ip + "\n")
            elif "/doc/page/login" in response.text:
                print(f"Hikvision camera found: {ip}")
                with open("hikvision", "a") as file:
                    file.write(ip + "\n")
            else: 
                print(f"Other camera found: {ip}")
                with open("others", "a") as file:
                    file.write(ip + "\n")
        else:
            print(ip + ' is not responding properly')
    except requests.exceptions.RequestException:
        print(ip + ' is down')
