from datetime import datetime, timedelta
from collections import Counter

with open('inp.txt') as f:
    raw_data = f.readlines()

data = []
guards_log = {}
for d in raw_data:
    raw_date, command = d.split('] ')
    date = datetime.strptime(raw_date.strip('[ '), '%Y-%m-%d %H:%M')
    if 'Guard' in command:
        command = int(command.split()[1][1:])
        if command not in guards_log:
            guards_log[command] = [0 for _ in range(60)]
    else:
        command = command.strip()
    data.append((date, command))

data.sort()

minute = timedelta(minutes=1)
current_guard = None
falls_at = None
best = None, 0, 0

most_asleep = Counter()

for time_, command in data:
    if isinstance(command, int):
        current_guard = command
    elif command == 'falls asleep':
        assert falls_at is None
        falls_at = time_
    elif command == 'wakes up':
        while falls_at != time_:
            if falls_at.hour == 0:
                guards_log[current_guard][falls_at.minute] += 1
                if guards_log[current_guard][falls_at.minute] > best[2]:
                    best = (
                        current_guard, falls_at.minute,
                        guards_log[current_guard][falls_at.minute])
                most_asleep[current_guard] += 1
            falls_at = falls_at + minute
        falls_at = None

most_asleep_guard = most_asleep.most_common(1)[0][0]
most_asleep_minute = guards_log[most_asleep_guard].index(
    max(guards_log[most_asleep_guard]))
print('Part 1:', (most_asleep_guard, most_asleep_minute), (
    most_asleep_guard * most_asleep_minute))
print('Part 2:', best[:2], best[0] * best[1])
