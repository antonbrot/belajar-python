# coin_flip.py
import random

heads_count = 0

for i in range(1, 6):
    result = random.choice(["Heads", "Tails"])
    print(f"Flip {i}: {result}")
    if result == "Heads":
        heads_count += 1

print(f"\nJumlah 'Heads' yang muncul: {heads_count}")