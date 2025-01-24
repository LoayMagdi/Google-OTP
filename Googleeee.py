import requests
import time
import os
import pyperclip
from colorama import Fore, Style, init
from rich.console import Console
from rich.panel import Panel
import sys  # Import sys for exit()
#sfbrxuufteprixr115446-zone-resi
#ljgdacsxij
# Initialize colorama
init(autoreset=True)
#7d2e231fcdc0ad3e2228f381ea8c4928c3a33f62
# Initialize rich console
console = Console()

# Function to display the logo
def LOGO():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console for Windows and Unix
    console.print(
        Panel(""" 
[bold blue]██╗      ██████╗  █████╗    ██╗   ██╗
[bold blue]██║      ██╔═══██╗██╔══██╗  ██║   ██║
[bold green]██║      ██║   ██║███████║  ██║   ██║
[bold white]██║      ██║   ██║██╔══██║╚ ██╗   ██╔╝
[bold white]███████  ╚██████╔╝██║  ██║  ╚████╔██║╝ 
[bold white]╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚═══╝██║
[bold white]                            ████████
[bold #FFD700]Coded By LoayMagdy
[bold #7289DA]Discord:scorepion
[underline green]WhatsApp:+201100575125""", width=55, style="bold bright_white"))


# Prompt the user to input their token
token = input(Fore.MAGENTA + Style.BRIGHT + "Please enter your token:   7d2e231fcdc0ad3e2228f381ea8c4928c3a33f62 ")

# First API URL to get the phone number and ID
url_get_number = f"https://api.thuesim.app/api/google/{token}"

# Base URL for the second API (we'll append the ID later)
url_get_otp_base = "https://api.thuesim.app/api/order"

def get_otp():
    try:
        # Step 1: Fetch the phone number and ID from the first API
        response_number = requests.get(url_get_number)
        response_number.raise_for_status()
        number_data = response_number.json()  # Convert response to JSON

        # Extract phone number and ID from the response
        phone_number = number_data.get("phoneNumber")  # Phone number
        number_id = number_data.get("id")  # ID

        if phone_number and number_id:
            # Display phone number in yellow and ID in blue
            console.print(f"\n[bold Red]Phone Number: [bold cyan]{phone_number}")
            console.print(f"[bold Red]ID: [bold cyan ]{number_id}")

            # Copy the phone number to the clipboard
            pyperclip.copy(phone_number)
            console.print(f"[bold green]Phone number copied to clipboard ")

            # Wait for user input to request the OTP
            input(Fore.MAGENTA + "Press Enter to start fetching the OTP...")

            # Step 2: Build the OTP API URL using the ID
            url_get_otp = f"{url_get_otp_base}/{number_id}/{token}"

            otp = None
            while True:
                # Print a message indicating a new attempt
                console.print("[bold yellow]Attempting to fetch OTP...")

                # Fetch the OTP
                response_otp = requests.get(url_get_otp)
                response_otp.raise_for_status()
                otp_data = response_otp.json()  # Convert response to JSON

                # Extract OTP from the response
                otp = otp_data.get("code")  # Get the value of "code"

                if otp:
                    # Copy the OTP to the clipboard
                    pyperclip.copy(otp)
                    console.print(f"[bold green]\nOTP: [bold yellow]{otp}")
                    console.print(f"[bold cyan]OTP copied to clipboard: [bold yellow]{otp}")
                    break
                else:
                    console.print("[bold Red]OTP not received yet... Retrying in 3 seconds.")

                # Wait for 3 seconds before the next attempt
                time.sleep(3)

        else:
            console.print("[bold red]The response does not contain a phone number or ID.")
            input(Fore.MAGENTA + "Press any key to close...")  # Wait for the user to press any key to close the program
            sys.exit()  # Close the program immediately after key press

    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error while fetching data: {e}")

# Main loop to get new numbers and OTPs
while True:
    # Display the logo
    LOGO()

    # Call the function to fetch number and OTP
    get_otp()

    # Wait for the user to press Enter to get a new number
    input(Fore.MAGENTA + "Press Enter to get a new number and OTP...")
