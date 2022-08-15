import ffmpeg
import os 

cd = os.getcwd()
filename = os.path.basename(__file__)
folder_list=os.listdir(cd)
folder_list.remove(filename)


def convert(current_file, folder):
    file = ffmpeg.input(folder + "\\" + current_file)
    output = ffmpeg.output(file, folder + "\\" + current_file.split(".")[0] + ".mp4")
    ffmpeg.run(output)
    os.remove(folder + "\\" + current_file)

def main():
    for i in range (len(folder_list)):
        file_list=os.listdir(cd + "\\" + folder_list[i])
        print (file_list)
        folder = folder_list[i]
        for j in range(len(file_list)):
            current_file = file_list[j]
            convert(current_file, folder)

main()
