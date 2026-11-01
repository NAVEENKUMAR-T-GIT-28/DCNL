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
