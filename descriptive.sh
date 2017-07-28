
image_type=$ARG1
sftp_pass=$ARG2
sftp_usrname=$ARG3
sftp_hostname=$ARG4
input_dir=$ARG5
folder_name=$ARG6
pet_Val="PET"
mri_val="MRI"

echo "hello"
echo "$sftp_usrname"
cd "$image_type"/"$folder_name"

echo "$image_type and $pet_Val"
if [ "$image_type" == "$pet_Val" ]
then
    echo "PET images"
    sshpass -p "$sftp_pass" sftp "$sftp_usrname"@"$sftp_hostname"
    cd APET
    put *
    exit
    # put zip_file
fi

if [ "$image_type" == "$mri_val" ]
then
    echo "PET images"
    sshpass -p "$sftp_pass" sftp "$sftp_usrname"@"$sftp_hostname"
    cd MRI
    put *
    exit
fi
