from urllib.request import urlopen

with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8') # バイナリデータをテキストにデコード
        if 'EST' in line or 'EDT' in line: # 東部標準時を探す
            print(line)
