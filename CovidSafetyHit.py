import time

from requests import get

if __name__ == "__main__":
    with open('./bids.txt', "r") as f:
        data = f.readlines()
        for line in data:
            try:
                r=get('http://localhost/v1/flight/sendWhatsappCovid/'+str(line).strip(), timeout=5)
                print(r,line)
            except:
                print("retry",line)
                with open("failed.txt", "a") as myfile:
                    myfile.write(line)

            # time.sleep(0.005)
            # print(str(line).strip())




