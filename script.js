async function sendMessage() {

    let input = document.getElementById("message");
    let message = input.value.trim();

    if (message === "") return;

    let chat = document.getElementById("chat");

    chat.innerHTML += `
        <p><b>You:</b> ${message}</p>
    `;

    input.value = "";

    try {

        let response = await fetch("http://127.0.0.1:5000/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        let data = await response.json();

        chat.innerHTML += `
            <p><b>Spidey-AI:</b> ${data.reply}</p>
        `;

    } catch (error) {

        chat.innerHTML += `
            <p><b>Spidey-AI:</b> Unable to connect to backend.</p>
        `;

    }

    chat.scrollTop = chat.scrollHeight;
}
