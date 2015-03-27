import ftplib

ftp = ftplib.FTP('ftp.debian.org')
ftp.login()
ftp.cwd('debian')
#ftp.retrlines('LIST')
#ftp.dir()
ftp.retrbinary('RETR README', open('/home/zxwqxtu/xp/xxxx', 'wb').write)
ftp.retrlines('RETR README', open('/home/zxwqxtu/xp/xxx', 'wb').write)
list = ftp.nlst()
print list
ftp.quit()

