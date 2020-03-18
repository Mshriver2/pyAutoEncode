#(c)2020 Keker LLC
#Automatically encodes movies from the remux copy of a movie using x264, AvspMod, FFMpeg and Avs2YUV.
import sys
import subprocess
import os.path

# checks to see if pip pyfiglet package is importable
try:
    # imports pyfiglet - used for ascii banner generation
    import pyfiglett
    from pyfiglet import Figlett

# runs if pyfiglet can't be imported
except:
    # prints out the non ascii_banner
    print("##################################################################")
    print('#                          pyAutoEncode                          #')
    print("##################################################################\n")

# if pyfiglet can be imported defines the main ascii banner
else:
    # command for fonts list: [pyfiglet --list_fonts] [font examples = http://www.figlet.org/examples.html]
    ascii_banner_title = Figlet(font='doom')

    # prints out the ascii_banner
    print("##################################################################")
    print(ascii_banner_title.renderText('pyAutoEncode'))
    print("##################################################################\n")

# gets all of the user input
path = raw_input("Enter path of movie to encode: ")
resolution = raw_input("Quality of encode - (1080/720/both) - both does not work for tests: ")
audio_name = raw_input("Enter a name for the .wav file: ")
encode_name = raw_input("Enter a name for encoded mkv file: ")
is_test = raw_input("Would you like to run a test encode? (Y / N): ")

# vars from x264.ini for use in the run_encode function
from ConfigParser import SafeConfigParser
x264_config = SafeConfigParser()
x264_config.read('./config/x264.ini')

c_threads = x264_config.get('x264', 'cfg_threads')
c_vbv_maxrate = x264_config.get('x264', 'cfg_vbv_maxrate')
c_color_matrix = x264_config.get('x264', 'cfg_color_matrix')
c_color_prim = x264_config.get('x264', 'cfg_color_prim')
c_transfer = x264_config.get('x264', 'cfg_transfer')

print(c_threads)

# function for running a test encode, it selects 30 seconds worth of random frames for the test
def test_encode(res, filename, file_path, test_name):

    if res == "1080p":

        #Writes to file 1080p-test.avs for AvspMod (1080p test mode)
        f = open(filename,'wb')
        f.write('ffvideosource("' + file_path + '")\nSelectRangeEvery(2000,50,10000)\nAutoCrop(mode=0, wMultOf=4, hMultOf=2, leftAdd=0, topAdd=0, rightAdd=0, bottomAdd=0, threshold=40, samples=10, samplestartframe=0, sampleendframe=-1, aspect=0)')

        #runs the test encode in 1080p
        run_encode(filename, test_name, '1080p')

    elif res == "720p":

        #Writes to file 1080p-test.avs for AvspMod (1080p test mode)
        f = open(filename,'wb')
        f.write('ffvideosource("' + file_path + '")\nSelectRangeEvery(2000,50,10000)\nAutoCrop(mode=0, wMultOf=4, hMultOf=2, leftAdd=0, topAdd=0, rightAdd=0, bottomAdd=0, threshold=40, samples=10, samplestartframe=0, sampleendframe=-1, aspect=0)')

        #runs the test encode in 720p
        run_encode(filename, test_name, '720p')

# function for writing .avs files
def write_avs(filename, res, file_path):

    if res == "1080":

        #Writes to file 1080p.avs for AvspMod (1080p mode)
        f = open(filename,'wb')
        f.write('ffvideosource("' + file_path + '")\nAutoCrop(mode=0, wMultOf=4, hMultOf=2, leftAdd=0, topAdd=0, rightAdd=0, bottomAdd=0, threshold=40, samples=10, samplestartframe=0, sampleendframe=-1, aspect=0)')

    elif res == "720":

        #Writes to file 720p.avs for AvspMod (720p mode)
        f = open(filename,'wb')
        f.write('ffvideosource("' + file_path + '")\nSpline36ResizeMod(1280, 720)\nAutoCrop(mode=0, wMultOf=4, hMultOf=2, leftAdd=0, topAdd=0, rightAdd=0, bottomAdd=0, threshold=40, samples=10, samplestartframe=0, sampleendframe=-1, aspect=0)')

    elif res == "both":

        #Writes to both 1080p.avs and 720p.avs for AvspMod (both modes)
        f = open(filename + res + '.avs','wb')
        f.write('ffvideosource("' + file_path + '")\nAutoCrop(mode=0, wMultOf=4, hMultOf=2, leftAdd=0, topAdd=0, rightAdd=0, bottomAdd=0, threshold=40, samples=10, samplestartframe=0, sampleendframe=-1, aspect=0)')
        f.close()

        f = open('720p.avs','wb')
        f.write('ffvideosource("' + file_path + '")\nSpline36ResizeMod(1280, 720)\nAutoCrop(mode=0, wMultOf=4, hMultOf=2, leftAdd=0, topAdd=0, rightAdd=0, bottomAdd=0, threshold=40, samples=10, samplestartframe=0, sampleendframe=-1, aspect=0)')

    f.close()




