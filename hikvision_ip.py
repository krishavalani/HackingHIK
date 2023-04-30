import glob
import threading
import socket

def check_port(ip):
    if ":" in ip:
        ip = ip.split(":")[0]
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            # if s.connect_ex((ip, 80)) == 0 and s.connect_ex((ip, 554)) == 0:
            #     print(ip, "is open on both ports")
            #     with open("open_ips.txt", "a") as f:
            #         f.write(ip + "\n")
            if s.connect_ex((ip, 554)) == 0:
                print(ip, "is open on port 554")
                with open("open_554.txt", "a") as f:
                    f.write(ip + "\n")
                if s.connect_ex((ip, 80)) == 0:
                    print(ip, "is open on port 80")
                    with open("open_80.txt", "a") as f:
                        f.write(ip + "\n")
            else:
                print(ip, "is not open on both ports")
    except:
        print(ip, "is not valid")

if __name__ == '__main__':
    files = glob.glob("./*")
    for file in files:
        with open(file, "r") as f:
            ips = f.readlines()
            threads = []
            for ip in ips:
                ip = ip.strip()
                t = threading.Thread(target=check_port, args=(ip,))
                threads.append(t)
                t.start()

            for thread in threads:
                thread.join()
    # print(check_port("10.1.77.18"))
