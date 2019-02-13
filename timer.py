#!/usr/bin/env python3

import datetime
import argparse
import json


parser = argparse.ArgumentParser(description='Time tracking using python.')

parser.add_argument('--start', action='store_true',
                    default=False,
                    dest='start_time',
                    help='Start timer')

parser.add_argument('--stop', action='store_true',
                    default=False,
                    dest='stop_time',
                    help='Stop timer')
results = parser.parse_args()
args = vars(parser.parse_args())


if results.stop_time:
    args['stop_time'] = datetime.datetime.now
    
if results.start_time:
    args['start_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# print(args)

with open('outfile', 'a') as outfile:
    json.dump(args, outfile)
