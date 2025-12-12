-- Alembic Version
INSERT INTO public.alembic_version (version_num) VALUES
('1c8299227e2a');

-- Categories
INSERT INTO public.categories (name) VALUES
('Garbage'),
('Flood'),
('Pollution'),
('Road'),
('Water'),
('Electricity'),
('Other');

-- Statuses
INSERT INTO public.statuses (name) VALUES
('Pending'),
('In Progress'),
('Resolved');

-- Reports (sample data)
INSERT INTO public.reports 
(title, description, address, photo_url, created_at, updated_at, category_id, status_id) VALUES
('illegal dumping','Lots of dumps near road','San Miguel Padre Garcia/near Ate Pasing house','/uploads/CAM00574.jpg','2025-11-18 00:04:57.364239','2025-12-03 01:40:08.527149',1,3),
('Flood','Flooding near the capitol','San Miguel Padre Garcia Batangas','/uploads/Screenshot_2025-11-16_044659.png','2025-11-17 23:14:10.803049','2025-11-18 07:46:26.50984',2,2),
('Garbage Pile-up Near Barangay Hall','Too much garbage near the hall. Smells bad','Purok 5, Barangay Poblacion, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_164535.png','2025-12-09 08:45:48.582975','2025-12-09 08:45:48.582975',1,1),
('Flooding in San Miguel Road','Road floods when it rains. Hard to pass','San Miguel Road, Barangay San Miguel, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_164654.png','2025-12-09 08:47:07.281373','2025-12-09 08:47:07.281373',2,1),
('Damaged Street Lights in Barangay Banaybanay','Street lights broken. Dark at night.','Barangay Banaybanay, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_164759.png','2025-12-09 08:48:08.789258','2025-12-09 08:48:08.789258',8,1),
('Illegal Dumping in Forest Area','People dumping trash in the forest. Not good.','Forest Area, Barangay Payapa, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_164927.png','2025-12-09 08:49:39.823606','2025-12-09 08:49:39.823606',1,1),
('Water Leakage in Public Faucet','Faucet leaking. Wasting water.','Public Faucet, Barangay Quilo-quilo North, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_165032.png','2025-12-09 08:50:48.14604','2025-12-09 08:50:48.14604',7,1),
('Vandalism in Public Park','Park has graffiti. Looks bad.','Public Park, Barangay Mangas, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_165210.png','2025-12-09 08:52:19.996806','2025-12-09 08:52:19.996806',9,1),
('Contaminated River Water','River is dirty. Not safe to use.','River, Barangay Castillo, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_165320.png','2025-12-09 08:53:33.493366','2025-12-09 08:53:33.493366',3,1),
('Improper Waste Segregation','People mix trash. Hard to recycle.','Various locations in Barangay Payapa Ibaba, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_165435.png','2025-12-09 08:55:17.020748','2025-12-09 08:55:17.020748',1,1),
('Potholes on Main Road','Road has holes. Bumpy ride.','Main Road, Barangay Pansol, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_165742.png','2025-12-09 08:57:53.074559','2025-12-09 08:57:53.074559',6,1),
('Chemical Waste Leakage','Chemicals leaking. Dangerous.','Near Factory, Barangay Bukal, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_165947.png','2025-12-09 08:59:59.438085','2025-12-09 08:59:59.438085',3,1),
('Clogged Drainage System','Drains are blocked. Causes flooding.','Various locations in Barangay San Felipe, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_165502.png','2025-12-09 09:01:06.998612','2025-12-09 09:01:06.998612',2,1),
('Unsafe Electrical Wiring','Wires are exposed. Dangerous to touch.','Public Area, Barangay San Felipe, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_170205.png','2025-12-09 09:02:13.213292','2025-12-09 09:02:13.213292',8,1),
('Stagnant Water and Mosquito Breeding Sites','Old tires and containers are collecting rainwater, creating breeding grounds for mosquitos. Increased risk of dengue fever.','Barangay Cawongan, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_170304.png','2025-12-09 09:03:22.884887','2025-12-09 09:03:22.884887',3,1),
('Abandoned Vehicle','Old car/unattended car blocking the road.','Along the road, Barangay Quilo Quilo North, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_170528.png','2025-12-09 09:05:39.636714','2025-12-09 09:05:39.636714',6,1),
('Deforestation in Protected Area','Trees being cut down. Forest disappearing.','Forest Area, Barangay Pansol, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_170723.png','2025-12-09 09:07:38.157874','2025-12-09 09:07:38.157874',9,1),
('Uncollected Waste in Residential Area','Trash not picked up. Smells bad.','Residential Area, Barangay Tangob, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_170850.png','2025-12-09 09:09:00.940974','2025-12-09 09:09:00.940974',1,1),
('Erosion Along Riverbank','Riverbank is washing away.','Riverbank, Barangay Maugat, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_171626.png','2025-12-09 09:16:42.513008','2025-12-09 09:16:42.513008',9,1),
('Air Pollution from Factory','Factory makes too much smoke. Hard to breathe.','Barangay Bawi, Padre Garcia, Batangas','/uploads/Screenshot_2025-12-09_171954.png','2025-12-09 09:20:09.275203','2025-12-09 09:20:09.275203',3,1);


-- Reset Sequences
SELECT setval('public.categories_id_seq', (SELECT MAX(id) FROM public.categories), true);
SELECT setval('public.reports_id_seq', (SELECT MAX(id) FROM public.reports), true);
SELECT setval('public.statuses_id_seq', (SELECT MAX(id) FROM public.statuses), true);
