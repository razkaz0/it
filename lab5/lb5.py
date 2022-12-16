import os
import re
import statistics
import gzip
import io


default_logs_path = './logs'


def main():
    relative_logs_path = input(f'Path to logs DIR [{default_logs_path}]: ')
    if (relative_logs_path == ''):
        relative_logs_path = default_logs_path
    log_name = sorted(os.listdir(relative_logs_path))[-1]
    print(log_name)
    log_path = f'{relative_logs_path}/{log_name}'
    if os.path.splitext(log_path) == '.gz':
        with gzip.open(log_path, 'r') as arch:
            with io.TextIOWrapper(arch, encoding='utf-8') as file:
                logs = read_logs(file)
                print_logs(logs)

    with open(log_path, 'r') as file:
        logs = read_logs(file)
        print_logs(logs)


def read_logs(file):
    output = {}
    total_count = 0
    pattern = re.compile(r'\"[A-Z]+ (\S+) .* (\d+\.\d+)\n')
    for line in file:
        result = pattern.findall(line)
        if not len(result):
            continue
        total_count += 1
        url, time = result[0]
        if not url in output:
            output[url] = []
        output[url].append(float(time))
    return [output, total_count]


def print_logs(logs):
    [logs, total_count] = logs
    for url in logs:
        count = len(logs[url])
        print([url, count, (count * 100 / total_count),
                           sum(logs[url]) / count, statistics.median(logs[url]), max(logs[url])])
    print('Total Logs Count: ', total_count)


if __name__ == '__main__':
    main()