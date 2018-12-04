import InputHelper as iH
import time
import datetime
import collections

iH = iH.InputHelper("4")
lines = iH.lines

nlines = []
for line in lines:
    lline = list(line)
    lline[1] = "2"
    lline[2] = "0"
    nlines.append("".join(lline))

d = {}

for line in nlines:
    date = line[1:17]
    times = int(time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d %H:%M").timetuple()))
    text = line[18:]
    d[times] = text

od = collections.OrderedDict(sorted(d.items()))

g = {}
l = {}
currentg = -1
last_ts = 1520635560
last_state = False

for key in od:
    if 'Guard' in od[key]:
        splits = od[key].split(" ")
        guard = int(splits[2][1:])
        if guard in g:
            pass
        else:
            g[guard] = {'sleeptime': 0, 'ms': {}}

        if guard in l:
            pass
        else:
            l[guard] = [0, 0]

        if currentg != -1:
            if not last_state:
                value = (key - last_ts) / 60
                g[currentg]['sleeptime'] += value

                for m in range(datetime.datetime.fromtimestamp(last_ts).minute,
                               datetime.datetime.fromtimestamp(key).minute):
                    if m not in g[currentg]['ms']:
                        g[currentg]['ms'][m] = 1
                    else:
                        g[currentg]['ms'][m] += 1

                if l[currentg][1] < value:
                    l[currentg][0] = datetime.datetime.fromtimestamp(key).minute
                    l[currentg][1] = value

        currentg = guard
        last_state = True
        last_ts = key

    if 'asleep' in od[key]:
        last_state = False
        last_ts = key

    if 'up' in od[key]:
        value = (key - last_ts) / 60
        g[currentg]['sleeptime'] += value
        for m in range(datetime.datetime.fromtimestamp(last_ts).minute,
                       datetime.datetime.fromtimestamp(key).minute):
            if m not in g[currentg]['ms']:
                g[currentg]['ms'][m] = 1
            else:
                g[currentg]['ms'][m] += 1

        if l[currentg][1] < value:
            l[currentg][0] = datetime.datetime.fromtimestamp(key).minute
            l[currentg][1] = value
        last_state = True
        last_ts = key

lastmax = 0
for key in g:
    if g[key]['sleeptime'] > lastmax:
        maxkey = key
        lastmax = g[key]['sleeptime']

print(maxkey, lastmax)

lastminmaxv = 0

for key in g[maxkey]['ms']:
    if g[maxkey]['ms'][key] > lastminmaxv:
        maxminkey = key
        lastminmaxv = g[maxkey]['ms'][key]

print("result = " + str(maxkey * maxminkey))

cg = 0
maxfminute = 0
max_f = 0
for key in g:
    for key2 in g[key]['ms']:
        if g[key]['ms'][key2] > max_f:
            max_f = g[key]['ms'][key2]
            maxfminute = key2
            cg = key

print(cg, maxfminute)
print(cg * maxfminute)
