# 🔧 System Health Monitoring API

A lightweight backend API built using **FastAPI** and **Python** to monitor system performance metrics such as CPU usage, RAM usage, disk usage, network status, ping availability, and port checks.  
This project demonstrates backend development, Linux interaction, and networking fundamentals — ideal for system and backend engineering roles.

---

## 🚀 Features

- 📊 **System Metrics Monitoring**  
  Returns CPU, RAM, and disk usage in real time.

- 🖥️ **Linux Command Integration**  
  Uses Python + Linux commands to fetch OS-level system data.

- 🌐 **Networking Checks**  
  - Ping a host to check reachability  
  - Check if a local port is open  

- ⚡ **REST API Endpoints**  
  Built using FastAPI for fast and scalable backend development.

---

## 🛠 Tech Stack

- **Backend:** FastAPI, Python  
- **System Monitoring:** psutil  
- **OS Commands:** subprocess  
- **Platform:** Linux / Windows (auto-detection)

---

## 📂 API Endpoints

### GET `/system`
Returns CPU, RAM, and disk usage.

```json
{
  "cpu_usage": 14.2,
  "memory_usage": 52.3,
  "disk_usage": 71.5
}
