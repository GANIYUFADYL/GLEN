from flask import Flask, render_template, jsonify, request
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv() 

EMAIL_USER="ganiyufadi@gmail.com"
EMAIL_PASS="fnirixblextjgzku"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/content")
def content():
    return render_template("content.html")

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()
    choice = data.get("choice")
    subject = "Tam's Response"
    body = f"Hi Glen,\n\nShe picked {choice}!!!."
    try:
        connection = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        connection.login(user=EMAIL_USER, password=EMAIL_PASS)
        connection.sendmail(from_addr=EMAIL_USER, 
                            to_addrs="gleneze46@gmail.com", 
                            msg=f"Subject: {subject}\n\n{body}")
        connection.quit()
    except smtplib.SMTPConnectError as e:
        print(f"SMTP connection error: {e}")
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
    except TimeoutError as e:
        print(f"Timeout error: {e}")

    return jsonify({"message": f"✅ Response with choice '{choice}' sent successfully!"})

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=3000)

