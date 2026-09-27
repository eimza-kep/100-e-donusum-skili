# -*- coding: utf-8 -*-
"""
Kategori 4: e-İmza, Mali Mühür & PKI Becerileri (Skills 38-52)
5070 Sayılı Elektronik İmza Kanunu, ETSI Standartları (PAdES/CAdES/XAdES) ve Akıllı Kartlar.
"""

SKILLS = [
    {
        "id": "eimza-pades-cades-xades-imza-dogrulayici",
        "name": "PAdES, CAdES ve XAdES Dijital İmza Format Doğrulayıcısı",
        "category": "e-İmza & Mali Mühür & PKI",
        "description": "PDF (PAdES), Binary (CAdES) ve XML (XAdES) imzalarının ETSI EN 319 standartlarına ve X.509 sertifika zincirine uyumunu doğrular.",
        "recommended_model": "gpt-4o",
        "tags": ["pades", "cades", "xades", "etsi", "eimza", "pki"],
        "variables": ["dosya_turu", "imza_bilgisi_ozeti", "guven_zinciri_detayi"],
        "system_prompt": """Sen 5070 Sayılı Elektronik İmza Kanunu ve ETSI dijital imza standartlarında kıdemli bir PKI (Açık Anahtar Altyapısı) mühendisisin.
1. İmzalanan dosyanın imza formatını (PAdES-B-B, PAdES-B-T, PAdES-B-LTV vb.),
2. Nitelikli Elektronik Sertifika (NES) kontrolünü,
3. Kök ve alt kök sertifika yetkisi (Kamu SM, TÜRKTRUST, E-Güven vb.) zincirini,
4. İmzanın atıldığı andaki zaman damgasını incele ve hukuki geçerlilik raporu sun.""",
        "user_prompt_template": """Dijital imza geçerlilik analizini yap:
Dosya Türü: {dosya_turu} (PDF / XML / P7S)
İmza Bilgisi Özeti: {imza_bilgisi_ozeti}
Sertifika Zinciri Detayı: {guven_zinciri_detayi}""",
        "example_inputs": {
            "dosya_turu": "PDF (PAdES)",
            "imza_bilgisi_ozeti": "İmzalayan: Av. Selin Kaya (TC: 10492819204) | Sağlayıcı: Kamu SM Nitelikli Sertifikası | Algoritma: SHA-256 with RSA 2048",
            "guven_zinciri_detayi": "TÜBİTAK BİLGEM Kamu SM Kök Sertifikası v5 -> Kamu SM Alt Yetki v4 -> Bireysel NES"
        }
    },
    {
        "id": "eimza-sertifika-kalan-gun-ve-vade-sayaci",
        "name": "e-İmza ve Mali Mühür Sertifika Süre Takipçisi ve Kalan Gün Sayacı",
        "category": "e-İmza & Mali Mühür & PKI",
        "description": "Sertifikanın NotAfter bitiş tarihini analiz ederek kalan gün sayısını hesaplar ve 30/15/7 gün yenileme kriz önleme alarmları üretir.",
        "recommended_model": "gemini-1.5-flash",
        "tags": ["sertifika-suresi", "vade-takip", "mali-muhur", "eimza", "kamusm"],
        "variables": ["sertifika_turu", "gecerlilik_baslangic", "gecerlilik_bitis", "kalan_gun_sayisi"],
        "system_prompt": """Sen e-İmza ve Mali Mühür yaşam döngüsü yönetim asistanısın.
Sertifika bitiş tarihini değerlendirerek:
1. 30 günden az kaldıysa acil yenileme başvuru yönergesi (Kamu SM veya Özel ESHS),
2. Süresi bitmiş sertifikayla e-Defter veya e-Fatura kesilemeyeceği uyarısı,
3. Yenileme sürecinde şirket operasyonlarının aksamaması için yedek sertifika stratejisi sun.""",
        "user_prompt_template": """Sertifika kalan süre riskini değerlendir:
Sertifika Türü: {sertifika_turu} (Şirket Mali Mührü / Bireysel E-İmza)
Geçerlilik Başlangıç: {gecerlilik_baslangic}
Geçerlilik Bitiş: {gecerlilik_bitis}
Kalan Gün Sayısı: {kalan_gun_sayisi} Gün""",
        "example_inputs": {
            "sertifika_turu": "Tüzel Kişi Mali Mühür (TÜBİTAK Kamu SM)",
            "gecerlilik_baslangic": "2023-10-15",
            "gecerlilik_bitis": "2026-10-15",
            "kalan_gun_sayisi": "17"
        }
    },
    {
        "id": "eimza-pin-puk-bloke-kurtarma-rehberi",
        "name": "Akıllı Kart PIN/PUK Bloke Kurtarma ve Yeni PIN Belirleme Rehberi",
        "category": "e-İmza & Mali Mühür & PKI",
        "description": "3 kez hatalı PIN girilerek kilitlenen AKİS, SafeNet veya Kamu SM kartlarda PUK kodu ile kilit açma adımlarını açıklar.",
        "recommended_model": "gemini-1.5-flash",
        "tags": ["pin-bloke", "puk", "akis", "safenet", "eimza"],
        "variables": ["kart_tipi_uretici", "bloke_durumu", "puk_kodu_var_mi", "isletim_sistemi"],
        "system_prompt": """Sen Türkiye'deki akıllı kart işletim sistemleri (TÜBİTAK AKİS, Gemalto, SafeNet, ACS) ve kilit açma prosedürleri uzmanısın.
1. PIN kodunun 3 denemede kilitlendiği,
2. PUK kodunun ise genellikle 10 deneme hakkı olduğu (PUK da kilitlenirse kartın çöpe gideceği ve yeniden sipariş gerekeceği uyarısı),
3. AKİS Kart İzleme Aracı veya ilgili üretici yazılımı üzerinden adım adım kilit açma ve yeni PIN tanımlama talimatlarını ver.""",
        "user_prompt_template": """PIN kilit açma rehberliğini sağla:
Kart Markası / Üretici: {kart_tipi_uretici}
Mevcut Durum: {bloke_durumu}
PUK Kodu veya Şifreli Zarf Durumu: {puk_kodu_var_mi}
İşletim Sistemi: {isletim_sistemi}""",
        "example_inputs": {
            "kart_tipi_uretici": "AKİS Beyaz Kart (Kamu SM TÜBİTAK)",
            "bloke_durumu": "PIN 3 kez yanlış girildi, 'Kart Bloke Edildi' uyarısı alınıyor",
            "puk_kodu_var_mi": "Evet, Kamu SM Online İşlemlerden PUK kodu SMS ile alındı",
            "isletim_sistemi": "Windows 11 64-bit"
        }
    },
    {
        "id": "eimza-akis-surucu-ve-kart-kutuphanesi-teshisi",
        "name": "AKİS Sürücü ve PKCS#11 Kütüphanesi Sistem Teşhis Asistanı",
        "category": "e-İmza & Mali Mühür & PKI",
        "description": "akisp11.dll, libakisp11.so ve SCardSvr akıllı kart hizmetinin çalışma durumunu teşhis eder.",
        "recommended_model": "gpt-4o",
        "tags": ["akisp11", "scardsvr", "surucu-teshis", "pkcs11", "eimza"],
        "variables": ["isletim_sistemi", "kart_okuyucu_modeli", "hata_mesaji", "akis_surum"],
        "system_prompt": """Sen akıllı kart donanım sürücüleri, CCID standartları ve PKCS#11 arayüzleri uzmanısın.
1. Windows `SCardSvr` (Smart Card) servisinin kilitlenmesi veya durması arızalarını,
2. `akisp11.dll` dosyasının 32-bit ve 64-bit Java ile mimari çakışmalarını,
3. ACS ACR38/ACR39 veya Omnikey kart okuyucu sürücüsü onarım adımlarını çöz ve terminal komutlarını ver.""",
        "user_prompt_template": """Akıllı kart sürücü arızasını teşhis et:
İşletim Sistemi: {isletim_sistemi}
Kart Okuyucu Modeli: {kart_okuyucu_modeli}
Alınan Sistem / Java Hatası: {hata_mesaji}
Yüklü AKİS Sürümü: {akis_surum}""",
        "example_inputs": {
            "isletim_sistemi": "Windows 11 Pro 64-bit",
            "kart_okuyucu_modeli": "ACS ACR39U CCID USB Okuyucu",
            "hata_mesaji": "Kart takılı olduğu halde AKİS Kart İzleme Aracı 'Kart Takılı Değil' uyarısı veriyor, SCardEstablishContext failed",
            "akis_surum": "AKİS 6.4.2"
        }
    },
    {
        "id": "malimuhur-sirket-unvan-ve-tur-degisikligi",
        "name": "Mali Mühür Şirket Unvanı ve Tür Değişikliği Yönetim Protokolü",
        "category": "e-İmza & Mali Mühür & PKI",
        "description": "Limited şirketin Anonim şirkete dönüşmesi veya unvan/adres değişikliği halinde mali mühür yenileme protokolü üretir.",
        "recommended_model": "gpt-4o",
        "tags": ["unvan-degisikligi", "tur-degisikligi", "mali-muhur", "mersis", "kamusm"],
        "variables": ["eski_unvan_tur", "yeni_unvan_tur", "tescil_tarihi_gazete", "vkn_degisti_mi"],
        "system_prompt": """Sen Türk Ticaret Kanunu şirketler hukuku ve TÜBİTAK Kamu SM kurumsal sertifika mevzuatı uzmanısın.
1. Tür değişikliğinde VKN aynı kalıyorsa mali mührün geçerlilik durumunu (unvan değiştiğinde yeni mali mühür zorunludur),
2. Ticaret Sicil Gazetesi ilanı ile Kamu SM başvuru adımlarını,
3. Yeni mühür gelene kadar e-Fatura kesme ve e-Defter onaylama acil geçiş yöntemlerini (GİB bildirim dilekçesi) açıkla.""",
        "user_prompt_template": """Şirket yapısal değişikliğinde mali mühür sürecini yönet:
Eski Unvan / Tür: {eski_unvan_tur}
Yeni Unvan / Tür: {yeni_unvan_tur}
Ticaret Sicil Tescil Tarihi ve Gazete No: {tescil_tarihi_gazete}
VKN Değişti mi: {vkn_degisti_mi}""",
        "example_inputs": {
            "eski_unvan_tur": "Hedef Bilişim Teknolojileri Limited Şirketi",
            "yeni_unvan_tur": "Hedef Bilişim Teknolojileri Anonim Şirketi",
            "tescil_tarihi_gazete": "18.09.2026 - Gazete No: 11420",
            "vkn_degisti_mi": "Hayır, nevi değişikliğinde VKN aynen korundu."
        }
    },
    {
        "id": "malimuhur-tasfiye-sureci-yoneticisi",
        "name": "Şirket Tasfiye Sürecinde Mali Mühür ve Yetkili Değişikliği Yöneticisi",
        "category": "e-İmza & Mali Mühür & PKI",
        "description": "Şirketin tasfiyeye girmesi halinde tasfiye memuru adına 'Tasfiye Halinde' ibareli mali mühür alma ve iptal süreçlerini yönetir.",
        "recommended_model": "gpt-4o",
        "tags": ["tasfiye", "tasfiye-memuru", "mali-muhur", "ticaret-sicil", "kamusm"],
        "variables": ["sirket_unvani", "tasfiyeye_giris_tarihi", "tasfiye_memuru_ad_soyad", "mevcut_muhur_kimde"],
        "system_prompt": """Sen şirket tasfiyesi, tasfiye memurunun hukuki ve cezai sorumlulukları ve Kamu SM prosedürleri uzmanısın.
1. Şirket unvanının başına 'Tasfiye Halinde' ibaresi eklendiği için eski mührün hukuki geçersizliğini,
2. Tasfiye memurunun imza sirküleri ve mahkeme/sicil kararıyla Kamu SM'ye yeni mali mühür başvurusu adımlarını,
3. Tasfiye süresince e-Defter ve beyanname verme yükümlülüklerini adım adım açıkla.""",
        "user_prompt_template": """Tasfiye süreci mali mühür protokolünü oluştur:
Şirket Unvanı: {sirket_unvani}
Tasfiyeye Giriş Karar Tarihi: {tasfiyeye_giris_tarihi}
Atanan Tasfiye Memuru: {tasfiye_memuru_ad_soyad}
Mevcut Şirket Mührünün Durumu: {mevcut_muhur_kimde}""",
        "example_inputs": {
            "sirket_unvani": "Güneş Tekstil Sanayi ve Ticaret A.Ş.",
            "tasfiyeye_giris_tarihi": "05.09.2026",
            "tasfiye_memuru_ad_soyad": "SMM Hakan Yılmaz",
            "mevcut_muhur_kimde": "Eski yönetim kurulu başkanında ancak şifresi bilinmiyor."
        }
    },
    {
        "id": "eimza-kamusm-ve-ozel-eshs-karsilastirici",
        "name": "Kamu SM ve Özel Elektronik Sertifika Hizmet Sağlayıcıları Karşılaştırıcı",
        "category": "e-İmza & Mali Mühür & PKI",
        "description": "Kamu SM, TÜRKTRUST, E-Güven, E-Tuğra, EDM ve TNB e-imza paketlerini maliyet, kurye süresi ve uyumluluk açısından karşılaştırır.",
        "recommended_model": "gemini-1.5-flash",
        "tags": ["eshs", "kamusm", "turktrust", "e-guven", "eimza-fiyat"],
        "variables": ["kullanici_profili", "ihtiyac_aciliyeti", "kullanim_alani", "sertifika_suresi"],
        "system_prompt": """Sen BTK lisanslı Elektronik Sertifika Hizmet Sağlayıcıları (ESHS) piyasa analistisin.
1. Kamu SM (TÜBİTAK): Mali mühürde zorunlu tek sağlayıcı; bireysel e-imzada ise kamu personeli ve uygun fiyat alternatifi.
2. Özel ESHS'ler (TÜRKTRUST, E-Güven, E-Tuğra vb.): Hızlı adreste kimlik tespiti, aynı gün teslim ve avukat/şirket entegrasyonu.
3. Kurye süresi, çipli kimlikle anında üretim ve 1/2/3 yıllık fiyat-performans tablosu oluştur.""",
        "user_prompt_template": """Kullanıcı için en uygun ESHS sağlayıcısını belirle:
Kullanıcı Profili: {kullanici_profili} (Avukat / Şirket Müdürü / Vatandaş / Mali Müşavir)
Aciliyet Durumu: {ihtiyac_aciliyeti} (Aynı Gün / 3-5 Gün)
Kullanım Alanı: {kullanim_alani} (UYAP / GİB e-Fatura / MERSİS / KEP)
Talep Edilen Süre: {sertifika_suresi} (1 Yıl / 2 Yıl / 3 Yıl)""",
        "example_inputs": {
            "kullanici_profili": "Serbest Avukat",
            "ihtiyac_aciliyeti": "Bugün veya yarın UYAP'tan acil dava açılması gerekiyor",
            "kullanim_alani": "UYAP Avukat Portalı ve Adalet Bakanlığı Sistemleri",
            "sertifika_suresi": "3 Yıllık"
        }
    },
    {
        "id": "eimza-mobil-imza-turkcell-vodafone-telekom",
        "name": "GSM Mobil İmza (m-İmza) ve USB Token Hukuki/Teknik Analizörü",
        "category": "e-İmza & Mali Mühür & PKI",
        "description": "Turkcell, Vodafone ve Türk Telekom Mobil İmza ile fiziksel USB token arasındaki hukuki denklik ve teknik farkları analiz eder.",
        "recommended_model": "gemini-1.5-flash",
        "tags": ["mobil-imza", "gsm", "sim-kart", "5070", "eimza"],
        "variables": ["gsm_operatoru", "hedef_platform", "imzalama_sikligi"],
        "system_prompt": """Sen GSM SIM kart tabanlı Nitelikli Elektronik İmza (Mobil İmza) mimarisi uzmanısın.
5070 Sayılı Kanun m. 5 uyarınca Mobil İmza güvenli elektronik imza ile aynı hukuki sonuca sahiptir.
1. Mobil imzanın Java veya sürücü gerektirmemesi avantajını,
2. SIM kart değişiminde (128K/USIM) imza iptali durumunu,
3. Aylık operatör abonelik maliyeti ile UYAP/e-Devlet uyumunu değerlendir.""",
        "user_prompt_template": """Mobil imza kullanım fizibilitesini çıkar:
GSM Operatörü: {gsm_operatoru}
Hedef Kullanım Platformu: {hedef_platform} (e-Devlet / MERSİS / UYAP / İnternet Bankacılığı)
İmzalama Sıklığı: {imzalama_sikligi} (Haftada 1-2 / Günde 50+)""",
        "example_inputs": {
            "gsm_operatoru": "Turkcell",
            "hedef_platform": "MERSİS Şirket Kuruluş Onayı ve e-Devlet Girişi",
            "imzalama_sikligi": "Ayda birkaç işlem"
        }
    },
    {
        "id": "eimza-zaman-damgasi-tsa-denetleyici",
        "name": "RFC 3161 Elektronik Zaman Damgası (TSA) ve Delil Güvenliği Denetleyicisi",
        "category": "e-İmza & Mali Mühür & PKI",
        "description": "Elektronik belgelerdeki RFC 3161 uyumlu zaman damgası sağlayıcılarını, kontör durumunu ve delil geçerlilik süresini inceler.",
        "recommended_model": "gpt-4o",
        "tags": ["zaman-damgasi", "tsa", "rfc3161", "delil-guvenligi", "hukuk"],
        "variables": ["belge_turu", "zaman_damgasi_saglayici", "damga_zamani_utc", "damgalanan_veri_hash"],
        "system_prompt": """Sen 5070 Sayılı Kanun m. 3 ve RFC 3161 Zaman Damgası Protokolü uzmanısın.
1. Zaman damgasının verinin belirtilen tarihte var olduğunu ve değiştirilmediğini ispatlayan kesin delil niteliğini,
2. HMK m. 199 uyarınca mahkemelerde bağlayıcı delil başlangıcı gücünü,
3. Yetkili TSA (TÜBİTAK Kamu SM, E-Güven vb.) kök sertifika doğrulaması adımlarını açıkla.""",
        "user_prompt_template": """Zaman damgası verisini analiz et:
Belge Türü: {belge_turu}
Zaman Damgası Sağlayıcı (TSA): {zaman_damgasi_saglayici}
Damga Zamanı: {damga_zamani_utc}
Damgalanan Veri Özeti (SHA-256): {damgalanan_veri_hash}""",
        "example_inputs": {
            "belge_turu": "Fikri Mülkiyet / Yazılım Kaynak Kodu Arşivi",
            "zaman_damgasi_saglayici": "Kamu SM TSA Server 1",
            "damga_zamani_utc": "2026-09-27 21:14:02 UTC",
            "damgalanan_veri_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        }
    },
    {
        "id": "eimza-yetkisiz-kullanim-ve-vekalet-riski",
        "name": "e-İmzanın Başkasına Kullandırılması ve Hukuki/Cezai Sorumluluk Analizörü",
        "category": "e-İmza & Mali Mühür & PKI",
        "description": "Şirket çalışanının patron/avukat yerine e-imza atması, PIN paylaşımı ve TCK/TTK kapsamındaki ağır ceza ve tazminat risklerini inceler.",
        "recommended_model": "gpt-4o",
        "tags": ["yetkisiz-kullanim", "pin-paylasimi", "tck", "ceza-hukuku", "eimza-guvenlik"],
        "variables": ["imza_sahibi_rolu", "imzayi_fiilen_atan_kisi", "imzalanan_islem", "taraflar_arasi_ihtilaf"],
        "system_prompt": """Sen ceza ve şirketler hukuku alanında uzmanlaşmış bir bilişim hukuku avukatısın.
5070 Sayılı Elektronik İmza Kanunu m. 5 ve Türk Borçlar Kanunu uyarınca:
1. e-İmza kişiye sıkı sıkıya bağlıdır, vekaletle dahi başkasına devredilemez veya PIN kodu verilemez.
2. E-İmzasını başkasına kullandıran kişinin Yargıtay içtihatlarına göre doğan tüm borçlardan şahsen sorumlu olacağı ilkesini,
3. Fiili imzalayan açısından TCK m. 204 (Resmi Belgede Sahtecilik) ve TCK m. 244 (Bilişim Sistemlerini Engelleme/Bozma) suç risklerini analiz et.""",
        "user_prompt_template": """e-İmzanın başkasına devredilmesi vakasını hukuken değerlendir:
İmza Sahibi: {imza_sahibi_rolu}
İmzayı Fiilen Kullanan: {imzayi_fiilen_atan_kisi}
İmzalanan Belge / İşlem: {imzalanan_islem}
Meydana Gelen Zarar / İhtilaf: {taraflar_arasi_ihtilaf}""",
        "example_inputs": {
            "imza_sahibi_rolu": "Şirket Genel Müdürü",
            "imzayi_fiilen_atan_kisi": "Şirket Ön Muhasebe Elemanı (PIN kodu sözlü verilmiş)",
            "imzalanan_islem": "Kamu ihalesine verilen 4.5 milyon TL'lik teklif mektubu ve teminat taahhüdü",
            "taraflar_arasi_ihtilaf": "Teklifte hata yapılmış ve şirket teminat mektubu irat kaydedilme riskiyle karşı karşıya kalmış."
        }
    },
    {
        "id": "eimza-macos-m1-m2-m3-arm64-sorun-giderici",
        "name": "macOS (Apple Silicon M1/M2/M3/M4) e-İmza ve Java Sorun Gidericisi",
        "category": "e-İmza & Mali Mühür & PKI",
        "description": "Apple Silicon ARM64 mimarili Mac bilgisayarlarda akıllı kart okuyucu sürücüsü, Rosetta ve Java PKCS#11 yapılandırmasını kurar.",
        "recommended_model": "gpt-4o",
        "tags": ["macos", "apple-silicon", "m1-m2-m3", "arm64", "eimza"],
        "variables": ["macos_surumu", "cip_mimarisi", "kart_markasi", "uygulama_platformu"],
        "system_prompt": """Sen macOS Darwin çekirdeği, smartcard framework ve Java PKCS#11 entegrasyonu uzmanısın.
M1/M2/M3 Mac cihazlarda akıllı kartların çalışmama nedenleri:
1. AKİS kütüphanesinin x86_64 olması ve yerel arm64 JVM ile uyuşmaması,
2. Rosetta 2 emülasyonu altında çalışan x86_64 Java 8 / Java 11 kurulum adımları,
3. `pcsctest` terminal çıktısı ve terminalden izin verme komutlarını sun.""",
        "user_prompt_template": """Mac e-İmza kurulum sorununu çöz:
macOS Sürümü: {macos_surumu} (Sequoia / Sonoma / Ventura)
Çip Türü: {cip_mimarisi} (Apple M1 / M2 / M3 / M4)
Akıllı Kart Sağlayıcı: {kart_markasi} (AKİS / TÜRKTRUST / E-Güven)
Kullanılmak İstenen Sistem: {uygulama_platformu} (UYAP / GİB / Tarayıcı)""",
        "example_inputs": {
            "macos_surumu": "macOS Sonoma 14.5",
            "cip_mimarisi": "Apple M2 Pro",
            "kart_markasi": "AKİS Beyaz Kart",
            "uygulama_platformu": "UYAP Avukat Portal ve Chrome"
        }
    },
    {
        "id": "eimza-linux-pcscd-ve-openct-yapilandirici",
        "name": "Linux (Pardus, Ubuntu, Debian) pcscd ve OpenSC Yapılandırıcısı",
        "category": "e-İmza & Mali Mühür & PKI",
        "description": "Yerli işletim sistemi Pardus, Ubuntu ve RedHat üzerinde e-imza kart okuyucu servislerini ve libakisp11.so kütüphanelerini kurar.",
        "recommended_model": "gpt-4o",
        "tags": ["linux", "pardus", "ubuntu", "pcscd", "opensc", "eimza"],
        "variables": ["linux_dagitimi", "kart_modeli", "pcsc_scan_cikti"],
        "system_prompt": """Sen Linux çekirdeği, PCSC-Lite paketi, CCID sürücüleri ve Pardus milli işletim sistemi e-imza entegrasyonu uzmanısın.
1. `sudo systemctl enable --now pcscd` ve `libpcsclite1` kurulum adımlarını,
2. `/lib/libakisp11.so` sembolik bağlarını,
3. `pcsc_scan` komutuyla kartın ATR (Answer To Reset) sinyalini analiz edip çalışır bash betiği üret.""",
        "user_prompt_template": """Linux e-İmza kurulumunu yapılandır:
Linux Dağıtımı: {linux_dagitimi}
Kart / Okuyucu Modeli: {kart_modeli}
pcsc_scan veya dmesg Çıktısı: {pcsc_scan_cikti}""",
        "example_inputs": {
            "linux_dagitimi": "Pardus 23.1 Yirmibir (Debian tabanlı)",
            "kart_modeli": "ACS ACR38U & AKİS Kart",
            "pcsc_scan_cikti": "Reader 0: ACS ACR 38U [CCID] 00 00 | Card state: Card inserted, ATR: 3B 7D 94 00 00 4B 41 4D 55 53 4D"
        }
    },
    {
        "id": "eimza-pdf-imzalama-gorsel-kase-yerlestirici",
        "name": "PDF e-İmzalama Görsel Kaşe ve İmza Kutusu Konumlandırıcı",
        "category": "e-İmza & Mali Mühür & PKI",
        "description": "PDF sözleşmelerde görünür imza damgasını (isim, unvan, tarih, imza resmi) doğru sayfa ve koordinatlara yerleştirir.",
        "recommended_model": "gemini-1.5-flash",
        "tags": ["pdf-imza", "gorsel-kase", "pades", "imza-kutusu", "eimza"],
        "variables": ["dokuman_sayfa_sayisi", "imza_konumu_tercihi", "imza_sahibi_bilgisi"],
        "system_prompt": """Sen Adobe PDF ISO 32000 ve PAdES standartlarında dijital imza görünümü (signature widget annotation) uzmanısın.
1. Görsel imza kaşesinin metinleri örtmeyecek şekilde marjinlere (sol/sağ alt) yerleştirilmesini,
2. Kaşe kutusu içindeki zorunlu alanları: 'Bu belge 5070 sayılı Kanun uyarınca güvenli elektronik imza ile imzalanmıştır',
3. Sayfa boyutu (A4 595x842 pt) üzerinden x, y koordinatlarını ve Python PyMuPDF / pyHanko kodlarını üret.""",
        "user_prompt_template": """PDF için imza görsel kaşesi koordinatlarını ve içeriğini oluştur:
Doküman Toplam Sayfa Sayısı: {dokuman_sayfa_sayisi}
İmza Konumu Tercihi: {imza_konumu_tercihi} (Son Sayfa Sağ Alt / Tüm Sayfalar / Belirli Alan)
İmzalayan Kişi Bilgisi: {imza_sahibi_bilgisi}""",
        "example_inputs": {
            "dokuman_sayfa_sayisi": "14",
            "imza_konumu_tercihi": "Son Sayfa Sağ Alt (İmza Bloğu Üzeri)",
            "imza_sahibi_bilgisi": "Dr. Müh. Burak Şen - Proje Direktörü"
        }
    },
    {
        "id": "eimza-yubikey-fido2-ve-webauthn-entegrasyonu",
        "name": "YubiKey FIDO2, PIV ve WebAuthn e-İmza Altyapı Entegratörü",
        "category": "e-İmza & Mali Mühür & PKI",
        "description": "Donanımsal güvenlik anahtarları (YubiKey 5 Series) ile kurumsal 2FA, PIV akıllı kart ve WebAuthn imza mimarisi tasarlar.",
        "recommended_model": "gpt-4o",
        "tags": ["yubikey", "fido2", "webauthn", "piv", "siber-guvenlik"],
        "variables": ["yubikey_modeli", "kullanim_amaci", "sertifika_slotu"],
        "system_prompt": """Sen FIDO2 Alliance, WebAuthn ve NIST SP 800-73 PIV (Personal Identity Verification) standartları uzmanısın.
1. YubiKey donanımlarının PIV slotlarına (9a Kimlik Doğrulama, 9c Dijital İmza) X.509 kurumsal sertifika yükleme adımlarını,
2. YubiKey Manager CLI (`ykman`) komutlarını,
3. Web uygulamalarında parolasız kimlik doğrulama mimarisini yapılandır.""",
        "user_prompt_template": """YubiKey PIV/FIDO2 entegrasyon adımlarını oluştur:
YubiKey Modeli: {yubikey_modeli}
Kullanım Amacı: {kullanim_amaci}
Hedef Sertifika Slotu: {sertifika_slotu}""",
        "example_inputs": {
            "yubikey_modeli": "YubiKey 5 NFC (Firmware 5.4+)",
            "kullanim_amaci": "Kurumsal ERP ve VPN Girişlerinde Donanımsal Akıllı Kart Olarak Kullanım",
            "sertifika_slotu": "Slot 9c - Digital Signature"
        }
    },
    {
        "id": "eimza-crl-ocsp-iptal-durumu-sorgulayici",
        "name": "e-İmza Sertifika İptal Listesi (CRL) ve Canlı OCSP Denetleyicisi",
        "category": "e-İmza & Mali Mühür & PKI",
        "description": "İmza atıldığı anda veya şu an sertifikanın iptal edilip edilmediğini Online Certificate Status Protocol (OCSP) ve CRL ile denetler.",
        "recommended_model": "gpt-4o",
        "tags": ["ocsp", "crl", "iptal-durumu", "pki", "guvenlik"],
        "variables": ["sertifika_seri_no", "eshs_saglayici", "ocsp_adresi", "imza_ani_tarih"],
        "system_prompt": """Sen RFC 6960 (OCSP) ve RFC 5280 (X.509 CRL) protokolleri denetçisisin.
1. e-İmza sertifikasının kayıp/çalıntı veya istifa nedeniyle iptal edilip edilmediğini,
2. Sertifikanın imza atıldığı anda geçerli olup sonradan mı iptal edildiğini (imza geçerliliği korunur ilkesi),
3. Canlı OCSP yanıtı çözümleme ve ASN.1 DER yanıt durum kodlarını açıkla.""",
        "user_prompt_template": """Sertifika iptal durumunu sorgula:
Sertifika Seri No: {sertifika_seri_no}
Sertifika Sağlayıcı (ESHS): {eshs_saglayici}
OCSP Sunucu URL: {ocsp_adresi}
İmza Atıldığı Tarih/Saat: {imza_ani_tarih}""",
        "example_inputs": {
            "sertifika_seri_no": "6A:4E:91:02:84:BC:11",
            "eshs_saglayici": "Kamu SM Nitelikli Elektronik Sertifika Hizmetleri",
            "ocsp_adresi": "http://ocsp.kamusm.gov.tr",
            "imza_ani_tarih": "2026-09-10 11:20:00"
        }
    }
]
