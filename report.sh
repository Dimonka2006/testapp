#прочитать файл, отфильтровать с датой  30..... и создать выборку
  #for i in 1 2 3 4 5 6 7 8 9 0; do
set -x
cat data-2024-04-07-03-00-01.csv | grep "/3[0-9];" > report.txt
#done
 