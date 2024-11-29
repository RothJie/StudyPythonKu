import requests
import re

url = 'https://movie.douban.com/chart'


headers = {
    "cookie":"__cf_bm=swzEu4Kyic2EKZEunOngSEH3D.3lncO_C3C600._lsI-1732881019-1.0.1.1-90n7eQIJ9zG.F7GW8Hm6N2po8RsViAKBfR_ZOkNTIO4UMkrgdNL0PsU6GSdDbRqMjKH7Li..I6cK8gfW8jOcFQ; path=/; expires=Fri, 29-Nov-24 12:20:19 GMT; domain=.pexels.com; HttpOnly; Secure; SameSite=None",
    "user-agent":"https://www.pexels.com/zh-cn/videos/"
}

resp_ = requests.get(url,headers=headers)

html = resp_.text

# print(html)
pattern = r'<a class="nbg" href="(.*?)"  title="([^"]+)">'
matches = re.findall(pattern, html)
for link,k in matches:
    print(link,k)
