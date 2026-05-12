from datetime import datetime
import os

# ANSI Colors
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

os.system("")  # Enable ANSI on some Windows terminals

cat = rf"""
{CYAN}
 /\_/\\
( o.o )
 > ^ <
{RESET}
"""

banner = f"""
{GREEN}======================================
        PYTHON HELLO PROGRAM
======================================{RESET}
"""

message = f"""
{YELLOW}Hello, World! 👋
Current Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
{RESET}
"""

print(banner)
print(cat)
print(message)