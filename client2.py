from ftplib import FTP

ftp = FTP('')
ftp.connect('localhost',1026)
ftp.login()
ftp.cwd('') #replace with your directory
ftp.retrlines('LIST')

def uploadFile():
 filename = 'test.txt' #replace with your file in your home folder
 ftp.storbinary('STOR '+filename, open(filename, 'rb'))
 ftp.quit()

def downloadFile():
 filename = 'testfile.txt' #replace with your file in the directory ('directory_name')
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

uploadFile()