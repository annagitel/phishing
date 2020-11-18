# Anna Sandler 208749648
import sys
import smtplib
import urllib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_mail(server, my_email, user_email, job_title, message):
    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = user_email
    msg['Subject'] = f"Dear {job_title}"
    msg.attach(MIMEText(message, 'plain'))
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("attachment.py", "rb").read())
    encoders.encode_base64(part)

    part.add_header('Content-Disposition', 'attachment; filename="attachment.py"')
    msg.attach(part)

    try:
        server.sendmail(my_email, user_email, msg.as_string())
    except:
        print('failed')


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
    if len(sys.argv) == 4:
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

    user_email = username + "@" + mail_server

    my_email = 'mymail@gmail.com'
    password = 'Aa123456'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.ehlo()
    server.login(my_email, password)
    send_mail(server, my_email, user_email, job_title, mail_body)
    server.quit()


main()
