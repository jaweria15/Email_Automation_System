# Email Automation System

## Project Overview
This **Email Automation System** is designed to simplify the process of sending customized emails by filling in specific details automatically from a form. It’s especially helpful when you need to send repetitive emails with personalized information, ensuring consistency and saving time.

## Features
- Automatically fills email content based on form input, avoiding manual repetition.
- Allows users to select sender information based on a given name.
- Supports basic email details like recipient email, subject, company name, and hiring manager’s name.
- Provides a convenient, web-based interface for sending emails using **Flask**.

## Tech Stack
- **Flask**: For web application and form handling
- **SMTP (smtplib)**: For email sending functionality
- **HTML**: For the email form interface

## How It Works
1. **User enters details** in a web form, including the recipient's email, subject, name, and additional fields like field of study and company name.
2. **Email template** is populated with these details to create a personalized message.
3. **Email is sent** to the specified recipient using secure SMTP settings.

## Setting up Google App Password for Email Sending
Since Google has strict security policies for less secure app access, you need to set up an **App Password** in your Google account to allow this application to send emails on your behalf.

## Steps to Generate an App Password
1. **Enable Two-Step Verification** for your Google account. This is required to set up an App Password.
   - Go to [Google Account Security](https://myaccount.google.com/security) and turn on **2-Step Verification**.
   
2. After enabling 2-Step Verification, go to the **App Passwords** section:
   - Open this link: [Google App Passwords](https://myaccount.google.com/apppasswords).
   
3. **Create a new App Password**:
   - Under **Select the app**, choose **Other (Custom name)**.
   - Enter a name of your choice (e.g., "Email Automation App").
   - Click **Generate** to get a unique 16-character App Password.
   
4. **Copy the App Password** shown on the screen and paste it into your code:
   - Replace the `email_pass` variable in the code with this password.

   ```python
   email_pass = 'your_generated_app_password_here'
This setup ensures that your Google account remains secure, while still allowing this app to send emails on your behalf.

## Installation Prerequisites
Python 3.x
Flask
## Steps
1. Clone the repository:
Copy code
git clone https://github.com/yourusername/email-automation-system.git

2. Install dependencies:
Copy code
pip install Flask
3. Run the application:
Copy code
python app.py
## Usage
1. Start the Flask app by running python app.py.
2. Open your browser and navigate to http://localhost:5000/.
3. Fill in the required details in the form, such as:
- Your Name
- Receiver’s Email
- Subject
- Field (e.g., Python, Machine Learning)
- Company Name
- Hiring Manager’s Name
4. Click Send Email to send the customized email.
## License
This project is open-source and available for anyone interested in simplifying their email workflows.






