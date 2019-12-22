# Upload tool for circDraw

This tool servers as a command line tool for uploading files to circDraw server which is part of circDraw-clt project. It is designed to benefit research labs to use [circDraw](https://www.circdraw.com) service from their command line server which may not have a GUI. Users can upload files to circDraw server by using this command line tool and retrieve analysis reports from any computer with a web browser and specific urls. 

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
circDraw-upload also supports upload file from one init file to avoid tedious typing through command line. You can specify the uploaded filename, file type and its origin species in a single csv file. The cvs file should follow the following format with "," seperate each column:

Upload filename | Upload file type | Origin species
--- | --- | ---
 | | 

__Note__: Currently circDraw only supports limited filetype and species, they are specified in the following table:

Uploaded file type | Represent string | Description
--- | --- | ---
_.BED_ | 'BED' | BED (Browser Extensible Data) format provides a flexible way to define the data lines that are displayed in an annotation track. BED lines have three required fields for each line: chrom, chromStart, chromEnd. For more information about BED format we accepted, please visit our example in circDraw [upload](https://www.circdraw.com/tools/) page.
_.CIRI_ | 'CIRI' | Output file from 'Gao, Y., Wang, J. & Zhao, F. CIRI: an efficient and unbiased algorithm for de novo circular RNA identification. Genome Biol 16, 4 (2015) doi:10.1186/s13059-014-0571-3'


Species | Represent string | Description
--- | --- | ---
Human(hg19) | 'human-hg19' | Human Genome Reference Sequencing [(GRCh37/h19)](https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg19&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr1%3A11102837%2D11267747&hgsid=784255443_iXvZctwCCbA7VtPbVPYG30Ix5ueN) from Feb 2009.
Human(hg38) | 'human-hg38' | Human Genome Reference Sequencing [(GRCh38/h38)](https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr1%3A11102837%2D11267747&hgsid=784255443_iXvZctwCCbA7VtPbVPYG30Ix5ueN)
Mouse(mm10) | 'mouse-mm10' | Mouse Genome Reference Sequencing [(GRCm38/mm10)](https://genome.ucsc.edu/cgi-bin/hgTracks?hgsid=784255443_iXvZctwCCbA7VtPbVPYG30Ix5ueN&org=Mouse&db=mm10&position=chr12%3A56%2C694%2C976-56%2C714%2C605&pix=1420) from Dec 2011.
Rat(rn6) | 'rar-rn6' | Rat Genome Reference Sequencing [(RGSC6.0/rn6)](https://genome.ucsc.edu/cgi-bin/hgTracks?db=rn6&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr1%3A80608553%2D80639261&hgsid=784255443_iXvZctwCCbA7VtPbVPYG30Ix5ueN) from Jul 2014.
Yeast(sacCer3) | 'yeast-sacCer3' | Yeast Genome Reference Sequencing [(SacCer_Apr2011/sacCer3)](https://genome.ucsc.edu/cgi-bin/hgTracks?db=sacCer3&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chrIV%3A765966%2D775965&hgsid=784255443_iXvZctwCCbA7VtPbVPYG30Ix5ueN) from Apr 2014.
Zebra Fish(danRer11) | 'zebra-fish-danRer11' | Zebra Fish Genome Reference Sequencing [(GRCz11/danRer11)](https://genome.ucsc.edu/cgi-bin/hgTracks?db=danRer11&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr6%3A43426669%2D43433274&hgsid=784255443_iXvZctwCCbA7VtPbVPYG30Ix5ueN) from May 2017.




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

