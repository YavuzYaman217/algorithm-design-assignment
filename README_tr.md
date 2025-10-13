# Algoritma Tasarımı ve Analizi - Ders Projeleri

🇹🇷 Türkçe | [🇬🇧 English](README.md)

Bu depo, dönem boyunca geliştirilen algoritma tasarımı projelerini ve uygulamalarını içermektedir. Her proje, detaylı algoritma açıklamaları, çalışan kod uygulamaları ve kapsamlı test senaryoları içerir.

## 📚 Ders Bilgileri

**Ders:** Algoritma Tasarımı ve Analizi  
**Dönem:** Güz 2025/2026  
**Odak Alanları:** Problem çözme, algoritma tasarımı, karmaşıklık analizi, optimizasyon

## 🗂️ Depo Yapısı

```
Algorithm and Analysis/
│
├── README.md                    # Proje dokümantasyonu (İngilizce)
├── README_tr.md                 # Proje dokümantasyonu (Türkçe)
├── test_wrapper.py              # Evrensel test framework'ü
│
└── week-01/                     # Haftalık ödevler
    ├── nearest-square/
    │   ├── algorithm.txt        # Algoritma açıklaması
    │   ├── nearest_square.py    # Uygulama
    │   └── test_cases.txt       # Test senaryoları
    │
    └── prime-finder/
        ├── algorithm.txt
        ├── prime_finder.py
        └── test_cases.txt
```

## 🧪 Test Framework'ü

Bu depo, `test_cases.txt` dosyalarında tanımlanan test senaryolarına karşı herhangi bir fonksiyonu otomatik olarak test eden güçlü bir **Test Wrapper** framework'ü içerir.

### Özellikler:
- ✅ `.txt` dosyalarından otomatik test senaryosu yükleme
- ⚡ Performans ölçümü (çalışma süresi)
- 📊 Başarılı/başarısız durum içeren detaylı test raporları
- 🎯 Herhangi bir Python fonksiyonu ile kolay entegrasyon

### Kullanım:

```python
from test_wrapper import TestWrapper

# Örnek: nearest_square fonksiyonunu test et
from week_01.nearest_square.nearest_square import nearest_square

wrapper = TestWrapper(
    function=nearest_square,
    test_file="week-01/nearest-square/test_cases.txt"
)
wrapper.run_all_tests()
```

### Test Senaryosu Formatı:

Test senaryoları, `test_cases.txt` dosyalarında INI formatı kullanılarak tanımlanır:

```ini
[TEST1]
description = Temel pozitif sayı
input = 10
expected = 9

[TEST2]
description = Tam kare
input = 16
expected = 16
```

## 📝 Hafta 01 - Ödevler

### 1. En Yakın Tam Kare
**Problem:** Verilen pozitif bir N tam sayısına en yakın tam kareyi bulun.

**Algoritma Özellikleri:**
- √N hesapla
- Alt ve üst tam kareleri bul
- Mesafeleri karşılaştırarak en yakınını belirle

**Dosya:** `week-01/nearest-square/nearest_square.py`

### 2. Asal Sayı Bulucu
**Problem:** Verilen pozitif bir N tam sayısına kadar olan tüm asal sayıları bulun.

**Algoritma Özellikleri:**
- Deneme bölmesi yöntemi
- √i limiti kullanarak optimizasyon
- Verimli asal sayı tespiti

**Dosya:** `week-01/prime-finder/prime_finder.py`

## 🚀 Nasıl Çalıştırılır

### Depoyu Klonla
```bash
git clone https://github.com/YavuzYaman217/algorithm-design-assignment.git
cd "Algorithm and Analysis"
```

### Tekil Uygulamaları Çalıştır
```bash
# En yakın tam kare bulucuyu çalıştır
python week-01/nearest-square/nearest_square.py

# Asal sayı bulucuyu çalıştır
python week-01/prime-finder/prime_finder.py
```

### Test Framework'ü ile Çalıştır
```python
# Bir test scripti oluştur veya Python'u interaktif olarak kullan
from test_wrapper import TestWrapper
from week_01.nearest_square.nearest_square import nearest_square

wrapper = TestWrapper(nearest_square, "week-01/nearest-square/test_cases.txt")
wrapper.run_all_tests()
```

## 🛠️ Gereksinimler

- Python 3.7 veya üzeri
- Harici bağımlılık yok (sadece standart kütüphane kullanılır)

## 📊 Test Etme

Tüm uygulamalar aşağıdakileri kapsayan kapsamlı test senaryoları içerir:
- ✅ Normal durumlar
- ✅ Uç durumlar (küçük sayılar, tam kareler, vb.)
- ✅ Sınır koşulları
- ✅ Performans kriterleri

## 📖 Öğrenme Hedefleri

Bu projeler aracılığıyla öğrenciler:
1. Yaygın problemler için verimli algoritmalar tasarlayacak
2. Zaman ve alan karmaşıklığını analiz edecek
3. Temiz, dokümante edilmiş kod yazacak
4. Kapsamlı test senaryoları oluşturacak
5. Gerçek dünya problemlerine algoritmik düşünceyi uygulayacak

## 🤝 Katkıda Bulunma

Bu bir ders projesi deposudur. Eğer bir öğrenci veya eğitmen iseniz ve sorunlar bulursanız veya önerileriniz varsa:
1. Depoyu fork'layın
2. Bir özellik dalı (feature branch) oluşturun
3. Pull request gönderin

## 📄 Lisans

Bu proje, Algoritma Tasarımı ve Analizi dersinin bir parçası olarak eğitim amaçlı oluşturulmuştur.

## 👤 Yazar

**Yavuz Yaman**
- GitHub: [@YavuzYaman217](https://github.com/YavuzYaman217)

---

**Not:** Bu depo, dönem boyunca her hafta yeni ödevler ve uygulamalarla güncellenecektir.
