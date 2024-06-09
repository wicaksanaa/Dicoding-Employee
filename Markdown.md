```markdown
# Proyek Akhir: Menyelesaikan Permasalahan Human Resources

## Business Understanding
Perusahaan menghadapi tantangan dalam mempertahankan karyawan, yang terlihat dari tingginya tingkat attrition (perpindahan karyawan). Tingginya attrition dapat menyebabkan biaya tambahan untuk perekrutan dan pelatihan karyawan baru, serta potensi penurunan produktivitas. Tujuan dari proyek ini adalah untuk menganalisis faktor-faktor yang mempengaruhi attrition dan membuat model prediktif untuk mengidentifikasi karyawan yang berisiko tinggi meninggalkan perusahaan.

## Permasalahan Bisnis
1. **Tingginya Tingkat Attrition:** Perusahaan Jaya Jaya Maju memiliki attrition rate yang tinggi dimana mencapai 10%. Dimana Attrition rate yang tinggi terjadi karena masalah pengelolaan karyawan, dimana dapat memberikan efek buruk kepada perusahaan.

## Cakupan Proyek
Proyek ini mencakup beberapa aspek utama:
- **Analisis Data Karyawan:** Memahami distribusi dan karakteristik data karyawan.
- **Preprocessing Data:** Membersihkan dan mempersiapkan data untuk analisis lebih lanjut.
- **Modeling:** Membangun dan mengevaluasi model prediktif menggunakan algoritma Random Forest.
- **Visualisasi Data:** Membuat visualisasi untuk memahami pola attrition berdasarkan berbagai fitur karyawan.

## Persiapan
**Sumber data:**
- Data karyawan (employee_data.csv) - https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

**Setup environment:**
1. Buat virtual environment
python -m venv myenv

2. Aktifkan virtual environment
.\myenv\Scripts\activate

3. Install library dari requirements.txt
pip install -r requirements.txt

## Business Dashboard
Dashboard ini memberikan visualisasi mengenai distribusi attrition berdasarkan berbagai fitur seperti umur, pendapatan bulanan, lama bekerja di perusahaan, dan total pengalaman kerja. Visualisasi ini membantu dalam memahami pola attrition dan faktor-faktor yang mempengaruhinya.

## Conclusion
Dari analisis yang dilakukan, ditemukan bahwa faktor-faktor seperti umur, pendapatan bulanan, lama bekerja di perusahaan, dan total pengalaman kerja memiliki pengaruh signifikan terhadap tingkat attrition. Model Random Forest yang dibangun menunjukkan kinerja yang baik dalam memprediksi karyawan yang berisiko tinggi meninggalkan perusahaan, dengan akurasi sebesar 86%.

## Rekomendasi Action Items (Optional)
Berikut beberapa rekomendasi action items yang dapat dilakukan perusahaan guna menyelesaikan permasalahan:

1. **Meningkatkan Monthly Income Karyawan:** Karena pada Monthly Income dengan range 2500$-5000$ adalah tingkat Attrition yang tertinggi. Maka salah satu solusinya adalah dengan meningkatkan penghasilan bulanan kepada karyawan. Dimana Range diatas 7500$ merupakan range monthly income yang memiliki tingkat Attrition yang rendah. 


## Prediksi dan Penggunaan Model
### **Cara Script Python Untuk Prediksi :** 
1. **Letakkan File prediction.py serta dataset employee_data.csv pada 1 Folder yang sama**
2. **Kemudian Buka Terminal Baru, lalu arahkan direktori terminal pada Folder prediction.py dan employee_data.csv**
3. **Ketikan python prediction.py untuk menggunakan Script Python tersebut**
4. **Hasil Prediksi akan muncul pada terminal**

```
