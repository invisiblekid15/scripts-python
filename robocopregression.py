import json
import time
import pymysql.cursors
import pymysql


from requests import post



if __name__ == "__main__":
   with open('./testrobocop.json', "r") as f:
       data = json.loads(f.read())
       count = 0

       for d in data:
           # if d['airline'] == 'INDIGO' and d['processType'] == 'NOSHOW':
               # sending post request and saving response as response object
               #  print("sending ", d)
            # r = post(url = "http://core-mojo-flightsrobocop.ecs.mmt/flights-robocop/v1/mojo/addJobs", data = json.dumps(d))
            r = post(url = "http://core-mojo-rest.ecs.mmt/v4/flight/pushScannerData/"+bid+"?isV2Scanner=true", data = json.dumps(d))
               # time.sleep(1)
            count+=1
            if(count == 3):
                break;
       print(count);