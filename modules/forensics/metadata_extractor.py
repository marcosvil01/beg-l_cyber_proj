import os
from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(file_path):
    """
    Extracts EXIF metadata from an image file and basic file stats.
    """
    results = {
        "File Name": os.path.basename(file_path),
        "Size": os.path.getsize(file_path),
        "EXIF": {}
    }
    
    try:
        img = Image.open(file_path)
        exif_data = img._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                results["EXIF"][tag_name] = str(value)
    except Exception as e:
        results["Error"] = str(e)
        
    return results
