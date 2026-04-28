import time
from datetime import datetime

#current timestamp
timestamp = time.time()

formatted = f"{timestamp:,.4f}"
scientific = f"{timestamp:.2e}"

print(f"Seconds since January 1, 1970: {formatted} or {scientific} in scientific notation")

#Oct 21 2022
date_str = datetime.now().strftime("%b %d %Y") #strftime() - Format time tuple as string.
print(date_str)