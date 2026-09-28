# 🚀 100 E-Dönüşüm Yapay Zeka Skili & Hazır Prompt Kütüphanesi

[![CI Test Suite](https://github.com/eimza-kep/100-e-donusum-skili/actions/workflows/ci.yml/badge.svg)](https://github.com/eimza-kep/100-e-donusum-skili/actions)
[![Skills Count](https://img.shields.io/badge/Beceriler-100%20Skil-blue.svg)](skills.json)
[![Categories](https://img.shields.io/badge/Kategori-8%20Ana%20Alan-orange.svg)](docs/)
[![Python](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-brightgreen.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/Lisans-MIT-green.svg)](LICENSE)
[![Organization](https://img.shields.io/badge/Organizasyon-eimza--kep-purple.svg)](https://github.com/eimza-kep)

**Türkiye E-Dönüşüm Ekosistemi (GİB, VUK, TTK, UETS, KEP, UYAP, KVKK)** standartlarına tam uyumlu; **Cursor, Claude, Antigravity, OpenAI GPT-4o ve Ollama/DeepSeek** ajanları için geliştirilmiş **100 uzman yapay zeka becerisi, sistem istemleri (system prompts) ve parametrik prompt şablonları.**

---

## 📌 Neden Bu Kütüphane?

Yapay zeka modelleri genel konularda başarılı olsa da, Türkiye e-Dönüşüm mevzuatındaki kritik ayrıntılarda (UBL-TR 1.2.1 şeması, KDV tevkifat oranları, 8 günlük ticari fatura itiraz süresi, berat hash algoritmaları, UETS 5 günlük yasal tebellüğ kuralı, UDF doküman yapısı, KVKK 72 saat kriz protokolü) sıklıkla halüsinasyon görür.

Bu kütüphane, **her biri mevzuat maddeleriyle (VUK, TTK, HMK, İİK, 5070, 6698) sınırlandırılmış ve doğrulanmış 100 uzman yapay zeka becerisini** hazır promptlar ve test edilmiş girdilerle sunar.

---

## 📁 Dizin Yapısı

```bash
100-e-donusum-skili/
├── .cursorrules                  # Cursor IDE kuralları ve beceri tanımları
├── claude_skills.xml             # Claude Projects için XML formatında sistem istemleri
├── skills.json                   # 100 becerinin makine tarafından okunabilir tam kataloğu
├── run_skill.py                  # CLI aracı (Arama, listeleme, mock çalıştırma, dışa aktarma)
├── test_skills.py                # 100 beceri için şema ve interpolasyon test paketi
├── generate_docs.py              # Otomatik dokümantasyon üretici
├── docs/                         # Kategori bazlı ayrıntılı dokümanlar
│   ├── 01_efatura_ve_earsiv.md   # e-Fatura & e-Arşiv Becerileri (Skills 1-15)
│   ├── 02_edefter_ve_berat.md    # e-Defter & Berat Becerileri (Skills 16-27)
│   ├── 03_eirsaliye_ve_lojistik.md# e-İrsaliye & Lojistik Becerileri (Skills 28-37)
│   ├── 04_eimza_ve_malimuhur.md  # e-İmza & Mali Mühür Becerileri (Skills 38-52)
│   ├── 05_kep_ve_uets.md         # KEP & UETS Becerileri (Skills 53-64)
│   ├── 06_uyap_ve_hukuk.md       # UYAP & LegalTech Becerileri (Skills 65-80)
│   ├── 07_smmm_ve_beyanname.md   # Vergi, SMMM & Beyanname Becerileri (Skills 81-92)
│   ├── 08_kvkk_ve_guvenlik.md    # KVKK & Siber Güvenlik Becerileri (Skills 93-100)
│   └── integration_guide.md      # Cursor, Claude, OpenAI & Ollama Entegrasyon Kılavuzu
└── skills/                       # Modüler Python beceri paketleri
    ├── __init__.py               # ALL_SKILLS, SKILLS_BY_ID, SKILLS_BY_CATEGORY
    ├── category_01_efatura.py    # 15 Beceri
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
# Kategorileri ve beceri sayılarını listele
python run_skill.py --categories

# Tüm 100 beceriyi listele
python run_skill.py --list

# Beceriler arasında arama yap (örn: 'tevkifat', 'irsaliye', 'uyap', 'kvkk')
python run_skill.py --search tevkifat

# Belirli bir becerinin promptunu ve değişkenlerini incele
python run_skill.py --skill efatura-kdv-tevkifat-denetleyici

# Beceriyi örnek girdilerle mock simülasyon olarak çalıştır
python run_skill.py --run efatura-kdv-tevkifat-denetleyici --mock

# Dışa aktarma araçları:
python run_skill.py --export-json     # skills.json üretir
python run_skill.py --export-claude   # claude_skills.xml üretir
python run_skill.py --export-cursor   # .cursorrules üretir
```

---

## 💻 Python Kütüphanesi Olarak Kullanım

```python
from skills import SKILLS_BY_ID

# İstenen beceriyi al
skill = SKILLS_BY_ID["efatura-8-gun-ticari-fatura-itiraz-yoneticisi"]

# Özel parametreleri hazırla
inputs = {
    "fatura_teblig_tarihi": "2026-09-20",
    "bugunun_tarihi": "2026-09-27",
    "itiraz_kanali": "KEP (Kayıtlı Elektronik Posta)",
    "itiraz_gerekcesi": "Sözleşme harici fiyat artışı ve eksik teslimat",
    "fatura_tutari": "145.000 TL"
}

# Şablonu doldur
user_prompt = skill["user_prompt_template"].format(**inputs)
system_prompt = skill["system_prompt"]

# OpenAI, Claude veya Anthropic API'sine gönder
print("SYSTEM:", system_prompt)
print("USER:", user_prompt)
```

---

## 📊 100 E-Dönüşüm Becerisi Tam Kataloğu

### 1. e-Fatura & e-Arşiv Becerileri (15 Beceri)
Detaylı doküman: [`docs/01_efatura_ve_earsiv.md`](docs/01_efatura_ve_earsiv.md)

| No | Beceri ID | Beceri Adı | Model |
|:---|:---|:---|:---|
| 1 | `efatura-ubl-anomali-avcisi` | UBL-TR 1.2.1 Şema ve Schematron Anomali Avcısı | `gpt-4o` |
| 2 | `efatura-kdv-tevkifat-denetleyici` | e-Fatura KDV Tevkifat Kod ve Oran Denetleyicisi | `gemini-1.5-flash` |
| 3 | `efatura-8-gun-ticari-fatura-itiraz-yoneticisi` | TTK m. 18/3 ve 21/2 Kapsamında 8 Günlük Ticari Fatura İtiraz Yöneticisi | `gpt-4o` |
| 4 | `efatura-earsiv-5bin-ve-vergisiz-limit-radari` | 509 Sıra No.lu VUK Kapsamında e-Arşiv Fatura Limit ve TCKN/VKN Radarı | `gpt-4o` |
| 5 | `efatura-istisna-ve-muafiyet-kod-eslestirici` | KDV İstisna Kodları (300'lü ve 350'li kodlar) ve GİB Eşleştirici | `gpt-4o` |
| 6 | `efatura-mukerrer-kayit-ve-sahte-fatura-tespiti` | Mükerrer e-Fatura ve Fatura Bölme Tespiti (VUK m. 359 Radarı) | `gpt-4o` |
| 7 | `efatura-temel-ticari-senaryo-karar-agaci` | Temel Fatura vs Ticari Fatura Senaryo Seçim Asistanı | `gemini-1.5-flash` |
| 8 | `efatura-dovizli-fatura-tcmb-kur-denetimi` | Dövizli e-Faturalarda TCMB Efektif/Döviz Alış Kuru Denetleyicisi | `gemini-1.5-flash` |
| 9 | `efatura-fiyat-artisi-ve-vade-farki-hesaplayici` | Fiyat Farkı ve Kur Farkı Faturası KDV/Matrah Ayrıştırıcı | `gpt-4o` |
| 10 | `efatura-mahsup-fisi-ve-muhasebe-kod-ureteci` | e-Fatura XML'inden TDHP Tekdüzen Hesap Planı Yevmiye Fişi Üreteci | `gpt-4o` |
| 11 | `efatura-otv-listesi-ve-ozel-matrah-denetleyicisi` | ÖTV Listeleri (I, II, III, IV Sayılı) ve Özel Matrah Şekli Analizörü | `gpt-4o` |
| 12 | `efatura-iade-ve-yansitma-faturasi-dogrulayici` | Satıştan İade ve Masraf Yansıtma Faturası Eşleştirici | `gemini-1.5-flash` |
| 13 | `efatura-vkn-tckn-gib-mukellef-sorgu-yardimcisi` | GİB e-Fatura Kayıtlı Kullanıcı ve Posta Kutusu Etiket Doğrulayıcısı | `gemini-1.5-flash` |
| 14 | `efatura-ba-bs-mutabakat-ve-anomali-dedektoru` | Form Ba-Bs ile e-Fatura/e-Arşiv Otomatik Çapraz Mutabakatçısı | `gpt-4o` |
| 15 | `efatura-eihracat-gtip-ve-gumruk-beyannamesi-eslestirici` | e-İhracat Faturası GTİP ve GÇB (Gümrük Çıkış Beyannamesi) Eşleştiricisi | `gpt-4o` |

---

### 2. e-Defter & Berat Becerileri (12 Beceri)
Detaylı doküman: [`docs/02_edefter_ve_berat.md`](docs/02_edefter_ve_berat.md)

| No | Beceri ID | Beceri Adı | Model |
|:---|:---|:---|:---|
| 16 | `edefter-yevmiye-kebir-balans-denetleyici` | e-Defter Yevmiye-Kebir Borç/Alacak Matematiksel Balans Denetleyicisi | `gpt-4o` |
| 17 | `edefter-ardisiklik-ve-tarih-tutarlilik-kontrolu` | Yevmiye Madde Numarası ve Tarih Ardışıklık Denetleyicisi | `gemini-1.5-flash` |
| 18 | `edefter-berat-sha256-hash-dogrulayici` | e-Defter Berat Dosyası SHA-256 Hash ve İmza Doğrulayıcısı | `gpt-4o` |
| 19 | `edefter-gib-zaman-damgasi-ve-onay-takipcisi` | GİB Onaylı Berat Zaman Damgası ve Berat İletim Doğrulayıcısı | `gemini-1.5-flash` |
| 20 | `edefter-belge-turu-documenttype-siniflandirici` | GİB e-Defter DocumentType (Fatura, Çek, Dekont vb.) Eşleştiricisi | `gemini-1.5-flash` |
| 21 | `edefter-odeme-yontemi-paymentmethod-standartlastirici` | Ödeme Yöntemi ve Kasa/Banka Tahsilat Standartlaştırıcısı | `gemini-1.5-flash` |
| 22 | `edefter-berat-yukleme-takvimi-ve-gecikme-riski-hesaplayici` | Aylık ve Geçici Vergi Dönemleri e-Defter Berat Yükleme Takvimi | `gemini-1.5-flash` |
| 23 | `edefter-ters-bakiye-ve-avans-hesaplari-radari` | 100 Kasa, 102 Banka ve 320/120 Ters Bakiye Denetleyicisi | `gpt-4o` |
| 24 | `edefter-parcali-defter-100mb-bolucu-asistan` | 100 MB Limitini Aşan e-Defterlerin Parçalanması ve XML Bütünlüğü | `gemini-1.5-flash` |
| 25 | `edefter-ikincil-kopya-gib-saklama-denetleyicisi` | GİB e-Defter İkincil Kopya Gönderim ve Arşiv Doğrulayıcısı | `gpt-4o` |
| 26 | `edefter-zayi-belgesi-ve-mubrum-sebep-yoneticisi` | Siber Saldırı veya Donanım Arızasında TTK m. 82/7 Zayi Belgesi Asistanı | `gpt-4o` |
| 27 | `edefter-ozel-entegrator-ve-yerel-yazilim-imza-uyumu` | e-Defter İmzalama Altyapısı (Mali Mühür vs Özel Entegratör İmzası) | `gpt-4o` |

---

### 3. e-İrsaliye & Lojistik Becerileri (10 Beceri)
Detaylı doküman: [`docs/03_eirsaliye_ve_lojistik.md`](docs/03_eirsaliye_ve_lojistik.md)

| No | Beceri ID | Beceri Adı | Model |
|:---|:---|:---|:---|
| 28 | `eirsaliye-karekod-ve-veri-ayristirma-asistani` | e-İrsaliye Karekod (QR Kod) Veri Ayrıştırma ve Doğrulama Asistanı | `gemini-1.5-flash` |
| 29 | `eirsaliye-fiili-sevk-saati-ve-zaman-denetimi` | Düzenleme Tarihi vs Fiili Sevk Saati/Zamanı Mevzuat Denetleyicisi | `gpt-4o` |
| 30 | `eirsaliye-plaka-ve-sofor-bilgisi-eksiklik-avcisi` | Taşıyıcı Bilgileri (Plaka, Şoför TCKN, Dorse) Doğrulayıcısı | `gemini-1.5-flash` |
| 31 | `eirsaliye-yanit-kabul-ret-kismi-kabul-yoneticisi` | e-İrsaliye Yanıtı (Kabul, Ret, Kısmi Kabul) Senaryo Yöneticisi | `gpt-4o` |
| 32 | `eirsaliye-irsaliyeli-fatura-ve-irsaliye-fatura-iliskisi` | e-İrsaliye - e-Fatura 7 Günlük Dönüştürme ve Eşleştirme Motoru | `gpt-4o` |
| 33 | `eirsaliye-hal-kayit-sistemi-hks-kunye-dogrulayici` | Yaş Sebze Meyve Ticaretinde HKS Künye Numarası ve e-İrsaliye Uyumu | `gpt-4o` |
| 34 | `eirsaliye-demir-celik-ve-otv-1-kapsam-denetleyicisi` | Demir-Çelik ve ÖTV-I Sayılı Liste Zorunlu e-İrsaliye Kapsam Radarı | `gpt-4o` |
| 35 | `eirsaliye-yol-denetimi-kolluk-ve-maliye-ibraz-rehberi` | Yol Denetiminde Maliye ve Kolluk Kuvvetlerine Karekod İbraz Rehberi | `gemini-1.5-flash` |
| 36 | `eirsaliye-konsinye-ve-zincirleme-sevk-asistani` | Konsinye Satış, Şubeler Arası Sevk ve Zincirleme Teslimat Mimarisi | `gpt-4o` |
| 37 | `eirsaliye-fason-uretim-ve-tamir-bakim-sevk-yoneticisi` | Fason Üretim, Boyahane ve Tamir Amaçlı Geçici Sevk İrsaliyesi | `gemini-1.5-flash` |

---

### 4. e-İmza & Mali Mühür & PKI Becerileri (15 Beceri)
Detaylı doküman: [`docs/04_eimza_ve_malimuhur.md`](docs/04_eimza_ve_malimuhur.md)

| No | Beceri ID | Beceri Adı | Model |
|:---|:---|:---|:---|
| 38 | `eimza-pades-cades-xades-imza-formati-dogrulayici` | ETSI PAdES, CAdES ve XAdES Elektronik İmza Formatı Doğrulayıcısı | `gpt-4o` |
| 39 | `eimza-sertifika-vade-ve-yenileme-sayaci` | Nitelikli Elektronik Sertifika (NES) Geçerlilik ve Kalan Gün Takipçisi | `gemini-1.5-flash` |
| 40 | `eimza-pin-puk-bloke-ve-akis-kurtarma-asistani` | AKİS Akıllı Kart PIN/PUK Bloke Çözme ve Sürücü Kurtarma Asistanı | `gemini-1.5-flash` |
| 41 | `eimza-akis-surucu-ve-kart-okuyucu-teshis-doktoru` | Akıllı Kart Okuyucu (Omnikey, ACS) ve AKİS Sürücü Teşhis Doktoru | `gemini-1.5-flash` |
| 42 | `malimuhur-unvan-ve-tur-degisikligi-muhur-yenileme-asistani` | Şirket Nevi/Unvan Değişikliğinde Mali Mühür İptal ve Yenileme Rehberi | `gpt-4o` |
| 43 | `malimuhur-tasfiye-donemi-ve-tasfiye-memuru-kullanimi` | Tasfiye Halindeki Şirketlerde Tasfiye Memuru Mali Mühür Kullanım Protokolü | `gpt-4o` |
| 44 | `eimza-kamu-sm-vs-ozel-eshs-secim-danismani` | TÜBİTAK Kamu SM vs Özel ESHS (E-Tuğra, TÜRKTRUST, E-İmzaTR) Seçim Danışmanı | `gemini-1.5-flash` |
| 45 | `eimza-mobil-imza-gsm-operator-ve-sim-kart-asistani` | GSM Mobil İmza (Turkcell, Vodafone, Türk Telekom) 5070 Eşdeğerlik Denetimi | `gemini-1.5-flash` |
| 46 | `eimza-zaman-damgasi-tsa-rfc3161-dogrulayici` | RFC 3161 Zaman Damgası (TSA) ve Hukuki İspat Gücü Doğrulayıcısı | `gpt-4o` |
| 47 | `eimza-yetkisiz-kullanim-ve-vekalet-riski-analizoru` | E-İmzanın Başkasına Kullandırılması Hukuki ve Cezai Risk Analizörü | `gpt-4o` |
| 48 | `eimza-macos-m1-m2-m3-arm64-surucu-rehberi` | macOS Apple Silicon (M1/M2/M3/M4) AKİS ve Java PKCS#11 Kurulum Rehberi | `gemini-1.5-flash` |
| 49 | `eimza-linux-pcscd-ve-libakisp11-konfiguratoru` | Linux (Ubuntu, Debian, Pardus) pcscd ve OpenSC / libakisp11 Yapılandırıcısı | `gemini-1.5-flash` |
| 50 | `eimza-pdf-gorsel-kase-ve-imza-yeri-koordinat-hesaplayici` | PDF İmzalama Görsel Kaşe (Signature Appearance) ve Koordinat Hesaplayıcı | `gemini-1.5-flash` |
| 51 | `eimza-yubikey-fido2-piv-ve-kurumsal-hsm-entegrasyonu` | YubiKey PIV SmartCard, Kurumsal HSM ve E-Dönüşüm İmzalama Mimarisi | `gpt-4o` |
| 52 | `eimza-crl-ve-ocsp-ile-anlik-iptal-kontrol-motoru` | X.509 CRL (İptal Listesi) ve OCSP ile Sertifika Geçerlilik Denetim Motoru | `gpt-4o` |

---

### 5. KEP & UETS & Elektronik Tebligat Becerileri (12 Beceri)
Detaylı doküman: [`docs/05_kep_ve_uets.md`](docs/05_kep_ve_uets.md)

| No | Beceri ID | Beceri Adı | Model |
|:---|:---|:---|:---|
| 53 | `kep-adresi-sozdizim-ve-saglayici-dogrulayici` | KEP Adresi Sözdizimi (RFC 5322) ve Yetkili Sağlayıcı Doğrulayıcısı | `gemini-1.5-flash` |
| 54 | `uets-adres-formati-ve-ulusal-tebligat-analizoru` | UETS Adres Formatı ve PTT Ulusal Elektronik Tebligat Analizörü | `gemini-1.5-flash` |
| 55 | `uets-5-gun-kurali-ve-kesin-teblig-tarihi-hesaplayici` | 7201 Sayılı Kanun m. 7/a Kapsamında UETS 5 Günlük Süre Hesaplayıcısı | `gpt-4o` |
| 56 | `kep-resmi-ihtarname-ve-sozlesme-fesih-metni-mimari` | TTK m. 18/3 Uyumlu KEP İhtarnamesi ve Sözleşme Fesih Metni Mimarı | `gpt-4o` |
| 57 | `kep-delil-paketi-eys-eas-ve-delil-hukuku-asistani` | KEP Delil Paketleri (EYS, EAS) ve Hukuki İspat Gücü Asistanı | `gpt-4o` |
| 58 | `kep-iik-89-1-haciz-ihbarnamesi-7-gun-itiraz-yoneticisi` | İİK 89/1 KEP Haciz İhbarnamesine Karşı 7 Günlük İtiraz Yöneticisi | `gpt-4o` |
| 59 | `kep-calisan-hakli-fesih-ve-savunma-talep-asistani` | 4857 Sayılı İş Kanunu Uyarınca KEP ile Savunma İstemi ve Haklı Fesih | `gpt-4o` |
| 60 | `kep-sirket-kurulusu-mersis-ve-zorunlu-kep-yonetimi` | Anonim ve Limited Şirketler İçin KEP Zorunluluğu ve MERSİS Entegrasyonu | `gemini-1.5-flash` |
| 61 | `kep-posta-kutusu-kota-ve-ekli-dosya-optimizasyonu` | KEP Posta Kutusu Kota ve Ekli Dosya Boyut (MB) Optimizasyon Asistanı | `gemini-1.5-flash` |
| 62 | `kep-arsivleme-ve-10-yil-saklama-sorumlulugu` | TTK m. 82 Uyarınca KEP İletileri ve Delil Paketlerini 10 Yıl Saklama Mimarı | `gpt-4o` |
| 63 | `kep-uets-farklari-ve-kamu-tebligat-rehberi` | Ticari KEP ve Resmi UETS Ayrımı ve Kamu Tebligat Rehberi | `gemini-1.5-flash` |
| 64 | `kep-ik-bordro-ve-ozluk-tebligat-sistemi` | Kurumsal İK Ücret Pusulası ve Bordro KEP Tebligat Mimarı | `gpt-4o` |

---

### 6. UYAP & Hukuk & LegalTech Becerileri (16 Beceri)
Detaylı doküman: [`docs/06_uyap_ve_hukuk.md`](docs/06_uyap_ve_hukuk.md)

| No | Beceri ID | Beceri Adı | Model |
|:---|:---|:---|:---|
| 65 | `uyap-udf-xml-yapisi-ve-etiket-ayristirici` | UYAP UDF 1.8 XML Doküman Yapısı ve Metadata Ayrıştırıcı | `gpt-4o` |
| 66 | `uyap-udf-to-markdown-ve-rag-vektor-donusturucu` | UDF Dosyalarını Markdown ve Hukuki RAG Vektör Verisine Dönüştürücü | `gemini-1.5-flash` |
| 67 | `uyap-editor-donma-ve-onbellek-onarim-doktoru` | UYAP Doküman Editörü Bellek (JVM Heap) ve Önbellek Onarım Doktoru | `gemini-1.5-flash` |
| 68 | `uyap-hmk-119-dava-dilekcesi-zorunlu-unsur-kontrolu` | HMK m. 119 Uyarınca Dava Dilekçesi Zorunlu Unsurlar Denetleyicisi | `gpt-4o` |
| 69 | `uyap-6325-arabuluculuk-son-tutanak-ve-dava-sarti-asistani` | 6325 Sayılı Kanun Arabuluculuk Son Tutanağı ve Dava Şartı Kontrolcüsü | `gpt-4o` |
| 70 | `uyap-iik-58-icra-takip-talebi-ve-odeme-emri-mimari` | İİK m. 58 İcra Takip Talebi ve Ödeme Emri Şablon Mimarı | `gpt-4o` |
| 71 | `uyap-aaut-vekalet-ucreti-ve-yargilama-gideri-hesaplayici` | AAÜT Nisbi/Maktu Vekalet Ücreti ve Harç/Gider Avansı Hesaplayıcı | `gpt-4o` |
| 72 | `uyap-yargitay-ictihat-ve-emsal-karar-ozetleyicisi` | Yargıtay Hukuk/Ceza Genel Kurulu Emsal Karar Özetleme ve Analizörü | `gpt-4o` |
| 73 | `uyap-adli-tatil-ve-sure-uzama-kurali-hesaplayici` | HMK m. 102-104 Adli Tatil ve Sürelerin Son Günü Hesaplayıcı | `gpt-4o` |
| 74 | `uyap-bilirkisi-raporuna-itiraz-ve-celiski-avcisi` | Bilirkişi Raporundaki Maddi Hata ve Çelişkileri Tespit Eden İtiraz Motoru | `gpt-4o` |
| 75 | `uyap-bam-istinaf-layihasi-ve-kesinlik-siniri-kontrolcusu` | HMK m. 341 Bölge Adliye Mahkemesi (BAM) İstinaf ve Kesinlik Sınırı Motoru | `gpt-4o` |
| 76 | `uyap-mohuk-yabanci-mahkeme-karari-tenfiz-asistani` | MÖHUK m. 50-58 Yabancı Mahkeme/Hakem Kararlarının Tenfizi Asistanı | `gpt-4o` |
| 77 | `uyap-ihtiyati-haciz-ve-ihtiyati-tedbir-talep-mimari` | İİK m. 257 İhtiyati Haciz ve HMK m. 389 İhtiyati Tedbir Dilekçe Mimarı | `gpt-4o` |
| 78 | `uyap-10mb-dosya-kucultme-ve-tiff-donusturucu` | UYAP Portal 10 MB Dosya Boyut Limiti Optimizasyon ve TIFF Dönüştürücü | `gemini-1.5-flash` |
| 79 | `uyap-vatandas-portali-dava-sorgu-ve-dosya-inceleme-rehberi` | UYAP Vatandaş Portalı Dava Dosyası İnceleme ve Harç Ödeme Rehberi | `gemini-1.5-flash` |
| 80 | `uyap-ceza-savunma-layihasi-ve-cmk-sure-asistani` | 5271 Sayılı CMK Uyarınca Ceza Savunma Layihası ve Temyiz Süre Asistanı | `gpt-4o` |

---

### 7. Vergi, SMMM & Beyanname Denetim Becerileri (12 Beceri)
Detaylı doküman: [`docs/07_smmm_ve_beyanname.md`](docs/07_smmm_ve_beyanname.md)

| No | Beceri ID | Beceri Adı | Model |
|:---|:---|:---|:---|
| 81 | `smmm-kdv1-beyanname-on-denetim-motoru` | 1 No'lu KDV Beyannamesi Ön Denetim ve Kümülatif Matrah Motoru | `gpt-4o` |
| 82 | `smmm-muhtasar-ve-prim-hizmet-mphb-denetimi` | Muhtasar ve Prim Hizmet Beyannamesi (MPHB) Stopaj/SGK Denetleyicisi | `gpt-4o` |
| 83 | `smmm-gecici-vergi-kkeg-ve-oran-denetleyicisi` | Geçici Vergi, KKEG (Kanunen Kabul Edilmeyen Gider) ve %25 KV Denetleyicisi | `gpt-4o` |
| 84 | `smmm-arge-ve-teknopark-vergi-istisnasi-radari` | 4691 Sayılı Teknopark ve 5746 Sayılı Ar-Ge İstisna/Muafiyet Radarı | `gpt-4o` |
| 85 | `smmm-esmm-brutten-nete-hesaplama-motoru` | e-SMM Brütten Nete ve Netten Brüte Makbuz Hesaplama Motoru | `gemini-1.5-flash` |
| 86 | `smmm-kidem-ihbar-tavani-ve-damga-vergisi-hesaplayici` | Kıdem Tazminatı Tavanı, İhbar Tazminatı ve Damga Vergisi Hesaplayıcı | `gpt-4o` |
| 87 | `smmm-vuk-315-amortisman-ve-itfa-plani-denetleyicisi` | VUK m. 315 Amortisman Listesi, Kıst Amortisman ve İtfa Planı Denetleyicisi | `gemini-1.5-flash` |
| 88 | `smmm-enflasyon-duzeltmesi-vuk-298a-asistani` | VUK Geçici 33 ve Mükerrer 298/A Kapsamında Enflasyon Düzeltmesi Asistanı | `gpt-4o` |
| 89 | `smmm-vergi-ceza-ihbarnamesi-376-ve-uzlasma-danismani` | VUK m. 376 İndirim vs Tarhiyat Öncesi/Sonrası Uzlaşma Karar Motoru | `gpt-4o` |
| 90 | `smmm-sahte-fatura-vuk-359-ve-kod-listesi-riski` | Sahte Fatura (VUK m. 359) ve Özel Esaslar (Kod Listesi) Risk Analizörü | `gpt-4o` |
| 91 | `smmm-5510-sgk-tesvik-ve-istihdam-destek-eslestirici` | 5510 Sayılı Kanun %5 Prim İndirimi ve İlave İstihdam Teşvik Eşleştiricisi | `gpt-4o` |
| 92 | `smmm-mizan-ve-cfo-finansal-rasyo-analizoru` | Mizan Analizi, Cari Oran, Likidite ve Asit-Test CFO Rasyo Analizörü | `gpt-4o` |

---

### 8. KVKK, Dijital Kimlik & Siber Güvenlik Becerileri (8 Beceri)
Detaylı doküman: [`docs/08_kvkk_ve_guvenlik.md`](docs/08_kvkk_ve_guvenlik.md)

| No | Beceri ID | Beceri Adı | Model |
|:---|:---|:---|:---|
| 93 | `kvkk-11-madde-ilgili-kisi-basvuru-asistani` | KVKK Madde 11 İlgili Kişi Başvuru ve 30 Günlük Yasal Cevap Asistanı | `gpt-4o` |
| 94 | `kvkk-aydinlatma-metni-ve-acik-riza-mimari` | KVKK m. 10 Aydınlatma Metni ve Açık Rıza Ayrım Mimarı | `gpt-4o` |
| 95 | `kvkk-verbis-veri-envanteri-kontrolcusu` | VERBİS Kayıt Eşiği ve Kişisel Veri İşleme Envanteri Denetleyicisi | `gpt-4o` |
| 96 | `kvkk-veri-ihlali-ve-kuruma-72-saat-bildirimi` | KVKK Veri İhlali Bildirim Formu ve 72 Saat Kriz Protokolü | `gpt-4o` |
| 97 | `guvenlik-oltalama-ve-sahte-efatura-analizoru` | Sahte E-Fatura, KEP ve GİB Kimlik Avı (Phishing) Analizörü | `gpt-4o` |
| 98 | `guvenlik-api-anahtari-ve-byok-denetleyicisi` | E-Dönüşüm Entegratör API Anahtarı, HSM ve BYOK Güvenlik Denetleyicisi | `gpt-4o` |
| 99 | `guvenlik-kisisel-veri-anonimlestirme-maskeleyici` | E-Dönüşüm Veri Maskeleme ve Pseudonimleştirme Aracı | `gpt-4o` |
| 100 | `guvenlik-zero-trust-e-donusum-mimari` | Zero Trust (Sıfır Güven) E-Dönüşüm ve E-Defter Saklama Mimarisi | `gpt-4o` |

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

Tüm 100 becerinin şema bütünlüğünü, değişken interpolasyonunu ve sistem promptu derinliğini doğrulamak için:

```bash
python test_skills.py
```

---

## 🤝 Katkıda Bulunma

1. Bu depoyu Fork edin (`gh repo fork eimza-kep/100-e-donusum-skili`).
2. Yeni beceri dalınızı oluşturun (`git checkout -b feature/yeni-skil`).
3. İlgili kategori dosyasına (`skills/category_XX_...py`) becerinizi ekleyin.
4. Testleri çalıştırın (`python test_skills.py`).
5. Dokümanları güncelleyin (`python generate_docs.py`).
6. Değişikliklerinizi commit edin ve Pull Request açın.

---

## 📜 Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakınız.
