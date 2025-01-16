from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from assistant import VirtualHealthAssistant
import warnings

# Suppress warnings
def warn(*args, **kwargs):
    pass

warnings.warn = warn 

# Initialize Flask app
app = Flask(__name__)
load_dotenv()  # Load environment variables from .env file
assistant = VirtualHealthAssistant()
chat_history = []



# Function to format and display chat history
def display_chat_history(chat_history):
    """
    Formats and displays the chat history in a readable way.
    """
    print("\n===== Conversation History =====\n")
    if not chat_history:
        print("No conversation history available.")
    for i, exchange in enumerate(chat_history, 1):
        print(f"Exchange {i}:")
        print(f"    👤 Patient: {exchange['patient_query']}")
        print(f"    🤖 Assistant: {exchange['assistant_response']}\n")
    print("================================\n")


# Main function to run the conversation flow
def run(assistant):
    """
    This function runs the continuous conversation flow with the patient.

    Parameters:
    assistant (VirtualHealthAssistant): An instance of the VirtualHealthAssistant class.
    """
    assistant.printer.print_message("Welcome to the virtual health service. Type 'exit' to quit.", message_type="welcome")
    chat_history = []

    while True:
        assistant.printer.console.print("[bold cyan]You[/bold cyan]:", end=" ")
        patient_query = input().strip()  

        if patient_query.lower() == 'exit':
            assistant.printer.print_message("Thank you for using the service. Goodbye!", message_type="exit")
            display_chat_history(chat_history)
            break

        # Process patient input and get assistant response
        response = handle_patient_query(assistant, patient_query, chat_history)
        chat_history.append({"patient_query": patient_query, "assistant_response": response})  
        assistant.printer.print_message(response, message_type="assistant")
        
        
        
        
        
# Handle patient question
def handle_patient_query(assistant, patient_input, chat_history):
    """
    This function gets the response from the assistant's chat chain based on the patient's input.

    Parameters:
    assistant (VirtualHealthAssistant): An instance of the VirtualHealthAssistant class.
    patient_input (str): The input query from the patient.
    chat_history (list): The conversation history up to the current point.

    Returns:
    str: The response from the assistant.
    """
    response = assistant.chat_chain({"patient_input": patient_input, "chat_history": chat_history})
    return response['text']

@app.route('/')
def home():
    """
    Render the main chat interface.
    """
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    """
    Handle user input from the frontend, process it, and return the assistant's response.
    """
    global chat_history
    user_input = request.json.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "Empty input is not allowed!"}), 400

    response = handle_patient_query(assistant, user_input, chat_history)
    chat_history.append({"patient_query": user_input, "assistant_response": response})
    return jsonify({"response": response, "chat_history": chat_history})

if __name__ == '__main__':
    
    #Run this for web interface chat interaction only
    app.run(debug=True) 

    #Rund this for terminal mode chat interaction only 
    """
    load_dotenv()  # Load environment variables from .env file
    assistant = VirtualHealthAssistant()
    run(assistant)
    """
