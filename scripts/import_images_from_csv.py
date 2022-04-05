from rois.models import Image
import os
import sys
import glob
import pytz
import datetime
import shutil
from multiprocessing import Pool


def do_import(line):

    tokens = line.split(',')
    image_name = tokens[1]

    im = Image(image_id=image_name)
    image_meta = im.explode_id()

    timestamp_number = int(image_meta['unixtime'])
    if timestamp_number < 1390443064 or timestamp_number > 1536443141:
        return

    im.major_axis_length = int(tokens[2])
    im.minor_axis_length = int(tokens[3])

    if im.major_axis_length != 0:
        im.aspect_ratio = im.minor_axis_length/im.major_axis_length
    else:
        im.aspect_ratio = 1

    im.timestamp = datetime.datetime.fromtimestamp(
        image_meta['unixtime'],
        tz=pytz.UTC
    )
    # Set the image width and height
    im.image_width = image_meta['width']
    im.image_height = image_meta['height']

    try:
        im.save()
    except:
        print('could not import images, maybe it already exists.')


def run(*args):

    input_dir = '/home/spcadmin/cameradata/'

    csv_files = sorted(glob.glob(os.path.join(input_dir,'*.csv')),reverse=True)

    print(input_dir)

    print(csv_files)

    for csv_file in csv_files:
        print(csv_file)
        print('reading lines from csv file')
        with open(csv_file,'r') as f:
            lines = f.readlines()

        p = Pool(12)
        print('running lines through pooled import.')
        p.map(do_import,lines)

        os.remove(csv_file)
