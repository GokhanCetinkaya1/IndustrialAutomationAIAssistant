#!/bin/bash

echo "========================================"
echo "Endüstriyel Otomasyon AI Asistanı"
echo "========================================"
echo ""

# Sanal ortam var mı kontrol et
if [ ! -d "venv" ]; then
    echo "Virtual environment oluşturuluyor..."
    python3 -m venv venv
    echo ""
fi

# Sanal ortamı aktif et
echo "Virtual environment aktif ediliyor..."
source venv/bin/activate
echo ""

# Gereksinimleri yükle
echo "Gerekli paketler yükleniyor..."
pip install -q -r requirements.txt
echo ""

# Uygulamayı başlat
echo "Uygulama başlatılıyor..."
echo ""
echo "Tarayıcınızda http://localhost:8501 açılacak."
echo "Kapatmak için CTRL+C basın."
echo ""
streamlit run perso.py
