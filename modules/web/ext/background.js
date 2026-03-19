chrome.runtime.onInstalled.addListener(() => {
  console.log("CyberHub Shield installed.");
});

// Mock background security checks
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === 'complete' && tab.url) {
    console.log(`Scanning tab ${tabId}: ${tab.url}`);
    // Here we would implement real-time URL scanning
  }
});
