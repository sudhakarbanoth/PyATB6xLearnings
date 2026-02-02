# Simulate a page loading check using a while loop.
# If page_loaded becomes True within 5 seconds, print success; else timeout.
#
# Hint: Use a counter (like wait_time) and break condition.

import time
import random

wait_time = 0
timeout = 5

while wait_time < timeout:
    # Simulate page load status (True = loaded, False = still loading)
    page_loaded = random.choice([False, True])

    if page_loaded:
        print(f"✅ Page loaded successfully in {wait_time + 1} seconds.")
        break

    print(f"⏳ Waiting... {wait_time + 1} second(s)")
    time.sleep(1)
    wait_time += 1
else:
    print("❌ Timeout: Page did not load within 5 seconds")