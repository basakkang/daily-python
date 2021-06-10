import timeit

def print_results(count, tests):
    avg_iteration = sum(tests) / len(tests)
    print(f'\n원소 수: {count:>5,} 걸린시간: {avg_iteration:.6f}초')
    return count, avg_iteration

def print_delta(before, after):
    before_count, before_time = before
    after_count, after_time = after
    growth = 1 + (after_count - before_count) / before_count
    slowdown = 1 + (after_time - before_time) / before_time
    print(f'데이터 크기 {growth:>4.1f}배, 걸린 시간 {slowdown:>4.1f}배')

import collections

def deque_append_benchmark(count):
    def prepare():
        return collections.deque()

    def run(queue):
        for i in range(count):
            queue.append(i)

    tests = timeit.repeat(
        setup='queue = prepare()',
        stmt='run(queue)',
        globals=locals(),
        repeat=1000,
        number=1)
    return print_results(count, tests)

baseline = deque_append_benchmark(500)
for count in (1_000, 2_000, 3_000, 4_000, 5_000):
    comparison = deque_append_benchmark(count)
    print_delta(baseline, comparison)
