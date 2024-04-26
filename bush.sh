# создать папку arhive скриптом (что бы проверял и делал если нет созданной)
arhive=$(find . -type d -name "arhive")
for n in $arhive; do
if [!-d ./$n]
then
mkdir ./$n
echo "direction_compled"
done