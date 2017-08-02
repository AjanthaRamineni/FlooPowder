image_type=$ARG1
echo "Entered"
now=$(date +'%m_%d_%y')
alias image="cd {}".format
# cd $image_type && exec pwd
mkdir $image_type+"/"+$now
exit
