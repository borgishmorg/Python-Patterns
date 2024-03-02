# Echo client program
# Based on https://docs.python.org/3/library/socket.html#example
import socket
import time
from dataclasses import dataclass
from concurrent.futures import ProcessPoolExecutor


HOST = 'localhost'    # The remote host
PORT = 50007          # The same port as used by the server
TOTAL_TIME = 30       # in seconds
DATA = b'A' * 1024
NTHREADS = [1, 2, 4, 8, 12]


@dataclass
class TestResult:
    attempts = 0
    errors = 0


@dataclass
class BenchmarkResult:
    n_threads: int
    attempts: int
    errors: int
    actual_time: float


def caller(*args, **kwargs) -> TestResult:
    result = TestResult()
    start_time = time.perf_counter()

    while time.perf_counter() - start_time <= TOTAL_TIME:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(DATA)
                data = s.recv(1024)
                assert data == DATA
        except Exception:
            result.errors += 1
        finally:
            result.attempts += 1
    
    return result


benchmark_results: list[BenchmarkResult] = []
for n_threads in NTHREADS:
    with ProcessPoolExecutor(max_workers=n_threads) as pool:
        actual_start_time = time.perf_counter()
        results = list(pool.map(caller, range(n_threads)))
        actual_end_time = time.perf_counter()

    benchmark_results.append(BenchmarkResult(
        n_threads=n_threads,
        attempts = sum(r.attempts for r in results),
        errors = sum(r.errors for r in results),
        actual_time=actual_end_time-actual_start_time,
    ))

print('\n'.join([
    f'Threads count  | ' + '|'.join(f'{br.n_threads:10}' for br in benchmark_results) + '|',
    f'Actual time (s)| ' + '|'.join(f'{br.actual_time:10.3f}' for br in benchmark_results) + '|',
    f'Total attempts | ' + '|'.join(f'{br.attempts:10}' for br in benchmark_results) + '|',
    f'Total errors   | ' + '|'.join(f'{br.errors:10}' for br in benchmark_results) + '|',
    f'RPS            | ' + '|'.join(f'{br.attempts/br.actual_time:10.3f}' for br in benchmark_results) + '|',
    f'SRPS           | ' + '|'.join(f'{(br.attempts - br.errors)/br.actual_time:10.3f}' for br in benchmark_results) + '|',
]))
