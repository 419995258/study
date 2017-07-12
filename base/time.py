import time

# print base.time()
print time.localtime()
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
for i in range(100):
    # time.sleep(i*0.01)
    print i