import time

from requests import get
from joblib import Parallel, delayed


def processPacket(line):
    try:
        r = get('http://localhost/v1/flight/sendWhatsappDigiYatra/' + str(line).strip(), timeout=5)
        print(r, line)
    except:
        print("retry", line)
        with open("failed.txt", "a") as myfile:
            myfile.write(line)


if __name__ == "__main__":
    with open('./bids.txt', "r") as f:
        data = f.readlines()
        Parallel(n_jobs=6)(delayed(processPacket)(line) for line in data)

            # time.sleep(0.005)
            # print(str(line).strip())




