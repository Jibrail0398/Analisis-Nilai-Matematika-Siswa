import streamlit as st
import io
import Data_load as dt
import Data_cleansing as dc
import Analisis_Visualisasi as av

st.title('Analisis Siswa Matematika')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.write("""### Oleh Muhammad Jibrail Natadilaga""")
option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Dataframe','Data Cleansing','Analisis dan Visualisasi')
)
if option == 'Dataframe' or option == '':
    st.header(""" Dataframe""") #Menampilkan Dataframe
    st.dataframe(dt.load_data(),1500,300)
    st.write("""## Info dataset""")
    pilihan = st.selectbox("Silahkan pilih",['Informasi Dataset','Jumlah baris dan kolom','Jumlah nilai null','Value kolom kategori'])
    if pilihan == "Jumlah nilai null":
        st.text("Nilai null pada masing-masing kolom")
        st.write(dt.df.isnull().sum())
    elif pilihan == 'Informasi Dataset':
        buffer = io.StringIO()
        dt.df.info(buf = buffer)
        s = buffer.getvalue()
        st.text(s)
    elif pilihan == 'Jumlah baris dan kolom':
        st.text(str(dt.df.shape[0]) + " Baris")
        st.text(str(dt.df.shape[1]) + " Kolom")
    elif pilihan == 'Value kolom kategori':
        for col in dt.df.columns:
            for val in dt.df[col].unique():
                if type(val) == str:
                    st.write(col + ' :',val)
                else:
                    continue
elif option == 'Data Cleansing':
    st.header("""Data Cleansing""") #Menampilkan proses Data Cleansing
    st.write("""### Hapus nilai null""")
    st.caption("Jumlah kolom null")
    st.write(dc.df.isna().sum())
    st.write("""### Menambah kolom baru dan menghapus kolom yang tidak diperlukan""")
    st.caption("Menambah kolom dengan nama 'Learning Method' dan menghapus kolom 'wesson' ")
    st.dataframe(dc.clean_data,1500,300)
elif option == 'Analisis dan Visualisasi':
    st.header("""Analisis dan Visualisasi""") #Menampilkan Analisis dan Visualisasi 
    pilihan = st.selectbox("Pilih visualisasi",['Demografi Siswa','Nilai Siswa Berdasarkan etnis',
    'Nilai Siswa Berdasarkan Metode Belajar','Nilai Siswa Berdasarkan Guru yang Mengajar','Nilai Siswa Berdasarkan Freeredu'])
    if pilihan == 'Demografi Siswa':
        st.caption("Demografi Siswa")
        av.pie_chart()
        av.demo_bar_chart()
    if pilihan == 'Nilai Siswa Berdasarkan etnis':
        st.caption('Rata-Rata Nilai Siswa Berdasarkan etnis')
        av.score_ethnic()
    if pilihan == 'Nilai Siswa Berdasarkan Metode Belajar':
        st.caption('Rata-Rata Nilai Siswa Berdasarkan Metode Belajar')
        av.score_Learning_Method()
        av.score_Learning_Method1()
    if pilihan == 'Nilai Siswa Berdasarkan Guru yang Mengajar':
        st.caption('Nilai Siswa Berdasarkan Guru yang Mengajar')
        av.score_by_teacher()
        av.score_by_teacher1()
    if pilihan == 'Nilai Siswa Berdasarkan Freeredu':
        st.caption('Nilai Siswa Berdasarkan Freeredu')
        av.score_by_freeredu()
