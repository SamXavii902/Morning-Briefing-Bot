import psutil

def get_system_stats():
    # 1. Battery Check
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    
    if plugged:
        battery_status = f"Charging at {percent}%"
    else:
        battery_status = f"Running on battery at {percent}%"

    # 2. CPU & RAM Check
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    
    return {
        "battery": battery_status,
        "cpu": cpu_usage,
        "ram": ram_usage
    }

def get_vitals_report():
    stats = get_system_stats()
    return f"System Status: {stats['battery']}. CPU load is {stats['cpu']}%. Memory usage is {stats['ram']}%."