#! /bin/bash
cd /opt/pub/software/repository/Services/ManageOne/
fileDate=$1
serviceList=$(ls)
branchLog=/opt/pub/software/repository/Services/ManageOne/branchLog.log
for service in $serviceList
do
  if [ -d $service ]; then
    cd $service
    echo "======================= Service $service start ==================" >> $branchLog
    appList=$(ls)
    for app in $appList
    do
      if [ -d $app ]; then
        cd $app
        echo "======================= APP $app start ==================" >> $branchLog
        newFile=$(ls -rt | tail -1)
        newDateFile=${newFile%[0-9]*}
        newDay=${newDateFile:0:(${#newDateFile}-5)}
        echo "========>> keep file $newDateFile* <<==========" >> $branchLog
        find ./ -maxdepth 1 -name "[A-Z]*" ! -name "$newDay*" | xargs ls >> $branchLog 
        echo "======================= APP $app end ==================" >> $branchLog
        echo "" >> $branchLog
        cd ..
      fi
    done
    echo "======================= Service $service end ==================" >> $branchLog
    echo "" >> $branchLog
    cd ..
  fi
done
