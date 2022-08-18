-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 07, 2021 at 05:32 AM
-- Server version: 10.6.0-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `car_rental_database`
--
CREATE DATABASE IF NOT EXISTS `car_rental_database` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `car_rental_database`;

-- --------------------------------------------------------

--
-- Table structure for table `cars`
--

DROP TABLE IF EXISTS `cars`;
CREATE TABLE `cars` (
  `Vehicle_ID` int(20) NOT NULL,
  `Car_Type` varchar(20) NOT NULL,
  `Make` varchar(20) NOT NULL,
  `Model` varchar(20) NOT NULL,
  `Year` int(20) NOT NULL,
  `Available` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cars`
--

INSERT INTO `cars` (`Vehicle_ID`, `Car_Type`, `Make`, `Model`, `Year`, `Available`) VALUES
(1, 'TRUCK', 'GMC', 'Sierra', 2005, 'YES'),
(2, 'MEDIUM', 'Chevrolet', 'Cruze', 2017, 'NO'),
(3, 'COMPACT', 'Honda', 'Civic', 2021, 'YES'),
(4, 'SUV', 'Acura', 'RDX', 2009, 'YES'),
(5, 'MEDIUM', 'Chevrolet', 'Malibu', 2016, 'YES'),
(6, 'SUV', 'Kia', 'Sorento', 2013, 'YES'),
(7, 'SUV', 'GMC', 'Terrain', 2013, 'YES'),
(8, 'MEDIUM', 'Toyota', 'Camry', 2018, 'YES'),
(9, 'SUV', 'Nissan', 'Rogue', 2010, 'YES'),
(10, 'TRUCK', 'Chevrolet', 'Silverado', 1995, 'YES'),
(11, 'COMPACT', 'Kia', 'Soul', 2018, 'YES'),
(12, 'SUV', 'Jeep', 'Patriot', 2016, 'NO'),
(13, 'LARGE', 'Pontiac', 'G8', 2009, 'YES'),
(14, 'COMPACT', 'Volkswagen', 'Jetta', 2019, 'YES'),
(15, 'TRUCK', 'Ford', 'F250', 2004, 'YES'),
(16, 'LARGE', 'Hyundai', 'Azera', 2010, 'YES'),
(17, 'VAN', 'Honda', 'Odyssey', 2015, 'YES'),
(18, 'VAN', 'Toyota', 'Sienna', 2010, 'YES'),
(19, 'LARGE', 'Buick', 'LaCrosse', 2011, 'YES'),
(20, 'COMPACT', 'Toyota', 'Prius', 2015, 'YES'),
(21, 'LARGE', 'Kia', 'Cadenza', 2014, 'YES'),
(22, 'MEDIUM', 'Nissan', 'Sentra', 2016, 'YES'),
(23, 'COMPACT', 'Chevrolet', 'Cruze', 2013, 'YES'),
(24, 'COMPACT', 'Chevrolet', 'Aveo', 2011, 'NO');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
CREATE TABLE `customers` (
  `Id_No` int(20) NOT NULL,
  `Name` varchar(25) NOT NULL,
  `Phone` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`Id_No`, `Name`, `Phone`) VALUES
(1, 'John Smith', '(123) 456-7890'),
(2, 'Launce Alphege', '(577) 914-1287'),
(3, 'Nina Tine', '(659) 425-6922'),
(4, 'Hania Apurva', '(950) 488-5307'),
(5, 'Florinda Casper', '(701) 614-9156'),
(6, 'Takondwa Pirkko', '(209) 498-3973'),
(7, 'Amleto Rasmus', '(978) 382-1876'),
(8, 'Adaeze Apikalia', '(428) 330-7387'),
(9, 'Liwia Eadwine', '(298) 816-6422'),
(10, 'Tyr Gregorio', '(748) 717-5916'),
(11, 'Solveig Evaristus', '(540) 702-9866'),
(12, 'Karim Kabbara', '(888) 888-8888'),
(13, 'Ronald McDonald', '(800) 244-6227');

-- --------------------------------------------------------

--
-- Table structure for table `rental`
--

DROP TABLE IF EXISTS `rental`;
CREATE TABLE `rental` (
  `Trans_ID` int(20) NOT NULL,
  `Customer_ID` int(20) NOT NULL,
  `Vehicle_ID` int(20) NOT NULL,
  `Rental_Type` varchar(20) NOT NULL,
  `Start_Date` varchar(10) NOT NULL,
  `Return_Date` varchar(10) NOT NULL,
  `Rental_Length` int(20) NOT NULL,
  `Amount_Due` float NOT NULL,
  `Rental_Status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rental`
--

INSERT INTO `rental` (`Trans_ID`, `Customer_ID`, `Vehicle_ID`, `Rental_Type`, `Start_Date`, `Return_Date`, `Rental_Length`, `Amount_Due`, `Rental_Status`) VALUES
(1, 12, 2, 'Daily', '2021-05-05', '2021-06-24', 50, 2215.62, 'Active'),
(3, 2, 12, 'Daily', '2021-05-05', '2021-05-09', 4, 254.491, 'Active'),
(4, 13, 24, 'Weekly', '2021-05-20', '2021-06-10', 21, 912.254, 'Scheduled');

--
-- Triggers `rental`
--
DROP TRIGGER IF EXISTS `rDate`;
DELIMITER $$
CREATE TRIGGER `rDate` BEFORE INSERT ON `rental` FOR EACH ROW SET new.Return_Date = date_add(new.Start_Date, INTERVAL NEW.Rental_Length DAY)
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `rentalrates`
--

DROP TABLE IF EXISTS `rentalrates`;
CREATE TABLE `rentalrates` (
  `RR_Car_Type` varchar(20) NOT NULL,
  `Effective_Date` varchar(10) NOT NULL,
  `Daily_Rate` float NOT NULL,
  `Weekly_Rate` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rentalrates`
--

INSERT INTO `rentalrates` (`RR_Car_Type`, `Effective_Date`, `Daily_Rate`, `Weekly_Rate`) VALUES
('COMPACT', '2021-05-06', 40.16, 281.56),
('LARGE', '2021-05-06', 51.89, 362.69),
('MEDIUM', '2021-04-30', 41.03, 287.25),
('SUV', '2021-05-04', 58.91, 412.25),
('TRUCK', '2021-04-30', 67.82, 474.75),
('VAN', '2021-04-30', 107.11, 749.72);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cars`
--
ALTER TABLE `cars`
  ADD PRIMARY KEY (`Vehicle_ID`),
  ADD KEY `Car_Type` (`Car_Type`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`Id_No`);

--
-- Indexes for table `rental`
--
ALTER TABLE `rental`
  ADD PRIMARY KEY (`Trans_ID`),
  ADD UNIQUE KEY `Customer_ID_3` (`Customer_ID`),
  ADD KEY `Vehicle_ID` (`Vehicle_ID`),
  ADD KEY `Customer_ID` (`Customer_ID`),
  ADD KEY `Customer_ID_2` (`Customer_ID`);

--
-- Indexes for table `rentalrates`
--
ALTER TABLE `rentalrates`
  ADD PRIMARY KEY (`RR_Car_Type`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cars`
--
ALTER TABLE `cars`
  ADD CONSTRAINT `cars_ibfk_1` FOREIGN KEY (`Car_Type`) REFERENCES `rentalrates` (`RR_Car_Type`);

--
-- Constraints for table `rental`
--
ALTER TABLE `rental`
  ADD CONSTRAINT `rental_ibfk_1` FOREIGN KEY (`Vehicle_ID`) REFERENCES `cars` (`Vehicle_ID`),
  ADD CONSTRAINT `rental_ibfk_2` FOREIGN KEY (`Customer_ID`) REFERENCES `customers` (`Id_No`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
