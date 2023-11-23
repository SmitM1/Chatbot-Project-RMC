CREATE TABLE RTI_Application_Status (
Application_No int NOT NULL,
A_Status varchar(200),
PRIMARY KEY(Application_No));

insert into RTI_Application_Status(Application_No, A_Status) 
values(17,'Application Submitted to officer');
insert into RTI_Application_Status(Application_No, A_Status) 
values(12,'Application cleared stage 1 ');
insert into RTI_Application_Status(Application_No, A_Status) 
values(13,'Application Accepted');
insert into RTI_Application_Status(Application_No, A_Status) 
values(16,'Application Rejected');
insert into RTI_Application_Status(Application_No, A_Status) 
values(18,'Application Format Invalid');
insert into RTI_Application_Status(Application_No, A_Status) 
values(19,'Application Accepted by the Officer');

select*from RTI_Application_Status;