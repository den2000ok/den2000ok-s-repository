import json
from pathlib import Path
scanner_config = {
    "tool_name": "NetSentinel",
    "target_ip": "192.168.1.1",
    "open_ports": [22, 80],
    "is_active": True
}
config_path = Path("sentinel_config.json")
with open(config_path, "w", encoding="utf-8") as f:
    json.dump(scanner_config, f, indent=4)
with open(config_path, "r") as f:
    sentinel_config = json.load(f)
sentinel_config["open_ports"].append(443)
print(sentinel_config["open_ports"])