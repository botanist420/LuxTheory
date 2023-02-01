echo "Please type the table name, I will show you all the columns in this table: "

read tbl_name

sleep 1
echo "Generating sql script...This is the output:"
echo " "
sleep 1 

value="SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public' AND TABLE_NAME = '$tbl_name';"

echo $value
