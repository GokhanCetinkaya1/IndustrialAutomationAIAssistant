
PLC ve Robot programlama için yapay zeka destekli kod üretici chatbot.

##  Özellikler

###  AI Desteği
-  **Google Gemini** 
-  **DeepSeek** 
-  **Anthropic Claude** (Önerilen)
-  **OpenAI GPT**

### PLC Desteği
-  **ST (Structured Text)** - IEC 61131-3 standardı
-  **SCL (Siemens)** - S7-1200/1500 için
-  **STL (Statement List)** - Klasik Siemens S7-300/400 programlama

### Robot Desteği
-  **Fanuc** - TP/Karel programlama
-  **ABB Rapid** - RAPID dili
-  **KUKA KRL** - KUKA Robot Language
-  **YASKAWA INFORM** - YASKAWA Robot Language

## Hızlı Başlangıç

### 1. Gereksinimleri Yükleyin

```bash
# Proje klasörüne gidin
cd industrial_ai_chatbot

# Virtual environment oluşturun (önerilen)
python -m venv venv

# Virtual environment'i aktifleştirin
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Paketleri yükleyin
pip install -r requirements.txt
```

### 2. API Key Alın

**Önerilen: Google Gemini** 

1. [Google AI Studio](https://aistudio.google.com/app/apikey) adresine gidin
2. Google hesabınızla giriş yapın
3. "Create API Key" tıklayın
4. Key'i kopyalayın
5. **Ücretsiz - Kredi kartı gerekmez!**

**Alternatifler:**
- [DeepSeek Platform](https://platform.deepseek.com) 
- [Anthropic Console](https://console.anthropic.com) 
- [OpenAI Platform](https://platform.openai.com) 


### 3. Uygulamayı Başlatın

```bash
streamlit run perso.py
```

Tarayıcınızda otomatik olarak `http://localhost:8501` açılacaktır.

### 4. API Key'i Girin

- Sol sidebar'daki "Anthropic API Key" alanına key'inizi yapıştırın
- Platform (PLC/Robot) ve dil seçimini yapın
- Chatbot kullanıma hazır!

## Kullanım Örnekleri

### PLC (ST) Örneği
```
Soru: "3 konveyör bandı sırayla çalışsın, her biri 10 saniye aktif olsun"

Yanıt: Tam çalışan ST kodu + açıklamalar
```

### Robot (Fanuc) Örneği
```
Soru: "4x4 grid şeklinde palet üzerinde pick and place yap"

Yanıt: Tam çalışan Fanuc TP kodu + pozisyon tanımları
```

##  Proje Yapısı

```
industrial_ai_chatbot/
├── perso.py                      # Ana Streamlit uygulaması
├── requirements.txt            # Python bağımlılıkları
├── .env.example               # Örnek environment dosyası
├── prompts/
│   ├── plc_prompts.py        # PLC için AI promptları
│   └── robot_prompts.py      # Robot için AI promptları
└── utils/
    └── code_formatter.py     # Yardımcı fonksiyonlar
```

### Yeni Bir Robot Markası Eklemek

`prompts/robot_prompts.py` dosyasını açın ve `robot_specific` dictionary'sine yeni marka ekleyin.

## Gelişmiş Özellikler (Gelecek Versiyonlar)

- Kod validasyonu ve hata kontrolü,
- NC hatalarını ekle.
- Simülasyon entegrasyonu
- Kod versiyonlama ve karşılaştırma
- Çoklu dil desteği (İngilizce, Almanca)
- Kod kütüphanesi ve şablonlar
- Export/Import fonksiyonları
- Offline mod (local LLM)

## Güvenlik

- API key'ler güvenli bir şekilde saklanır
- Hiçbir veri harici sunucularda tutulmaz
- Session bazlı çalışır (yeniden başlatınca temizlenir)

## Lisans

Bu proje kişisel ve ticari kullanım için açık kaynaklıdır.

## Katkıda Bulunma

Önerileriniz ve katkılarınız için pull request gönderebilir veya issue açabilirsiniz.

## İletişim

Sorularınız için GitHub Issues kullanabilirsiniz.

---

**Not:** Bu bir prototip uygulamadır. Üretim ortamında kullanmadan önce üretilen kodları mutlaka test edin!
