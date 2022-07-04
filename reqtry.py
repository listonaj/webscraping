import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
if res.status_code == requests.codes.ok:
    print(res.text[1350:5000])
else:
    res.raise_for_status()

playfile = open('RomeoAndJuliet.txt','wb')
for chunk in res.iter_content(10000):
    playfile.write(chunk)
playfile.close()