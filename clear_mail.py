#!/usr/bin/env python
#temp pochtasidagi hatlarni har kunu ikki mahal o'chirish
#to'g'risi brauzerdan kirib o'chirgani erinaman !!!! 
import poplib
 
username = 'info'
password = 'password'
 
mail_server = 'mailserver'
 
p = poplib.POP3(mail_server)
p.user(username)
p.pass_(password)
for msg_id in  p.list()[1]:
    #print msg_id
    outf = open('%s.eml' % msg_id, 'w')
    outf.write('n'.join(p.dele(msg_id)[1]))
    #outf.write('n'.join(p.retr(msg_id)[1]))
    outf.close()
p.quit()
