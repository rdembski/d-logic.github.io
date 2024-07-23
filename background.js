// background.js

browser.runtime.onMessage.addListener((message, sender, sendResponse) => {
    return new Promise((resolve, reject) => {
        // Twoje asynchroniczne operacje
        resolve();
    });
});
