import sys
import os
import yaml
import time
# import subprocess

def go_to_library(config_path):
    #Read in the config file. If the config file is missing or the wrong format, exit the program.
    try:
        with open(config_path, 'r') as config_file:
            config = yaml.load(config_file.read())
    except:
        print("Error: Check config file")
        exit()
    return config

def infiltrate_common_room(zip_dir):
    upload_config = go_to_library('Upload_Config.yaml')
    username = upload_config.get('Username')
    print username
    scp_pass = upload_config.get('scp_Password')
    sftp_usrname = upload_config.get('sftp_Username')
    print sftp_usrname
    sftp_hostname = upload_config.get('sftp_Host')
    sftp_pass = upload_config.get('sftp_Password')
    image_type = raw_input("What type of Images are those? (MRI/PET) ")
    script_file = "descriptive.sh"
    make_script_file = "make_directory.sh"
    os.system("chmod 774 {}".format(script_file))
    os.system("chmod 774 {}".format(make_script_file))

    # origin  = os.path.join(zip_dir,zip_file)
    destination = "{}@tools2.ctsi.ufl.edu".format(username)

    os.system("cat {} | ssh {} ARG1={} 'bash -s' ".format(make_script_file, destination, image_type))
    folder_name = time.strftime("%m_%d_%y")
    dest_path = "/home/{}/{}/{}".format(username,image_type,folder_name)
    for zip_file in os.listdir(zip_dir):
        if not zip_file == ".DS_Store":
            origin  = os.path.join(zip_dir,zip_file)
            os.system('scp {} {}:{}'.format(origin,destination,dest_path))

    os.system("cat {} | ssh {} ARG1={} ARG2={} ARG3={} ARG4={} ARG5={} ARG6={} 'bash -s' ".format(script_file,destination,image_type,sftp_pass,sftp_usrname,sftp_hostname,zip_dir,folder_name))


    #
    # for zip_file in os.listdir(zip_dir):
    #     # if not zip_file == ".DS_Store":
    #     # print zip_dir
    #     # print zip_file
    #     origin  = os.path.join(zip_dir,zip_file)
    #     # print origin
    #
    #     destination = "{}@tools2.ctsi.ufl.edu".format(username)
    #     print destination
    #     dest_path = "/home/{}/{}".format(username,image_type)
    #
    #     os.system('sshpass -p {} scp {} {}:{}'.format(scp_pass,origin,destination,dest_path))

def main(argv):
    zip_dir = argv
    infiltrate_common_room(zip_dir)

if __name__ == '__main__':
    main(sys.argv[1])
