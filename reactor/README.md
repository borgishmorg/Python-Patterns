# Reactor pattern

## Описание

Реактор (англ. Reactor) — предназначен для синхронной передачи запросов сервису от одного или нескольких источников. [1]

Шаблон проектирования реактора представляет собой шаблон обработки событий для обработки запросов на обслуживание, передаваемых одновременно обработчику услуг одним или несколькими входами. Обработчик сервиса затем демультиплексирует входящие запросы и отправляет их синхронно связанным обработчикам запросов.

**Плюсы:**

Модель реактора полностью отделяет конкретный код приложения от реализации реактора, что означает, что компоненты приложения можно разделить на модульные, повторно используемые детали. Кроме того, из-за синхронного вызова обработчиков запросов шаблон реактора допускает простой параллельный анализ, не добавляя сложность нескольких потоков в систему.

**Минусы:**

Модель реактора может быть сложнее отлаживать, чем процедурный шаблон из-за перевернутого потока управления. Кроме того, только синхронно обрабатывая обработчики запросов, шаблон реактора ограничивает максимальный параллелизм, особенно на симметричном многопроцессорном оборудовании. Масштабируемость шаблона реактора ограничена не только вызовом обработчиков запросов синхронно, но и демультиплексором.

## Тесты производительности

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

## Литература

1. Паттерн Reactor - Реактор. Описания паттернов проектирования. Паттерны проектирования. Design pattern ru ([article](https://design-pattern.ru/patterns/reactor.html))
2. Reactor. An Object Behavioral Pattern for Demultiplexing and Dispatching Handles for Synchronous Events Douglas C. Schmidt ([article](https://www.dre.vanderbilt.edu/~schmidt/PDF/reactor-siemens.pdf))
3. The Proactor and Reactor Design Patterns ([video](https://youtu.be/Vm5l8zH4hOE?si=Rsn9q3zrqssb-q4x))
4. CIS566 - Reactor Design Pattern - SangjunLee ([video](https://youtu.be/prooCOgqcJc?si=v8AGrfQPsnCe2ho_))
