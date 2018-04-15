import time
from datetime import datetime as dt
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.amazon.com", "daraz.com.bd"]

while True:
    print(1)
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
    else:
        print("Free hours...")
    time.sleep(5)
