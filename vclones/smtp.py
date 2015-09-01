__author__ = 'gabriel'

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email_notifications(vms, host, datacenter, cluster, rcpt_from, rcpt_to, smtp_host):
    msg = MIMEMultipart()
    msg['Subject'] = 'Clone report on {0} [dc:{1},cl:{2}'.format(host, datacenter, cluster)
    msg['From'] = rcpt_from
    msg['To'] = rcpt_to

    msgbody = """\
<h2 style="text-align: center;">Cluster informations</h2>
<ul>
    <li><strong>Host          : </strong>""" + host + """</i></li>
    <li><strong>Datacenter    : </strong>""" + datacenter + """</i></li>
    <li><strong>Cluster       : </strong>""" + cluster + """</i></li>
</ul>
<h2 style="text-align: center;">VM Info</h2>
<ul>
    <li><strong>Total VMs: """ + len(vms).__str__() + """</strong>
</ul>
"""
    msg.attach(MIMEText(msgbody, 'html'))

    s = smtplib.SMTP(smtp_host)
    s.sendmail(msg['From'], rcpt_to.split(', '), msg.as_string())
    s.quit()