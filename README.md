# Network-Scann

A lightweight Python-based tool designed to identify and map active devices on a local network with high efficiency and accuracy.  

---

#### Features:  
- **Device Discovery**: Detects all active devices in the network and retrieves their IP and MAC addresses.  
- **Real-Time Scanning**: Provides live updates during the scan to monitor progress.  
- **Multi-threading Support**: Speeds up scanning processes for large networks.  
- **Platform Independent**: Works seamlessly across multiple operating systems with Python.  

---

#### Highlights:  
- Utilizes **Scapy** for ARP requests and packet handling.  
- Lightweight design ensures minimal resource consumption.  
- Customizable scanning range to focus on specific subnets.  
- Results are saved in a structured output file for easy reference.  

---

#### Requirements:  
- Python 3.8 or higher  
- Dependencies: `scapy`, `argparse`  
- Proper permissions to send ARP packets on the target network.  

---

#### Usage:  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/network-scanner.git  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Run the script:  
   ```bash  
   python scanner.py --target <network/subnet>  
   ```  

---
####ScreenShot's:-
1.Single Host Scan:
![image](https://github.com/user-attachments/assets/adf388db-226d-443b-b7cf-d9b740af0303)

#### Disclaimer:  
This project is intended for educational and ethical purposes only. Unauthorized use of network scanning tools may violate laws or ethical guidelines. Always obtain proper authorization before scanning any network.  



