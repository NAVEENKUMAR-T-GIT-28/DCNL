from scapy.all import sniff, IP, TCP, UDP, DNS


def analyze_packet(packet):
    if IP not in packet:
        return

    source = packet[IP].src
    destination = packet[IP].dst
    length = len(packet)
    service = "Other"

    if DNS in packet:
        service = "DNS"
    elif TCP in packet:
        ports = {packet[TCP].sport, packet[TCP].dport}
        if 80 in ports:
            service = "HTTP"
        elif 443 in ports:
            service = "HTTPS/TLS"
        elif 25 in ports or 587 in ports:
            service = "SMTP"
        elif 21 in ports:
            service = "FTP"
        else:
            service = "TCP"
    elif UDP in packet:
        ports = {packet[UDP].sport, packet[UDP].dport}
        if 53 in ports:
            service = "DNS"
        else:
            service = "UDP"

    print("Source IP        :", source)
    print("Destination IP   :", destination)
    print("Service/Protocol :", service)
    print("Packet Length    :", length, "bytes")
    print("-" * 40)


print("Network Traffic Analysis Started")
print("Generate network traffic (for example, open a website) during capture.")

try:
    sniff(prn=analyze_packet, count=10, store=False)
except PermissionError:
    print("Permission denied. Run the terminal with administrator/root privileges.")
except Exception as error:
    print("Packet capture failed:", error)

print("Network Traffic Analysis Completed")
