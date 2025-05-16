const form = document.getElementById("chat-form");
const input = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  
  const userMessage = input.value;
  appendMessage(userMessage, "user");
  input.value = "";

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: userMessage })
    });

    const data = await response.json();
    appendMessage(data.reply, "bot");
  } catch (error) {
    appendMessage("⚠️ Error getting reply.", "bot");
  }
});

function appendMessage(message, sender) {
  const div = document.createElement("div");
  div.className = sender;
  div.textContent = message;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}
