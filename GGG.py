import requests
import time
import os
import pyperclip

# First API URL to get the phone number and ID
url_get_number = "https://api.thuesim.app/api/google/7d2e231fcdc0ad3e2228f381ea8c4928c3a33f62"

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
            print(f"Phone Number: {phone_number}")
            print(f"ID: {number_id}")

            # Copy the phone number to the clipboard
            pyperclip.copy(phone_number)
            print(f"Phone number copied to clipboard: {phone_number}")

            # Wait for user input to request the OTP
            input("Press Enter to fetch the OTP...")

            # Step 2: Build the OTP API URL using the ID
            url_get_otp = f"{url_get_otp_base}/{number_id}/7d2e231fcdc0ad3e2228f381ea8c4928c3a33f62"

            otp = None
            while otp == "" or otp is None:
                # Fetch the OTP
                response_otp = requests.get(url_get_otp)
                response_otp.raise_for_status()
                otp_data = response_otp.json()  # Convert response to JSON

                # Extract OTP from the response
                otp = otp_data.get("code")  # Get the value of "code"

                if otp:
                    print(f"OTP: {otp}")
                else:
                    print("OTP not received yet, retrying...")

                # Wait for 3 seconds before retrying
                time.sleep(3)

        else:
            print("The response does not contain a phone number or ID.")
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data: {e}")

# Main loop to get new numbers and OTPs
while True:
    # Clear the console to hide previous data
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for Windows and Unix

    # Call the function to fetch number and OTP
    get_otp()

    # Wait for the user to press Enter to get a new number
    input("Press Enter to get a new number and OTP...")
