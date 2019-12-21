import requests
import sys
import json

"""
> python3 upload.py -f filename.bed -t BED -s hg19
"""
def get_parameters(argv):
    argv = " ".join(argv)
    def locate(argv, name):
        string = [i for i in argv.split("-") if i[0] == name][0]
        if string[-1] == " ":
            string = string[:-1]
        return string.split(" ")[1:]


    filenames = locate(argv, "f")
    filetypes = locate(argv, "t")
    species = locate(argv, "s")
    return filenames, filetypes, species


filenames, filetypes, species = get_parameters(sys.argv)
uploads = zip(filenames, filetypes, species)


url_base = "http://www.circdraw.com"
url = url_base + '/tools/upload/'

for up in uploads:
    print("Begin uploading file {}...".format(up[0]))
    file_up = {'file': open(up[0], 'rb')}
    PARAM = {'parameters': json.dumps({'filetype': up[1], 'species': up[2]})}
    #r = requests.post(url, files=file_up, parameters= PARAM)
    r = requests.post(url, files=file_up, data=PARAM)
    md5 = r.json()[0]['md5']
    ss_status = r.json()[0]['save_status']
    visiting_url = url_base + '/tools/display/' + md5
    if ss_status == 'Finished':
        print("Your request has been processed, please visit the report through the following url: \n {}".format(visiting_url))
    elif ss_status == 'Running':
        print("Your request is Running in our backend, please visit the report through the following url: \n {}".format(visiting_url))

    ## call run
    elif ss_status == True:
        run_url = url_base + '/tools/run'
        run_param = {'caseid': md5}
        print("Your request has been initiated and will be processed soon, please visit the report through the following url: \n {}".format(visiting_url))

        run_response = requests.get(run_url, params=run_param)
        sleep(10)

    elif ss_status == False:
        print("Upload failed, please check your file and parameters and try again...")

    print("________")
print("@circDraw 2019")



