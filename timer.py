#!/usr/bin/env python3

import datetime
import argparse
import json


parser = argparse.ArgumentParser(description='Time tracking using python.')

parser.add_argument('--start',
                    action='store_true',
                    default=False,
                    dest='start_time',
                    help='Start timer')

parser.add_argument('--stop',
                    action='store_true',
                    default=False,
                    dest='stop_time',
                    help='Stop timer')


results = parser.parse_args()
args = vars(parser.parse_args())

out_dict = dict()
current_date = datetime.datetime.now().strftime("%d-%m-%Y")
out_dict[current_date] = []

def start_time():
    args['start_time'] = datetime.datetime.now().strftime("%H:%M")
    out_dict[current_date].append(args['start_time'])
    with open('kronos', 'a') as kronos_file:
        json.dump(out_dict, kronos_file)

def stop_time():
    args['stop_time'] = datetime.datetime.now().strftime("%H:%M")
    if len(file_[current_date]) == 1:
        file_[current_date].append(args['stop_time'])        
    elif len(file_[current_date]) ==2:
        print('Already stopped.')
def read_file():
    with open('kronos', 'r') as kronos_file:
        data = kronos_file.read()
        data_json = json.loads(data)
        return data_json



if results.start_time:
    start_time()

file_ = read_file()
print(file_)

if results.stop_time:
    stop_time()

with open('kranos','w+') as out_:
    json.dump(file_, out_)


