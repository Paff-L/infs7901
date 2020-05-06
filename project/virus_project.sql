-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 06, 2020 at 06:13 AM
-- Server version: 5.7.28-0ubuntu0.18.04.4
-- PHP Version: 7.2.24-0ubuntu0.18.04.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `virus_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `Area`
--

CREATE TABLE `Area` (
  `AreaID` int(11) NOT NULL,
  `Latitude` decimal(10,8) DEFAULT NULL,
  `Longitude` decimal(11,8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Area`
--

INSERT INTO `Area` (`AreaID`, `Latitude`, `Longitude`) VALUES
(2, '-27.48483139', '153.03616652'),
(3, '-37.81866339', '144.98332940'),
(4, '-27.49199803', '153.00766664'),
(5, '-33.85416325', '151.20916583'),
(6, '-33.85597991', '151.20666584'),
(8, '-35.10210000', '139.14240000'),
(9, '-33.86982985', '151.20433252'),
(10, '-33.84166330', '151.05799977'),
(11, '-42.00000000', '147.00000000');

-- --------------------------------------------------------

--
-- Table structure for table `Contracted`
--

CREATE TABLE `Contracted` (
  `PatientID` int(11) NOT NULL,
  `VirusID` int(11) NOT NULL,
  `ContractDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Contracted`
--

INSERT INTO `Contracted` (`PatientID`, `VirusID`, `ContractDate`) VALUES
(1, 1, '2020-02-05'),
(1, 2, '2020-01-08'),
(7, 1, '2020-01-23'),
(9, 1, '2020-01-19'),
(2, 1, '2020-02-08'),
(3, 1, '2020-03-04'),
(4, 1, '2020-03-19'),
(5, 1, '2020-01-31'),
(6, 1, '2020-02-18'),
(8, 1, '2020-04-02'),
(10, 1, '2020-02-25');

-- --------------------------------------------------------

--
-- Table structure for table `Event`
--

CREATE TABLE `Event` (
  `AreaID` int(11) NOT NULL,
  `Name` varchar(64) DEFAULT NULL,
  `TotalVisitors` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Event`
--

INSERT INTO `Event` (`AreaID`, `Name`, `TotalVisitors`) VALUES
(2, '1st Test: Australia v Pakistan (d1)', 13561),
(3, 'AFL: Richmond d Carlton', 21000),
(5, 'Ludovico Einaudi | 20 & 21 Jan', 3577),
(10, 'NRL: Rabbitohs d Sharks', 6235);

-- --------------------------------------------------------

--
-- Table structure for table `HighRiskContact`
--

CREATE TABLE `HighRiskContact` (
  `ContactID` int(11) NOT NULL,
  `PatientID` int(11) NOT NULL,
  `FirstName` varchar(32) DEFAULT NULL,
  `LastName` varchar(32) DEFAULT NULL,
  `Gender` enum('m','f') DEFAULT NULL,
  `State` varchar(32) DEFAULT NULL,
  `Postcode` varchar(16) DEFAULT NULL,
  `PhoneNumber` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `HighRiskContact`
--

INSERT INTO `HighRiskContact` (`ContactID`, `PatientID`, `FirstName`, `LastName`, `Gender`, `State`, `Postcode`, `PhoneNumber`) VALUES
(1, 1, 'Yuri', 'Thompson', 'f', 'Queensland', '4350', '0404638492'),
(2, 1, 'Roland', 'Thompson', 'm', 'Queensland', '4350', '0746356208'),
(3, 1, 'Jesse', 'Brock', 'm', 'South Australia', '5000', '0882530494'),
(4, 2, 'Jessica', 'Masters', 'f', 'New South Wales', '2000', '0281035235'),
(5, 2, 'Alexis', 'Guy', 'm', 'New South Wales', '2000', '0286491522'),
(6, 4, 'Samantha', 'Kaw', 'f', 'Western Australia', '6743', '0890728189'),
(7, 5, 'Hayley', 'Rimmer', 'f', 'New South Wales', '2551', '0240345203'),
(8, 5, 'Madeline', 'George', 'f', 'New South Wales', '2424', '0249769134'),
(9, 5, 'Charlie', 'Mead', 'm', 'New South Wales', '2800', '0240020278'),
(10, 5, 'Taj', 'Neumayer', 'm', 'New South Wales', '2836', '0240070037'),
(11, 5, 'Noah', 'Livingston', 'm', 'New South Wales', '2790', '0240000554'),
(12, 6, 'Savannah', 'Styles', 'f', 'Queensland', '4600', '0753200261'),
(13, 6, 'Dylan', 'Bage', 'm', 'Queensland', '4740', '0749393657'),
(14, 7, 'Maya', 'Rudd', 'f', 'Tasmania', '7304', '0362437766'),
(15, 9, 'Archer', 'Braund', 'm', 'South Australia', '5000', '0882092021'),
(16, 10, 'Anthony', 'Leane', 'm', 'Victoria', '3871', '0353156250'),
(17, 10, 'Tayla', 'Sinclaire', 'f', 'Victoria', '3707', '0353244344'),
(18, 10, 'Sean', 'Archibald', 'm', 'Victoria', '3764', '0387977897');

-- --------------------------------------------------------

--
-- Table structure for table `Location`
--

CREATE TABLE `Location` (
  `AreaID` int(11) NOT NULL,
  `Name` varchar(32) DEFAULT NULL,
  `AvgVisitors` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Location`
--

INSERT INTO `Location` (`AreaID`, `Name`, `AvgVisitors`) VALUES
(4, 'University of Queensland', 9000),
(6, 'International Towers Sydney 1', 4650),
(8, 'Monarto Zoo', 1600),
(9, 'Hilton Hotel Sydney', 200),
(11, 'MONA', 950);

-- --------------------------------------------------------

--
-- Table structure for table `Patient`
--

CREATE TABLE `Patient` (
  `PatientID` int(11) NOT NULL,
  `FirstName` varchar(32) NOT NULL,
  `LastName` varchar(32) NOT NULL,
  `Gender` enum('m','f') NOT NULL,
  `Nationality` varchar(32) DEFAULT NULL,
  `State` varchar(32) DEFAULT NULL,
  `Postcode` int(4) DEFAULT NULL,
  `DOB` date NOT NULL,
  `PhoneNumber` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Patient`
--

INSERT INTO `Patient` (`PatientID`, `FirstName`, `LastName`, `Gender`, `Nationality`, `State`, `Postcode`, `DOB`, `PhoneNumber`) VALUES
(1, 'Roland', 'Thompson', 'm', 'Australian', 'Queensland', 4170, '1995-09-29', '0411111111'),
(2, 'Mary', 'Winchester', 'f', 'American', 'New South Wales', 2453, '1978-05-18', '0267586000'),
(3, 'Harry', 'Farrar', 'm', 'Australian', 'Northern Territory', 810, '1980-07-31', '0889928309'),
(4, 'Isla', 'Maiden', 'f', 'Canadian', 'Western Australia', 6630, '1995-03-05', '0890917711'),
(5, 'Aidan', 'Isles', 'm', 'English', 'New South Wales', 2872, '1968-04-27', '0282567682'),
(6, 'Eliza', 'Gopinko', 'f', 'Australian', 'Queensland', 4610, '1977-04-07', '0745474645'),
(7, 'Zhong', 'Yang', 'm', 'Chinese', 'Tasmania', 7252, '1979-10-22', '0362773241'),
(8, 'Darcy', 'Lanigan', 'm', 'Australian', 'Queensland', 4352, '1996-12-02', '0745047217'),
(9, 'Lin', 'Wen', 'f', 'Chinese', 'South Australia', 5253, '1985-05-08', '0882785599'),
(10, 'Hannah', 'Hardwick', 'f', 'American', 'Victoria', 3517, '1988-03-27', '0353899611');

-- --------------------------------------------------------

--
-- Table structure for table `Transport`
--

CREATE TABLE `Transport` (
  `TransportID` int(11) NOT NULL,
  `TransportType` varchar(16) DEFAULT NULL,
  `StartLocation` varchar(64) DEFAULT NULL,
  `EndLocation` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Transport`
--

INSERT INTO `Transport` (`TransportID`, `TransportType`, `StartLocation`, `EndLocation`) VALUES
(1, 'Airplane', 'Wuhan Tianhe International Airport', 'Sydney Airport'),
(2, 'Airplane', 'Sydney Airport', 'Hobart Airport'),
(3, 'Airplane', 'Sydney Airport', 'Adelaide Airport'),
(4, 'Bus', 'Adelaide Airport', 'Begley Street Busstop'),
(5, 'Train', 'Norman Park Station', 'Park Road Station'),
(6, 'Bus', 'Boggo Road', 'UQ Lakes'),
(7, 'Train', 'Ashfield Station', 'ANZ Stadium Station'),
(8, 'Train', 'Cheltenham Station', 'Flinders Street Station');

-- --------------------------------------------------------

--
-- Table structure for table `Virus`
--

CREATE TABLE `Virus` (
  `VirusID` int(11) NOT NULL,
  `Name` varchar(32) DEFAULT NULL,
  `LastOutbreak` int(11) DEFAULT NULL,
  `Symptoms` varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Virus`
--

INSERT INTO `Virus` (`VirusID`, `Name`, `LastOutbreak`, `Symptoms`) VALUES
(1, 'SARS-CoV-2', 2019, 'Fever, cough, shortness of breath'),
(2, 'SARS-CoV-1', 2003, 'Fever, dry cough, headache, muscle aches, shortness of breath'),
(3, 'Swine Influenza', 2009, 'Fever, cough, sore throat, chills, sneezing, runny nose'),
(4, 'Avian influenza', 1918, 'Fever, cough, sore throat, headache, fatigue');

-- --------------------------------------------------------

--
-- Table structure for table `Visited`
--

CREATE TABLE `Visited` (
  `VisitID` int(11) NOT NULL,
  `PatientID` int(11) NOT NULL,
  `TransportID` int(11) DEFAULT NULL,
  `AreaID` int(11) NOT NULL,
  `StartTime` datetime DEFAULT NULL,
  `EndTime` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Visited`
--

INSERT INTO `Visited` (`VisitID`, `PatientID`, `TransportID`, `AreaID`, `StartTime`, `EndTime`) VALUES
(1, 1, 5, 4, '2020-03-01 08:00:00', '2020-03-01 12:00:00'),
(2, 1, 6, 4, '2020-03-01 08:00:00', '2020-03-01 12:00:00'),
(3, 2, 7, 10, '2020-03-14 15:30:00', '2020-03-14 21:00:00'),
(4, 5, 7, 10, '2020-03-14 16:00:00', '2020-03-14 22:30:00'),
(5, 6, NULL, 2, '2020-01-21 09:00:00', '2020-01-21 18:00:00'),
(8, 2, 7, 10, '2020-03-14 15:30:00', '2020-03-14 21:00:00'),
(9, 5, 7, 10, '2020-03-14 16:00:00', '2020-03-14 22:30:00'),
(10, 6, NULL, 2, '2020-01-21 09:00:00', '2020-01-21 18:00:00'),
(11, 6, NULL, 4, NULL, NULL),
(12, 7, 2, 11, '2020-02-28 13:25:00', '2020-02-28 19:30:00'),
(13, 9, 3, 8, NULL, NULL),
(14, 10, 8, 3, '2020-03-19 18:00:00', '2020-03-19 22:45:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Area`
--
ALTER TABLE `Area`
  ADD PRIMARY KEY (`AreaID`);

--
-- Indexes for table `Contracted`
--
ALTER TABLE `Contracted`
  ADD KEY `PatientID` (`PatientID`),
  ADD KEY `VirusID` (`VirusID`);

--
-- Indexes for table `Event`
--
ALTER TABLE `Event`
  ADD KEY `AreaID` (`AreaID`);

--
-- Indexes for table `HighRiskContact`
--
ALTER TABLE `HighRiskContact`
  ADD PRIMARY KEY (`ContactID`),
  ADD KEY `PatientID` (`PatientID`);

--
-- Indexes for table `Location`
--
ALTER TABLE `Location`
  ADD KEY `AreaID` (`AreaID`);

--
-- Indexes for table `Patient`
--
ALTER TABLE `Patient`
  ADD PRIMARY KEY (`PatientID`);

--
-- Indexes for table `Transport`
--
ALTER TABLE `Transport`
  ADD PRIMARY KEY (`TransportID`);

--
-- Indexes for table `Virus`
--
ALTER TABLE `Virus`
  ADD PRIMARY KEY (`VirusID`);

--
-- Indexes for table `Visited`
--
ALTER TABLE `Visited`
  ADD PRIMARY KEY (`VisitID`),
  ADD KEY `PatientID` (`PatientID`),
  ADD KEY `TransportID` (`TransportID`),
  ADD KEY `AreaID` (`AreaID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Area`
--
ALTER TABLE `Area`
  MODIFY `AreaID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT for table `HighRiskContact`
--
ALTER TABLE `HighRiskContact`
  MODIFY `ContactID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
--
-- AUTO_INCREMENT for table `Patient`
--
ALTER TABLE `Patient`
  MODIFY `PatientID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `Transport`
--
ALTER TABLE `Transport`
  MODIFY `TransportID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `Virus`
--
ALTER TABLE `Virus`
  MODIFY `VirusID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `Visited`
--
ALTER TABLE `Visited`
  MODIFY `VisitID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `Contracted`
--
ALTER TABLE `Contracted`
  ADD CONSTRAINT `Contracted_ibfk_1` FOREIGN KEY (`PatientID`) REFERENCES `Patient` (`PatientID`),
  ADD CONSTRAINT `Contracted_ibfk_2` FOREIGN KEY (`VirusID`) REFERENCES `Virus` (`VirusID`);

--
-- Constraints for table `Event`
--
ALTER TABLE `Event`
  ADD CONSTRAINT `Event_ibfk_1` FOREIGN KEY (`AreaID`) REFERENCES `Area` (`AreaID`);

--
-- Constraints for table `HighRiskContact`
--
ALTER TABLE `HighRiskContact`
  ADD CONSTRAINT `HighRiskContact_ibfk_1` FOREIGN KEY (`PatientID`) REFERENCES `Patient` (`PatientID`);

--
-- Constraints for table `Location`
--
ALTER TABLE `Location`
  ADD CONSTRAINT `Location_ibfk_1` FOREIGN KEY (`AreaID`) REFERENCES `Area` (`AreaID`);

--
-- Constraints for table `Visited`
--
ALTER TABLE `Visited`
  ADD CONSTRAINT `Visited_ibfk_1` FOREIGN KEY (`PatientID`) REFERENCES `Patient` (`PatientID`),
  ADD CONSTRAINT `Visited_ibfk_2` FOREIGN KEY (`TransportID`) REFERENCES `Transport` (`TransportID`),
  ADD CONSTRAINT `Visited_ibfk_3` FOREIGN KEY (`AreaID`) REFERENCES `Area` (`AreaID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
