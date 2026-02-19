@echo off
chcp 65001 > nul
echo ========================================
echo Endustriyel Otomasyon AI Asistani
echo ========================================
echo.

REM Dogru klasorde olup olmadigini kontrol et
if not exist "perso.py" (
    echo [HATA] perso.py dosyasi bulunamadi!
    echo.
    echo Lutfen start.bat dosyasini dogru klasorde calistirin.
    echo.
    echo Dogru yapi:
    echo   industrial_ai_chatbot\
    echo   +-- perso.py
    echo   +-- requirements.txt
    echo   +-- start.bat  [BURAYA CIFT TIKLAYIN]
    echo   +-- prompts\
    echo   +-- utils\
    echo.
    echo Cozum:
    echo 1. ZIP'i tam olarak cikarttiginizdan emin olun
    echo 2. "industrial_ai_chatbot" klasorune girin
    echo 3. start.bat'a TEKRAR cift tiklayin
    echo.
    pause
    exit /b 1
)

if not exist "requirements.txt" (
    echo [HATA] requirements.txt dosyasi bulunamadi!
    echo Dosyalar eksik olabilir. ZIP'i yeniden cikartmayi deneyin.
    echo.
    pause
    exit /b 1
)

REM Python yuklu mu kontrol et
python --version > nul 2>&1
if errorlevel 1 (
    echo [HATA] Python bulunamadi!
    echo.
    echo Python yuklemek icin:
    echo 1. https://www.python.org/downloads/ adresine gidin
    echo 2. Python 3.8 veya uzerini indirin
    echo 3. Kurulum sirasinda "Add Python to PATH" isaretleyin
    echo.
    pause
    exit /b 1
)

REM Sanal ortam var mi kontrol et
if not exist "venv\" (
    echo [1/3] Virtual environment olusturuluyor...
    python -m venv venv
    if errorlevel 1 (
        echo [HATA] Virtual environment olusturulamadi!
        pause
        exit /b 1
    )
    echo       Tamam!
    echo.
)

REM Sanal ortami aktif et
echo [2/3] Virtual environment aktif ediliyor...
call venv\Scripts\activate.bat
echo       Tamam!
echo.

REM Gereksinimleri yukle
echo [3/3] Gerekli paketler yukleniyor...
echo       (Ilk seferde 1-2 dakika surebilir)
pip install -q -r requirements.txt
if errorlevel 1 (
    echo [HATA] Paketler yuklenemedi!
    echo Internet baglantinizi kontrol edin.
    pause
    exit /b 1
)
echo       Tamam!
echo.

REM Uygulamayi baslat
echo ========================================
echo ^>^> UYGULAMA BASLATILIYOR...
echo ========================================
echo.
echo Tarayicinizda http://localhost:8501 acilacak
echo.
echo ONEMLI:
echo  - Sol sidebar'dan API Key girin
echo  - Kapatmak icin CTRL+C basin
echo.
streamlit run perso.py

pause
