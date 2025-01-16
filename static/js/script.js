$(document).ready(function () {
    const chatBox = $("#chat-box");

    function appendMessage(sender, message) {
        const timestamp = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

        // Use FontAwesome icons for AI and User
        const senderIcon = sender === "You" 
            ? '<i class="fas fa-user" style="font-size: 20px;"></i>' 
            : '<i class="fas fa-robot" style="font-size: 20px;"></i>';
        
        const messageHtml = `
            <div class="message ${sender === "You" ? "patient" : "assistant"}">
                <div class="icon">${senderIcon}</div>
                <div class="content">
                    <p>${message}</p>
                    <div class="timestamp">${timestamp}</div>
                </div>
            </div>
        `;
        chatBox.append(messageHtml);
        chatBox.scrollTop(chatBox[0].scrollHeight); // Scroll to the latest message
    }

    $("#send-btn").click(function () {
        const message = $("#user-input").val().trim();
        if (!message) return;

        // Add user message to chat box
        appendMessage("You", message);

        // Send message to backend
        $.ajax({
            url: "/ask",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ message }),
            success: function (data) {
                appendMessage("Assistant", data.response);
                $("#user-input").val(""); // Clear input field
            },
            error: function () {
                alert("Error processing your request. Please try again!");
            }
        });
    });

    // Enable "Enter" key to send message
    $("#user-input").keypress(function (e) {
        if (e.which == 13) {
            $("#send-btn").click();
        }
    });

    // Scroll to the bottom of the chat on page load
    const chat = document.getElementById('chat-box');
    chat.scrollTop = chat.scrollHeight - chat.clientHeight;
});
