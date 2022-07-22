import os

def get_whois(url):
    command = "C:\WhoIs\.\whois.exe " + url
    process = os.popen(command)
    results = str(process.read())
    return results
url= input('Enter url: ')
 
print(get_whois(url))

