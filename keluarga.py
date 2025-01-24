import streamlit as st
import heapq
import mysql.connector
import time  # Untuk pengukuran waktu eksekusi

"""
Anggota Kelompok :
Aditya Sendy Ardiansyah (32602200030)
Iven Aurananta Damaivila (32602200013)
Nicho Aditya Yudhistira (32602200112)
Uday Akhmal Firmansyah(32602200128)
Helmi Septianto (32602200074)
"""

# Fungsi untuk mengambil data dari database
def get_family_tree():
    # Koneksi ke database MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='root',  # Ganti dengan username MySQL Anda
        password='',  # Ganti dengan password MySQL Anda
        database='keluarga'
    )
    
    cursor = conn.cursor()
    cursor.execute("SELECT parent, child, cost FROM family_tree")
    
    # Membuat graph dari data yang diambil
    family_tree = {}
    for parent, child, cost in cursor.fetchall():
        if parent not in family_tree:
            family_tree[parent] = []
        family_tree[parent].append((child, cost))
        
        # Ensure all child nodes are also in the family_tree
        if child not in family_tree:
            family_tree[child] = []
    
    cursor.close()
    conn.close()
    
    return family_tree

# Fungsi untuk algoritma A* (Heuristic Search) dengan pengukuran waktu dan simpul eksplorasi
def a_star_search(family_tree, start, goal, heuristic):
    start_time = time.time()  # Mulai hitung waktu
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    
    g_score = {node: float('inf') for node in family_tree}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in family_tree}
    f_score[start] = heuristic.get(start, float('inf'))  # Gunakan heuristic.get untuk menghindari KeyError
    
    explored_nodes = 0  # Inisialisasi penghitung simpul yang dieksplorasi

    while open_list:
        current = heapq.heappop(open_list)[1]
        explored_nodes += 1  # Tambah hitungan simpul yang dieksplorasi
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            execution_time = time.time() - start_time
            return path[::-1], explored_nodes, execution_time

        for neighbor, cost in family_tree.get(current, []):
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic.get(neighbor, float('inf'))
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    execution_time = time.time() - start_time
    return None, explored_nodes, execution_time

# Fungsi untuk Breadth-First Search (Blind Search) dengan pengukuran waktu dan simpul eksplorasi
def blind_search(family_tree, start, goal):
    start_time = time.time()  # Mulai hitung waktu
    queue = [(start, [start])]
    explored_nodes = 0  # Inisialisasi penghitung simpul yang dieksplorasi
    
    while queue:
        (current, path) = queue.pop(0)
        explored_nodes += 1  # Tambah hitungan simpul yang dieksplorasi
        if current == goal:
            execution_time = time.time() - start_time
            return path, explored_nodes, execution_time
        for neighbor, _ in family_tree.get(current, []):
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    
    execution_time = time.time() - start_time
    return None, explored_nodes, execution_time

# Fungsi utama untuk Streamlit GUI
def main():
    st.title("Aplikasi Pencarian Silsilah Keluarga")

    # Ambil data silsilah dari database
    family_tree = get_family_tree()

    # Pilihan metode pencarian
    search_type = st.sidebar.selectbox("Pilih Metode Pencarian", ["Blind Search", "Heuristic Search"])

    # Input node awal dan tujuan
    start_node = st.text_input("Masukkan Anggota Keluarga (Awal):", "")
    goal_node = st.text_input("Masukkan Anggota Keluarga (Tujuan):", "")

    # Heuristic (untuk A*), kustomisasi
    heuristic = {
    "Qushay": 5,
    "Abdul Manaf": 3,
    "Khasim": 2,
    "Abdul Mutalib": 1,
    "Muhammad": 0  # "Muhammad" sebagai tujuan
    }

    # Tombol untuk mulai pencarian
    if st.button("Cari Jalur"):
        if search_type == "Blind Search":
            path, explored_nodes, execution_time = blind_search(family_tree, start_node, goal_node)
            if path:
                st.success(f"Jalur ditemukan dengan Blind Search (BFS) : {' -> '.join(path)}")
                st.info(f"Jumlah simpul yang dieksplorasi: {explored_nodes}")
                st.info(f"Waktu eksekusi: {execution_time:.6f} detik")
            else:
                st.error("Jalur tidak ditemukan.")

        elif search_type == "Heuristic Search":
            path, explored_nodes, execution_time = a_star_search(family_tree, start_node, goal_node, heuristic)
            if path:
                st.success(f"Jalur ditemukan dengan Heuristic Search (A*) : {' -> '.join(path)}")
                st.info(f"Jumlah simpul yang dieksplorasi: {explored_nodes}")
                st.info(f"Waktu eksekusi: {execution_time:.6f} detik")
            else:
                st.error("Jalur tidak ditemukan.")

if __name__ == "__main__":
    main()
