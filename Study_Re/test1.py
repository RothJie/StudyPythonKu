import re

html = """<script type="text/javascript" src="https://assets.msn.cn/bundles/v1/edgeChromium/latest/experience.80ecb7588d9cda3b33a1.js">这是一个js</script>
<script type="text/javascript" src="https://assets.msn.cn/bundles/v1/edgehChromium/latest/experience.80ecb7588d9cda3b33a1.js">这是js</script>
<script type="text/jaghjvascript" src="https://assets.msn.cn/bundles/v1/edgeChromium/latest/experience.80ecb7588d9cda3b33a1.js">是一个js</script>
<script type="text/jyuioavascript" src="https://assets.msn.cn/bundles/v1/edgeChromopium/latest/experience.80ecb7588d9cda3b33a1.js">这一个js</script>"""

pattern = r'https.+?js'  # 匹配src
# pattern = r'src="([^"]+)"'
# pattern = r'src="(.*?)"'

# pattern = r'type="([^"]+)"'  # 匹配type
# pattern = r'type="([^<]+?)"'

# pattern = r'js">(.*?)js</script>'  # 匹配文本

matches = re.findall(pattern, html)
for match in matches:
    print(match)

