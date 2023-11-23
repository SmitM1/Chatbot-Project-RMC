CREATE TABLE Property_Tax_View(
property_number int NOT NULL,
R_Name varchar(100),
Amount_Payable float,
Amount_Due float,
PRIMARY KEY (property_number));

insert into Property_Tax_View(property_number, R_Name, Amount_Payable, Amount_Due) 
values(2112601070,'Pankit',56.00,00.00);
insert into Property_Tax_View(property_number, R_Name, Amount_Payable, Amount_Due) 
values(2112601072,'Smit',57.56,85.00);
insert into Property_Tax_View(property_number, R_Name, Amount_Payable, Amount_Due) 
values(2112601023,'Kavan',78.70,567.00);
insert into Property_Tax_View(property_number, R_Name, Amount_Payable, Amount_Due) 
values(2112601036,'Kushal',103.00,00.00);
insert into Property_Tax_View(property_number, R_Name, Amount_Payable, Amount_Due) 
values(2112601078,'Dhruv',119.00,30.00);
insert into Property_Tax_View(property_number, R_Name, Amount_Payable, Amount_Due) 
values(2112601067,'Parth',369.40,820.00);



select*from Property_Tax_View;