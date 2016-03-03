import os
import sys
import subprocess
import json
import urllib2
from urllib2 import urlopen, URLError, HTTPError

# Option 1: Open mp4 file from url
def downloadFile():

    # Input mp4 URL
    url = raw_input('Input mp4 url: ')
    if not url:
        print "No url provided!"
        quit()
    # Download mp4 and save to disk
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    #mime = meta.getheader('Content-Type')
    file_size = int(meta.getheaders("Content-Length")[0])
    print "\nDownloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()

    return file_name;

# Option 2: Open mp4 file from folder
# Note should be in same folder as this script
def openFile():
    # Input filename
    file_name = raw_input('Input mp4 filename: ')
    if not file_name:
        print "No filename provided!"
        quit()
    return file_name

# Select options for reading mp4 files
try:
    option = int(raw_input('1. Download File\n2. Open File\nSelect an option: '))
except ValueError:
    print "Invalid selection provided!"
    quit()

if option == 1:
    file_name = downloadFile()
elif option == 2:
    file_name = openFile()
else:
    print "Not a valid selection!"
    quit()

# Use ffmpeg's ffprobe to read the mp4 metadata and save as a json file
file_name_json = file_name+".json"

subprocess.call('ffprobe -v quiet -print_format json -show_streams -show_format "'+file_name+'" > "'+file_name_json+'"', shell=True)

with open(file_name_json) as data_file:    
    data = json.load(data_file)

# Video JSON Data
bitrate = data["streams"][0]["bit_rate"]
bitrate_overall = data["format"]["bit_rate"]
duration = data["streams"][0]["duration"]
width = data["streams"][0]["width"]
height = data["streams"][0]["height"]
video_codec = data["streams"][0]["codec_name"]
video_profile = data["streams"][0]["profile"]
video_level = data["streams"][0]["level"]

# Audio JSON Data
audio_codec = data["streams"][1]["codec_name"]
audio_profile = data["streams"][1]["profile"]

# Convert bitrate to an integer
bitrate = int(float(bitrate))
# Round bitrate to nearst 1000th
bitrate = round(bitrate, -3)
# Divide by 1000 to get kbps
bitrate = bitrate/1000

# Convert bitrate to an integer
bitrate_overall = int(float(bitrate_overall))
# Round bitrate to nearst 1000th
bitrate_overall = round(bitrate_overall, -3)
# Divide by 1000 to get kbps
bitrate_overall = bitrate_overall/1000

# Change seconds into HH:MM:SS format
def vast_duration_format(secs):
	mins, secs = divmod(secs, 60)
	hours, mins = divmod(mins, 60)
	return '%02d:%02d:%02d' % (hours, mins, secs)

# Format duration
duration = vast_duration_format(float(duration))

# Print out mp4 information
print "\n"
print "Video Bitrate (kbps): %i" % bitrate
print "Overall Bitrate (kbps): %i" % bitrate_overall
print "Duration: %s" % duration
print "Width: %s" % width
print "Height: %s" % height
print "Video Codec: %s" % video_codec
print "Video Profile: %s" % video_profile
print "Video Level: %s" % video_level
print "Audio Codec: %s" % audio_codec
print "Audio Profile: %s" % audio_profile
print "\n"

# Cleanup/delete mp4 and json file after process completes
# os.remove(file_name)
# os.remove(file_name_json)