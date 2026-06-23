# OpsCenter

<p align="center">
  <img src="./assets/banner.png" alt="OpsCenter" width="800"/>
</p>

InfraHub is a platform built for IT professionals, sysadmins, and DevOps learners who want faster, smarter infrastructure management. Download preconfigured system installers, access ready-to-run Ansible playbooks, and deploy containerized environments with a single command — all from one place.

---

## 📺 Video Tutorials

| Thumbnail | Tutorial |
|-----------|----------|
| [![Setup Flask App](https://img.youtube.com/vi/YOUR_VIDEO_ID_1/mqdefault.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_1) | **Setting Up a Flask App from Scratch** — Clone the repo, create a virtual environment, install dependencies, and run your first local server. |
| [![Reverse Proxy Setup](https://img.youtube.com/vi/YOUR_VIDEO_ID_2/mqdefault.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_2) | **Configuring a Reverse Proxy** — Route traffic through Nginx or Caddy to your Flask app running on a local port. |
| [![Docker Deploy](https://img.youtube.com/vi/YOUR_VIDEO_ID_3/mqdefault.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_3) | **Deploying with Docker** — Containerize the app and run it with a single command using a preconfigured Dockerfile. |
| [![Autoinstaller ISO](https://img.youtube.com/vi/YOUR_VIDEO_ID_4/mqdefault.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_4) | **Building an Autoinstaller ISO** — Create a bootable ISO with preseed/kickstart configs for hands-free system provisioning. |

> Replace `YOUR_VIDEO_ID_1` etc. with the actual YouTube video IDs from your video URLs (e.g. `https://youtube.com/watch?v=dQw4w9WgXcQ` → ID is `dQw4w9WgXcQ`).

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
