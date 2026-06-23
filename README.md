# OpsCenter

InfraHub is a platform built for IT professionals, sysadmins, and DevOps learners who want faster, smarter infrastructure management. Download preconfigured system installers, access ready-to-run Ansible playbooks, and deploy containerized environments with a single command — all from one place.

---

## 📺 Video Tutorials

| Thumbnail | Tutorial |
|-----------|----------|
| [![Video 1](https://img.youtube.com/vi/qnawmYbv_xY/mqdefault.jpg)](https://youtu.be/qnawmYbv_xY) | **EXAMPLE 1 |
| [![Video 2](https://img.youtube.com/vi/4KiVolDbvIU/mqdefault.jpg)](https://youtu.be/4KiVolDbvIU) | **EXAMPLE 2 |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- Git
- Docker (optional)

### Installation

```bash
# Clone the repository
git clone git@github.com:YOUR_USERNAME/opscenter.git
cd opscenter

# Create and activate virtual environment
python -m venv venv

# Windows (PowerShell)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate

# Install in editable mode
pip install -e .

# Run the app
python app.py
```

---

## 🛠 Features

- **System Installers** — Download preconfigured, ready-to-run installers
- **Ansible Playbooks** — Access and run infrastructure automation playbooks
- **Docker Environments** — Deploy containerized stacks with a single command
- **Reverse Proxy Support** — Built-in config examples for Nginx/Caddy
- **Autoinstaller ISO** — Bootable ISOs for automated bare-metal provisioning

---

## 📦 Project Structure

```
opscenter/
├── app.py
├── pyproject.toml
├── venv/
└── ...
```

---

## 🤝 Contributing

```bash
git add .
git commit -m "Your message"
git push origin main
```

---

## 📄 License

MIT
