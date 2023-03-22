nmap 10.10.10.4/24              #finds live hosts on the network

# find a host of interest.
# substitute in the live host number under ###
nmap -A  10.10.10.###           # scans the top 1000 ports on the network

# TCP
#     20: ftp data
#     21: ftp control
#     22: ssh
#     23: telnet
#     25: SMTP (mail)
#     37: Time protocol
#     53: Bind/DNS
#     69: TFTP (Trivial FTP)
#     80: HTTP
#     109: POP2
#     110: POP3
#     111: RPC Remote Procedure Call
#     137: Netbios Name Service
#     138: Netbios Datagram Service
#     139: Netbios Session Service
#     143: IMAP (mail)
#     161: SNMP
#     220: IMAP
#     389: LDAP
#     443: HTTPS
#     445: MS Active Directory, SMB
#     464: Kerberos
#     1521: Oracle Database
#     3000: Node JS
#     3306: MySQL
# UDP
#     69: TFTP
#     161: SNMP



# feroxbuster install
curl -sL https://raw.githubusercontent.com/epi052/feroxbuster/master/install-nix.sh | bash

# dirb install
sudo apt-get install -y dirb # installs dir buster

# again, insert the host of interest as ###
dirb http://10.10.10.###         #scans the file structure of the server hosted on that port
