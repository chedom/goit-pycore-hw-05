from collections import namedtuple
from typing import Iterable,Counter

# Log tuple represents parsed log line
Log = namedtuple('Log', ['date', 'time', 'level', 'message'])

def parse_log_line(line: str) -> Log:
    date, time, level, msg = line.strip().split(' ', 3)
    return Log(date, time, level, msg)


def load_logs(file_path: str) -> list[Log]:
    logs = list[Log]()

    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            logs.append(parse_log_line(line.strip()))

    return logs
 
# def load_logs(file_path: str) -> Iterable[Log]:
#     with open(file_path, 'r', encoding="utf-8") as file:
#         for line in file:
#             yield parse_log_line(line.strip())

def filter_logs_by_level(logs: Iterable[Log], level: str) -> Iterable[Log]:
    # or return [log for log in logs if log.level == level]
    return filter(lambda log: log.level == level, logs)

# Notes: used `Iterable[tuple[str, int]]` instead of proposed `dict` because it preserves the
# order from the most common to the least
def count_logs_by_level(logs:  Iterable[Log]) -> Iterable[tuple[str, int]]:
    log_counter = Counter(log.level for log in logs)
    return log_counter.most_common()

def display_log_counts(counts: Iterable[tuple[str, int]]):
    # print header
    print('Рівень логування | Кількість')
    print('-----------------|----------')
    # print level statistics
    for stat in counts:
        # align the columns according to the headers len
        print(f'{stat[0]:<17}| {stat[1]:<8}')

def display_log(logs: list[Log], level: str):
    print(f"Деталі логів для рівня '{level.upper()}':") # print header

    for log in logs: # print logs
        print(f'{log.date} {log.time} - {log.message}')