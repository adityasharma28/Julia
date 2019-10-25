#import the required libraries
import requests
from bs4 import BeautifulSoup
import smtplib
#paste the link of a product
url='https://www.amazon.in/Fusefit-Tramp-Running-Shoes-7-FFR-133/dp/B07HKTMSFD/ref=sr_1_1_sspa?pf_rd_i=14311960031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=39e2276e-8ffc-4696-befc-3367bd57201c&pf_rd_r=9XPYSPQG557X8RTBXRP6&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1571657960&refinements=p_6%3AA14FG3FHN6HO9H%7CA173W2C6ZVF30Z%7CA24C076CQPFHLF%7CA2L90Y54FJK6W9%7CA2QX6NNXDXIFAE%7CA2S3NERJZR3X4J%7CA368O17UO4G1I%7CA3HWX32UOZXKKE%7CA3OZBP9WERCHBG%7CAI52EU9WFYI4L%7CAT95IG9ONZD7S%2Cp_36%3A-49900&s=shoes&smid=AT95IG9ONZD7S&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyOUJJRDZCNkM4UEhXJmVuY3J5cHRlZElkPUEwNzI5ODUzMzJLMDRCUjlBRUtVTSZlbmNyeXB0ZWRBZElkPUEwODY3MDM5M0pEU1hWSkRQRFBWSCZ3aWRnZXROYW1lPXNwX2F0Zl9icm93c2UmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
#install gecko drivers
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

#initialize the variables
page=requests.get(url,headers=headers)
soup=BeautifulSoup(page.content,'html.parser')
#for getting the name of product
title=soup.find(id="productTitle").text()
#for getting price of product
price=soup.find(id="priceblock_ourprice").text()
pc=(price[0:10])
print(pc)
n=''
for i in pc:
    if i==".":
        break
    if i in ['0','1','2','3','4','5','6','7','8','9']:
        n=n+i
pc=int(n)
#for sending email
if pc<200:
    send_email()
def send_email():
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('aditya28071999@gmail.com','imcadeejdrsvufmy')
    subject="Price fell down"
    body=" check price"
    msg=f"Subject: {subject}\n\n{body}"
    server.sendmail("aditya28071999@gmail.com","pandit28071999@gmail.com",msg)
    print("email sent")
    server.quit()

    
print(title.strip())

