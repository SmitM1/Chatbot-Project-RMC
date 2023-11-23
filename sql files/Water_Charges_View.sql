CREATE TABLE Water_Charges_View(
Connection_No int NOT NULL,
R_Name varchar(100),
Avg_Water_Terrif float,
Avg_Amount_Due float,
PRIMARY KEY (Connection_No));

insert into Water_Charges_View(Connection_No, R_Name, Avg_Water_Terrif, Avg_Amount_Due) 
values(91026,'Pankit',56.00,00.00);
insert into Water_Charges_View(Connection_No, R_Name, Avg_Water_Terrif, Avg_Amount_Due) 
values(91072,'Smit',57.56,85.00);
insert into Water_Charges_View(Connection_No, R_Name, Avg_Water_Terrif, Avg_Amount_Due) 
values(91023,'Kavan',78.70,567.00);
insert into Water_Charges_View(Connection_No, R_Name, Avg_Water_Terrif, Avg_Amount_Due) 
values(91036,'Kushal',103.00,00.00);
insert into Water_Charges_View(Connection_No, R_Name, Avg_Water_Terrif, Avg_Amount_Due) 
values(91001,'Dhruv',119.00,30.00);
insert into Water_Charges_View(Connection_No, R_Name, Avg_Water_Terrif, Avg_Amount_Due) 
values(91067,'Parth',369.40,820.00);


select*from Water_Charges_View;