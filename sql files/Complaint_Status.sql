CREATE TABLE Complaint_Status(
complaint_id int NOT NULL,
C_Status varchar(200),
PRIMARY KEY (complaint_id));



insert into Complaint_Status(complaint_id, C_Status) 
values(142,' Work In Progress');
insert into Complaint_Status(complaint_id, C_Status) 
values(133,'Issue Resolved');
insert into Complaint_Status(complaint_id, C_Status) 
values(139,'Work Completed');
insert into Complaint_Status(complaint_id, C_Status) 
values(136,'Issue will be resolved soon');
insert into Complaint_Status(complaint_id, C_Status) 
values(135,'Issue Overcomed');
insert into Complaint_Status(complaint_id, C_Status) 
values(132,'Successfully Resolved the Issue');

select*from Complaint_Status;