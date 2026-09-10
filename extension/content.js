// Listen for messages from the background service worker
chrome.runtime.onMessage.addListener((message) => {

    if (message.type === "PHISHING_WARNING") {

        // Create warning box
        const warning = document.createElement("div");

        warning.innerHTML = `
            <div style="
                position: fixed;
                top: 20px;
                left: 50%;
                transform: translateX(-50%);
                z-index: 999999;
                background: #dc2626;
                color: white;
                padding: 20px 30px;
                border-radius: 12px;
                font-family: Arial, sans-serif;
                box-shadow: 0 4px 20px rgba(0,0,0,0.3);
                text-align: center;
                max-width: 500px;
            ">
                <h2 style="margin: 0 0 10px;">
                    ⚠️ Phishing Warning
                </h2>

                <p style="margin: 0 0 10px;">
                    This website may be a phishing website.
                </p>

                <p style="
                    font-size: 12px;
                    word-break: break-all;
                    margin: 0;
                ">
                    ${message.url}
                </p>
            </div>
        `;

        document.body.appendChild(warning);
    }
});