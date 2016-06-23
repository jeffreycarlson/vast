import os
import sys
import subprocess
import json
import urllib2
from urllib2 import urlopen, URLError, HTTPError

# Open mp4 file from url
def downloadFile(url):
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

# Calculate bitrate
def calculate_bitrate(bitrate):
    # Convert bitrate to an integer
    bitrate = int(float(bitrate))
    # Round bitrate to nearst 1000th
    bitrate = round(bitrate, -3)
    # Divide by 1000 to get kbps 
    # Note that /1000, not /1024, is used for bandwidth bit calculations
    bitrate = bitrate/1000 
    return bitrate

# Change seconds into HH:MM:SS format
def vast_duration_format(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '%02d:%02d:%02d' % (hours, mins, secs)

# Calculate video size
def calculate_video_size(video_size):
    video_size = float(video_size)
    # Divide by 1000000 to get MB size
    return video_size / 1000000

# Input mp4 URL
url = raw_input('Input mp4 url: ')
if not url:
    print "No url provided!"
    quit()

file_name = downloadFile(url)

# Use ffmpeg's ffprobe to read the mp4 metadata and save as a json file
file_name_json = file_name+".json"

subprocess.call('ffprobe -v quiet -print_format json -show_streams -show_format "'+file_name+'" > "'+file_name_json+'"', shell=True)

with open(file_name_json) as data_file:    
    data = json.load(data_file)

codec_type = data["streams"][0]["codec_type"]

if codec_type == 'video':
    video_stream = 0
    audio_stream = 1
elif codec_type == 'audio':
    video_stream = 1
    audio_stream = 0
else:
    print "Error parsing video metadata!"
    quit()

# Video JSON Data
bitrate_video = data["streams"][video_stream]["bit_rate"]
bitrate_audio = data["streams"][audio_stream]["bit_rate"]
bitrate_overall = data["format"]["bit_rate"]
duration = data["streams"][video_stream]["duration"]
width = data["streams"][video_stream]["width"]
height = data["streams"][video_stream]["height"]
video_codec = data["streams"][video_stream]["codec_name"]
video_profile = data["streams"][video_stream]["profile"]
video_level = data["streams"][video_stream]["level"]
video_size = data["format"]["size"]

# Audio JSON Data
audio_codec = data["streams"][audio_stream]["codec_name"]
audio_profile = data["streams"][audio_stream]["profile"]

bitrate_video = calculate_bitrate(bitrate_video)
bitrate_audio = calculate_bitrate(bitrate_audio)
bitrate_overall = calculate_bitrate(bitrate_overall)

# Format duration
duration = vast_duration_format(float(duration))

# Format video size
video_size_mb = calculate_video_size(video_size)

# Print out mp4 information
print "\n"
#print "Video Bitrate (kbps): %i" % bitrate_video
#print "Audio Bitrate (kbps): %i" % bitrate_audio
#print "Overall Bitrate (kbps): %i" % bitrate_overall
#print "Duration: %s" % duration
#print "Width: %s" % width
#print "Height: %s" % height
#print "Video Codec: %s" % video_codec
#print "Video Profile: %s" % video_profile
#print "Video Level: %s" % video_level
#print "Audio Codec: %s" % audio_codec
#print "Audio Profile: %s" % audio_profile
#print "File Size (mb): %.2f" % video_size_mb
print "VAST MediaFile:\n"
# Print video/mp4
print "<MediaFile delivery=\"progressive\" type=\"video/mp4\" bitrate=\"%i\" width=\"%s\" height=\"%s\" scalable=\"true\" maintainAspectRatio=\"true\">\n\t<![CDATA[%s]]>\n</MediaFile>" % (bitrate_video, width, height, url)
print "\n"

# Cleanup/delete mp4 and json file after process completes
# os.remove(file_name)
# os.remove(file_name_json)