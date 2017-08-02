pet_Val="PET"
mri_val="MRI"

echo "hello"
echo "$username"
cd "$image_type"/"$folder"

echo "$image_type and $pet_Val"
if [ $image_type == $pet_Val ]
then
    image_type="APET"
fi

sshpass -p "$password" sftp "$username"@"$hostname":"$image_type"
pwd
put *
"This program will self-destruct (but it worked, trust me!)."
exit
