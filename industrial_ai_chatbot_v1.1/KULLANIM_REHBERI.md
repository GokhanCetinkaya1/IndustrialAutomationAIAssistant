# 📖 Adım Adım Kullanım Rehberi

## 🎯 Başlamadan Önce

### Gereksinimler
- Python 3.8 veya üzeri
- İnternet bağlantısı
- Anthropic API Key (ücretsiz deneme mevcut)

##  Kurulum Adımları

### Adım 1: API Key Alma (5 dakika)

1. https://console.anthropic.com adresine gidin
2. "Sign Up" ile hesap oluşturun (email ile)
3. Email onayını yapın
4. Console'a giriş yapın
5. Sol menüden "API Keys" seçin
6. "Create Key" butonuna tıklayın
7. Key'e bir isim verin (örn: "PLC-Robot-Bot")
8. "Create" butonuna basın
9. **ÖNEMLİ:** Key'i kopyalayıp güvenli bir yere kaydedin (bir daha gösterilmez!)

### Adım 2: Projeyi İndirme

Zip dosyasını indirip klasöre çıkartın.

### Adım 3: Başlatma

**Windows Kullanıcıları:**
1. `start.bat` dosyasına çift tıklayın
2. İlk çalıştırmada gerekli paketler otomatik yüklenecek (2-3 dk)
3. Tarayıcıda otomatik açılacak

**Mac/Linux Kullanıcıları:**
1. Terminal'i açın
2. Proje klasörüne gidin: `cd yol/industrial_ai_chatbot`
3. Çalıştırın: `./start.sh`
4. Tarayıcıda otomatik açılacak

**Manuel Başlatma:**
```bash
# Virtual environment oluştur
python -m venv venv

# Aktif et (Windows)
venv\Scripts\activate
# Aktif et (Mac/Linux)
source venv/bin/activate

# Paketleri yükle
pip install -r requirements.txt

# Çalıştır
streamlit run app.py
```

##  İlk Kullanım

### 1. API Key Girişi
- Sol sidebar'da "Anthropic API Key" alanını bulun
- Kopyaladığınız key'i yapıştırın
- Key kaybolmaz, tarayıcı kapanana kadar kalır

### 2. Platform Seçimi
- **PLC** veya **Robot** seçin
- Dil/Marka seçin (örn: ST, Fanuc)

### 3. İlk Kodunuz
Chat kutusuna şunu yazın:
```
Konveyör bant kontrolü için kod yaz. 
Başlat butonuna basınca çalışsın, 
durdur butonuna basınca dursun.
```

Enter'a basın ve bekleyin! 

### Örnekler

**PLC (ST) için:**
```
3 tanklı dolum sistemi. 
Tank1'e önce su doldur, dolunca Tank2'ye geç, 
sonra Tank3'e geç. Her tank için seviye sensörü var.
Float switch ile kontrol et.
```

**Fanuc Robot için:**
```
Palet üzerinde 3x3 grid halinde kutular var.
Her kutuyu al, 500mm yukarı kaldır, 
90 derece dön ve place pozisyonuna bırak.
Gripper sinyali DO[1], parça sensörü DI[1].
```

**ABB Rapid için:**
```
2 nokta arası linear hareket.
Ortada dairesel bir path çiz.
Hız 500mm/s, fine hassasiyette.
İşlem başında digital output 5'i aç.
```

##  Özellikler

### Sohbet Geçmişi
- Önceki sorularınız ve cevaplar saklanır
- Üzerine devam edebilirsiniz
- "Bunu değiştir" diyebilirsiniz

### Kod Açıklamaları
- Her kod bloğu açıklamalı gelir
- Değişkenler Türkçe açıklanır
- Güvenlik notları dahildir

### Çoklu Dil Desteği
- Aynı anda farklı diller deneyebilirsiniz
- Platform değiştirerek karşılaştırma yapabilirsiniz

## 🐛 Sorun Giderme

### "API Key Hatası"
- Key'i doğru kopyaladığınızdan emin olun
- Başında/sonunda boşluk olmasın
- Console'da key'in aktif olduğunu kontrol edin

### "Modül Bulunamadı"
```bash
pip install -r requirements.txt --upgrade
```

### "Streamlit Çalışmıyor"
```bash
pip uninstall streamlit
pip install streamlit
```

### Yavaş Yanıt
- Normal, AI düşünüyor 😊
- 10-30 saniye arası bekleme normal
- Çok uzun kod için daha fazla sürebilir

## 📊 API Kullanım Limitleri

Anthropic ücretsiz tier:
- Günlük token limiti var
- Karmaşık kodlar daha fazla token harcar
- Console'dan kullanımınızı takip edebilirsiniz

##  İleri Seviye

### Conversation Flow
1. Genel bir kod isteyin
2. "Buna emergency stop ekle" deyin
3. "Şimdi timer ekle" deyin
4. Artımlı olarak geliştirin

### Kod İyileştirme
```
Yukarıdaki kodu optimize et.
Daha az bellek kullansın.
```

### Debugging
```
Bu kodda hata var mı kontrol et.
Güvenlik açısından eksik ne var?
```

### Dokümantasyon
```
Bu kod için kullanım kılavuzu yaz.
Yeni başlayanlar için açıkla.
```

## Öğrenme Kaynakları

Bot'a şunları sorabilirsiniz:
- "PLC programlamada timer nasıl kullanılır?"
- "Fanuc'ta position register nedir?"
- "ABB RAPID'de zone data ne işe yarar?"
- "KUKA'da interrupt nasıl çalışır?"

## Yardım

Takıldığınız yerde:
1. README.md dosyasına bakın
2. Sidebar'daki örnek sorulara bakın
3. Daha basit bir soruyla başlayın
4. Google'da "streamlit error [hata mesajı]" arayın

##  Checklist - İlk Kullanım

- [ ] Python kurulu mu? (`python --version`)
- [ ] API Key aldım mı?
- [ ] start.bat / start.sh çalıştırdım mı?
- [ ] Tarayıcı açıldı mı?
- [ ] API Key'i yapıştırdım mı?
- [ ] Platform ve dil seçtim mi?
- [ ] İlk soruyu sordum mu?

Hepsini yaptıysanız, hazırsınız! 🎉

##  Sonraki Adımlar

1. Basit bir kod isteyin
2. Kodu kopyalayıp PLC/Robot simülatörünüzde test edin
3. Feedback verin: "Bu kod çalıştı ama şunu ekle"
4. Daha karmaşık projeler deneyin
5. Kendi kod kütüphanenizi oluşturun

---
