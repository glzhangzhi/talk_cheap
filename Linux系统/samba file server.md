# install

sudo apt-get install samba
apt-get install smbfs //?

# add user

sudo useradd sambauser
sudo passwd sambauser
sudo mkdir /home/sambauser
sudo chown -R sambauser:sambauser /home/sambauser

# add this user to samba server and its password

sudo smbpasswd -a sambauser

# make publick direction

mkdir /home/sambauser/sambashare
chown -R sambauser:sambauser /home/sambauser/sambashare
chmod 777 /home/sambauser/sambashare

# configurate smb.conf

cd /etc/samba
mv smb.conf
vim smb.conf

[global]
security=user // security level, user means need username and password, share mean don't need password
[sambashare] // share name
path=/home/sambauser/sambashare //which folder you want to share
valid users=sambauser //only user1 can enter this folder
public=no //only user1 can see this folder in samba service
writable=yes

# restart samba service

sudo /etc/init.d/smbd restart

# visit share folder on windows

\\192.168.xx.xxx\sambashare

# visit share folder on linux

on other location of file browers, in the bottom of window
smb://192.168.xx.xxx/sambashare

# visit share folder on IPad

on file app, click ... and connect to server
smb://192.168.xx.xxx/sambashare