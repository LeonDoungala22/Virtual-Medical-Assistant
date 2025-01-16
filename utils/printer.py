from rich.console import Console
from rich.panel import Panel
from rich.theme import Theme
from rich.text import Text
import warnings

# Suppress warnings
def warn(*args, **kwargs):
    pass

warnings.warn = warn

class Printer:
    def __init__(self):
        """
        Initialize a Printer object with a custom theme for the rich console.

        The theme includes colors for different message types:
        - primary: cyan
        - secondary: magenta
        - success: green
        - error: red
        - info: blue
        """
        theme = Theme({
            "primary": "#00FFFF",    # Futuristic cyan
            "secondary": "#FF00FF",   # Vivid magenta
            "success": "#00FF00",     # Bright green
            "error": "#FF3333",       # Bright red for errors
            "info": "#3399FF",        # Soft blue for info
        })
        self.console = Console(theme=theme)

    def print_message(self, message, message_type="info"):
        """
        Print a message with a specific style based on the message type.

        Parameters:
        - message (str): The message to be printed.
        - message_type (str): The type of message. It can be one of the following:
          - "welcome": Print a welcome message with a custom title and border style.
          - "assistant": Print a message from the virtual assistant with a specific style.
          - "exit": Print an exit message with a bold red color.
          - Any other value: Print the message without any style.

        Returns:
        - None
        """
        panel_title = ""
        panel_style = "info"
        
        if message_type == "welcome":
            panel_title = "🤖 [bold cyan]AI Health Assistant[/bold cyan] 🤖"
            panel_style = "primary"
        elif message_type == "assistant":
            panel_title = "[bold magenta]Assistant[/bold magenta]"
            message = f"{message}"
            panel_style = "info"
        elif message_type == "exit":
            panel_title = "[bold red]Exit[/bold red]"
            panel_style = "error"
        else:
            # General message
            panel_title = None

        # Create and print the panel
        self.console.print(
            Panel(
                Text(message, style=panel_style),
                title=panel_title,
                title_align="center" if message_type == "welcome" else "left",
                border_style=panel_style
            )
        )
