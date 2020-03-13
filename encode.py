#(c)2020 Keker LLC
#Automatically encodes movies from the remux copy of a movie using x264, AvspMod, FFMpeg and Avs2YUV.
import sys
import subprocess

path = raw_input("Enter path of movie to encode: ")
resolution = raw_input("Quality of encode - (1080p/720p/both): ")
audio_name = raw_input("Enter a name for the .wav file: ")
encode_name = raw_input("Enter a name for encoded mkv file: ")

# function for writing .avs files
def write_avs(filename, res, file_path):

    if res == "1080":

        #Writes to file 1080p.avs for AvspMod (1080p mode)
        f = open(filename,'wb')
        f.write('ffvideosource("' + file_path + '")\nAutoCrop(mode=0, wMultOf=4, hMultOf=2, leftAdd=0, topAdd=0, rightAdd=0, bottomAdd=0, threshold=40, samples=10, samplestartframe=0, sampleendframe=-1, aspect=0)')

    elif res == "720":

        #Writes to file 720p.avs for AvspMod (720p mode)
        f = open(filename,'wb')
        f.write('ffvideosource("' + path + '")\nSpline36ResizeMod(1280, 720)\nAutoCrop(mode=0, wMultOf=4, hMultOf=2, leftAdd=0, topAdd=0, rightAdd=0, bottomAdd=0, threshold=40, samples=10, samplestartframe=0, sampleendframe=-1, aspect=0)')

    elif res == "both":

        #Writes to both 1080p.avs and 720p.avs for AvspMod (both modes)
        f = open('1080p' + filename + '.avs','wb')
        f.write('ffvideosource("' + path + '")\nAutoCrop(mode=0, wMultOf=4, hMultOf=2, leftAdd=0, topAdd=0, rightAdd=0, bottomAdd=0, threshold=40, samples=10, samplestartframe=0, sampleendframe=-1, aspect=0)')
        f.close()

        f = open('720p.avs','wb')
        f.write('ffvideosource("' + path + '")\nSpline36ResizeMod(1280, 720)\nAutoCrop(mode=0, wMultOf=4, hMultOf=2, leftAdd=0, topAdd=0, rightAdd=0, bottomAdd=0, threshold=40, samples=10, samplestartframe=0, sampleendframe=-1, aspect=0)')

    f.close()

################

#Extracts .wav file from MKV
def extract_wav(file_path, name):

    #Runs wav extraction command in new shell + waits for finish
    subprocess.check_output("start /wait ffmpeg -i " + file_path + " -acodec pcm_s16le -ac 2 " + name + ".wav", shell=True)\

#encodes the remux mkv file with x264 using avs2yuv
def run_encode(avs_file, name, resolution):

    #Runs avs2yuv encode command in new shell + waits for finish
    subprocess.check_output("start /wait avs2yuv \"" + avs_file + "\" -o - | x264 --level 4.1 --preset veryslow --crf 18.0 --deblock -3:-3 --bframes 16 --vbv-bufsize 78125 --qcomp 0.6 --direct auto --min-keyint 24 --vbv-maxrate 62500 --no-mbtree --trellis 2 --rc-lookahead 250 --merange 34 --subme 11 --no-dct-decimate --threads 8 --no-fast-pskip --colormatrix bt709 --colorprim bt709 --transfer bt709 --aq-mode 3 -o " + name + "-" + resolution + "encode.mkv --demuxer y4m - 2>&1", shell=True)

#converts the wav audio file to ac3 using AHK
def convert_to_ac3():

    #imports the pynput python keyboard packages
    from pynput.keyboard import Key, Controller

    #defines controller to execute key presses
    keyboard = Controller()

    #executes ahk script
    keyboard.press(Key.alt)
    keyboard.press('8')
    keyboard.release('8')
    keyboard.release(Key.alt)

################ Main ################

if resolution == "1080":

    #Executes the write_avs function in 1080p mode
    write_avs('1080p.avs', '1080', path)
    extract_wav(path, audio_name)
    run_encode('1080p.avs', encode_name, '1080p')

elif resolution == "720":

    #Executes the write_avs function in 720p mode
    write_avs('720p.avs', '720', path)
    extract_wav(path, audio_name)
    run_encode('720p.avs', encode_name, '720p')

elif resolution == "both":
    #Executes the write_avs function in both modes
    write_avs('', 'both', path)
    extract_wav(path, audio_name)
    run_encode('1080p.avs', encode_name, '1080p')
    run_encode('720p.avs', encode_name, '720p')

else:
    print("error")
