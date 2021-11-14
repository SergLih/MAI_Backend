# MAI_Backend

#### Замечание: неудачное название.
###### tennis_app - это проект, а tennis_application - приложение.

## Тестирование через ab:

```
ab -n 6000 -c 20 -t 2 -v 2 http://127.0.0.1:8001/

...
Finished 11548 requests


Server Software:        gunicorn/19.10.0
Server Hostname:        127.0.0.1
Server Port:            8001

Document Path:          /
Document Length:        14 bytes

Concurrency Level:      20
Time taken for tests:   2.000 seconds
Complete requests:      11548
Failed requests:        0
Total transferred:      1859228 bytes
HTML transferred:       161672 bytes
Requests per second:    5773.73 [#/sec] (mean)
Time per request:       3.464 [ms] (mean)
Time per request:       0.173 [ms] (mean, across all concurrent requests)
Transfer rate:          907.78 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     0    3   0.3      3       5
Waiting:        0    3   0.3      3       5
Total:          1    3   0.3      3       5

Percentage of the requests served within a certain time (ms)
  50%      3
  66%      4
  75%      4
  80%      4
  90%      4
  95%      4
  98%      4
  99%      4
 100%      5 (longest request)
```

Вывод по тестированию:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1) Было проведено 6000 запросов для 20 параллельных клиентов. Из них было 0 запросов, завершившихся ошибкой веб-сервера.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2) Производительность веб-сервера: обработано 5774 запроса в секунду.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3) Среднее время обработки 1 запроса 3.464 мс.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4) 50% запросов выполнились за 3 мс, еще 40% запросов за 4 мс, самый долгий запрос составил 5 мс.
