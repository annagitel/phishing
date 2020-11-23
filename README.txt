import getpass
from requests import get
from scapy.layers.dns import DNS, DNSQR, IP
from scapy.layers.inet import UDP
from scapy.sendrecv import send
import sys
import smtplib
import urllib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from urllib import request