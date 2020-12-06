from requests_html import HTMLSession

s = HTMLSession()

url = "https://www.hanjutv2020.com/hanju/7803.html"
h = s.get(url)

ul = h.html.find(".juji-list")[0]

def get_video_url(detail_url):
    detail_content = s.get(detail_url)
    video_url = detail_content.html.find("#playPath")[0].attrs['src']
    video_url = "https:" + video_url
    return video_url


for link in ul.find("a"):
    detail_url = 'https://www.hanjutv2020.com' + link.attrs['href']
    video_url = get_video_url(detail_url)
    print(detail_url, video_url)

