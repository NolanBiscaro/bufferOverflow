# Stack Smash

This project aims to provide an educational resource for understanding buffer overflow vulnerabilities and their exploitation in a controlled environment. It includes a vulnerable program, a buffer overflow exploit, and a detailed analysis of the exploited vulnerability, along with mitigation strategies to protect against similar attacks in the future.

## Dependencies

To run this project, you will need the following dependencies:

- Python 3: Download and install Python 3 from the [official website](https://www.python.org/downloads/).
- Docker: Download and install Docker from the [official website](https://www.docker.com/get-started).
- QEMU: Install QEMU using Homebrew: 

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install qemu
```


## Project Description

The project focuses on exploiting a buffer overflow vulnerability in a target program running on an x86 32-bit virtual machine. The virtual machine is created using Docker and QEMU to ensure compatibility with various host systems, including macOS ARM64.

## How to Use the Project

1. Clone the repository: 
```
git clone https://github.com/yourusername/buffer-overflow-exploit.git
```

2. Change to the project directory: 
```
cd buffer-overflow-exploit
```

3. Run the Python script to start the exploit: 
```
python3 main.py
```


The script will guide you through the exploitation process, showcasing the tools and techniques used to exploit buffer overflow vulnerabilities.

**Note:** This project is for educational purposes only. Do not use it to exploit vulnerabilities in real-world systems without proper authorization.

