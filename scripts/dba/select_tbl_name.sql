-- this script is for selecting user define table name by setting \set tblname

-- \set tblname $1
-- \set tbllimit $2

SELECT * FROM :tblname LIMIT :tbllimit;