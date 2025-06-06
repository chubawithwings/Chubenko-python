# В исходном текстовом файле(radio stations.txt) найти все домены из URL-адресов
# (например, в URL-apece http://stream.hoster.by:8081/pilotfm/audio/icecast.audio
# домен выделен полужирным).

import re

with open('PZ_14\\radio_stations.txt', 'r', encoding='utf-8') as f1:
    allfile = f1.read()

res = re.findall(r'[a-z0-9]\w+\.[a-z0-9]\w+\.[a-z0-9]\w+', allfile)
for i in res:
    print(i)