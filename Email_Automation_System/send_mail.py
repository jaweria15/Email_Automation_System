from flask import Flask, request, render_template, flash, redirect
import smtplib
import ssl
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flashing messages


@app.route('/')
def index():
    return render_template('email_form.html')


@app.route('/', methods=['POST'])
def send_email():
    # Collect form data
    Name = request.form.get('Name')
    receiver_email = request.form.get('receiver_email')
    subject = request.form.get('subject')
    manager_name = request.form.get('manager_name')
    field = request.form.get('field')
    company_name = request.form.get('company_name')
# replace all information according to yours
    if Name == 'Jaweria' or Name == 'jaweria': # replace jaweria to your name 
        sender_email = 'abc@gmail.com' #replace this email with yours email 
        email_pass = '16 digit email password'  # In readme file I mention how to get this password 
        phone = '+92XXXXXX' 
        linkedin = 'https://www.linkedin.com/in/jaweria15/'

    elif Name == 'your_name' or Name == 'your_name':
        sender_email = 'abc3@gmail.com'
        email_pass = '16 digit email password'
        phone = '+92xxxxxxxx'
        linkedin = 'https://pk.linkedin.com/in/muhammadfurqannasir'

    if field == 'Python' or 'python':
        specific = 'programming'

    elif field == 'Machine Learning ' or 'machine learning':
        specific = 'programming and data analysis'


    body = f'''Hi {manager_name},

    I hope you're doing well. My name is {Name}, and I'm currently pursuing my Bachelor's in Computer Science. I am seeking a {field} internship to apply my {specific} skills.

    I've worked on projects like the Email Automation System and Image to Pencil Sketch, showcasing my proficiency in Python and web development with Flask. Additionally, my Bitcoin Price Prediction project helped me deepen my understanding of time series forecasting and deep learning models like LSTM.

    I've attached my resume for your reference and would appreciate the opportunity to discuss any available positions at {company_name}.

    Thank you for your time!

    Best regards,
    {Name}
    {phone}
    {linkedin}
    '''

    # Compose the message
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.set_content(body)

    # Send the email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender_email, email_pass)
            smtp.send_message(message)
        flash("Email sent successfully!", "success")
    except Exception as e:
        flash(f"Failed to send email. Error: {e}", "error")

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
