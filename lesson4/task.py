import requests


class TvManager(object):
    def __init__(self):
        self._url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=20&page_start=0"
        self._headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        }
        self.tvs = []

    def load(self):
        data = requests.get(self._url, headers=self._headers).json()
        self.tvs = data["subjects"]

    def show(self):
        for tv in self.tvs:
            print("%s\t%s\t%s" % (tv["id"], tv["title"], tv["url"]))

    def find(self, title):
        # for tv in self.tvs:
        #     if tv["title"] == title:
        #         return tv
        # return None
        li = [tv for tv in self.tvs if tv["title"] == title]
        if len(li) == 0:
            return None
        else:
            return li[0]

    def remove(self, title):
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # newlist = [expression for item in iterable if condition == True]
        self.tvs = [tv for tv in self.tvs if tv["title"] != title]

    def search(self, subtitle):
        # 子字符串，也可以搜索
        pass


manager = TvManager()
# manager.load()
# # manager.show()
# tv = manager.find("有翡")
# print(tv)
# print(manager.tvs[0]['title'])
# manager.remove("有翡")
# print(manager.tvs[0]['title'])

while True:
    data = input(">>> ")
    comps = data.split()
    cmd = comps[0]
    if cmd == "load":
        manager.load()
        print("load success")
    elif cmd == "show":
        manager.show()
    elif cmd == "find":
        assert len(comps) == 2
        tv = manager.find(comps[1])
        if tv is None:
            print("found nothing!")
        else:
            print("found: %s\t%s\t%s" % (tv["id"], tv["title"], tv["url"]))
    elif cmd == "remove":
        assert len(comps) == 2
        manager.remove(comps[1])
    else:
        print("not supported cmd")
