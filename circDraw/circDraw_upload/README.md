# Upload tool for circDraw

This tool servers as a command line tool for uploading files to circDraw server which is part of circDraw-clt project. It is designed to help labs to use [circDraw](https://www.circdraw.com) service from their command line server which may not have a GUI. Users can upload files to circDraw server by using this command line tool and retrieve analysis reports from any computer with a web browser and specific urls. 

## Install

This tool is installed automatically as part of circDraw-clt, please refer to the `Install` section on the [README.md](https://github.com/Mr-Milk/circDraw-py) of the whole project.

## Usage

### Upload on command line
#### Upload files with parameters
- Sinle upload file
```bash
$ circDraw-upload -f test_circfile.bed -t BED -s human-hg19
```

![](/src/circDraw-upload-fts-single.png)


- Multiple upload files
```bash
$ circDraw-upload -f test_circfile.bed -t BED -s human-hg19 -f test_circfile.bed -t BED -s human-hg19
```

![](/src/circDraw-upload-fts-multiple.png)

#### Upload file with init file
- Single upload file
```bash
$ circDraw-upload -i test_init_single.txt
```

![](/src/circDraw-upload-i-single.png)

- Multiple upload files
```bash
$ circDraw-upload -i test_init_multiple.txt
```
![](/src/circDraw-upload-i-multiple.png)





### Help
```bash
$ circDraw-upload -h
$ circDraw-upload --help

usage: circDraw-upload [-h] [-f FILE] [-t {BED,CIRI}]
                       [-s {human-hg19,human-hg38,mouse-mm10,rat-rn6,yeast-sacCer3,zebra-fish-danRer11}]
                       [-i INITFILE]

Upload command line interface for circDraw web server.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Filename you want to upload.
  -t {BED,CIRI}, --type {BED,CIRI}
                        Filetype of your file, circDraw currently supports
                        ['BED', 'CIRI']. Names of the selected file type
                        should be exactly matched.
  -s {human-hg19,human-hg38,mouse-mm10,rat-rn6,yeast-sacCer3,zebra-fish-danRer11}, --species {human-hg19,human-hg38,mouse-mm10,rat-rn6,yeast-sacCer3,zebra-fish-danRer11}
                        Specify your species, currently circDraw support
                        ['human-hg19', 'human-hg38', 'mouse-mm10', 'rat-rn6',
                        'yeast-sacCer3', 'zebra-fish-danRer11']. Names of the
                        species should be exactly matched.
  -i INITFILE, --initfile INITFILE
                        header filename which specify the information of
                        uploaded filename, uploaded filetype and corresponding
                        species; File should be in csv format where each row
                        represents a file, and three column should be
                        (filename, filetype, species). Note that this mode
                        overwrites any '-f', '-t', '-s' input.

```

## Dependancy
## About

