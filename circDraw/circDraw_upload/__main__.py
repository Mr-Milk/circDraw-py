import sys
from .upload import upload_function
from .version import __version__
#from .draw import circDraw
import os
import argparse

def main():
    species_box = {'human-hg19':'hg19', 'human-hg38': 'hg38', 'mouse-mm10':'mm10', 'rat-rn6':'rn6', 'yeast-sacCer3': 'sacCer3', 'zebra-fish-danRer11':'danRer11'}
    filetype_box = ['BED', 'CIRI']


    #### Upload parameter parse
    parser = argparse.ArgumentParser(description="Upload command line interface for circDraw web server.")

    # version
    parser.add_argument("-v", "--version", action="store_true", help="Version of the package")

    # manually
    parser.add_argument("-f", "--file", action='append', help="Filename you want to upload.")
    parser.add_argument("-t", "--type", action='append', help="Filetype of your file, circDraw currently supports {}. Names of the selected file type should be exactly matched.".format(filetype_box), choices=filetype_box)
    parser.add_argument("-s", "--species", action='append', help="Specify your species, currently circDraw support {}. Names of the species should be exactly matched.".format(list(species_box.keys())), choices=list(species_box.keys()))

    # byfile
    parser.add_argument("-i", "--initfile", help="header filename which specify the information of uploaded filename, uploaded filetype and corresponding species; File should be in csv format where each row represents a file, and three column should be (filename, filetype, species). Note that this mode overwrites any '-f', '-t', '-s' input.")


    args = parser.parse_args()
    dict_args = vars(args)
    if not any(list(dict_args.values())):
        exit("Welcome to use circDraw-upload (" + __version__ + ")!")
    
    if args.version:
        exit("Version: " +  __version__)
    if args.initfile:
        try:
            if args.file or args.type or args.species:
                overwrite = input("CircDraw Warning: \n\tYou are mixing -f/-t/-s flag with -i flag, press Y/y to overwrite using -i mode, any other key to Abort: ")
                if overwrite.lower() != 'y':
                    print("Abort!")
                    exit()
            #assert args.file == None, "Do not mix -i flag with -f or --file flag..."
            #assert args.type == None, "Do not mix -i flag with -t or --type flag..."
            #assert args.species == None, "Do not mix -i flag with -s --speciesflag..."
            print("CircDraw: Using file as input for uploading... ")
            filenames, filetypes, input_species = [], [], []
            initfile_final = os.getcwd() + '/' + args.initfile
            with open(initfile_final) as f:
                line = f.readline()
                line_num = 1
                while line:
                    line_strip = line.strip()
                    info_file = line_strip.replace(" ", "").split(",")
                    assert len(info_file) == 3, "Critical information is missing in line {} of '{}' file...\n \t Line {} in '{}': '{}'".format(line_num, args.initfile, line_num, args.initfile, line_strip)
                    # check filetype
                    assert info_file[1] in filetype_box, "Filetype '{}' in line {} of '{}' is not supported, please use -h to see supported type...\n \t Line {} in '{}': '{}'".format(info_file[1], line_num, args.initfile, line_num, args.initfile, line_strip)
                    assert info_file[2] in species_box, "Species type '{}' in line {} of '{}' is not supported, please use -h to see supported species...\n \t Line {} in '{}': '{}'".format(info_file[2], line_num, args.initfile, line_num, args.initfile, line_strip)
                    filenames.append(info_file[0])
                    filetypes.append(info_file[1])
                    input_species.append(species_box[info_file[2]])
                    line = f.readline()
                    line_num += 1
            ### .initfile must be in the same directory with the data file
            os.chdir("/".join(initfile_final.split("/")[:-1]))

        except FileNotFoundError as e:
            print("CircDraw Error: File '{}' not found, recheck your parameter after -i: {}".format(args.initfile, e))
            print("Abort!")
            exit()
        except AssertionError as e2:
            print("CircDraw Error: ",e2)
            print("Abort!")
            exit()

    else:
        try:
            filenames = args.file
            filetypes = args.type
            input_species = args.species
            input_species = [species_box[i] for i in input_species]
            assert len(filenames) == len(filetypes), "the number of -f input doesn't match the number of -t input"
            assert len(input_species) == len(filenames), "the number of -f input doesn't match the number of -s input"
        except AssertionError as e3:
            print("CircDraw Error: ", e3)
            print("Abort!")
            exit()


    ##### Process

    ###### final check before sent:
    for i in zip(filenames, filetypes, input_species):
        try:
            with open(i[0]) as f:
                content = f.read()
                assert content != '', "Upload file '{} is empty!'".format(i[0])
            assert i[1] in filetype_box, "Filetype '{}' is not supported. Use -h to find supported file type.".format(i[1])
            assert i[2] in list(species_box.values()), "Species type '{}' is not supported. Use -h to find supported species type.".format(i[2])
        except FileNotFoundError as e_final:
            print("CircDraw Error: File '{}' not found for upload".format(i[0]))
            print("Abort!")
            exit()
        except AssertionError as e2_final:
            print("CircDraw Error: ",e2_final)
            print("Abort!")
            exit()

    print("CircDraw: Finished pre-check list for uploading, clear for uploading!")

    uploads = zip(filenames, filetypes, input_species)
    url_base = "https://www.circdraw.com"
    upload_function(url_base, uploads)

if __name__ == '__main__':
    main()
