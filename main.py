from email.message import EmailMessage
import smtplib, ssl
import argparse
import os
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Get the asyncio logger
log = logging.getLogger("asyncio")
log.setLevel(logging.INFO)

def parse_args():
    parser = argparse.ArgumentParser(description='Parse target email')
    parser.add_argument('--email', required=True, help='Recipient email')
    parser.add_argument('--wait', required=True, help='iteration to wait')
    return parser.parse_args()


def sendEmail(email):
    full_message = f'message received from docker sample'

    msg = EmailMessage()
    msg.set_content(full_message)
    msg["Subject"] = f'Docker Message Recieved'
    msg["From"] = 'e67067069@gmail.com'
    msg["To"] = email
    context = ssl.create_default_context()
    log.info(f'target email: {email}')

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as smtp:
        smtp.login('e67067069@gmail.com', 'xnkosujpzzrmmdie')
        smtp.send_message(msg)

    log.info('Email sent')

    return 'email sent'

def wait(seconds):
    for i in range(seconds):
        print(f"Message {i + 1}: printed at {time.strftime('%X')}")
        time.sleep(5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = parse_args()
    print('test env', os.environ.get('ENV_TEST'))
    sendEmail(args.email)
    wait(int(args.wait))

