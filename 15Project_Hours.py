from datetime import datetime, timedelta
import time

class Hours:
    def __init__(self, seconds):
        self.seconds = seconds

    def countdown(self):
        start = datetime.now()
        end = start + timedelta(seconds=self.seconds)

        while datetime.now() < end:
            remaining = (end - datetime.now()).seconds
            print(f"\rОсталось {remaining} секунд", end="", flush=True)
            time.sleep(1)

        print("\nВремя вышло!")

    def __str__(self):
        now = datetime.now()
        return f"Текущее время: {now.strftime('%H:%M:%S')}"

h = Hours(5)
print(h)
h.countdown()