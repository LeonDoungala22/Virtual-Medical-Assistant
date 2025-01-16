$(document).ready(function () {
    const chatBox = $("#chat-box");

    function appendMessage(sender, message) {
        const alignment = sender === "You" ? "text-end" : "text-start";
        chatBox.append(`<div class="${alignment} mb-2"><strong>${sender}:</strong> ${message}</div>`);
        chatBox.scrollTop(chatBox[0].scrollHeight); // Scroll to bottom
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
                $("#user-input").val(""); // Clear input
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
});
