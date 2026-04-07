# 🔐 Python Networking Scripts

This repository contains basic networking tools written in Python using the built-in `socket` module.

These scripts are designed for **learning and experimenting with networking concepts** such as port scanning and banner grabbing.

---

## 📦 Tools Included

### 🔎 Port Scanner

Scans a range of TCP ports on a target machine to identify open ports.

### 📡 Banner Grabber

Connects to a specific port and retrieves the service banner.

---

## ✨ Features

- Basic error handling
- Uses Python’s built-in `socket` module
- Interactive input (no command-line arguments required)
- Option to save scan results to a file

---

## 🛠️ Requirements

- Python 3.x
- No external libraries needed

---

## 🚀 How to Run

### 1. Port Scanner

Run the script:

```bash
python port_scanner.py
```

You will be prompted to enter:

- Target IP address or hostname
- Starting port
- Ending port
- Prompt question to save results

Example:

```text
Enter the target that you want to scan:
192.168.1.1
Enter first port: 20
Enter last port: 80
Save results to file? (y/n): y
Please enter filename: results.txt
```

Output:

```text
Scanning...

[+] Port 22 is OPEN
[+] Port 80 is OPEN
```

---

### 2. Banner Grabber

Run the script:

```bash
python banner_grabber.py
```

You will be prompted to enter:

- Target IP address or hostname
- Port number

Example:

```text
Enter the address you want to grab banner from:
192.168.1.1
Enter port number: 22
Connected!
b'SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3\r\n'
```

---

## 📁 Project Structure

```text
.
├── port_scanner.py
├── banner_grabber.py
└── README.md
```

---

## ⚠️ Disclaimer

> 🚨 This project is for educational purposes only.

- Only use these scripts on systems you own or have permission to test.
- Unauthorized port scanning or banner grabbing may be illegal.

---

## 📜 License

This project is licensed under the MIT License.

---
