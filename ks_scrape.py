from urllib.request import Request, urlopen
from re import split, match

def process_data(data):
    ks_data = {}
    for line in data:
        name_regex = match('<meta property="twitter:title" content="(.+)"/>', line)
        if name_regex != None:
            ks_data['name'] = name_regex.group(1)
            continue
            
        desc_regex = match('<meta property="twitter:description" content="(.+)"/>', line)
        if desc_regex != None:
            ks_data['desc'] = desc_regex.group(1)
            continue
            
        pledge_regex = match('.+data-goal="(.+?)" data-percent-raised="(.+?)" data-pledged="(.+?)".+>', line)
        if pledge_regex != None:
            ks_data['goal'] = process_currency(pledge_regex.group(1))
            ks_data['percent'] = process_percent(pledge_regex.group(2))
            ks_data['pledged'] = process_currency(pledge_regex.group(3))
            continue
            
        pledge_regex = match('pledged of <span class="money">(.+)</span> goal', line)
        if pledge_regex != None:
            ks_data['goal'] = pledge_regex.group(1)
            continue
            
        pledge_regex = match('<b>(.+) backers</b> pledged <span class="money">(.+)</span>.+', line)
        if pledge_regex != None:
            ks_data['backer_count'] = pledge_regex.group(1)
            ks_data['pledged'] = pledge_regex.group(2)
            
        update_regex = match('<span class="count">(\d+)</span>', line)
        if update_regex != None:
            ks_data['update_count'] = update_regex.group(1)
            continue
            
        backers_regex = match('.+data-backers-count="(\d+)".+>', line)
        if backers_regex != None:
            ks_data['backer_count'] = backers_regex.group(1)
            continue
            
        time_regex = match('.+data-hours-remaining="(\d+)".+>', line)
        if time_regex != None:
            ks_data['time_remaining'] = process_time(time_regex.group(1))
            continue
            
    return ks_data
    
def process_currency(amount):
    reg1 = match('(\d+)\.(\d+)', amount)
    dollars = reg1.group(1)
    cents = reg1.group(2)
    if cents == '0':
        cents = '00'
    if len(dollars) > 6:
        dollars = dollars[:-6] + ',' + dollars[-6:][:3] + ',' + dollars[-3:]
    elif len(dollars) > 3:
        dollars = dollars[:-3] + ',' + dollars[-3:]
    return '$' + dollars + '.' + cents

def process_percent(percent):
    reg1 = match('(\d+)\.(\d+)', percent)
    if reg1.group(1) == '0':
        pre_dec = reg1.group(2)[:2]
    else:
        pre_dec = reg1.group(1) + reg1.group(2)[:2]
    post_dec = reg1.group(2)[2:][:2]
    return pre_dec + '.' + post_dec + '%'
    
def process_time(time):
    time = int(time)
    if time > 24:
        return str(time // 24) + 'd' + str(time % 24) + 'h'
    return str(time) + 'h'
    
if __name__ == '__main__':
    address = 'https://www.kickstarter.com/projects/1986219362/dies-irae-english-localization-project-commences'
    # address = 'https://www.kickstarter.com/projects/tokyootakumode/re-sharin-no-kuni-project'
    # address = 'https://www.kickstarter.com/projects/muvluv/muv-luv-a-pretty-sweet-visual-novel-series'
    agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    
    req = Request(address, headers={'User-Agent': agent})
    input = urlopen(req)
    data = input.read()
    output = open('data2.txt', 'w', encoding='utf-8')
    output.write(data.decode())
    output.close()
    data = split('\n', data.decode())
    # input = open('data.txt', 'r', encoding='utf-8')
    # data = input
    
    ks_data = process_data(data)
    
    input.close()
    
    for key in ks_data.keys():
        print(key + ": " + ks_data[key])