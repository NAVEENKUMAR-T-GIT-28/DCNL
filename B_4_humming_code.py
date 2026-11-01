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
