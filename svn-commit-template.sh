#!/bin/sh 
# 
# Example SVN_EDITOR script 
#
[ $# -eq 1 ] || { 
    echo "usage: $0 file" 
    exit 1 
} 
file=$1 
ed=$VISUAL 
[ -z $ed ] && ed=$EDITOR 
[ -z $ed ] && ed=vi 

echo "Issue# " >> $file.$$
echo "Reviewer(s): " >> $file.$$
echo "Description: " >> $file.$$
echo "" >> $file.$$

cat $file >> $file.$$

sum=`cksum $file.$$` 
if $ed $file.$$; then 
    newsum=`cksum $file.$$` 
    if [ "$newsum" != "$sum" ]; then 
        rm -f $file 
        mv $file.$$ $file 
    else 
        # no changes 
        rm -f $file.$$ 
    fi 
else 
    echo "editor \"$ed\" failed" 
    exit 1 
fi
