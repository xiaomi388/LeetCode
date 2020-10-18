# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        seen = set()
        ori_host = startUrl.split("/")[2]
        def dfs(url):
            if url in seen: return
            seen.add(url)
            for nbr in htmlParser.getUrls(url):
                host = nbr.split("/")[2]
                if host != ori_host: continue
                dfs(nbr)
        dfs(startUrl)
        return list(seen)
