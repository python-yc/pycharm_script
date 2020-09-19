# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
import os
from datetime import datetime

print(os.name)

def func():
    print('func This is func!')


def tick():
    print('Tick! The time is: %s' %datetime.now())


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=2)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C   '))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
