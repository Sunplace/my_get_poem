#!/bin/sh

poem_num=`python rand_poem.py`
echo $poem_num
curl -o __"$poem_num"__.html http://so.gushiwen.org/view_"$poem_num".aspx
while [ !  -s __"$poem_num"__.html  ]
do
    curl -o __"$poem_num"__.html http://so.gushiwen.org/view_"$poem_num".aspx
done

echo '<HTML xmlns="http://www.w3.org/1999/xhtml>"' >> _"$poem_num"_.html
echo '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">' \
    >> _"$poen_num"_.html
echo '<HEAD><meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />' >> _"$poem_num"_.html
echo "<TITLE>To be or not to be,that is the question.</TITLE>" >> _"$poem_num"_.html
echo "</HEAD>" >> _"$poem_num"_.html
echo "<BODY>" >> _"$poem_num"_.html
grep '<h1>' __"$poem_num"__.html  >> _"$poem_num"_.html
grep '<p style="margin:' __"$poem_num"__.html |\
    sed 's/<.*><span>//g' | sed 's/<\/span>//g' |\
    sed 's/<a.*\">//g' | sed 's/<\/a>//g' | sed 's/<\/p>/<\/br>/g' >> _"$poem_num"_.html
python beliefy.py __"$poem_num"__.html _"$poem_num"_.html
echo "</BODY>" >> _"$poem_num"_.html
echo "</HTML>" >> _"$poem_num"_.html
mv _"$poem_num"_.html ./
rm __"$poem_num"__.html
exit

#~/bin/gethtml so.gushiwen.org/view_888.aspx 80 > tmp1111
#echo '<HTML>\n'
#echo '\t<HEAD>\n'
#echo '\t\t<TITLE>To be or not to be,that is the question.</TITLE>\n'
#echo '\t</HEAD>\n'
#echo '\t<BODY>\n'
#grep 'h1' tmp1111
#grep '<p' tmp1111 #| head -n 4
#echo '\t</BODY>\n'
#echo '</HTML>'
#exit
#rm tmp1111
