# Data Communication and Networking Laboratory
## Complete Record – 12 Regular Experiments

## Table of Contents

1. [Study of Network Devices, Cables and Basic Network Utilities](#experiment-1--study-of-network-devices-cables-and-basic-network-utilities)
2. [Configuration of IP Address and Subnetting](#experiment-2--configuration-of-ip-address-and-subnetting-using-cisco-packet-tracer)
3. [Implementation of CRC Error Detection](#experiment-3--implementation-of-crc-error-detection)
4. [Implementation of Hamming Code](#experiment-4--implementation-of-hamming-code)
5. [Implementation of Stop-and-Wait ARQ Protocol](#experiment-5--implementation-of-stop-and-wait-arq-protocol)
6. [Implementation of Sliding Window Protocol](#experiment-6--implementation-of-sliding-window-protocol)
7. [TCP Client-Server Communication](#experiment-7--implementation-of-tcp-client-server-communication)
8. [UDP Client-Server Communication](#experiment-8--implementation-of-udp-client-server-communication)
9. [Distance Vector Routing Algorithm](#experiment-9--implementation-of-distance-vector-routing-algorithm)
10. [Link State Routing Algorithm](#experiment-10--implementation-of-link-state-routing-algorithm)
11. [Routing Protocols and VLAN Configuration](#experiment-11--simulation-of-routing-protocols-and-vlan-configuration-using-cisco-packet-tracer)
12. [Network Traffic Analysis and Application Layer Services](#experiment-12--analysis-of-network-traffic-and-application-layer-services)

---

# Experiment 1 – Study of Network Devices, Cables and Basic Network Utilities

## AIM
To study different network devices, network cables, and basic network utility commands.

## ALGORITHM
1. Observe the available network devices such as router, switch and hub.
2. Identify the different types of network cables.
3. Open Command Prompt.
4. Execute the commands `ipconfig`, `ping`, `tracert` and `nslookup`.
5. Observe and record the outputs.

## PROGRAM / COMMANDS

This is a hardware observation and command-based experiment; no separate programming language is required.

Open **Windows Command Prompt** and execute:

```bat
ipconfig
ping google.com
tracert google.com
nslookup google.com
```

**Purpose of each command**

- `ipconfig` – Displays the computer's IP configuration.
- `ping google.com` – Checks connectivity to the destination using ICMP Echo requests.
- `tracert google.com` – Displays the route (hops) taken by packets to the destination.
- `nslookup google.com` – Queries DNS to obtain domain-name information, commonly its IP address.

**Devices and cables to identify**

- Router – Connects different networks.
- Switch – Connects devices within a LAN.
- Hub – Sends incoming data to all connected ports.
- UTP cable – Common copper Ethernet cable.
- Fibre-optic cable – Uses light to transmit data and supports high speed over long distances.

## OUTPUT

```text
Network devices identified:
Router, Switch and Hub

Network cables identified:
UTP cable and Fibre-optic cable

Commands executed:
ipconfig
ping google.com
tracert google.com
nslookup google.com

The commands display IP configuration, connectivity,
the route to the destination and DNS information.
```

Actual IP addresses, hop details and ping responses depend on the computer and network connection.

## RESULT
Thus, the study of network devices, cables, and network utilities was completed successfully.

---

# Experiment 2 – Configuration of IP Address and Subnetting Using Cisco Packet Tracer

## AIM
To configure IP addresses for network devices and perform subnetting using Cisco Packet Tracer, and to verify connectivity between the configured devices.

## ALGORITHM
1. Open Cisco Packet Tracer.
2. Place two PCs and one switch in the workspace.
3. Connect PC0 and PC1 to the switch using Copper Straight-Through cables.
4. Assign PC0 the IP address `192.168.10.1` and subnet mask `255.255.255.0`.
5. Assign PC1 the IP address `192.168.10.2` and subnet mask `255.255.255.0`.
6. Configure the subnet mask according to the given network requirement.
7. Open PC0 → Desktop → Command Prompt.
8. Use the `ping` command to test connectivity with PC1.
9. Verify that successful replies are received.

## PROGRAM / COMMANDS

### IP address configuration

In Packet Tracer, select each PC → **Desktop → IP Configuration**.

| Device | IP address | Subnet mask | Default gateway |
|---|---|---|---|
| PC0 | 192.168.10.1 | 255.255.255.0 | 192.168.10.254 |
| PC1 | 192.168.10.2 | 255.255.255.0 | 192.168.10.254 |

The default gateway is not needed for communication between these two PCs on the same LAN. It is included to match the lab-record addressing table.

### Connectivity command

On PC0 → Desktop → Command Prompt:

```text
ping 192.168.10.2
```

If a router is used, the following Cisco IOS commands can help verify it:

```text
show ip interface brief
show running-config
```

### Subnetting example

Given network: `192.168.10.0/24`

For 4 equal subnets, borrow 2 host bits:

- New prefix: `/26`
- Subnet mask: `255.255.255.192`
- Number of subnets: \(2^2 = 4\)
- Addresses per subnet: \(2^6 = 64\)
- Usable hosts per subnet: 62

| Subnet | Network address | Usable host range | Broadcast address |
|---|---|---|---|
| 1 | 192.168.10.0/26 | 192.168.10.1 – 192.168.10.62 | 192.168.10.63 |
| 2 | 192.168.10.64/26 | 192.168.10.65 – 192.168.10.126 | 192.168.10.127 |
| 3 | 192.168.10.128/26 | 192.168.10.129 – 192.168.10.190 | 192.168.10.191 |
| 4 | 192.168.10.192/26 | 192.168.10.193 – 192.168.10.254 | 192.168.10.255 |

## OUTPUT

Representative successful ping output:

```text
C:\> ping 192.168.10.2

Pinging 192.168.10.2 with 32 bytes of data:

Reply from 192.168.10.2: bytes=32 time<1ms TTL=128
Reply from 192.168.10.2: bytes=32 time<1ms TTL=128
Reply from 192.168.10.2: bytes=32 time<1ms TTL=128
Reply from 192.168.10.2: bytes=32 time<1ms TTL=128

Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)
```

## RESULT
Thus, the IP addresses were configured successfully, the network was subnetted, and connectivity between the devices was verified successfully using Cisco Packet Tracer.

---

# Experiment 3 – Implementation of CRC Error Detection

## AIM
To implement the Cyclic Redundancy Check (CRC) error detection technique using Python and detect errors in transmitted data.

## ALGORITHM
1. Start the program.
2. Read the data bits and generator bits.
3. Append `n-1` zeros to the data, where `n` is the length of the generator.
4. Perform XOR division using the generator.
5. Obtain the CRC remainder.
6. Append the CRC remainder to the original data to form the transmitted codeword.
7. Enter the received codeword at the receiver side.
8. Perform XOR division again using the same generator.
9. Check the remainder.
10. If the remainder contains only zeros, display **No error detected**.
11. Otherwise, display **Error detected**.
12. Stop.

## PROGRAM

```python
def crc(data, generator):
    """Return the CRC remainder using modulo-2 (XOR) division."""
    work = list(data)
    divisor = list(generator)

    for i in range(len(work) - len(divisor) + 1):
        if work[i] == "1":
            for j in range(len(divisor)):
                work[i + j] = str(int(work[i + j]) ^ int(divisor[j]))

    return "".join(work[-(len(divisor) - 1):])


# Sender side
data = input("Enter data bits: ").strip()
generator = input("Enter generator bits: ").strip()

if not data or any(bit not in "01" for bit in data):
    raise ValueError("Data must contain only 0 and 1.")
if len(generator) < 2 or any(bit not in "01" for bit in generator):
    raise ValueError("Generator must contain at least two binary bits.")
if generator[0] != "1":
    raise ValueError("The first bit of the generator must be 1.")

# Append zeros and calculate CRC
appended_data = data + "0" * (len(generator) - 1)
remainder = crc(appended_data, generator)
codeword = data + remainder

print("\nCRC Remainder:", remainder)
print("Transmitted Codeword:", codeword)

# Receiver side
received = input("\nEnter received codeword: ").strip()

if len(received) < len(generator):
    raise ValueError("Received codeword must be at least as long as the generator.")
if any(bit not in "01" for bit in received):
    raise ValueError("Received codeword must contain only 0 and 1.")

check_remainder = crc(received, generator)
print("Receiver Remainder:", check_remainder)

if "1" in check_remainder:
    print("Error detected in received data.")
else:
    print("No error detected. Data received correctly.")
```

## OUTPUT

```text
Enter data bits: 1101011011
Enter generator bits: 10011

CRC Remainder: 1110
Transmitted Codeword: 11010110111110

Enter received codeword: 11010110111110
Receiver Remainder: 0000
No error detected. Data received correctly.
```

If a bit is changed in the received codeword, the receiver will normally obtain a non-zero remainder and report an error.

## RESULT
Thus, the CRC Error Detection technique was successfully implemented using Python, and the presence or absence of errors in the received data was detected.

---

# Experiment 4 – Implementation of Hamming Code

## AIM
To implement Hamming Code for error detection and correction in a data communication system.

## ALGORITHM
1. Start the program.
2. Read the data bits from the user.
3. Calculate the number of redundant bits using \(2^p \geq m+p+1\), where `m` is the number of data bits and `p` is the number of parity bits.
4. Insert parity bits at positions 1, 2, 4, 8, and so on.
5. Calculate the values of the parity bits using even parity.
6. Generate and display the Hamming code.
7. Read the received Hamming code.
8. Recalculate the parity bits at the receiver.
9. Find the error position using the syndrome.
10. Correct the error if one is detected.
11. Extract and display the corrected data bits.
12. Stop.

## PROGRAM

```python
# Hamming Code using even parity (single-bit error correction)

data = input("Enter data bits: ").strip()

if not data or any(bit not in "01" for bit in data):
    raise ValueError("Enter only binary data bits.")

m = len(data)

# Find the number of parity bits
p = 0
while 2 ** p < m + p + 1:
    p += 1

n = m + p
hamming = ["0"] * (n + 1)

# Insert data bits into non-parity positions (1-based positions)
j = 0
for i in range(1, n + 1):
    if i & (i - 1):  # Not a power of 2
        hamming[i] = data[j]
        j += 1

# Calculate even parity bits
for pbit in range(p):
    pos = 2 ** pbit
    parity = 0
    for i in range(1, n + 1):
        if i & pos:
            parity ^= int(hamming[i])
    hamming[pos] = str(parity)

code = "".join(hamming[1:])
print("Hamming Code:", code)

# Receiver side
received = input("Enter received Hamming code: ").strip()

if len(received) != n or any(bit not in "01" for bit in received):
    raise ValueError(f"Enter exactly {n} binary bits.")

received = list(received)
error_pos = 0

# Calculate syndrome
for pbit in range(p):
    pos = 2 ** pbit
    parity = 0
    for i in range(1, n + 1):
        if i & pos:
            parity ^= int(received[i - 1])
    if parity:
        error_pos += pos

# Correct a single-bit error
if error_pos == 0:
    print("No error detected.")
elif error_pos <= n:
    print("Error detected at position:", error_pos)
    received[error_pos - 1] = "1" if received[error_pos - 1] == "0" else "0"
    print("Corrected Hamming Code:", "".join(received))
else:
    raise ValueError("Invalid syndrome; received data may contain multiple errors.")

# Extract data bits from non-parity positions
data_bits = ""
for i in range(1, n + 1):
    if i & (i - 1):
        data_bits += received[i - 1]

print("Corrected Data:", data_bits)
```

## OUTPUT

```text
Enter data bits: 1011
Hamming Code: 0110011
Enter received Hamming code: 0110111
Error detected at position: 5
Corrected Hamming Code: 0110011
Corrected Data: 1011
```

Note: This basic Hamming code implementation corrects a single-bit error. It does not reliably detect or correct multiple-bit errors.

## RESULT
Thus, the Hamming Code was successfully implemented, and a single-bit error in the received data was detected and corrected.

---

# Experiment 5 – Implementation of Stop-and-Wait ARQ Protocol

## AIM
To implement the Stop-and-Wait ARQ (Automatic Repeat reQuest) protocol using Python and demonstrate reliable data transmission using ACKs and retransmission when a frame is lost.

## ALGORITHM
1. Start the program.
2. Set the total number of frames to be transmitted.
3. Send one frame at a time.
4. Start a timer and wait for an acknowledgement (ACK).
5. If the ACK is received successfully, display that the frame was acknowledged and move to the next frame.
6. If the frame or ACK is lost, display a timeout message and retransmit the same frame.
7. Repeat until all frames are successfully transmitted.
8. Stop the program.

## PROGRAM

```python
import random
import time

total_frames = int(input("Enter the number of frames: "))
if total_frames <= 0:
    raise ValueError("Number of frames must be greater than zero.")

frame = 1

while frame <= total_frames:
    acknowledged = False

    while not acknowledged:
        print(f"\nSending Frame {frame}...")
        time.sleep(0.2)

        # Simulate frame or ACK loss (25% chance)
        if random.random() < 0.75:
            print(f"Frame {frame} received successfully.")
            time.sleep(0.1)
            print(f"ACK {frame} received.")
            acknowledged = True
        else:
            print(f"Frame {frame} or ACK {frame} lost!")
            print("Timeout... Retransmitting the frame.")

    frame += 1

print("\nAll frames transmitted successfully.")
```

## OUTPUT

One representative run (because loss is random):

```text
Enter the number of frames: 5

Sending Frame 1...
Frame 1 received successfully.
ACK 1 received.

Sending Frame 2...
Frame 2 or ACK 2 lost!
Timeout... Retransmitting the frame.

Sending Frame 2...
Frame 2 received successfully.
ACK 2 received.

Sending Frame 3...
Frame 3 received successfully.
ACK 3 received.

Sending Frame 4...
Frame 4 or ACK 4 lost!
Timeout... Retransmitting the frame.

Sending Frame 4...
Frame 4 received successfully.
ACK 4 received.

Sending Frame 5...
Frame 5 received successfully.
ACK 5 received.

All frames transmitted successfully.
```

## RESULT
Thus, the Stop-and-Wait ARQ protocol was successfully implemented in Python. The program demonstrated ACK-based transmission and retransmission of lost frames, ensuring reliable data delivery.

---

# Experiment 6 – Implementation of Sliding Window Protocol

## AIM
To implement and simulate the Sliding Window Protocol using Python and demonstrate the transmission of multiple frames before receiving acknowledgements.

## ALGORITHM
1. Start the program.
2. Read the total number of frames and window size.
3. Divide the frames into transmission windows according to the window size.
4. Send all frames present in the current window.
5. Receive acknowledgements for the transmitted frames.
6. If a frame is successfully acknowledged, slide the window forward.
7. If a frame is lost or its acknowledgement is not received, retransmit the required frame.
8. Continue until all frames are successfully transmitted.
9. Stop the program.

## PROGRAM

```python
import random

total_frames = int(input("Enter the total number of frames: "))
window_size = int(input("Enter the window size: "))

if total_frames <= 0 or window_size <= 0:
    raise ValueError("Frames and window size must be positive.")

base = 1

while base <= total_frames:
    end = min(base + window_size - 1, total_frames)

    print("\nCurrent Window:")
    for i in range(base, end + 1):
        print(f"Frame {i}", end=" ")
    print()

    # Simulate transmission and ACK of each frame in this window
    for i in range(base, end + 1):
        acknowledged = False
        while not acknowledged:
            print(f"\nSending Frame {i}...")

            if random.random() < 0.75:
                print(f"Frame {i} received.")
                print(f"ACK {i} received.")
                acknowledged = True
            else:
                print(f"Frame {i} lost or ACK lost!")
                print(f"Timeout for Frame {i}.")
                print(f"Retransmitting Frame {i}...")

    base = end + 1
    if base <= total_frames:
        print("\nWindow slides forward.")

print("\nAll frames transmitted successfully.")
```

## OUTPUT

One representative run:

```text
Enter the total number of frames: 6
Enter the window size: 3

Current Window:
Frame 1 Frame 2 Frame 3

Sending Frame 1...
Frame 1 received.
ACK 1 received.

Sending Frame 2...
Frame 2 received.
ACK 2 received.

Sending Frame 3...
Frame 3 lost!
Timeout for Frame 3.
Retransmitting Frame 3...
Frame 3 received.
ACK 3 received.

Window slides forward.

Current Window:
Frame 4 Frame 5 Frame 6

Sending Frame 4...
Frame 4 received.
ACK 4 received.

Sending Frame 5...
Frame 5 received.
ACK 5 received.

Sending Frame 6...
Frame 6 received.
ACK 6 received.

All frames transmitted successfully.
```

## RESULT
Thus, the Sliding Window Protocol was successfully implemented and simulated using Python. The program demonstrated multiple-frame transmission, acknowledgement, retransmission of lost frames, and sliding of the transmission window.

---

# Experiment 7 – Implementation of TCP Client-Server Communication

## AIM
To implement TCP client-server communication using Python socket programming.

## ALGORITHM
1. Import the socket module.
2. Create a server socket using `SOCK_STREAM`.
3. Bind the socket to localhost and a port number.
4. Listen for a client connection.
5. Accept the client connection.
6. Create a client socket and connect to the server.
7. Send a message from the client.
8. Receive the message at the server.
9. Send a response from the server.
10. Receive and display the response at the client.
11. Close both sockets.

## PROGRAM

Save the following as two separate files.

### File 1: `TCP.py`

```python
import socket
import threading

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 5000))
    server_socket.listen(1)

    conn, addr = server_socket.accept()
    print("Client connected:", addr)

    message = conn.recv(1024).decode()
    print("Message from client:", message)

    response = "Hello Client, message received!"
    conn.send(response.encode())

    conn.close()
    server_socket.close()


# Start server
server_thread = threading.Thread(target=server)
server_thread.start()

# Create client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5000))

message = input("Enter message: ")
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print("Response from server:", response)

client_socket.close()
server_thread.join()
```

### Execution

Open two terminals in the same folder.

Terminal 1:

```bash
python server.py
```

Terminal 2:

```bash
python client.py
```

Run the server first, then run the client. The server binds to destination port 5000. The client does not bind to port 5000; the operating system assigns it a temporary source port automatically.

## OUTPUT

**Server terminal:**

```text
TCP Server is waiting for a connection...
Client connected: ('127.0.0.1', 54321)
Message from client: Hello Server
```

**Client terminal:**

```text
Enter message: Hello Server
Response from server: Hello Client, message received!
```

The client-side port number may differ on each run.

## RESULT
Thus, the TCP client-server communication was successfully implemented using Python socket programming.

---

# Experiment 8 – Implementation of UDP Client-Server Communication

## AIM
To implement UDP client-server communication using Python socket programming.

## ALGORITHM
1. Import the socket module.
2. Create a UDP socket using `SOCK_DGRAM`.
3. Bind the server to a local IP address and port.
4. Create a client socket.
5. Send a message from the client to the server.
6. Receive the message at the server.
7. Send a response from the server.
8. Receive and display the response at the client.
9. Close the sockets.

## PROGRAM

Save the following as two separate files.

### File 1: `UDP.py`

```python
import socket
import threading

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("127.0.0.1", 5000))

    message, address = server_socket.recvfrom(1024)
    print("Message from client:", message.decode())

    response = "Hello Client, message received!"
    server_socket.sendto(response.encode(), address)

    server_socket.close()


# Start server
server_thread = threading.Thread(target=server)
server_thread.start()

# Create client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input("Enter message: ")

# Send message to server
client_socket.sendto(message.encode(), ("127.0.0.1", 5000))

# Receive response
response, address = client_socket.recvfrom(1024)
print("Response from server:", response.decode())

client_socket.close()
server_thread.join()
```

### Execution

Open two terminals in the same folder.

Terminal 1:

```bash
python server.py
```

Terminal 2:

```bash
python client.py
```

Run the server first, then run the client. The server binds to UDP port 5000. The client uses an automatically assigned temporary source port, so both files do not bind to the same port.

## OUTPUT

**Server terminal:**

```text
UDP Server is waiting for a message...
Message from client: Hello Server
```

**Client terminal:**

```text
Enter message: Hello Server
Response from server: Hello Client, message received!
```

## RESULT
Thus, UDP client-server communication was successfully implemented using Python socket programming. The client successfully sent a message to the server, and the server received and responded to the message.

---

# Experiment 9 – Implementation of Distance Vector Routing Algorithm

## AIM
To implement the Distance Vector Routing Algorithm using Python and find the shortest distance between the nodes in a network.

## ALGORITHM
1. Read the number of nodes.
2. Read the cost matrix of the network.
3. Initialize the distance table with the given costs.
4. Set the distance from a node to itself as 0.
5. Update the distance using the formula:

   `D[i][j] = min(D[i][j], D[i][k] + D[k][j])`

6. Repeat the process until the shortest distances are obtained.
7. Display the final distance table.
8. Stop.

## PROGRAM

```python
INF = 999

# Read number of nodes
n = int(input("Enter the number of nodes: "))
if n <= 0:
    raise ValueError("Number of nodes must be greater than zero.")

# Read the initial link-cost matrix
print("Enter the cost matrix:")
print("Enter 999 for no direct connection")

cost = []
for i in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
        raise ValueError("Each row must contain exactly n values.")
    if any(value < 0 for value in row):
        raise ValueError("Link costs cannot be negative.")
    cost.append(row)

# Each node initially knows its direct neighbours and itself
dist = [row[:] for row in cost]
for i in range(n):
    dist[i][i] = 0

# Distance Vector updates: exchange routing information until stable
changed = True
while changed:
    changed = False
    previous = [row[:] for row in dist]
    updated = [row[:] for row in previous]

    for i in range(n):
        for destination in range(n):
            for neighbour in range(n):
                if i != neighbour and cost[i][neighbour] < INF:
                    candidate = cost[i][neighbour] + previous[neighbour][destination]
                    if candidate < updated[i][destination]:
                        updated[i][destination] = candidate
                        changed = True

    dist = updated

# Display final distance table
print("\nFinal Distance Table:")
print("    " + "  ".join(f"N{j + 1}" for j in range(n)))

for i in range(n):
    values = ["INF" if value >= INF else str(value) for value in dist[i]]
    print(f"N{i + 1}  " + "  ".join(values))
```

## OUTPUT

**Sample input:**

```text
Enter the number of nodes: 4
Enter the cost matrix:
Enter 999 for no direct connection
0 2 5 999
2 0 1 4
5 1 0 2
999 4 2 0
```

**Output:**

```text
Final Distance Table:

       N1    N2    N3    N4
N1      0     2     3     5
N2      2     0     1     3
N3      3     1     0     2
N4      5     3     2     0
```

## RESULT
Thus, the Distance Vector Routing Algorithm was implemented using Python, and the shortest distance between all nodes was obtained.

---

# Experiment 10 – Implementation of Link State Routing Algorithm

## AIM
To implement the Link State Routing Algorithm using Python and find the shortest path and minimum cost from a source node to all other nodes in a network.

## ALGORITHM
1. Start the program.
2. Read the number of nodes in the network.
3. Read the cost/adjacency matrix.
4. Select the source node.
5. Initialize the distance of the source node as 0 and all other nodes as infinity.
6. Select the unvisited node with the smallest distance.
7. Mark the selected node as visited.
8. Update the distance of its neighbouring nodes using:

   `New Distance = Current Distance + Link Cost`

9. Repeat steps 6–8 until all reachable nodes are visited.
10. Display the shortest distance from the source node to every other node.
11. Stop.

## PROGRAM

```python
INF = 999

# Read number of nodes
n = int(input("Enter the number of nodes: "))
if n <= 0:
    raise ValueError("Number of nodes must be greater than zero.")

# Read cost/adjacency matrix
print("Enter the cost matrix:")
print("Enter 999 for no direct connection")

graph = []
for i in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
        raise ValueError("Each row must contain exactly n values.")
    if any(value < 0 for value in row):
        raise ValueError("Dijkstra's algorithm requires non-negative link costs.")
    graph.append(row)

# Read source node (1-based input)
source = int(input("Enter the source node: ")) - 1
if source < 0 or source >= n:
    raise ValueError("Invalid source node.")

distance = [INF] * n
visited = [False] * n
distance[source] = 0

# Dijkstra's shortest-path algorithm
for _ in range(n):
    min_distance = INF
    current = -1

    for i in range(n):
        if not visited[i] and distance[i] < min_distance:
            min_distance = distance[i]
            current = i

    if current == -1:
        break

    visited[current] = True

    for neighbour in range(n):
        link_cost = graph[current][neighbour]
        if not visited[neighbour] and link_cost < INF:
            new_distance = distance[current] + link_cost
            if new_distance < distance[neighbour]:
                distance[neighbour] = new_distance

print("\nShortest Paths from Node", source + 1)
for i in range(n):
    if distance[i] >= INF:
        print(f"Node {source + 1} -> Node {i + 1} : No Path")
    else:
        print(f"Node {source + 1} -> Node {i + 1} : {distance[i]}")
```

## OUTPUT

**Sample input:**

```text
Enter the number of nodes: 4
Enter the cost matrix:
Enter 999 for no direct connection
0 2 5 999
2 0 1 4
5 1 0 2
999 4 2 0
Enter the source node: 1
```

**Output:**

```text
Shortest Paths from Node 1
Node 1 -> Node 1 : 0
Node 1 -> Node 2 : 2
Node 1 -> Node 3 : 3
Node 1 -> Node 4 : 5
```

## RESULT
Thus, the Link State Routing Algorithm was successfully implemented using Python, and the shortest paths from the selected source node to all other nodes were determined.

---

# Experiment 11 – Simulation of Routing Protocols and VLAN Configuration Using Cisco Packet Tracer

## AIM
To simulate routing protocols using RIP version 2 and configure Virtual Local Area Networks (VLANs) using Cisco Packet Tracer, and to verify communication between different networks.

## ALGORITHM

### Part A – Simulation of Routing Protocols
1. Start Cisco Packet Tracer.
2. Place two routers and two PCs in the workspace.
3. Connect each PC to a router and connect the two routers.
4. Assign IP addresses to all PCs and router interfaces.
5. Enable the router interfaces using the `no shutdown` command.
6. Configure RIP version 2 on both routers.
7. Configure the default gateway on each PC.
8. Verify the routing table using `show ip route`.
9. Test connectivity between the PCs using `ping`.

### Part B – VLAN Configuration
10. Place one switch and four PCs in the workspace.
11. Connect all PCs to the switch using Copper Straight-Through cables.
12. Create VLAN 10 and VLAN 20 on the switch.
13. Assign switch ports Fa0/1 and Fa0/2 to VLAN 10.
14. Assign switch ports Fa0/3 and Fa0/4 to VLAN 20.
15. Configure IP addresses for all PCs in their respective subnets.
16. Verify the VLAN configuration using `show vlan brief`.
17. Test communication between PCs in the same VLAN and in different VLANs.

## PROGRAM / CISCO IOS COMMANDS

### Part A – IP addressing table

| Device | Interface | IP address | Subnet mask |
|---|---|---|---|
| PC0 | NIC | 192.168.1.2 | 255.255.255.0 |
| Router0 | G0/0 | 192.168.1.1 | 255.255.255.0 |
| Router0 | G0/1 | 10.0.0.1 | 255.255.255.252 |
| Router1 | G0/1 | 10.0.0.2 | 255.255.255.252 |
| Router1 | G0/0 | 192.168.2.1 | 255.255.255.0 |
| PC1 | NIC | 192.168.2.2 | 255.255.255.0 |

Default gateways:
- PC0 – `192.168.1.1`
- PC1 – `192.168.2.1`

### Router0 configuration

```text
enable
configure terminal

interface gigabitEthernet 0/0
ip address 192.168.1.1 255.255.255.0
no shutdown
exit

interface gigabitEthernet 0/1
ip address 10.0.0.1 255.255.255.252
no shutdown
exit

router rip
version 2
no auto-summary
network 192.168.1.0
network 10.0.0.0
end
```

### Router1 configuration

```text
enable
configure terminal

interface gigabitEthernet 0/0
ip address 192.168.2.1 255.255.255.0
no shutdown
exit

interface gigabitEthernet 0/1
ip address 10.0.0.2 255.255.255.252
no shutdown
exit

router rip
version 2
no auto-summary
network 192.168.2.0
network 10.0.0.0
end
```

### Verify routing

```text
show ip route
```

From PC0:

```text
ping 192.168.2.2
```

### Part B – VLAN configuration

| PC | VLAN ID | IP address | Subnet mask |
|---|---|---|---|
| PC0 | 10 | 192.168.10.2 | 255.255.255.0 |
| PC1 | 10 | 192.168.10.3 | 255.255.255.0 |
| PC2 | 20 | 192.168.20.2 | 255.255.255.0 |
| PC3 | 20 | 192.168.20.3 | 255.255.255.0 |

### Switch VLAN configuration

```text
enable
configure terminal

vlan 10
name CSE
exit

vlan 20
name ECE
exit

interface range fastEthernet 0/1-2
switchport mode access
switchport access vlan 10
exit

interface range fastEthernet 0/3-4
switchport mode access
switchport access vlan 20
exit

end
```

### Verify VLANs

```text
show vlan brief
```

Test communication:
- PC0 to PC1 – Same VLAN; expected to succeed.
- PC2 to PC3 – Same VLAN; expected to succeed.
- PC0 to PC2 – Different VLANs; expected to fail because inter-VLAN routing is not configured.

## OUTPUT

### Part A – Routing table verification

Representative `show ip route` entries on Router0:

```text
R   192.168.2.0/24 [120/1] via 10.0.0.2
C   192.168.1.0/24 is directly connected
C   10.0.0.0/30 is directly connected
```

Ping test from PC0:

```text
ping 192.168.2.2

Reply from 192.168.2.2: bytes=32 time<1ms TTL=126
Reply from 192.168.2.2: bytes=32 time<1ms TTL=126
Reply from 192.168.2.2: bytes=32 time<1ms TTL=126
Reply from 192.168.2.2: bytes=32 time<1ms TTL=126
```

### Part B – VLAN verification

Representative `show vlan brief` output:

```text
VLAN   Name       Status    Ports
1      default    active
10     CSE        active    Fa0/1, Fa0/2
20     ECE        active    Fa0/3, Fa0/4
```

Expected ping results:

| Test | Expected result |
|---|---|
| PC0 to PC1 (same VLAN) | Successful |
| PC2 to PC3 (same VLAN) | Successful |
| PC0 to PC2 (different VLANs) | Request timed out; inter-VLAN routing is not configured |

The first ping may time out while ARP resolution takes place. Actual output may vary with the Packet Tracer device model and configuration.

## RESULT
The simulation of RIP version 2 routing and VLAN configuration was completed using Cisco Packet Tracer. Routing between different IP networks and communication within VLANs were verified.

---

# Experiment 12 – Analysis of Network Traffic and Application Layer Services

## AIM
To capture and analyze network traffic using Python and identify various application layer services and network protocols based on packet information.

## ALGORITHM
1. Start the program and import the required Scapy modules.
2. Define a function to analyze each captured network packet.
3. Check whether the packet contains an IP layer.
4. Extract the source IP address, destination IP address and packet length.
5. Identify the protocol using DNS, TCP and UDP headers.
6. Identify application layer services using port numbers such as 53, 80, 443, 25 and 21.
7. Display the packet details and the corresponding protocol.
8. Capture a specified number of packets from the network interface.
9. Stop the capture and display the completion message.

## PROGRAM

Install Scapy before running:

```bash
python -m pip install scapy
```

On Windows, packet capture may also require Npcap. Run the terminal with the required capture permissions. The program captures 10 IP packets; generate network activity while it is running.

```python
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
```

## OUTPUT

Representative output:

```text
Network Traffic Analysis Started

Source IP        : 192.168.1.5
Destination IP   : 8.8.8.8
Service/Protocol : DNS
Packet Length    : 74 bytes
----------------------------------------

Source IP        : 192.168.1.5
Destination IP   : 142.250.183.14
Service/Protocol : HTTPS/TLS
Packet Length    : 128 bytes
----------------------------------------

...

Network Traffic Analysis Completed
```

The program captures packets generated by network activities such as opening a website, sending DNS queries and establishing TCP connections. Actual IP addresses, packet lengths and services depend on the captured traffic.

## RESULT
Thus, network traffic was captured and analyzed using Python and Scapy. Various network protocols and application layer services were identified based on the captured packet information.

---

## End of 12 Regular Experiments
