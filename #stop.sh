#stop.sh
stop=$(sudo ps aux | grep "flask run" | grep -v grep | cut -d " " -f7)
for i in $stop;do
kill -9 $i
echo "mesti svershilas - klient ubit"
done
