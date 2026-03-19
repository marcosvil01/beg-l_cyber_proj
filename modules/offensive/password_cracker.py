import hashlib
import os
import itertools
import string

def crack_password(target_hash, hash_type, dictionary_path, progress_callback=None):
    """
    Attempts to crack a password hash using a dictionary attack.
    """
    if not os.path.exists(dictionary_path):
        return f"Error: Dictionary file not found."

    try:
        # Count lines for progress
        total_lines = sum(1 for _ in open(dictionary_path, 'r', encoding='utf-8', errors='ignore'))
        current_line = 0
        
        with open(dictionary_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                word = line.strip()
                if hash_type == "md5":
                    current_hash = hashlib.md5(word.encode()).hexdigest()
                elif hash_type == "sha256":
                    current_hash = hashlib.sha256(word.encode()).hexdigest()
                else:
                    return "Error: Unsupported hash type."

                if current_hash == target_hash:
                    return f"SUCCESS! Password found: {word}"
                
                current_line += 1
                if progress_callback and current_line % 100 == 0:
                    progress_callback(current_line / total_lines)
        
        return "FAILED: Password not in dictionary."
    except Exception as e:
        return f"Error: {str(e)}"

def brute_force(target_hash, hash_type, max_length=4, char_sets=None, progress_callback=None):
    """
    Enhanced Brute-force with multiple character sets.
    char_sets: list containing 'lower', 'upper', 'digits', 'special'
    """
    import time
    chars = ""
    if not char_sets: char_sets = ["lower", "digits"]
    
    if "lower" in char_sets: chars += string.ascii_lowercase
    if "upper" in char_sets: chars += string.ascii_uppercase
    if "digits" in char_sets: chars += string.digits
    if "special" in char_sets: chars += string.punctuation
    
    if not chars: chars = string.ascii_lowercase

    total_combinations = sum(len(chars)**i for i in range(1, max_length + 1))
    current_attempt = 0
    start_time = time.time()

    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            word = "".join(guess)
            if hash_type == "md5":
                current_hash = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == "sha256":
                current_hash = hashlib.sha256(word.encode()).hexdigest()
            
            if current_hash == target_hash:
                elapsed = time.time() - start_time
                return f"SUCCESS! Found: {word} (Time: {elapsed:.2f}s)"
            
            current_attempt += 1
            if progress_callback and current_attempt % 1000 == 0:
                progress_callback(current_attempt / total_combinations)
                
    return "FAILED: Brute-force range exceeded."

if __name__ == "__main__":
    # Example usage for standalone testing
    test_hash = hashlib.sha256("password123".encode()).hexdigest()
    print(f"Target Hash (sha256 of 'password123'): {test_hash}")
    # Note: In a real scenario, we'd provide a wordlist file
    # For now, we'll just demonstrate the logic
