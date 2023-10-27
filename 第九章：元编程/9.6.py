#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import time
import gevent


def task():
    gevent.sleep(1)


if __name__ == "__main__":
    start = time.time()
    coroutins = [gevent.spawn(task) for _ in range(1000000)]
    gevent.joinall(coroutins)

    print(time.time() - start)
