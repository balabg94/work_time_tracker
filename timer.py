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

def read_file():
    with open('kronos', 'a+') as kronos_file:
        return kronos_file



if results.start_time:
    args['start_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    out_dict[current_date].append(args['start_time'])
    with open('kronos', 'a') as kronos_file:
        json.dump(out_dict, kronos_file)

if results.stop_time:
    args['stop_time'] = datetime.datetime.now
    for i in out_dict[current_date]:
        print('ok')
        if len(i) == 1:
            print('in')
            i.append(args['stop_time'])
        else:
            print('none')
#import pdb; pdb.set_trace()
# print args

#print(out_dict)


# with open('outfile', 'a') as outfile:
#     json.dump(args, outfile)
