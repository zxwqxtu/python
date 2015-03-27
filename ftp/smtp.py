import smtplib

def prompt(prompt):
    return raw_input(prompt).strip()

fromaddr = prompt("From: ")
toaddrs  = prompt("To: ").split()
print "Enter message, end with ^D (Unix) or ^Z (Windows):"

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
'''
while 1:
    try:
        line = raw_input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line
'''
msg += raw_input()

print "Message length is " + repr(len(msg))

server = smtplib.SMTP('smtp.qq.com', 465)
server.set_debuglevel(1)
server.login('960875184@qq.com', 'wang960875184')
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
