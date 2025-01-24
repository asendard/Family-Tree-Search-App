-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 09 Okt 2024 pada 15.49
-- Versi server: 10.4.22-MariaDB
-- Versi PHP: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `keluarga`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `family_tree`
--

CREATE TABLE `family_tree` (
  `id` int(11) NOT NULL,
  `parent` varchar(50) DEFAULT NULL,
  `child` varchar(50) DEFAULT NULL,
  `cost` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `family_tree`
--

INSERT INTO `family_tree` (`id`, `parent`, `child`, `cost`) VALUES
(1, 'NULL', 'Qushay', 1),
(2, 'Qushay', 'Abdul Uzza', 1),
(3, 'Qushay', 'Abdul Manaf', 1),
(4, 'Qushay', 'Abdul Dar', 1),
(5, 'Abdul Uzza', 'Asad', 1),
(6, 'Abdul Manaf', 'Muthalib', 1),
(7, 'Abdul Manaf', 'Hasyim', 1),
(8, 'Abdul Manaf', 'Noufal', 1),
(9, 'Abdul Manaf', 'Abdu Syams', 1),
(10, 'Asad', 'Khuwailid', 1),
(11, 'Hasyim', 'Abdul Muthalib', 1),
(12, 'Abdu Syams', 'Umayyah', 1),
(13, 'Khuwailid', 'Awwam', 1),
(14, 'Khuwailid', 'Khadijah', 1),
(15, 'Abdul Muthalib', 'Hamzah', 1),
(16, 'Abdul Muthalib', 'Abbas', 1),
(17, 'Abdul Muthalib', 'Abdullah', 1),
(18, 'Abdul Muthalib', 'Abu Lahab', 1),
(19, 'Abdul Muthalib', 'Abu Thalib', 1),
(20, 'Abdul Muthalib', 'Harits', 1),
(21, 'Awwam', 'Zubair', 1),
(22, 'Abdullah', 'Muhammad', 1),
(23, 'Abu Thalib', 'Aqil', 1),
(24, 'Abu Thalib', 'Ali', 1),
(25, 'Abu Thalib', 'Jafar', 1),
(26, 'Umayyah', 'Harb', 1),
(27, 'Aqil', 'Muslim', 1),
(28, 'Ali', 'Hasan', 1),
(29, 'Ali', 'Husain', 1),
(30, 'Harb', 'Abu Sufyan', 1),
(31, 'Abu Sufyan', 'Muawiyah', 1);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `family_tree`
--
ALTER TABLE `family_tree`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `family_tree`
--
ALTER TABLE `family_tree`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
