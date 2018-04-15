import time
from datetime import datetime as dt

hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.amazon.com", "www.daraz.com.bd"]
restricted_hour_start = 8
restricted_hour_end = 23
restriction_starts = dt(dt.now().year, dt.now().month, dt.now().day, restricted_hour_start)
restriction_ends = dt(dt.now().year, dt.now().month, dt.now().day, restricted_hour_end)

while True:
    if restriction_starts < dt.now() < restriction_ends:
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website not in content:
                    file.write("\n" + redirect + " " + website)
    else:
        c = 0
        print("Free hours...")
        with open(hosts_path, "r") as file:
            content = file.readlines()
        with open(hosts_path, "w") as file:
            for line in content:
                for website in website_list:
                    if website in line:
                        c = c + 1
                if c == 0:
                    file.write(line)
                else:
                    c = 0

    time.sleep(5)
