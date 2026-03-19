import psutil

def get_system_stats():
    """
    Returns a dictionary with CPU usage, virtual memory, and top 5 processes.
    """
    stats = {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "processes": []
    }
    
    # Get top 5 CPU consuming processes
    for proc in sorted(psutil.process_iter(['name', 'cpu_percent']), key=lambda x: x.info['cpu_percent'], reverse=True)[:5]:
        stats["processes"].append({
            "name": proc.info['name'],
            "cpu": proc.info['cpu_percent']
        })
        
    return stats
