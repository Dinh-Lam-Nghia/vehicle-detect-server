-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: localhost:3306
-- Thời gian đã tạo: Th5 11, 2024 lúc 07:39 AM
-- Phiên bản máy phục vụ: 8.0.30
-- Phiên bản PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `vehicle_db`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `admin`
--

CREATE TABLE `admin` (
  `id` int NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Đang đổ dữ liệu cho bảng `admin`
--

INSERT INTO `admin` (`id`, `email`, `password`) VALUES
(1, 'admin', '21232f297a57a5a743894a0e4a801fc3');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `log`
--

CREATE TABLE `log` (
  `id` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  `time` varchar(30) NOT NULL,
  `vehicle_id` varchar(255) NOT NULL,
  `role` tinyint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Đang đổ dữ liệu cho bảng `log`
--

INSERT INTO `log` (`id`, `status`, `time`, `vehicle_id`, `role`) VALUES
(33, 0, '2024-01-01 10:00:00', '43A23789', 1),
(34, 0, '2024-02-01 12:00:00', '43A34108', 0),
(35, 0, '2024-03-01 08:00:00', '51G79984', 0),
(36, 0, '2024-04-01 02:00:00', '77K58536', 0),
(37, 1, '2024-05-01 06:00:00', '43A23789', 1),
(38, 1, '2024-06-01 15:00:00', '43A34108', 1),
(47, 1, '2024-01-07 02:44:22', '51G79984', 1),
(52, 0, '2024-01-07 02:44:22', '77K58536', 0),
(53, 0, '2024-01-13 08:10:25', '99h7-7060', 0),
(55, 1, '2024-01-13 08:11:26', '29aa-03194', 0),
(60, 0, '2024-01-13 08:22:45', '59v1-79379', 0),
(61, 1, '2024-01-13 08:22:51', '77h58836', 0),
(65, 0, '2024-01-13 09:16:09', '99h7-7060', 0),
(69, 0, '2024-05-11 13:37:14', '29aa-03194', 0),
(70, 1, '2024-05-11 13:37:51', '29aa-03194', 0),
(71, 0, '2024-05-11 13:38:12', '29aa-03194', 0);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `user`
--

CREATE TABLE `user` (
  `id` int NOT NULL,
  `name` text NOT NULL,
  `email` varchar(100) NOT NULL,
  `url_photo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Đang đổ dữ liệu cho bảng `user`
--

INSERT INTO `user` (`id`, `name`, `email`, `url_photo`) VALUES
(3, 'Phan Xuân Hiệp', 'hiepphan197420@gmail.com', 'https://lh3.googleusercontent.com/a/ACg8ocI4ovUmVOMoKrikkItYmqN0-b5pye0DJBOKgZgj5z7XSVA=s96-c'),
(13, 'Hiệp Phan Xuân', 'pxhiep.19it3@vku.udn.vn', 'https://lh3.googleusercontent.com/a/ACg8ocKS6yHp9MC4ycDjQ2pPWIaogqbOeh7oYr_EubEH4f2g=s96-c'),
(14, 'ao may', 'mayao.mayao123@gmail.com', 'https://lh3.googleusercontent.com/a/ACg8ocIrRszE2xuiBTPJlWi1Rs9tSVHTKQTxiWMrvZRdGHaWDXrVKQ=s96-c');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `vehicle`
--

CREATE TABLE `vehicle` (
  `id` int NOT NULL,
  `vehicle_id` varchar(100) NOT NULL,
  `role` tinyint(1) NOT NULL,
  `vehicle_model` varchar(50) NOT NULL,
  `vehicle_color` varchar(50) NOT NULL,
  `vehicle_type` tinyint(1) NOT NULL,
  `expires` varchar(10) DEFAULT NULL,
  `user_id` int NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '0',
  `phone` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Đang đổ dữ liệu cho bảng `vehicle`
--

INSERT INTO `vehicle` (`id`, `vehicle_id`, `role`, `vehicle_model`, `vehicle_color`, `vehicle_type`, `expires`, `user_id`, `active`, `phone`) VALUES
(3, '43A58036', 1, 'Wave', '0xffff004d', 0, '2024-01-26', 3, 0, '+84346056590'),
(4, '77K58536', 1, 'Sirius', '0xff0802A33', 1, '2023-12-31', 3, 0, '+84346056590'),
(5, '43E157246', 1, 'Honda', '0xff864af9', 1, '2024-11-25', 3, 0, '+84346056590'),
(6, '51G79984', 0, 'Vision', '0xff2196f3', 1, '2024-01-27', 3, 0, '+84346056590'),
(7, '77h58836', 0, 'wave', '0xfff44336', 1, '2024-02-13', 3, 0, '+84346056590'),
(10, '59v1-79379', 0, 'ex', '0xffff0000', 1, '2024-05-31', 14, 1, '+84386002562'),
(11, '99h7-7060', 0, 'wave', '0xffff0000', 1, '2024-05-31', 14, 1, '+84386002562'),
(12, '59v1-79379', 0, 'a', '0xffff0000', 1, '2024-05-06', 14, 1, '+84386002562'),
(13, '99h7-7060', 0, 'ab', '0xffff0000', 1, '2024-05-06', 14, 1, '+84386002562'),
(15, '324324', 0, 'wa', '0xffff5722', 1, '2024-05-12', 14, 0, '+84787572931'),
(17, '29aa-31294', 0, 'finalColor', '0xff3f51b5', 1, '2024-05-07', 14, 0, '+84787572931'),
(19, '82b1-39748', 0, 'h', '0xffff6e40', 1, '2024-05-08', 14, 0, '+84386002562'),
(22, '29aa-03194', 1, 'a', '0xff2196f3', 1, '2024-05-10', 14, 0, '+84386002562');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `vehicle_staff`
--

CREATE TABLE `vehicle_staff` (
  `id` int NOT NULL,
  `phone` varchar(12) NOT NULL,
  `vehicle_id` varchar(250) NOT NULL,
  `expires` varchar(12) NOT NULL,
  `role` tinyint(1) NOT NULL,
  `name` varchar(255) NOT NULL,
  `vehicle_model` varchar(255) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Đang đổ dữ liệu cho bảng `vehicle_staff`
--

INSERT INTO `vehicle_staff` (`id`, `phone`, `vehicle_id`, `expires`, `role`, `name`, `vehicle_model`, `active`) VALUES
(1, '+84346056590', '43A23789', '2023-10-20', 0, 'Phan Trường Huy', 'Honda', 0),
(2, '+84346056590', '43A34108', '2024-10-20', 1, 'Nguyễn Văn A', 'Honda', 0),
(3, '+84346056590', '51G79984', '2024-01-26', 1, 'Nguyễn Văn B', 'BMW', 0),
(4, '+843764529', '74a1-64537', '2024-05-12', 1, 'tho', 'sirius', 1),
(5, '+843764529', '74a1-64537', '2024-05-12', 1, 'thọ', 'si', 0);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `log`
--
ALTER TABLE `log`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `vehicle`
--
ALTER TABLE `vehicle`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_user_vehicle` (`user_id`);

--
-- Chỉ mục cho bảng `vehicle_staff`
--
ALTER TABLE `vehicle_staff`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `log`
--
ALTER TABLE `log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;

--
-- AUTO_INCREMENT cho bảng `user`
--
ALTER TABLE `user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT cho bảng `vehicle`
--
ALTER TABLE `vehicle`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT cho bảng `vehicle_staff`
--
ALTER TABLE `vehicle_staff`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `vehicle`
--
ALTER TABLE `vehicle`
  ADD CONSTRAINT `FK_user_vehicle` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
