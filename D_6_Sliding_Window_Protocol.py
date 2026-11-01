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
