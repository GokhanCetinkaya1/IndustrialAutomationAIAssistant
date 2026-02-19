# API KEY KURULUM REHBERİ

## Seçenek 1: Arayüzden Girin (Başlangıç için önerilen)

### Adımlar:
1. Uygulamayı başlatın (`start.bat` veya `start.sh`)
2. Tarayıcıda açılınca **sol tarafta** sidebar'ı görürsünüz
3. "API Key" yazan kutucuğa API key'inizi yapıştırın
4. Hemen kullanmaya başlayın!

### Artıları:
+ Çok kolay
+ Hemen çalışır
+ Kod değişikliği yok

### Eksileri:
- Her açılışta tekrar girmelisiniz
- Tarayıcı kapanınca kaybolur

---

**2. .env Dosyasını Düzenleyin:**

Dosyayı bir metin editörü ile açın (Notepad, VSCode, vb.)

Şunu bulun:
```
ANTHROPIC_API_KEY=buraya_api_keyinizi_yapiştirin
```

API key'inizi yapıştırın:
```
ANTHROPIC_API_KEY=sk-ant-api03-xxxxxxxxxxxxxxxxxxxxx
```

Kaydedin ve kapatın.

**3. Uygulamayı Başlatın:**

Artık her başlattığınızda API key otomatik yüklenecek!

### Artıları:
+ Bir kere girin, her zaman çalışır
+ Güvenli (dosyayı paylaşmazsanız)
+ Arayüzde görünür ama değiştirilebilir

### Eksileri:
- .env dosyasını asla paylaşmayın!
- Git'e yüklerken dikkat edin (.gitignore'a ekleyin)

---

##  ÖNEMLİ GÜVENLİK NOTLARI

### YAPMAYIN:
❌ API key'i kodun içine yazmayın
❌ .env dosyasını kimseyle paylaşmayın
❌ GitHub'a yüklerken .env'yi eklemeyin
❌ Screenshot'larda API key göstermeyin

### YAPIN:
✅ .env dosyasını local'de tutun
✅ .env.example'ı paylaşabilirsiniz (içinde key YOK)
✅ API key'i düzenli değiştirin
✅ Console'dan kullanım limitlerini takip edin

---

##  HIZLI BAŞLANGIÇ


1. `start.bat` veya `start.sh` çalıştır
2. Tarayıcıda açılınca sol sidebar'daki kutuya API key yapıştır
3. Platform seç (PLC veya Robot)
4. Kod istemeye başla!

##  Sorun Giderme

### "API Key Hatası" Alıyorum
- Key'i doğru kopyaladınız mı?
- Başında/sonunda boşluk var mı?
- `sk-ant-api03-` ile mi başlıyor?
- Console'da key aktif mi?

### .env Dosyası Çalışmıyor
- Dosya adı tam olarak `.env` mi? (`.env.txt` değil!)
- Dosya proje klasörünün ana dizininde mi?
- `python-dotenv` paketi kurulu mu? (`pip install python-dotenv`)
- Uygulamayı yeniden başlattınız mı?