################

#Extracts .wav file from MKV
def extract_wav(file_path, name):

    #Runs wav extraction command in new shell + waits for finish
    subprocess.check_output("start /wait ffmpeg -i " + file_path + " -acodec pcm_s16le -ac 2 " + name + ".wav", shell=True)\

#encodes the remux mkv file with x264 using avs2yuv
def run_encode(avs_file, name, resolution):

    #Runs avs2yuv encode command in new shell + waits for finish
    subprocess.check_output("start /wait avs2yuv \"" + avs_file + "\" -o - | x264 --level 4.1 --preset veryslow --crf 18.0 --deblock -3:-3 --bframes 16 --vbv-bufsize 78125 --qcomp 0.6 --direct auto --min-keyint 24 --vbv-maxrate " + c_vbv_maxrate + " --no-mbtree --trellis 2 --rc-lookahead 250 --merange 34 --subme 11 --no-dct-decimate --threads " + c_threads + " --no-fast-pskip --colormatrix " + c_color_matrix + " --colorprim " + c_color_prim + " --transfer " + c_transfer + " --aq-mode 3 -o " + name + "-" + resolution + "encode.mkv --demuxer y4m - 2>&1", shell=True)

#converts the wav audio file to ac3 using AHK
def convert_to_ac3(wav_name):

    #imports the clipboard package
    import clipboard

    #copys the audio name to clipboard
    clipboard.copy(audio_name + '.wav')

    #imports the pynput python keyboard packages
    from pynput.keyboard import Key, Controller

    #defines controller to execute key presses
    keyboard = Controller()

    #executes ahk script
    keyboard.press(Key.alt)
    keyboard.press('8')
    keyboard.release('8')
    keyboard.release(Key.alt)

#function that checks if a file already exists
def check_file(file_to_check):
    if os.path.isfile(file_to_check):
        print("The file " + file_to_check + " already exists. Ignoring.")
        return True
    else:
        print("The file " + file_to_check + " does not exist. Creating new file...")
        return False

################ Main ################

if is_test == "Y":

    test_encode(resolution, encode_name + resolution + '.test.avs', path, encode_name)

elif is_test == "N":

    if resolution == "1080":

        if not check_file(encode_name + resolution + '.avs'):
            #Executes the write_avs function in 1080p mode
            write_avs(encode_name + resolution + '.avs', '1080', path)
            print("Done!")

        if not check_file(audio_name + '.wav'):
            extract_wav(path, audio_name)
            print("Done!")

        if not check_file(audio_name + '.ac3'):
            convert_to_ac3(audio_name)
            print("Done!")

        if not check_file(encode_name + '-' + resolution + "pencode.mkv"):
            run_encode(encode_name + '1080.avs', encode_name, '1080p')
            print("Done!")

    elif resolution == "720":

        if not check_file(encode_name + resolution + '.avs'):
            #Executes the write_avs function in 1080p mode
            write_avs(encode_name + resolution + '.avs', '720', path)
            print("Done!")

        if not check_file(audio_name + '.wav'):
            extract_wav(path, audio_name)
            print("Done!")

        if not check_file(audio_name + '.ac3'):
            convert_to_ac3(audio_name)
            print("Done!")

        if not check_file(encode_name + '-' + resolution + "pencode.mkv"):
            run_encode(encode_name + '720.avs', encode_name, '720p')
            print("Done!")

    elif resolution == "both":

        #checks if .avs file exists for 720p
        if not check_file(encode_name + '720' + '.avs'):
            write_avs(encode_name + resolution + '.avs', '720', path)

            #checks if .avs file exists for 1080p
            if not check_file(encode_name + '1080' + '.avs'):
                #Executes the write_avs function in both modes
                write_avs(encode_name + resolution + '.avs', '1080', path)

        #checks if .wav exists
        if not check_file(audio_name + ".wav"):
                extract_wav(path, audio_name)

        #checks if .ac3 exits
        if not check_file(audio_name + ".ac3"):
                convert_to_ac3(audio_name)

        #checks if 1080encode.mkv exists exits
        if not check_file(encode_name + ".mkv"):
                run_encode(encode_name + '1080.avs', encode_name, '1080p')

        #checks if 7200encode.mkv exists exits
        if not check_file(encode_name + ".mkv"):
                run_encode(encode_name + '720.avs', encode_name, '720p')

    else:
        print("error")

else:
    print("Please answer Y or N for test encode question.")
