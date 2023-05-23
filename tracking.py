import math


# Mendefinisikan kelas EuclideanDistTracker yang akan digunakan untuk melacak objek.
class EuclideanDistTracker:
    # Metode konstruktor kelas EuclideanDistTracker yang akan dipanggil saat objek dari kelas ini dibuat. Di dalam metode ini, terdapat beberapa inisialisasi variabel.
    def __init__(self):
        # Simpan di posisi tengah objek dari setiap objek yang terdeteksi
        self.center_points = {}

        self.id_count = 0  # Pertahankan jumlah ID
        # setiap kali id ​​objek baru terdeteksi, hitungannya akan bertambah satu

    # Digunakan untuk memperbarui pemantauan objek berdasarkan persegi panjang yang diinputkan sebagai
    def update(self, objects_rect):
        # Metode ini akan mengembalikan daftar persegi panjang objek beserta ID objek yang terdeteksi.
        # Kotak objek dan id
        objects_bbs_ids = []
        # digunakan untuk menyimpan persegi panjang objek dan ID objek yang terdeteksi.

        # Mendapatkan titik pusat objek baru
        for rect in objects_rect:
            x, y, w, h = rect
            # Memecah persegi panjang objek menjadi empat variabel x, y, w, dan h, yang mewakili koordinat pojok kiri atas serta lebar dan tinggi persegi panjang tersebut.
            # Menghitung koordinat X titik tengah objek dengan menjumlahkan koordinat X awal dan akhir persegi panjang dan membagi hasilnya dengan 2.
            cx = (x + x + w) // 2
            # Menghitung koordinat Y titik tengah objek dengan menjumlahkan koordinat Y awal dan akhir persegi panjang dan membagi hasilnya dengan 2.
            cy = (y + y + h) // 2

            # Mencari tahu apakah objek itu sudah terdeteksi
            same_object_detected = False
            for id, pt in self.center_points.items():
                # Melakukan iterasi untuk setiap pasangan kunci-nilai dalam center_points, yang mewakili ID objek dan posisi tengahnya.
                dist = math.hypot(cx - pt[0], cy - pt[1])
                # Menghitung jarak Euclidean antara posisi tengah objek yang baru terdeteksi (cx, cy) dan posisi tengah objek yang sudah ada dalam center_points (pt[0], pt[1]).

                if dist < 25:
                    # Memperbarui posisi tengah objek yang sudah ada dalam center_points dengan posisi tengah objek yang baru terdeteksi.
                    self.center_points[id] = (cx, cy)
                    print(self.center_points)
                    # Menambahkan persegi panjang objek beserta ID objek ke dalam objects_bbs_ids.
                    objects_bbs_ids.append([x, y, w, h, id])
                    # untuk menandakan bahwa objek yang sama telah terdeteksi.
                    same_object_detected = True
                    break
                    # Menghentikan iterasi karena objek yang sama telah ditemukan.

            # Objek baru terdeteksi, kami menetapkan ID ke objek itu
            if same_object_detected is False:
                # Menambahkan posisi tengah objek yang baru terdeteksi ke dalam center_points dengan ID baru
                self.center_points[self.id_count] = (cx, cy)
                # Menambahkan persegi panjang objek beserta ID objek baru ke dalam objects_bbs_ids.
                objects_bbs_ids.append([x, y, w, h, self.id_count])
                # Menambahkan nilai self.id_count untuk mempersiapkan ID berikutnya untuk objek baru.
                self.id_count += 1

        # Clear dictionary dengan titik tengah untuk menghapus IDS yang tidak digunakan lagi
        new_center_points = {}
        # embuat dictionary new_center_points kosong yang akan digunakan untuk menyimpan posisi tengah objek yang masih terdeteksi.
        for obj_bb_id in objects_bbs_ids:
            #  Memecah elemen-elemen dalam objects_bbs_ids menjadi lima variabel, dengan object_id sebagai ID objek.
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        # Menambahkan posisi tengah objek ke dalam new_center_points berdasarkan ID objek.
        self.center_points = new_center_points.copy()
        # Memperbarui center_points dengan new_center_points setelah menghapus ID objek yang tidak digunakan lagi
        return objects_bbs_ids
        # Mengembalikan daftar persegi panjang objek beserta ID objek yang terdeteksi.
