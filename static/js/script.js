document.addEventListener("DOMContentLoaded", () => {
  const chatWindow = document.getElementById("chatWindow");
  const welcomeState = document.getElementById("welcomeState");
  const messagesEl = document.getElementById("messages");
  const chatForm = document.getElementById("chatForm");
  const messageInput = document.getElementById("messageInput");
  const sendBtn = document.getElementById("sendBtn");
  const clearChatBtn = document.getElementById("clearChatBtn");

  function scrollToBottom() {
    chatWindow.scrollTop = chatWindow.scrollHeight;
  }

  function hideWelcome() {
    if (welcomeState) {
      welcomeState.style.display = "none";
    }
  }

  function addMessage(text, role) {
    const msg = document.createElement("div");
    msg.className = `msg ${role}`;

    const avatar = document.createElement("div");
    avatar.className = "msg-avatar";
    avatar.textContent = role === "user" ? "🧑" : "🩺";

    const bubble = document.createElement("div");
    bubble.className = "msg-bubble";

    if (role === "bot" && window.marked) {
      bubble.innerHTML = marked.parse(text);
    } else {
      bubble.innerHTML = text;
    }

    msg.appendChild(avatar);
    msg.appendChild(bubble);
    messagesEl.appendChild(msg);
    scrollToBottom();

    return bubble;
  }

  function addTypingIndicator() {
    const msg = document.createElement("div");
    msg.className = "msg bot";
    msg.id = "typingIndicator";

    const avatar = document.createElement("div");
    avatar.className = "msg-avatar";
    avatar.textContent = "🩺";

    const bubble = document.createElement("div");
    bubble.className = "msg-bubble";
    bubble.innerHTML =
      '<span class="typing-dots"><span></span><span></span><span></span></span>';

    msg.appendChild(avatar);
    msg.appendChild(bubble);
    messagesEl.appendChild(msg);
    scrollToBottom();
  }

  function removeTypingIndicator() {
    const typing = document.getElementById("typingIndicator");
    if (typing) typing.remove();
  }

  async function sendMessage(text) {
    if (!text.trim()) return;

    hideWelcome();
    addMessage(escapeHtml(text), "user");
    messageInput.value = "";
    sendBtn.disabled = true;
    addTypingIndicator();

    try {
      const response = await fetch("/get", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ msg: text }),
      });

      const answer = await response.text();
      removeTypingIndicator();
      addMessage(answer, "bot");
    } catch (err) {
      removeTypingIndicator();
      addMessage(
        "Sorry, something went wrong reaching the server. Please try again.",
        "bot",
      );
    } finally {
      sendBtn.disabled = false;
      messageInput.focus();
    }
  }

  function escapeHtml(str) {
    const div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
  }

  chatForm.addEventListener("submit", (e) => {
    e.preventDefault();
    sendMessage(messageInput.value);
  });

  document.querySelectorAll(".chip").forEach((chip) => {
    chip.addEventListener("click", () => {
      sendMessage(chip.dataset.question);
    });
  });

  clearChatBtn.addEventListener("click", () => {
    messagesEl.innerHTML = "";
    if (welcomeState) welcomeState.style.display = "block";
  });
});
