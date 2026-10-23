# 🚀 100+ E-Dönüşüm Yapay Zeka Skili & Hazır Prompt Kütüphanesi (v1.1)

[![CI Test Suite](https://github.com/eimza-kep/100-e-donusum-skili/actions/workflows/ci.yml/badge.svg)](https://github.com/eimza-kep/100-e-donusum-skili/actions)
[![Skills Count](https://img.shields.io/badge/Beceriler-102%20Skil%20(v1.1)-blue.svg)](skills.json)
[![Playground](https://img.shields.io/badge/Demo-Canl%C4%B1%20Web%20Playground-brightgreen.svg)](https://eimza-kep.github.io/100-e-donusum-skili/)
[![Categories](https://img.shields.io/badge/Kategori-8%20Ana%20Alan-orange.svg)](docs/)
[![Python](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-brightgreen.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/Lisans-MIT-green.svg)](LICENSE)
[![Local LLM](https://img.shields.io/badge/Yerel%20LLM-Ollama%20%7C%20DeepSeek-purple.svg)](#-yerel-llm-ve-ollama-entegrasyonu)

**Türkiye E-Dönüşüm Ekosistemi (GİB, VUK, TTK, UETS, KEP, UYAP, KVKK)** standartlarına tam uyumlu; **Cursor, Claude, Antigravity, OpenAI GPT-4o ve Ollama/DeepSeek** ajanları için geliştirilmiş **102 uzman yapay zeka becerisi, etkileşimli Web Prompt Playground arayüzü ve parametrik prompt şablonları.**

---

## 🌟 v1.1 Sürümü ile Gelen Yenilikler

1. **🌐 WebAssembly & Statik Web Prompt Playground (`index.html`):**
   - Herhangi bir sunucu veya Python bağımlılığı olmadan, doğrudan tarayıcı üzerinden 102 beceriyi filtreleme, dinamik değişkenlerle prompt derleme ve tek tıkla kopyalama arayüzü.
   - Tarayıcı üzerinden doğrudan yerel `localhost:11434` Ollama API'sine bağlanarak %100 çevrimdışı çalıştırma desteği.
2. **🍽️ e-Adisyon Denetim Becerisi (`adisyon-masadan-faturaya-eslesme-denetleyici`):**
   - 509 Sıra No.lu VUK Genel Tebliği uyarınca masada sipariş anında e-Adisyon düzenlenmesi, GİB zaman damgası ve ödeme anında e-Fatura/ÖKC fişi dönüşüm zincirini denetler.
3. **🌾 e-Müstahsil Makbuzu (e-MM) Kesinti Motoru (`mustahsil-stopaj-ve-sgk-kesinti-motoru`):**
   - GVK m. 94 ve 5510 sayılı Kanun uyarınca çiftçiden doğrudan tarımsal/hayvansal ürün alımlarında GV stopajı (%1-%4), SGK Bağ-Kur prim kesintisi (%2) ve borsa tescil payı hesaplama otomasyonu.
4. **📦 Tek Komutla Web Başlatıcı:**
   - `python run_skill.py --web` komutu ile yerel sunucuyu tek tuşla başlatma ve varsayılan tarayıcıda açma.

---

## 📌 Neden Bu Kütüphane?

Yapay zeka modelleri genel konularda başarılı olsa da, Türkiye e-Dönüşüm mevzuatındaki kritik ayrıntılarda (UBL-TR 1.2.1 şeması, KDV tevkifat oranları, 8 günlük ticari fatura itiraz süresi, berat hash algoritmaları, UETS 5 günlük yasal tebellüğ kuralı, UDF doküman yapısı, KVKK 72 saat kriz protokolü) sıklıkla halüsinasyon görür.

Bu kütüphane, **her biri mevzuat maddeleriyle (VUK, TTK, HMK, İİK, 5070, 6698) sınırlandırılmış ve doğrulanmış 102 uzman yapay zeka becerisini** hazır promptlar ve test edilmiş girdilerle sunar.

---

## 🌐 Web Prompt Playground (Tarayıcıda Çalıştırma)

Hiçbir kodlama veya terminal bilgisine ihtiyaç duymadan, görsel arayüzle çalışmak için:

### 1. Canlı Web Sürümü (GitHub Pages):
👉 **[eimza-kep.github.io/100-e-donusum-skili](https://eimza-kep.github.io/100-e-donusum-skili/)** adresinden doğrudan tarayıcınızda açabilirsiniz.

### 2. Yerelde Tek Tıkla Başlatma:
Doğrudan repo kök dizinindeki `index.html` dosyasına çift tıklayabilir veya terminalden şu komutu çalıştırabilirsiniz:

```bash
python run_skill.py --web
```

Açılan modern arayüzde:
- **Anında Arama:** 102 beceri içinde isim, mevzuat, açıklama ve etiket bazlı arama yapın.
- **Kategori Filtreleri:** e-Fatura, e-Defter, e-İrsaliye, e-İmza, KEP/UETS, UYAP, SMMM ve KVKK arasında geçiş yapın.
- **Dinamik Parametre Formu:** Seçilen becerinin şablon değişkenleri (`{fatura_tutari}`, `{sevk_tarihi}` vb.) için otomatik üretilen form alanlarını doldurun.
- **Canlı Prompt Önizleme:** Değişkenler değiştikçe nihai kullanıcı istemini canlı izleyin ve tek tıkla kopyalayın.
- **Yerel Ollama Bağlantısı:** `http://127.0.0.1:11434` üzerinden yerel Llama 3 veya DeepSeek modelinize doğrudan tarayıcıdan istek gönderin!

---

## 📁 Dizin Yapısı

```bash
100-e-donusum-skili/
├── index.html                    # WebAssembly / İstemci taraflı interaktif Web Playground
├── web/index.html                # Alternatif web kök dosyası
├── build_web.py                  # Web Playground HTML derleyici betiği
├── .cursorrules                  # Cursor IDE kuralları ve 102 beceri referansı
├── claude_skills.xml             # Claude Projects için XML formatında sistem istemleri
├── skills.json                   # 102 becerinin makine tarafından okunabilir tam kataloğu
├── SKILLS_REFERENCE.md           # Markdown formatında kapsamlı beceri referans rehberi
├── Modelfile                     # Yerel Ollama modelleri için hazır sistem istemi
├── run_skill.py                  # CLI aracı (Arama, listeleme, web başlatıcı, mock çalıştırma)
├── test_skills.py                # 102 beceri için şema ve interpolasyon test paketi
├── generate_docs.py              # Otomatik dokümantasyon üretici
├── docs/                         # Kategori bazlı ayrıntılı dokümanlar
│   ├── 01_efatura_ve_earsiv.md   # e-Fatura, e-Arşiv, e-Adisyon & e-MM (17 Beceri)
│   ├── 02_edefter_ve_berat.md    # e-Defter & Berat Becerileri (12 Beceri)
│   ├── 03_eirsaliye_ve_lojistik.md# e-İrsaliye & Lojistik Becerileri (10 Beceri)
│   ├── 04_eimza_ve_malimuhur.md  # e-İmza & Mali Mühür Becerileri (15 Beceri)
│   ├── 05_kep_ve_uets.md         # KEP & UETS Becerileri (12 Beceri)
│   ├── 06_uyap_ve_hukuk.md       # UYAP & LegalTech Becerileri (16 Beceri)
│   ├── 07_smmm_ve_beyanname.md   # Vergi, SMMM & Beyanname Becerileri (12 Beceri)
│   ├── 08_kvkk_ve_guvenlik.md    # KVKK & Siber Güvenlik Becerileri (8 Beceri)
│   └── integration_guide.md      # Cursor, Claude, OpenAI & Ollama Entegrasyon Kılavuzu
└── skills/                       # Modüler Python beceri paketleri
    ├── __init__.py               # ALL_SKILLS, SKILLS_BY_ID, SKILLS_BY_CATEGORY
    ├── category_01_efatura.py    # 17 Beceri (e-Adisyon ve e-MM dahil)
    ├── category_02_edefter.py    # 12 Beceri
    ├── category_03_eirsaliye.py  # 10 Beceri
    ├── category_04_eimza.py      # 15 Beceri
    ├── category_05_kep.py        # 12 Beceri
    ├── category_06_uyap.py       # 16 Beceri
    ├── category_07_smmm.py       # 12 Beceri
    └── category_08_kvkk.py       # 8 Beceri
```

---

## ⚡ Hızlı Başlangıç (CLI Kullanımı)

Sıfır bağımlılık; yalnızca Python 3.9+ yeterlidir:

```bash
# Web Playground arayüzünü başlat ve tarayıcıda aç
python run_skill.py --web

# Kategorileri ve beceri sayılarını listele
python run_skill.py --categories

# Tüm 102 beceriyi listele
python run_skill.py --list

# Beceriler arasında anahtar kelime araması yap
python run_skill.py --search adisyon
python run_skill.py --search mustahsil
python run_skill.py --search tevkifat

# Belirli bir becerinin promptunu ve değişkenlerini incele
python run_skill.py --skill adisyon-masadan-faturaya-eslesme-denetleyici

# Beceriyi örnek girdilerle mock simülasyon olarak çalıştır
python run_skill.py --run mustahsil-stopaj-ve-sgk-kesinti-motoru --mock

# Dışa aktarma araçları:
python run_skill.py --export-json     # skills.json üretir
python run_skill.py --export-claude   # claude_skills.xml üretir
python run_skill.py --export-cursor   # .cursorrules üretir
python run_skill.py --export-markdown # SKILLS_REFERENCE.md üretir
python run_skill.py --export-ollama   # Yerel LLM'ler için Modelfile üretir
```

---

## 💻 Python Kütüphanesi Olarak Kullanım

Kendi projelerinizde veya backend servislerinizde doğrudan import edebilirsiniz:

```python
from skills import SKILLS_BY_ID

# 1. e-Adisyon Denetim Becerisini Çağırma:
skill = SKILLS_BY_ID["adisyon-masadan-faturaya-eslesme-denetleyici"]

inputs = {
    "masa_no": "Masa 7",
    "adisyon_zamani": "23.10.2026 12:30:00",
    "odeme_zamani": "23.10.2026 13:45:00",
    "fatura_belge_turu": "e-Arşiv Fatura",
    "fatura_zamani": "23.10.2026 13:46:12",
    "adisyon_tutari": "1.850 TL",
    "tahsilat_tutari": "1.850 TL"
}

user_prompt = skill["user_prompt_template"].format(**inputs)
system_prompt = skill["system_prompt"]

print("SİSTEM İSTEMİ:\n", system_prompt)
print("KULLANICI İSTEMİ:\n", user_prompt)
```

---

## 🦙 Yerel LLM ve Ollama Entegrasyonu

Verilerinizin gizliliği ve KVKK uyumu için modelleri tamamen yerel makinenizde çalıştırabilirsiniz:

1. [Ollama](https://ollama.com)'yı kurun ve modelinizi çekin:
   ```bash
   ollama pull llama3.2
   # veya
   ollama pull deepseek-r1:8b
   ```
2. Web Playground arayüzünden doğrudan erişebilmek için Ollama'yı CORS izniyle başlatın:
   ```bash
   # Windows PowerShell:
   $env:OLLAMA_ORIGINS="*" ; ollama serve

   # Linux & macOS:
   OLLAMA_ORIGINS="*" ollama serve
   ```
3. Proje içerisindeki `Modelfile` ile Türk E-Dönüşüm uzmanı bir yerel model oluşturun:
   ```bash
   ollama create edonusum-asistan -f Modelfile
   ollama run edonusum-asistan
   ```

---

## 📊 102 E-Dönüşüm Becerisi Tam Kataloğu

### 1. e-Fatura, e-Arşiv, e-Adisyon & e-MM Becerileri (17 Beceri)
Detaylı doküman: [`docs/01_efatura_ve_earsiv.md`](docs/01_efatura_ve_earsiv.md)

| No | Beceri ID | Beceri Adı | Model |
|:---|:---|:---|:---|
| 01 | `efatura-ubl-anomali-dedektoru` | e-Fatura UBL-TR XML Anomali Dedektörü | `gpt-4o` |
| 02 | `efatura-kdv-tevkifat-denetleyici` | e-Fatura KDV Tevkifat Kod ve Oran Denetleyicisi | `gemini-1.5-flash` |
| 03 | `efatura-8-gun-itiraz-asistani` | e-Fatura 8 Günlük Yasal İtiraz ve KEP İhtarname Asistanı | `gpt-4o` |
| 04 | `earsiv-gib-5000-30000-limit-kontrolcusu` | e-Arşiv Fatura GİB Portal Limit ve Zorunluluk Denetleyicisi | `gemini-1.5-flash` |
| 05 | `efatura-istisna-muafiyet-kod-eslestirici` | KDV İstisna Kodları (301, 351 vb.) ve Gerekçe Eşleştiricisi | `gpt-4o` |
| 06 | `efatura-ihracat-ve-gtip-denetleyicisi` | e-İhracat Faturası GTİP Kodu ve GÇB Eşleşme Denetleyicisi | `gpt-4o` |
| 07 | `efatura-otv-ve-ozel-matrah-hesaplayici` | ÖTV I-IV Sayılı Liste ve Özel Matrah e-Fatura Hesaplayıcı | `gpt-4o` |
| 08 | `efatura-mukellef-posta-kutusu-pk-sorgulama` | GİB Kayıtlı Kullanıcı PK/GB Posta Kutusu Yönlendirme Asistanı | `gemini-1.5-flash` |
| 09 | `earsiv-iptal-ve-iade-surec-yoneticisi` | e-Arşiv Fatura İptal/İade Süresi ve GİB Raporlama Kontrolü | `gpt-4o` |
| 10 | `efatura-dovizli-kur-farki-ve-kdv-duzeltici` | Dövizli e-Faturalarda TCMB Kuru ve Kur Farkı Faturası Denetleyicisi | `gpt-4o` |
| 11 | `efatura-tevkifatli-iade-ve-kdv2-mahsup-asistani` | KDV Tevkifatı Kaynaklı İade Talebi ve KDV-2 Mahsup Denetleyicisi | `gpt-4o` |
| 12 | `efatura-konaklama-vergisi-hesaplama-motoru` | %2 Konaklama Vergisi ve e-Fatura Matrah Ayrıştırma Motoru | `gemini-1.5-flash` |
| 13 | `earsiv-sms-eposta-ve-karekod-dogrulayici` | e-Arşiv Fatura Karekod (QR Code) ve İletim Doğrulayıcısı | `gemini-1.5-flash` |
| 14 | `efatura-babs-mutabakat-asistani` | e-Fatura Form Ba-Bs Sınır ve Cari Mutabakat Asistanı | `gpt-4o` |
| 15 | `efatura-ihracat-ve-gumruk-gtip-kontrolu` | e-İhracat Faturası ve Gümrük GTİP Kodu Kontrolcüsü | `gpt-4o` |
| 16 | `adisyon-masadan-faturaya-eslesme-denetleyici` | e-Adisyon Masadan Faturaya Eşleşme ve Zaman Damgası Denetleyicisi *(Yeni v1.1)* | `gpt-4o-mini` |
| 17 | `mustahsil-stopaj-ve-sgk-kesinti-motoru` | e-Müstahsil Makbuzu (e-MM) Stopaj ve SGK Prim Kesinti Motoru *(Yeni v1.1)* | `gemini-1.5-flash` |

---

### 2. e-Defter & Berat Becerileri (12 Beceri)
Detaylı doküman: [`docs/02_edefter_ve_berat.md`](docs/02_edefter_ve_berat.md)

| No | Beceri ID | Beceri Adı | Model |
|:---|:---|:---|:---|
| 18 | `edefter-yevmiye-madde-ve-kebir-denetleyici` | e-Defter Yevmiye Numaralama ve Kebir Denkliği Denetleyicisi | `gpt-4o` |
| 19 | `edefter-zaman-damgasi-ve-gib-onay-asistani` | GİB e-Defter Berat Yükleme Takvimi ve Zaman Damgası Denetleyicisi | `gemini-1.5-flash` |
| 20 | `edefter-berat-hash-ve-sha256-dogrulayici` | e-Defter Berat XML SHA-256 Hash ve İmza Doğrulayıcısı | `gpt-4o` |
| 21 | `edefter-ikincil-kopya-ve-gib-yedekleme-takipcisi` | GİB e-Defter İkincil Kopya Saklama ve Bulut Güvencesi Takipçisi | `gemini-1.5-flash` |
| 22 | `edefter-acilis-kapanis-ve-ters-kayit-analizoru` | Yıl Sonu Kapanış ve Yeni Yıl Açılış Yevmiye Maddesi Analizörü | `gpt-4o` |
| 23 | `edefter-belge-turu-ve-odeme-yontemi-denetleyicisi` | e-Defter Belge Tipleri ve Ödeme Yöntemi Uyum Denetleyicisi | `gemini-1.5-flash` |
| 24 | `edefter-muhasebe-fisi-ve-parcali-yevmiye-mimari` | Muhasebe Fişi Birleştirme ve Yevmiye Parçalama Mimarı | `gpt-4o` |
| 25 | `edefter-gib-berat-silme-ve-duzeltme-talebi-hazirlayici` | GİB Berat İptal / Düzeltme Talebi Resmi Yazı Hazırlayıcısı | `gpt-4o` |
| 26 | `edefter-ziyan-ve-mubeyyiz-mahkeme-karari-asistani` | VUK m. 13 Uyarınca e-Defter Zayi Belgesi ve Mücbir Sebep Başvuru Asistanı | `gpt-4o` |
| 27 | `edefter-uyumlu-yazilim-ve-xml-sema-kontrolu` | GİB Uyumlu Yazılım Defter XML Şema (XSD) Doğrulama Motoru | `gpt-4o` |
| 28 | `edefter-enflasyon-duzeltmesi-fark-kayit-denetleyicisi` | VUK 298/A Enflasyon Düzeltmesi 698 Hesap Yevmiye Denetleyicisi | `gpt-4o` |
| 29 | `edefter-denetim-ve-vergi-inceleme-paketi-hazirlayici` | VDK Müfettiş İncelemesi e-Defter Teftiş Paketi Hazırlayıcısı | `gpt-4o` |

*(Diğer tüm kategoriler ve 102 becerinin ayrıntılı açıklamaları için [SKILLS_REFERENCE.md](SKILLS_REFERENCE.md) dosyasını inceleyebilirsiniz).*

---

### 3. Diğer Kategoriler (Özet Dağılım)
- **e-İrsaliye & Lojistik:** 10 Beceri ([docs/03_eirsaliye_ve_lojistik.md](docs/03_eirsaliye_ve_lojistik.md))
- **e-İmza & Mali Mühür & PKI:** 15 Beceri ([docs/04_eimza_ve_malimuhur.md](docs/04_eimza_ve_malimuhur.md))
- **KEP & UETS & Elektronik Tebligat:** 12 Beceri ([docs/05_kep_ve_uets.md](docs/05_kep_ve_uets.md))
- **UYAP & Hukuk & LegalTech:** 16 Beceri ([docs/06_uyap_ve_hukuk.md](docs/06_uyap_ve_hukuk.md))
- **Vergi, SMMM & Beyanname Denetim:** 12 Beceri ([docs/07_smmm_ve_beyanname.md](docs/07_smmm_ve_beyanname.md))
- **KVKK, Dijital Kimlik & Siber Güvenlik:** 8 Beceri ([docs/08_kvkk_ve_guvenlik.md](docs/08_kvkk_ve_guvenlik.md))

---

## 🔗 eimza-kep Ekosistemi ve İlgili Projeler

Bu kütüphane, **[eimza-kep](https://github.com/eimza-kep)** organizasyonunun e-Dönüşüm araçları ve bilgi tabanları ile tam entegre çalışacak şekilde tasarlanmıştır:

- 🏛️ **[E-İmza Rehberi](https://eimzabilgi.site)** ([GitHub](https://github.com/eimza-kep/eimza-rehberi)): Elektronik imza kurulum, sürücü ve donanım rehberi
- 📮 **[KEP Akademisi](https://keprehberi.site)** ([GitHub](https://github.com/eimza-kep/kep-akademisi)): Kayıtlı Elektronik Posta (KEP) kullanım ve delil hukuku
- 🏢 **[Mali Mühür Merkezi](https://malimuhur.site)** ([GitHub](https://github.com/eimza-kep/mali-muhur-merkezi)): Mali mühür sertifikası ve şirket tür değişikliği yönetimi
- 🧾 **[E-Fatura Atölyesi](https://efaturabilgi.site)** ([GitHub](https://github.com/eimza-kep/efatura-atolyesi)): e-Fatura, e-Arşiv ve UBL-TR teknik atölyesi
- 💼 **[KOBİ E-Dönüşüm](https://edonusumkobi.site)** ([GitHub](https://github.com/eimza-kep/edonusum-kobi)): KOBİ'ler için e-Defter ve e-İrsaliye geçiş kılavuzu
- ⚖️ **[UYAP Teknik Destek](https://uyapteknikdestek.site)** ([GitHub](https://github.com/eimza-kep/uyap-teknik-destek)): Avukatlar ve hukuk büroları için UYAP & DYS desteği
- 🛡️ **[Dijital Kimlik & Güvenlik](https://kimlikguvenlik.site)** ([GitHub](https://github.com/eimza-kep/dijital-kimlik-guvenlik)): Dijital kimlik doğrulama, Zero Trust ve siber güvenlik
- 🔍 **[e-imza-validator](https://github.com/eimza-kep/e-imza-validator)**: PAdES, CAdES, XAdES doğrulama kütüphanesi
- 📑 **[e-fatura-validator](https://github.com/eimza-kep/e-fatura-validator)**: UBL-TR 1.2.1 şema ve schematron doğrulama motoru

---

## 🧪 Testleri Çalıştırma

Tüm 102 becerinin şema bütünlüğünü, değişken interpolasyonunu ve sistem promptu derinliğini doğrulamak için:

```bash
python test_skills.py
```

CI Test Çıktısı:
```text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

---

## 🤝 Katkıda Bulunma

1. Bu depoyu Fork edin (`gh repo fork eimza-kep/100-e-donusum-skili`).
2. Yeni beceri dalınızı oluşturun (`git checkout -b feature/yeni-skil`).
3. İlgili kategori dosyasına (`skills/category_XX_...py`) becerinizi ekleyin.
4. Testleri çalıştırın (`python test_skills.py`).
5. Dokümanları ve Web Playground'ı güncelleyin (`python generate_docs.py && python build_web.py`).
6. Değişikliklerinizi commit edin ve Pull Request açın.

---

## 📜 Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakınız.
