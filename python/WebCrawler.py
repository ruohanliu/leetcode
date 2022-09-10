from concurrent.futures import ThreadPoolExecutor
import asyncio

class Solution:
    async def process_url(self, url: str) -> None:
        self.seen.add(url)
        urls = set(u for u in await self.parse_url_async(url) if u.startswith(self.hostname))
        not_visited = urls - self.seen
        await asyncio.gather(*(self.process_url(u) for u in not_visited))

    async def parse_url_async(self, url):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(self.executor, self.htmlParser.getUrls, url)
        
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        self.seen = set()
        self.hostname = '/'.join(startUrl.split('/', 3)[:3])
        self.htmlParser = htmlParser

        with ThreadPoolExecutor(max_workers=64) as self.executor:
            asyncio.run(self.process_url(startUrl))

        return self.seen