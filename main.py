from fastapi import FastAPI
import psutil
import platform
import subprocess

app = FastAPI()

@app.get("/system")
def system_health():
    return {
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent
    }

@app.get("/ping/{host}")
def ping_host(host: str):
    try:
        # Detect OS and apply correct ping command
        param = "-n" if platform.system().lower() == "windows" else "-c"
        result = subprocess.run(["ping", param, "1", host], stdout=subprocess.DEVNULL)
        return {"status": "reachable" if result.returncode == 0 else "unreachable"}
    except:
        return {"status": "error"}
    
@app.get("/port/{port}")
def check_port(port: int):
    try:
        # Windows fix (nc not available)
        if platform.system().lower() == "windows":
            return {"error": "Port scan not supported on Windows"}
        
        result = subprocess.run(["nc", "-zv", "127.0.0.1", str(port)], stdout=subprocess.DEVNULL)
        return {"port_open": result.returncode == 0}
    except:
        return {"error": "Command failed"}
