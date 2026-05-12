# 🐱 Python Hello Program

A colorful Python terminal program featuring:

- ANSI color output
- ASCII cat art
- Current date & time display
- Clean terminal banner

---

## 📸 Preview

```text
======================================
        PYTHON HELLO PROGRAM
======================================

 /\_/\\
( o.o )
 > ^ <

Hello, World! 👋
Current Time: 2026-05-13 14:32:11
```

---

## 🚀 Features

✅ Colored terminal output  
✅ ASCII Art Cat  
✅ Real-time clock  
✅ Beginner-friendly code  
✅ Works on Linux / macOS / Windows Terminal

---

## 📂 Project Structure

```text
project/
│
├── main.py
└── README.md
```

---

## ▶️ Run the Program

### 1. Clone Repository

```bash
git clone https://github.com/your-username/python-hello-program.git
```

### 2. Enter Project Folder

```bash
cd python-hello-program
```

### 3. Run Python File

```bash
python main.py
```

---

## 🧠 Code Example

```python
from datetime import datetime
import os

# ANSI Colors
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Enable ANSI colors on Windows
os.system("")

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
```

---

## 🎨 ANSI Color Reference

| Color | Code |
|------|------|
| Green | `\033[92m` |
| Cyan | `\033[96m` |
| Yellow | `\033[93m` |
| Reset | `\033[0m` |

---

## 📌 Requirements

- Python 3.8+
- Terminal supporting ANSI colors

---

## ❤️ Author

Made with Python & coffee ☕

---

## 📜 License

MIT License