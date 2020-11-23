# Anna Sandler 208749648
import sys
import smtplib
import urllib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from urllib import request


def fill_template(username, jobtitle):
    str = f"Hello {username}, as the {jobtitle} of you company, I reach out to you with an urgent request." \
          f"I attached a file of the sales agreement and I need you to sign it ASAP and send it back to me," \
          f"thank you"

    return str


def main():
    username = sys.argv[1]
    mail_server = sys.argv[2]
    job_title = sys.argv[3]

    mail_body = ""
    if len(sys.argv) == 5:
        if 'www' in sys.argv[4]:  # url
            try:
                with urllib.request.urlopen(sys.argv[4]) as f:
                    mail_body = f.read().decode('utf-8')
            except:
                print("failed to read from 4th argument - url")

        elif '.txt' in sys.argv[4]:  # file
            try:
                with open(sys.argv[4], 'r') as file:
                    mail_body = file.read().replace('\n', '')
            except:
                print("failed to read from 4th argument")

        else:  # string
            mail_body = sys.argv[4]

    else:
        mail_body = fill_template(username, job_title)

    message = MIMEMultipart("alternative")
    message["Subject"] = "Urgent Request"
    message["From"] = "managment@arielu.ac.il"
    message["To"] = username + "@" + mail_server
    message.attach(MIMEText(mail_body, "plain"))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("attachment.py", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="attachment.py"')
    message.attach(part)

    hlp = message["To"]
    with smtplib.SMTP('localhost') as s:
        s.send_message(message)
        print(f"done. sent to {hlp}")


main()
