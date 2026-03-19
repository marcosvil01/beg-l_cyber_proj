import os
from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(file_path):
    """
    Extracts high-value forensic metadata and file system stats.
    """
    results = {
        "File Info": {
            "Name": os.path.basename(file_path),
            "Size (KB)": round(os.path.getsize(file_path) / 1024, 2),
            "Format": os.path.splitext(file_path)[1].upper()
        },
        "Forensic Meta": {}
    }
    
    try:
        img = Image.open(file_path)
        exif_data = img._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                # Filter for valuable forensic info
                if tag_name in ["Make", "Model", "Software", "DateTimeOriginal", "GPSInfo", "Software", "Artist", "HostComputer"]:
                    results["Forensic Meta"][tag_name] = str(value)
        
        if not results["Forensic Meta"]:
            results["Forensic Meta"] = "No EXIF data detected."
            
    except Exception as e:
        results["Error"] = f"Failed to parse image: {str(e)}"
        
    return results
