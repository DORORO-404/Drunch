# Drunch - Custom Wordlist Generator

![Project Status](https://img.shields.io/badge/status-active-brightgreen)  
![License](https://img.shields.io/badge/license-MIT-blue)

Welcome to **Drunch**, a Python-based tool inspired by `crunch`. It allows you to generate custom wordlists for use in penetration testing, password research, and ethical hacking.

## 🚀 About The Project

Drunch is a simple, lightweight tool that generates wordlists based on character sets and length ranges. It's designed to replicate and simplify the functionality of the original `crunch` tool, but written fully in Python.

The tool can:

- Generate all possible combinations of a given character set
- Allow control over minimum and maximum word length
- Save wordlists to a file or print them directly

## 🛠 Technologies Used

| Language   | Type     |      Requirements     |
|------------|----------|-----------------------|
| Python 3.x | CLI Tool | No external libraries |

**Python 3**: The tool is written purely in Python with no third-party dependencies, making it easy to run on most systems.

## ✨ Features

- ✅ Simple and fast wordlist generation
- ✅ Choose character set, min & max length
- ✅ Output to file or terminal
- ✅ Lightweight and beginner-friendly code
- ✅ Works offline, no dependencies

## 🧪 **Example Usage**

Generate a wordlist with 4-letter combinations of lowercase letters:

```bash
$ python3 drunch.py