import PCF8591 as ADC  # Import the library for the PCF8591 module
 import time  # Import the time library for adding delays
 # Initialize the PCF8591 module at I2C address 0x48.
 # This address is used for communication with the Raspberry Pi.
 ADC.setup(0x48)
 try:
    while True:  # Start an infinite loop to continuously monitor the sensor.
        # Read the analog value from the potentiometer connected to AIN0.
        # Channel range from 0 to 3 represents AIN0 to AIN3.
        # The potentiometer's rotation alters the voltage, which is read by the PCF8591.
        potentiometer_value = ADC.read(0)
        print(potentiometer_value)
        # Add a short delay of 0.2 seconds to make the loop more manageable.
        time.sleep(0.2)
 except KeyboardInterrupt:
    # If a KeyboardInterrupt (CTRL+C) is detected, exit the loop and end the program.
    print("Exit")

import smtplib
from email.message import EmailMessage

#Set the sender email and password and recipient email
from_email_addr = "A186268888@outlook.com"
from_email_pass = "cqmygysdssA2"
to_email_addr = "3338125685@qq.com"

# Create a message object
msg = EmailMessage()

# Set the email body
body ="Hello from Raspberry Pi"
msg.set_content(body)

# Set sender and recipient
msg['From'] = from_email_addr
msg['To'] = to_email_addr

# Set your email subject
msg['Subject'] = 'TEST EMAIL'

# Connecting to server and sending email
# Edit the following line with your provider's SMTP server details
server = smtplib.SMTP('smtp.email.com', 587)

# Comment out the next line if your email provider doesn't use TLS
server.starttls()
# Login to the SMTP server
server.login(from_email_addr, from_email_pass)

# Send the message
server.send_message(msg)

print('Email sent')

#Disconnect from the Server
server.quit()
