from threading import Thread,Lock
from concurrent.futures import ThreadPoolExecuter
from collectiosn import deque
class Solution:
    def __init__(self):
        self.visited = set()
        self.lock = Lock()
        self.hostname = None
        self.queue = deque()
    def getHostname(self,url):
        return  ".".join(url.split("/")[2].split(".")[1:])
    def download(self,url,htmlParser):
        waitlist = htmlParser.getUrls(url)
        for url in waitlist:
            with self.lock:
                if self.getHostname(url) == self.hostname and url not in self.visited:
                    self.visited.add(url)
                    self.queue.append(url)
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        self.queue.append(startUrl)
        self.hostname = self.getHostname(startUrl)
        self.visited.add(startUrl)

        while self.queue:
            url = self.queue.popleft()
            threads = []
            threads.append(Thread(target = self.download,args = (url,htmlParser)))

            while self.queue:
                url = self.queue.popleft()
                threads.append(Thread(target = self.download,args = (url,htmlParser)))
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()

        return list(self.visited)

class Solution:
    def __init__(self):
        self.visited = set()
        self.lock = Lock()
        self.hostname = None
        self.queue = deque()
    def getHostname(self,url):
        return  ".".join(url.split("/")[2].split(".")[1:])
    def download(self,url,htmlParser):
        waitlist = htmlParser.getUrls(url)
        for url in waitlist:
            with self.lock:
                if self.getHostname(url) == self.hostname and url not in self.visited:
                    self.visited.add(url)
                    self.queue.append(url)
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        self.queue.append(startUrl)
        self.hostname = self.getHostname(startUrl)
        self.visited.add(startUrl)

        with ThreadPoolExecuter(max_worker = 16) as executer:
            while self.queue:
                url = self.queue.popleft()
                executer.submit(htmlParser,url)
        return list(self.visited)