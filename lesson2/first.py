import requests

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'

header = {
    "Cookie": 'll="108288"; bid=_JBkZOW_i-o; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1607259083%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.872384656.1607259083.1607259083.1607259083.1; __utmb=30149280.0.10.1607259083; __utmc=30149280; __utmz=30149280.1607259083.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.2116037204.1607259083.1607259083.1607259083.1; __utmb=223695111.0.10.1607259083; __utmc=223695111; __utmz=223695111.1607259083.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=D02539B8E389FC16E903CB938BBC592F7|a97e50238ab4953461f8bbf895f8f27a; __yadk_uid=89pPe9GL6uaWuKKB6vjgcX5LWpfHxUwd; _pk_id.100001.4cf6=f44053bca324ac6b.1607259083.1.1607259844.1607259083.',
    "Host": 'movie.douban.com',
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
a = requests.get(url, headers=header).json()

for item in a['subjects']:
    print(item['title'], item['url'])