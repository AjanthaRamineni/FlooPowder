import sys
import os
import yaml
import time
# import subprocess

def connect_to_floo_network(config_path):
    #Read in the config file. If the config file is missing or the wrong format, exit the program.
    try:
        with open(config_path, 'r') as config_file:
            config = yaml.load(config_file.read())
    except:
        print("Error: Check config file")
        exit()
    return config

def step_into_fireplace(zip_dir):
    upload_config = connect_to_floo_network('Upload_Config.yaml')
    username = upload_config.get('Username')
    print username
    sftp_usrname = upload_config.get('sftp_Username')
    print sftp_usrname
    sftp_hostname = upload_config.get('sftp_Host')
    sftp_pass = upload_config.get('sftp_Password')
    image_type = raw_input("What type of images are you uploading? (MRI/PET) ")

    make_folder_script = "grab_powder.sh"
    put_files_script = "teleport.sh"
    os.system("chmod 774 {}".format(put_files_script))
    os.system("chmod 774 {}".format(make_folder_script))

    destination = "{}@tools2.ctsi.ufl.edu".format(username)
    print destination

    os.system("cat {} | ssh {} ARG1={} 'bash -s' ".format(make_folder_script, destination, image_type))
    folder_name = time.strftime("%m_%d_%y")
    dest_path = "/home/{}/{}/{}".format(username,image_type,folder_name)
    for zip_file in os.listdir(zip_dir):
        if not zip_file == ".DS_Store":
            origin  = os.path.join(zip_dir,zip_file)
            os.system('scp {} {}:{}'.format(origin,destination,dest_path))
 #"ssh {user}@{host}".format(**config)
    os.system("cat {} | ssh {} image_type={} zip_dir={} folder={} password={sftp_Password} username={sftp_Username} hostname={sftp_Host}  'bash -s' ".format(put_files_script, destination, image_type, zip_dir, folder_name, **upload_config))
        #ARG1={} ARG2={} ARG3={} ARG4={} ARG5={} ARG6={folder_name} 'bash -s' ".format(put_files_script,destination,image_type,sftp_pass,sftp_usrname,sftp_hostname,zip_dir,folder_name))

def main(argv):
    zip_dir = argv
    step_into_fireplace(zip_dir)

if __name__ == '__main__':
    main(sys.argv[1])
