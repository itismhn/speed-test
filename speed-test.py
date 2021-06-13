import speedtest
speed=speedtest.Speedtest()

# get download speed in bit and convert to mbit
print("geting download Speed...")
download_result=speed.download()/1024/1024
print(f"Your download speed is : {download_result:.2f}mbits/s")


# get Upload speed in mbit
print("get Upload Speed...")
upload_result=speed.upload()/1024/1024
print(f"Your upload speed is : {upload_result:.2f}mbits/s")


# test ping speed
print("ping test...")
ping_result=speed.results.ping
print(f"Your upload speed is : {ping_result}ms")