import socket
from IPy import IP

# Main function for scanning target
def scan(target, ports):
    ip = make_ip(target)
    print("Scanning " + ip)

    #for port in ports:
    #    scan_port(ip, port)

    for port in range(ports):
        scan_port(ip, port)

# Try to connect to a port to see if it is open
def scan_port(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((target, port))
        try:
            banner = get_banner(sock)
            print("[+] Open port " + str(port) + " : " + str(banner.decode().strip("\n").strip("\r")))
        except:
            print("[+] Open port " + str(port))
    except:
        print("[-] Closed port " + str(port))

# Read the banner of a socket which can tell you the running services on a port
def get_banner(s):
    return s.recv(1024)

# Checks IP format
#       | Creates an IP object from IP address or from hostname
def make_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def create_target_list(targets):
    target_list = []
    try:
        if ',' in targets:
            target_list = targets.split(',')
        elif '-' in targets:
            i = targets.index('-')
            
            pass
    except:
        pass

if __name__ == "__main__":

    # Verbose

    targets = input("[*]\tTarget IP Address(es)/hostname(s) [In a list separated by a comma or in a range]: ")
    ports = input("[*]\tTarget port(s) [In a list separated by a comma or in a range]: ")

    targets = targets.replace(" ", "")

    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '), int(ports))
    else:
        scan(targets, int(ports))

    #print(check_ip('Anthony'))
    #scan("Anthony", [135])

