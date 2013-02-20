import socket
def retBanner(ip, port):
   try:
      socket.setdefaulttimeout(2)
      s = socket.socket()
      s.connect((ip, port))
      banner = s.recv(1024)
      return banner
   except:
      return

def checkVulns(banner)
   f = open('vuln_banners.txt', 'r')
   for line in f.readlines():
      if line.strip('\n') in banner:
         print '[+] Server is vulnerable: '+banner.strip('\n')

def main():
   portlist = [21,22,25,80,110]
   for x in range(1, 255):
      for port in portlist:
         banner = retBanner('192.168.1.'+str(x), port)
         print '[+] Checking 192.168.1.' + str(x) + ' Port ' + str(port)
         if banner:
            print '[+] 192.168.1.' + str(x) + ': ' + banner      

if __name__ == '__main__':
   main()
