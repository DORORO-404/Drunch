# 🔐 Drunch - Custom Wordlist Generator

![Project Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.x-yellow)
![Platform](https://img.shields.io/badge/platform-Kali%20Linux%20%7C%20Windows%20%7C%20Linux-informational)

> A modern, Python-based alternative to `crunch` for generating wordlists with full customization and no dependencies.

---

## 🚀 About The Project

**Drunch** is a simple and powerful CLI wordlist generator designed for **penetration testers**, **CTF players**, and **security researchers**.  
It gives you full control over the **character set**, **minimum/maximum length**, and allows saving generated lists into organized output folders.

It brings the flexibility of tools like `crunch`, but in a more readable, beginner-friendly, and Pythonic way.

---

## ✨ Features

- ✅ Choose between numbers, letters, or custom characters
- ✅ Set custom minimum and maximum word lengths
- ✅ Fast generation using `itertools.product`
- ✅ Save results in `wordlists/` folder automatically
- ✅ Clean and colored terminal UI
- ✅ Offline tool, zero dependencies
- ✅ KeyboardInterrupt and safe exit handling
- ✅ Compatible with Kali Linux & Windows

---

## 🛠️ Built With

| Language    | Type     | Dependencies        |
|-------------|----------|---------------------|
| Python 3.x  | CLI Tool | None (uses built-ins only) |

---

## 📦 Installation

```bash
git clone https://github.com/DORORO-404/Drunch.git
cd Drunch
pip install -r requirements.txt
python drunch.py
```

## 🖥️ Example Usage
```bash
[+] ===== Welcome to Drunch Wordlist Generator ===== [+]
Enter the minimum password length: 2
Enter the maximum password length: 5

Choose a character set:
[1] Numbers only (0-9)
[2] Letters only (a-z)
[3] Custom characters
Enter your choice (1, 2, or 3): 1

Enter a file name to save the wordlist: passwords

[+] Generating the wordlist. Please wait...
Wordlist saved successfully as 'wordlists/passwords.txt'

Would you like to generate another wordlist? [Y/n]:
```

## 🤝 Contributing

Contributions are always welcome! Here’s how you can contribute:

1. Fork the repository.
2. Create your branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

Feel free to open issues for any bugs or feature requests.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## 📁 Project Structure
Drunch/
├── drunch.py              # Main Python script for the wordlist generator
├── README.md              # Project documentation
├── LICENSE                # MIT License file
└── wordlists/             # Folder where generated wordlists are saved
    └── passwords.txt      # Example output file
