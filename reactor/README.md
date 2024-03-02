# Reactor pattern

```shell
# python simple_server.py

(python-patterns-py3.10) borgishmorg@SEMON-LAPTOP-2:~/projects/python-patterns/reactor$ python simple_client_benchmark.py
Threads count  |          1|         2|         4|         8|        12|
Actual time (s)|     30.004|    30.004|    30.005|    30.008|    30.009|
Total attempts |     258127|    392912|    371773|    360748|    354104|
Total errors   |          0|         0|         0|         0|         0|
RPS            |   8603.098| 13095.378| 12390.333| 12021.666| 11799.910|
SRPS           |   8603.098| 13095.378| 12390.333| 12021.666| 11799.910|

# python reactor_server.py

(python-patterns-py3.10) borgishmorg@SEMON-LAPTOP-2:~/projects/python-patterns/reactor$ python simple_client_benchmark.py
Threads count  |          1|         2|         4|         8|        12|
Actual time (s)|     30.003|    30.004|    30.005|    30.008|    30.008|
Total attempts |     239874|    429222|    454500|    471935|    480055|
Total errors   |          0|         0|         0|         0|         0|
RPS            |   7994.944| 14305.666| 15147.573| 15726.966| 15997.386|
SRPS           |   7994.944| 14305.666| 15147.573| 15726.966| 15997.386|

# python reactor_server_optimized.py

(python-patterns-py3.10) borgishmorg@SEMON-LAPTOP-2:~/projects/python-patterns/reactor$ python simple_client_benchmark.py
Threads count  |          1|         2|         4|         8|        12|
Actual time (s)|     30.004|    30.004|    30.004|    30.008|    30.010|
Total attempts |     218218|    434276|    652325|    650318|    662918|
Total errors   |        261|       226|       112|         5|         0|
RPS            |   7273.027| 14474.072| 21740.921| 21671.707| 22089.649|
SRPS           |   7264.328| 14466.539| 21737.188| 21671.540| 22089.649|
```
