import os

def get_nmap(options, ip):
    command = "nmap " + options + " " + ip
    process = os.popen(command)
    results  = str(process.read())
    return results
ip = input('Enter the ip address for scan: ')

print(get_nmap('-Pn', ip))