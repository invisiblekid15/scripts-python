import time

from requests import get

if __name__ == "__main__":
    with open('./bids.txt', "r") as f:
        data = f.readlines()
        for line in data:
            r=get('http://core-mojo-rest.ecs.mmt/v4/flight/pushScannerData/'+str(line).strip()+"?isV2Scanner=true")
            print(r,line)
            time.sleep(0.1)
            # print(str(line).strip())




