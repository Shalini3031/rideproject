import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('shalinijoshi226@gmail.com', 'ixetzdavoszzkawx')
server.sendmail('shalinijoshi226@gmail.com', 'joshishalini734@gmail.com', 'Test email')
server.quit()
