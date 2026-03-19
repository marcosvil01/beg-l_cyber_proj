import os
import webbrowser

def launch_phishing_template(template_name="phishing_template.html"):
    """
    Launches the specified phishing template in the default web browser.
    """
    base_dir = os.path.dirname(__file__)
    template_path = os.path.join(base_dir, template_name)
    
    if os.path.exists(template_path):
        url = f"file://{os.path.abspath(template_path)}"
        webbrowser.open(url)
        return True
    return False

def get_awareness_tips():
    return [
        "Check the sender's email address for slight misspellings.",
        "Hover over links to see the actual destination URL.",
        "Be wary of urgent or threatening language.",
        "Look for generic greetings like 'Dear Customer'.",
        "Never provide sensitive information on a site reached via an email link."
    ]
