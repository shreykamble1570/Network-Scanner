import scapy.all as scapy
import threading
from queue import Queue
from colorama import Fore
import socket

# Fetch Current Interface IP
our_ip = socket.gethostbyname(socket.gethostname())
our_ip_octet = our_ip[:our_ip.rfind(".")+1]

# Printing Banner
print(Fore.YELLOW + '''
   shreytech
By @shrey_kamble1570
  '*'
''')

# Printing Table
print(Fore.RED + "IP Address\t\t\tMAC Address")
print(Fore.WHITE + "----------------------------------------")

# Function To Check IP & Its MAC
def check(target):
    try:
        arp = scapy.ARP(pdst=target)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        final_packet = broadcast / arp
        answered, _ = scapy.srp(final_packet, timeout=10, verbose=False)
        if answered:
            for element in answered:
                print(Fore.GREEN + element[1].psrc + "\t\t\t" + element[1].hwsrc)
    except Exception as e:
        print(Fore.RED + f"Error on {target}: {e}")

# Queue for IPs
ip_queue = Queue()
for last_octet in range(1, 256):
    ip_queue.put(our_ip_octet + str(last_octet))

# Worker Function
def worker():
    while not ip_queue.empty():
        target_ip = ip_queue.get()
        check(target_ip)
        ip_queue.task_done()

# Launch Threads
thread_count = 50  # Adjust based on your system capability
threads = []
for _ in range(thread_count):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

# Wait for Threads
ip_queue.join()

# Hold Terminal
print(Fore.BLUE + "\n[#] Scan Completed!")
input()
