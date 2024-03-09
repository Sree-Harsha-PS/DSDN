import smtplib

def sendMail(code):
    try:
        YOUR_GOOGLE_EMAIL = 'ashwintest03@gmail.com'
        YOUR_GOOGLE_EMAIL_APP_PASSWORD = 'iwyv wdwi zcmr ljxu'  
        smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtpserver.ehlo()
        smtpserver.login(YOUR_GOOGLE_EMAIL, YOUR_GOOGLE_EMAIL_APP_PASSWORD)
        sent_from = YOUR_GOOGLE_EMAIL
        sent_to = 'balajiagmohan@gmail.com'  
        email_text = "The OPT is\n"+str(code)
        smtpserver.sendmail(sent_from, sent_to, email_text)
        smtpserver.close()
        return "successful"
    except:
        return "failed"