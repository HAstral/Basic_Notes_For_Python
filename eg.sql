INSERT INTO roles (name, guard_name) VALUES 

('Admin', 'web'), 

('Manager', 'web'), 

('Staff', 'web'), 

('HR', 'web'), 

('Accountant', 'web'), 

('Developer', 'web'), 

('Tester', 'web'), 

('Designer', 'web'), 

('Analyst', 'web'), 

('Intern', 'web'); 

 

INSERT INTO departments (id, guid, code, slug, name, description) VALUES 

(1, 'guid-1', 'IT', 'it', 'Information Technology', 'Manages all IT related activities'), 

(2, 'guid-2', 'HR', 'hr', 'Human Resources', 'Handles employee relations and recruitment'), 

(3, 'guid-3', 'FIN', 'finance', 'Finance', 'Manages financial transactions and accounting'), 

(4, 'guid-4', 'MKT', 'marketing', 'Marketing', 'Promotes the company and its products'), 

(5, 'guid-5', 'SALES', 'sales', 'Sales', 'Handles sales and customer relations'); 

 

 

INSERT INTO users (id, department_id, guid, name, email, password) VALUES 

(1, 3, 'guid-1', 'Myat Amara', 'amara@gmail.com', 'password123'), 

(2, 4, 'guid-2', 'Atta Maung', 'atta@gmail.com', 'password456'), 

(3, 5, 'guid-3', 'Yadanar May', 'yadanar@gmail.com', 'password789'); 

 

INSERT INTO user_details (user_id, phone, address, dob, gender, nrc, parent_name, parent_phone, office_appoint_date, office_resign_date, cv, contract) VALUES 

(1, '09-988477356', '123 Main St', '1990-01-15', 'Male', 'NRC12345', 'Mahaw Amara', '09-989543553', '2020-05-01', NULL, 'myat_amara_cv.pdf', 'myat_amara_contract.pdf'), 

(2, '09-776563443', '456 RiverBank St', '1992-06-20', 'Female', 'NRC67890', 'Linn Hteik Kaung', '09-878543554', '2021-02-10', NULL, 'atta_maung_cv.pdf', 'atta_maung_contract.pdf'), 

(3, '09-450889554', '789 Min Kaung St', '1988-11-05', 'Female', 'NRC101112', 'Htut Bo', '09-7875454544','2019-09-15', '2023-10-20', 'yadanar_may_cv.pdf', 'yadanar_may_contract.pdf'); 

 

INSERT INTO attendances (user_id, date, check_in, check_out, working_hours) VALUES 

(1, '2024-07-01', '2024-07-01 09:00:00', '2024-07-01 17:00:00', 8.00), 

(1, '2024-07-02', '2024-07-02 09:30:00', '2024-07-02 17:30:00', 8.00), 

(1, '2024-07-03', '2024-07-03 09:00:00', '2024-07-03 18:00:00', 9.00), 

(1, '2024-07-04', '2024-07-04 09:00:00', '2024-07-04 17:00:00', 8.00), 

(1, '2024-07-05', '2024-07-05 09:00:00', '2024-07-05 17:00:00', 8.00), 

(1, '2024-07-08', '2024-07-08 09:00:00', '2024-07-08 17:00:00', 8.00), 

(1, '2024-07-09', '2024-07-09 09:00:00', '2024-07-09 17:00:00', 8.00), 

(1, '2024-07-10', '2024-07-10 09:00:00', '2024-07-10 17:00:00', 8.00), 

(1, '2024-07-11', '2024-07-11 09:00:00', '2024-07-11 17:00:00', 8.00), 

(1, '2024-07-12', '2024-07-12 09:00:00', '2024-07-12 17:00:00', 8.00); 

 

INSERT INTO attendances (user_id, date, check_in, check_out, working_hours) VALUES 

(2, '2024-07-01', '2024-07-01 09:00:00', '2024-07-01 17:00:00', 8.00), 

(2, '2024-07-02', '2024-07-02 09:30:00', '2024-07-02 17:30:00', 8.00), 

(2, '2024-07-03', '2024-07-03 09:00:00', '2024-07-03 18:00:00', 9.00), 

