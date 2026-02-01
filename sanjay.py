Table: employee (This table contains active employee records)
 
emp_id  emp_name  emp_dob  emp_ssn
340  John  03151978  334-555-7787
356  Mark  02201994  993-111-3345
200  Alex  11131980  334-555-7787
980  Christina  04151977  434-556-7899
20  Andy  02051986  434-556-7899
130 Elliot 03041988 222-555-3333
 
>>> Using the table employee -
 
Q1. Write a SQL query that will return the employee records for which the emp_ssn is not duplicated.

With emp_unique as (
Select emp_ssn, count(*) as cut from employee group by emp_ssn having count(*)=1)
Select * from employee where emp_ssn in (select emp_ssn from emp_unique)
 
Q2. Write a SQL query that will return the emp_ssn's that are duplicate (they appear more than once)
 Select emp_ssn from employee group by emp_ssn having count(*)>1

Q3. Write a SQL query that returns the name of the employees for which the SSN is duplicated.
 
With emp_unique as (
Select emp_ssn, count(*) as cut from employee group by emp_ssn having count(*)>1)
Select emp_name from employee where emp_ssn in (select emp_ssn from emp_unique)

 
Table: resigned_employee  (This table contains resigned employee records)
emp_id  emp_name  emp_dob  emp_ssn
340  Marco  03151978  114-556-7711
200 Peter 01021985 333-434-9967
 
>>> Using both tables employee and resigned_employee
 
Q4. Write a SQL query that returns both active employees and resigned employees
Select emp_id , emp_name,  emp_dob,  emp_ssn from employee
Union all
Select emp_id , emp_name,  emp_dob,  emp_ssn from resigne_employee

df = spark.createDataFrame(
    [
        ("sue", 32),
        ("li", 3),
        ("bob", 75),
        ("heo", 13),
    ],
    ["first_name", "age"],
)
 
 
df.show()
 
Q1:
add a new column to each row, the value in the column should be based on the age of the person as per the logic below -
 
>> if the age is < 13 then the value is "child"
>> if the age between 13 and 19 the value is "teenager"
>> else the value is "adult"
 
 
Q2:
>> retrieve only those records where the person is an adult.




Df = Df.withColumn('age_category', when(Col("age")<13).then("child").otherwise(when(col("age").between(13,19)).then("teenager").otherwise("adult"))

Df.filter(Col("age_category")=='adult').show()


























