FILEPCAP=ja4a4a4do0o0re-ssh.pcap

# `tcpdump -r ja4a4a4do0o0re-ssh.pcap -nn -q | awk '{print $3}'|cut -d \. -f 1,2,3,4 |sort|uniq`
for ip in `tcpdump -r ja4a4a4do0o0re-ssh.pcap -nn -q | awk '{print $3}'|cut -d \. -f 1,2,3,4 |sort|uniq`
do
    echo $ip
    tshark  -r ${FILEPCAP} -d tcp.port==2222,ssh -Y "ip.addr ==  ${ip} && ssh" -V > parsedbyshark${ip}.txt
done
