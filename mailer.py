import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

fromaddr =  #From Address
toaddr =  #To Address
password = #Password
subject = "AWS Cost Sheet for last month"
body = "AWS Cost for services utilized in last month"
msg=MIMEMultipart()
msg['From']=fromaddr
msg['To']=",".join(toaddr)
msg['Subject']=subject
msg.attach(MIMEText(body,'plain'))
filename="cost_sheet.csv"
attachment=open(filename,'rb')
part=MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)
msg.attach(part)
text=msg.as_string()
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(fromaddr,password)
server.sendmail(fromaddr,toaddr,text)
server.quit()
