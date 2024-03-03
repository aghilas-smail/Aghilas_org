--CREATE TABLE EmployeeDemographics
--(EmployeeID int,
--FirstName varchar(50),
--LastName varchar(50),
--Age int, 
--Gender varchar(50)
--)

--Drop table EmployeeDemographics

----EmployeeSalary TABLE

--create table EmployeeSalary
--(EmployeeID int,
--JobTitle varchar(50),
--Salary int)

--Insert into EmployeeDemographics VALUES
--(1001, 'Jim', 'Halpert', 30, 'Male'),
--(1002, 'Pam', 'Beasley', 30, 'Female'),
--(1003, 'Dwight', 'Schrute', 29, 'Male'),
--(1004, 'Angela', 'Martin', 31, 'Female'),
--(1005, 'Toby', 'Flenderson', 32, 'Male'),
--(1006, 'Michael', 'Scott', 35, 'Male'),
--(1007, 'Meredith', 'Palmer', 32, 'Female'),
--(1008, 'Stanley', 'Hudson', 38, 'Male'),
--(1009, 'Kevin', 'Malone', 31, 'Male')

--select * from EmployeeDemographics

----select top (5) [EmployeeID]
----		,[FirstName]
----		,[LastName]
----		,[Age]
----		,[Gender]
----	From [SQL_tuto].[dbo].[EmployeeDemographics]



--INSERT INTO EmployeeSalary VALUES
--(1001, 'Salesman', 45000), 
--(1002, 'Receptionist', 36000), 
--(1003, 'Salesman', 63000),
--(1004, 'Accountant', 47000),
--(1005, 'HR', 50000),
--(1006, 'Regional Manager', 65000),
--(1007, 'Supplier Relations', 41000),
--(1008, 'Salesman', 48000),
--(1009, 'Accountant', 42000)


--select * from EmployeeSalary


--select * from EmployeeDemographics

-- *retourne les nom qui on un S a la fin*
--where LastName Like '%S'
-- condition pour savoir si une le FirstName est null ou pas.
--where FirstName is Not null

--select *
--from EmployeeDemographics
----Order by Age, Gender DESC
--order by 4 Desc, 5 Desc

--select Gender ,age, COUNT(Gender) 
--from EmployeeDemographics
--Group By Gender, Age


--select Gender, COUNT(Gender) AS CountGender
--from EmployeeDemographics
--where Age > 31
--Group By Gender
--Order By CountGender ASC


--Select *
--FROM SQL_tuto.dbo.EmployeeDemographics 

--Select * 
--From SQL_tuto.dbo.EmployeeSalary

----------------------------------------

/*
Inner Joins, Full/ Left/ Right outer Joins

*/

--Insert into EmployeeDemographics VALUES
--(1001, 'Jim', 'Halpert', 30, 'Male'),
--(NULL, 'Pam', 'Beasley', NULL, NULL),
--(1013, 'Dwight', 'Schrute', NULL, 'Male')

--Insert into EmployeeSalary VALUES
--(1010, NULL, 47000),
--(NULL , 'Salesman',43000)

--select * from EmployeeDemographics
--select * from EmployeeSalary

-- Inner Join c'est comme l'intersection entre les 2 table.
Select * from SQL_tuto.dbo.EmployeeDemographics
Inner Join SQL_tuto.dbo.EmployeeSalary
	ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID

-- Full Outer Join c'est de prende le tous qui veut dire faire l'union.

Select * from EmployeeDemographics
FULL Outer Join EmployeeSalary
	ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID


-- Left Outer Join prende l'union mais sans la 2 table.
-- Et le right et de faire le contraire .

Select * from EmployeeDemographics
Right Outer Join EmployeeSalary
	ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
