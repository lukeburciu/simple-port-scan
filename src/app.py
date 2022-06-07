import sys
import socket
import csv
import requests




def scan_port(target, lower_port, upper_port):
    try:
        for port in range(lower_port, upper_port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()
    except KeyboardInterrupt:
        print("User stopped the processes")            
    except socket.gaierror:
        print("ERROR: Hostname could not be resolved")
        sys.exit()
    except socket.error:
        print("ERROR: Server not responding")


def grab_port_info(url):
    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter='\t')
        port_info = list(cr)

        return port_info


def main():
    url = "https://pastebin.com/raw/fXkCwZu2"
    grab_port_info(url)

if __name__ == "__main__":
    main()