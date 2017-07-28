image_type=$ARG1
echo "Making Directory"

now=$(date +'%m_%d_%y')
cd $image_type
mkdir $now

exit
