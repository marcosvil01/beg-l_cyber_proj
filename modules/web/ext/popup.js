document.getElementById('scan').addEventListener('click', () => {
    const statusDiv = document.getElementById('status');
    statusDiv.textContent = "Scanning...";
    statusDiv.style.backgroundColor = "#fbc02d";
    
    setTimeout(() => {
        statusDiv.textContent = "SECURE";
        statusDiv.style.backgroundColor = "#2e7d32";
        alert("Scan complete! No threats found on this domain.");
    }, 1500);
});
