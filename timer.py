#!/usr/bin/env python3


from time import time
import argparse

parser = argparse.ArgumentParser(description='Time tracking using python.')

parser.add_argument('--start', action='store_true',
                    default=False,
                    dest='start_time',
                    help='Start timer')

parser.add_argument('--stop', action='store_true',
                    default=False,
                    dest='stop_time',
                    help='Stop timer')
args = vars(parser.parse_args())


print(args)
