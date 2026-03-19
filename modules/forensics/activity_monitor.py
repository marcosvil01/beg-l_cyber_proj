import psutil

def get_system_stats():
    """
    Returns a dictionary with CPU usage, virtual memory, and top 5 processes.
    Using interval=None for non-blocking GUI updates.
    """
    stats = {
        "cpu_percent": psutil.cpu_percent(interval=None),
        "memory_percent": psutil.virtual_memory().percent,
        "processes": []
    }
    
    # Get top 5 CPU consuming processes (Note: first call might return 0.0)
    for proc in sorted(psutil.process_iter(['name', 'cpu_percent']), key=lambda x: x.info.get('cpu_percent', 0), reverse=True)[:5]:
        stats["processes"].append({
            "name": proc.info['name'],
            "cpu": proc.info.get('cpu_percent', 0)
        })
        
    return stats
