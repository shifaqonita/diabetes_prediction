import pickle
import streamlit as st

# Membaca model
diabetes_model = pickle.load(open('22611028_diabetes_model.sav', 'rb'))

# Judul web dengan warna
st.markdown("<h1 style='text-align: center; color: #FF6347;'>Prediksi Diabetes</h1>", unsafe_allow_html=True)

# Menambahkan gambar header (opsional)
# st.image('header_image.jpg', use_column_width=True)

# Deskripsi singkat dengan ukuran font kecil dan warna latar belakang
st.markdown("""
    <div style='background-color: #f0f8ff; padding: 10px; border-radius: 10px;'>
    <p style='text-align: center; font-size: 14px;'>Aplikasi ini akan memprediksi kemungkinan seseorang terkena diabetes berdasarkan beberapa parameter medis. Silakan masukkan data pada kolom di bawah untuk melakukan prediksi.</p>
    </div>
    """, unsafe_allow_html=True)

# Mengatur layout dengan dua kolom
with st.form(key='prediction_form'):
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.number_input('Jumlah Kehamilan', min_value=0, max_value=20, step=1, format='%d')
        Glucose = st.number_input('Konsentrasi glukosa', min_value=0, max_value=300, step=1, format='%d')
        BloodPressure = st.number_input('Tekanan darah diastolik', min_value=0, max_value=200, step=1, format='%d')
        SkinThickness = st.number_input('Ketebalan lipatan kulit trisep', min_value=0, max_value=100, step=1, format='%d')

    with col2:
        BMI = st.number_input('BMI', min_value=0.0, max_value=70.0, step=0.1, format='%.1f')
        Insulin = st.number_input('Insulin', min_value=0, max_value=1000, step=1, format='%d')
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0, step=0.01, format='%.2f')
        Age = st.number_input('Usia', min_value=0, max_value=120, step=1, format='%d')

    # Tombol untuk prediksi di luar kolom dengan warna
    submit_button = st.form_submit_button('Test Prediksi Diabetes', type='primary')

    if submit_button:
        # Memeriksa jika semua input sudah benar
        inputs = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        
        # Prediksi
        diab_prediction = diabetes_model.predict([inputs])
        
        if diab_prediction[0] == 1:
            diab_diagnosis = 'Pasien terkena Diabetes'
            st.error(diab_diagnosis, icon="🚨")
        else:
            diab_diagnosis = 'Pasien tidak terkena Diabetes'
            st.success(diab_diagnosis, icon="✅")
