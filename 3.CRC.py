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
