#!/usr/bin/env python3

import math
from datetime import datetime, timedelta

EVENT_FILENAME = "events.txt"


def save_event(text: str, start_timestamp: datetime):
    text = text.rstrip()
    if len(text) == 0:  # ignore empty events
        return

    current_timestamp = datetime.now()
    diff = current_timestamp - start_timestamp
    current_date = current_timestamp.strftime("%d.%m.%Y %H:%M:%S")
    elapsed_time = timedelta(seconds=math.ceil(diff.total_seconds()))

    with open(EVENT_FILENAME, 'a') as f:
        f.write(f'--- Event @ {current_date}, {elapsed_time} ---\n')
        f.write(f'{text}\n\n')
        print(f'Saved event @ {current_date}, elapsed time: {elapsed_time}\n')


def main():
    start_timestamp = datetime.now()
    while True:
        event_text = ""
        print('Event text (double <ENTER> to confirm and save, or <q> to quit):')
        while True:
            text = input('  ')
            if len(text) == 0:
                save_event(event_text, start_timestamp)
                break

            if text.lower() == 'q' or text.lower() == 'quit':
                save_event(event_text, start_timestamp)
                confirm_quit = input('Do you really want to quit the application [yN]: ').lower()
                if confirm_quit == 'y' or confirm_quit == 'yes':
                    return
                break

            event_text += f'{text}\n'


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
