#! /bin/bash
# 批量进入每个目录只保留最新版本目录
file=$(ls)
echo $file
for filename in $file
do
  if [ -d $filename ]; then
    cd $filename
    echo "======================= $filename start ==================" >> ../branchLog.log
    newbranch=$(ls | sort | tail -1)
    branchList=$(ls)
    echo "keep file ==> $newbranch <==" >> ../branchLog.log
    for branch in $branchList
    do
      if [ -d $branch ] && [ $newbranch -ne $branch ]; then
        echo "$branch" >> ../branchLog.log
        rm -rf $branch &
      fi
    done
    echo "======================= $filename end ==================/r/n/t" >> ../branchLog.log
    echo "" >> ../branchLog.log
  fi
  cd ..
done