(2, '2024-07-04', '2024-07-04 09:00:00', '2024-07-04 17:00:00', 8.00), 

(2, '2024-07-05', '2024-07-05 09:00:00', '2024-07-05 17:00:00', 8.00), 

(2, '2024-07-08', '2024-07-08 09:00:00', '2024-07-08 17:00:00', 8.00), 

(2, '2024-07-09', '2024-07-09 09:00:00', '2024-07-09 17:00:00', 8.00), 

(2, '2024-07-10', '2024-07-10 09:00:00', '2024-07-10 17:00:00', 8.00), 

(2, '2024-07-11', '2024-07-11 09:00:00', '2024-07-11 17:00:00', 8.00), 

(2, '2024-07-12', '2024-07-12 09:00:00', '2024-07-12 17:00:00', 8.00); 

 

INSERT INTO attendances (user_id, date, check_in, check_out, working_hours) VALUES 

(3, '2024-07-01', '2024-07-01 09:00:00', '2024-07-01 17:00:00', 8.00), 

(3, '2024-07-02', '2024-07-02 09:30:00', '2024-07-02 17:30:00', 8.00), 

(3, '2024-07-03', '2024-07-03 09:00:00', '2024-07-03 18:00:00', 9.00), 

(3, '2024-07-04', '2024-07-04 09:00:00', '2024-07-04 17:00:00', 8.00), 

(3, '2024-07-05', '2024-07-05 09:00:00', '2024-07-05 17:00:00', 8.00), 

(3, '2024-07-08', '2024-07-08 09:00:00', '2024-07-08 17:00:00', 8.00), 

(3, '2024-07-09', '2024-07-09 09:00:00', '2024-07-09 17:00:00', 8.00), 

(3, '2024-07-10', '2024-07-10 09:00:00', '2024-07-10 17:00:00', 8.00), 

(3, '2024-07-11', '2024-07-11 09:00:00', '2024-07-11 17:00:00', 8.00), 

(3, '2024-07-12', '2024-07-12 09:00:00', '2024-07-12 17:00:00', 8.00); 

 

INSERT INTO leave_requests (user_id, date_from, date_to, type, reason, status) VALUES 

(1, '2024-07-15', '2024-07-17', 'Vacation', 'Going on holiday', 'Approved'), 

(1, '2024-07-22', '2024-07-23', 'Sick Leave', 'Feeling unwell', 'Pending'), 

(1, '2024-07-29', '2024-07-30', 'Personal Leave', 'Family event', 'Rejected'), 

(1, '2024-08-05', '2024-08-07', 'Vacation', 'Long weekend trip', 'Approved'), 

(1, '2024-08-12', '2024-08-13', 'Sick Leave', 'Flu', 'Pending'); 

 

INSERT INTO leave_requests (user_id, date_from, date_to, type, reason, status) VALUES 

(2, '2025-01-15', '2025-01-16', 'Annual Leave', 'Family gathering', 'Approved'), 

(2, '2025-02-20', '2025-02-22', 'Sick Leave', 'Health issues',  'Approved'), 

(2, '2025-03-05', '2025-03-07', 'Casual Leave', 'Urgent personal work', 'Pending'), 

(2, '2025-02-01', '2025-02-02', 'Annual Leave', 'Family function', 'Approved'), 

(2, '2025-04-10', '2025-04-12', 'Casual Leave', 'Travel', 'Pending'); 

 

INSERT INTO leave_requests (user_id, date_from, date_to, type, reason, status) VALUES 

(3, '2025-02-10', '2025-02-12', 'Sick Leave', 'Medical reasons', 'Approved'), 

(3, '2025-02-15', '2025-02-16', 'Annual Leave', 'Family vacation', 'Approved'), 

(3, '2025-03-01', '2025-03-03', 'Casual Leave', 'Personal matters', 'Pending'), 

(3, '2025-01-25', '2025-01-27', 'Sick Leave', 'Flu recovery', 'Approved'), 

(3, '2025-04-05', '2025-04-07', 'Casual Leave', 'Personal matters','Pending'); 