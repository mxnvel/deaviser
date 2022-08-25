import ffmpeg
import os
import click


def convert(current_file, folder):

    file = folder + "\\" + current_file
    output = ffmpeg.output(ffmpeg.input(file), file.split(".")[0] + ".mp4")
    ffmpeg.run(output)
    os.remove(file)


def tree(dir):
    for (root,dirs,files) in os.walk(dir, topdown=True):

        for i in range (len(files)):
            print(files[i])
            
            if files[i].endswith(".avi"):
                convert(files[i], root,)
                

@click.command()
@click.option('--dir', required=True, help='path of the folder where your files are located (folder included).')
def main(dir):
    tree(dir)
    

if __name__ == '__main__':
    main()
