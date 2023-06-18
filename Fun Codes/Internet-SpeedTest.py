import speedtest

speed = speedtest.Speedtest()

download_speed = speed.download()
upload_speed = speed.upload()

print("Download Speed is ",download_speed)
print("Upload Speed is ",upload_speed)