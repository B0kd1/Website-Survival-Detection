#!/bin/python3
from threading import Thread
from queue import Queue
import requests
import sys

print(
'''\033[1;91m
$$$$$$$\   $$$$$$\  $$\             $$\   $$\          $$$$$$\   $$$$$$\             $$$$$$\  
$$  __$$\ $$$ __$$\ $$ |            $$ |$$$$ |        $$ ___$$\ $$  __$$\           $$  __$$\ 
$$ |  $$ |$$$$\ $$ |$$ |  $$\  $$$$$$$ |\_$$ |        \_/   $$ |$$ /  $$ |$$$$$$$\  $$ /  \__|
$$$$$$$\ |$$\$$\$$ |$$ | $$  |$$  __$$ |  $$ |          $$$$$ / $$$$$$$$ |$$  __$$\ $$ |$$$$\ 
$$  __$$\ $$ \$$$$ |$$$$$$  / $$ /  $$ |  $$ |          \___$$\ $$  __$$ |$$ |  $$ |$$ |\_$$ |
$$ |  $$ |$$ |\$$$ |$$  _$$<  $$ |  $$ |  $$ |        $$\   $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |
$$$$$$$  |\$$$$$$  /$$ | \$$\ \$$$$$$$ |$$$$$$\       \$$$$$$  |$$ |  $$ |$$ |  $$ |\$$$$$$  |
\_______/  \______/ \__|  \__| \_______|\______|$$$$$$\\______/ \__|  \__|\__|  \__| \______/ 
                                                \______|                                      
 \033[0m
 \033[1;34m Website Survival Detection v1.0\033[0m
 '''
 )

print("\033[1:32m")

if len(sys.argv) < 3 :
    print( 'Use: python3 B0kd1_Survive.py /tmp/urls.txt 1-200(This is threads)' )
    sys.exit()
def end():
    print("\t\033[1;91m[!] Bye bye !")
    time.sleep(0.5)
    sys.exit(1)
urls = sys.argv[1]
threads = int(sys.argv[2])


class UrlCheck(Thread):
    def __init__(self, url_queue, url_list):
        super().__init__()
        self.url_queue = url_queue  # UrlS
        self.url_list = url_list  # IPv4
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) '
                          'AppleWebKit/605.1.15 (KHTML, like Gecko) '
                          'Version/13.0.3 Mobile/15E148 Safari/604.1'
        }

    def run(self):
        while True:
            try:
                url = self.url_queue.get()
                if 'http' in url:
                    head = self.download(url)
                    if head is None:
                        continue
                    self.url_list.append(url)
                    print(url, head)
                else:
                    http_url = 'http://' + url
                    head = self.download(http_url)
                    if head:
                        self.url_list.append(http_url)
                        print(http_url, head)
                    https_url = 'https://' + url
                    head = self.download(https_url)
                    if head is None:
                        continue
                    self.url_list.append(https_url)
                    print(https_url, head)
            finally:
                self.url_queue.task_done()

    def download(self, url):
        try:
            head = requests.get(url, headers=self.headers, timeout=3)
        except requests.RequestException:
            head = None
        return head



if __name__ == '__main__':
    u_queue = Queue()
    checker = [k.strip() for k in open( urls, encoding='utf-8')]
    url_list = []
    save_name = "results.txt"  # results
    for url in checker:
        u_queue.put(url)
    #for i in range(50):
    for i in range(threads):
        bdm = UrlCheck(u_queue, url_list)
        bdm.daemon = True
        bdm.start()

    u_queue.join()

    f = open(save_name, mode='w', encoding='utf-8')
    for url in url_list:
        f.write(url+'\n')
    f.close()

    count = len(open(r"results.txt",'rb').readlines())
    print('[*] Detection is complete! The number of input lines is >>' + str(count))