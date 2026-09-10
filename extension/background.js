chrome.tabs.onUpdated.addListener(async (tabId, changeInfo, tab) => {

    if (changeInfo.status !== "complete") {
        return;
    }

    if (!tab.url || !tab.url.startsWith("http")) {
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: tab.url
            })
        });

        if (!response.ok) {
            console.error("API request failed:", response.status);
            return;
        }

        const data = await response.json();

        console.log("URL:", tab.url);
        console.log("API Prediction:", data.prediction);

        if (data.prediction === "Phishing") {
            chrome.tabs.sendMessage(tabId, {
                type: "PHISHING_WARNING",
                url: tab.url
            }).catch(() => {});
        }

    } catch (error) {
        console.error(
            "Could not connect to phishing detection API:",
            error
        );
    }
});