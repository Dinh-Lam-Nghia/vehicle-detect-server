-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Jan 14, 2024 at 01:17 PM
-- Server version: 5.7.39
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vehicle_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `email`, `password`) VALUES
(1, 'pxhiep.19it3@vku.udn.vn', '456a27917d02f68e90e85e85dba8cee1');

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

CREATE TABLE `log` (
  `id` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `time` varchar(30) NOT NULL,
  `vehicle_id` int(11) NOT NULL,
  `role` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `log`
--

INSERT INTO `log` (`id`, `status`, `time`, `vehicle_id`, `role`) VALUES
(33, 0, '2024-01-01 10:00:00', 3, 0),
(34, 0, '2024-02-01 12:00:00', 4, 0),
(35, 0, '2024-03-01 08:00:00', 5, 0),
(36, 0, '2024-04-01 02:00:00', 6, 0),
(37, 1, '2024-05-01 06:00:00', 1, 1),
(38, 1, '2024-06-01 15:00:00', 2, 1),
(47, 1, '2024-01-07 02:44:22', 3, 1),
(52, 0, '2024-01-07 02:44:22', 3, 1),
(53, 0, '2024-01-13 08:10:25', 3, 0),
(55, 1, '2024-01-13 08:11:26', 3, 0),
(60, 0, '2024-01-13 08:22:45', 3, 0),
(61, 1, '2024-01-13 08:22:51', 3, 0),
(62, 0, '2024-01-13 09:14:29', 3, 0),
(63, 1, '2024-01-13 09:15:15', 3, 0),
(64, 0, '2024-01-13 09:15:23', 3, 0),
(65, 0, '2024-01-13 09:16:09', 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(100) NOT NULL,
  `url_photo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `email`, `url_photo`) VALUES
(3, 'Phan Xuân Hiệp', 'hiepphan197420@gmail.com', 'https://lh3.googleusercontent.com/a/ACg8ocI4ovUmVOMoKrikkItYmqN0-b5pye0DJBOKgZgj5z7XSVA=s96-c'),
(13, 'Hiệp Phan Xuân', 'pxhiep.19it3@vku.udn.vn', 'https://lh3.googleusercontent.com/a/ACg8ocKS6yHp9MC4ycDjQ2pPWIaogqbOeh7oYr_EubEH4f2g=s96-c');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle`
--

CREATE TABLE `vehicle` (
  `id` int(10) NOT NULL,
  `vehicle_id` varchar(100) NOT NULL,
  `role` tinyint(1) NOT NULL,
  `vehicle_model` varchar(50) NOT NULL,
  `vehicle_color` varchar(50) NOT NULL,
  `vehicle_type` tinyint(1) NOT NULL,
  `expires` varchar(10) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '0',
  `phone` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `vehicle`
--

INSERT INTO `vehicle` (`id`, `vehicle_id`, `role`, `vehicle_model`, `vehicle_color`, `vehicle_type`, `expires`, `user_id`, `active`, `phone`) VALUES
(3, '43A58036', 1, 'Wave', '0xffff004d', 0, '2024-01-26', 3, 0, '+84346056590'),
(4, '77K58536', 1, 'Sirius', '0xff0802A33', 1, '2023-12-31', 3, 0, '+84346056590'),
(5, '43E157246', 1, 'Honda', '0xff864af9', 1, '2024-11-25', 3, 0, '+84346056590'),
(6, '51G79984', 0, 'Vision', '0xff2196f3', 1, '2024-01-27', 3, 0, '+84346056590'),
(7, '77h58836', 0, 'wave', '0xfff44336', 1, '2024-02-13', 3, 0, '+84346056590');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_staff`
--

CREATE TABLE `vehicle_staff` (
  `id` int(11) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `vehicle_id` varchar(250) NOT NULL,
  `expires` varchar(12) NOT NULL,
  `role` tinyint(1) NOT NULL,
  `name` varchar(255) NOT NULL,
  `vehicle_model` varchar(255) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `vehicle_staff`
--

INSERT INTO `vehicle_staff` (`id`, `phone`, `vehicle_id`, `expires`, `role`, `name`, `vehicle_model`, `active`) VALUES
(1, '+84346056590', '43A23789', '2023-10-20', 0, 'Phan Trường Huy', 'Honda', 0),
(2, '+84346056590', '43A34108', '2024-10-20', 1, 'Nguyễn Văn A', 'Honda', 0),
(3, '+84346056590', '51G79984', '2024-01-26', 1, 'Nguyễn Văn B', 'BMW', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `log`
--
ALTER TABLE `log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vehicle`
--
ALTER TABLE `vehicle`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_user_vehicle` (`user_id`);

--
-- Indexes for table `vehicle_staff`
--
ALTER TABLE `vehicle_staff`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `log`
--
ALTER TABLE `log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `vehicle`
--
ALTER TABLE `vehicle`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `vehicle_staff`
--
ALTER TABLE `vehicle_staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `vehicle`
--
ALTER TABLE `vehicle`
  ADD CONSTRAINT `FK_user_vehicle` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
