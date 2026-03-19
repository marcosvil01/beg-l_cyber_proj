def get_gpu_vs_cpu_stats():
    """
    Returns theoretical benchmarking data for GPU vs CPU cracking.
    """
    return {
        "CPU (Intel i7)": "25,000,000 hashes/sec",
        "GPU (Nvidia RTX 4090)": "120,000,000,000 hashes/sec",
        "Efficiency Factor": "4800x faster"
    }

def get_theory_overview():
    return "GPU cracking works by utilizing thousands of small cores to perform \n" \
           "massively parallel mathematical operations (hashing).\n\n" \
           "Key technologies: CUDA (Nvidia), OpenCL (Generic).\n" \
           "Popular tools: Hashcat, John the Ripper."
