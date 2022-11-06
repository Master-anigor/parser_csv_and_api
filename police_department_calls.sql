SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";

CREATE TABLE `police_department_calls` (
  `crime_id` int(11) NOT NULL,
  `crime_type` varchar(255) NOT NULL,
  `report_date` datetime NOT NULL,
  `call_date` datetime NOT NULL,
  `offense_date` datetime NOT NULL,
  `call_time` varchar(5) NOT NULL,
  `call_date_time` datetime NOT NULL,
  `disposition` varchar(255) NOT NULL,
  `address` text NOT NULL,
  `city` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `agency_Id` int(11) NOT NULL,
  `address_type` varchar(255) NOT NULL,
  `common_location` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `police_department_calls`
  ADD PRIMARY KEY (`crime_id`);
