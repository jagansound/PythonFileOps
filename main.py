import json
import copy
import csv
from datetime import datetime
from pytz import timezone

from bs4 import BeautifulSoup


def update_xml(X, Y):

    with open('test_payload1.xml', 'r') as f:
        data = f.read()
    bs_data = BeautifulSoup(data, 'xml')
    depart_tag = bs_data.DEPART
    depart_tag.string = X

    return_tag = bs_data.RETURN
    return_tag.string = Y

    with open('test_payload1_jaga.xml','w') as f:
        f.write(bs_data.prettify())

def update_json(element):

    with open('test_payload.json') as data_file:
        data = json.load(data_file)
    deleteElement(element, data)
    with open('test_payload_jaga.json','w') as f:
        json.dump(data,f)


def deleteElement(element, data_file):
    for key in list(data_file):
        if key == element:
            del data_file[key]
        else:
            if isinstance(data_file[key] , dict):
                deleteElement(element, data_file[key])


def readjtlFile():
    with open('Jmeter_log1.jtl',newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        my_timezone = timezone('US/Pacific')
        date_format='%m/%d/%Y %H:%M:%S %Z'
        for row in spamreader:
            if row['responseCode'] != '200':
                timestamp = datetime.fromtimestamp(float(row['timeStamp'])/1000)
                #print(type(datetime.now().timestamp()))
                pstTime = timestamp.astimezone(my_timezone)
                print(row['label'],row['responseCode'],row['responseMessage'],row['failureMessage'],pstTime.strftime(date_format))



if __name__ == '__main__':
    update_xml('PyCharm','tesing')
    update_json('appdate')
    readjtlFile()

