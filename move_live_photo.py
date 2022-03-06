import glob
import os.path
import time
import re

in_path = './'

file_list = []
for root, dirnames, filenames in os.walk(in_path):
    for filename in filenames:
        if os.path.splitext(filename)[1].lower() == ".mov":            
            file_list.append(os.path.join(root, filename))

for f in file_list:
    dst = os.path.dirname(f) + '/live_photo/'
    fn = os.path.splitext(f)[0]
    if fn.endswith('_HEVC'):
        fn = fn[:-5]
    jpg = fn + '.jpg'
    jpg_cap = fn + '.JPG'
    if os.path.isfile(jpg) or os.path.isfile(jpg_cap):
        #print(f'Live photo {f} found')
        if not os.path.exists(os.path.dirname(dst)):
            try:
                os.makedirs(os.path.dirname(dst))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        cmd = 'mv ' + f + ' ' + dst
        print(cmd)
        os.system(cmd)

