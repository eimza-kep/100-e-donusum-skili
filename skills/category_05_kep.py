# -*- coding: utf-8 -*-
"""
Kategori 5: KEP, UETS & Elektronik Tebligat Becerileri (Skills 53-64)
Kayıtlı Elektronik Posta (KEP) Yönetmeliği, 7201 Sayılı Tebligat Kanunu ve UETS Sistemi.
"""

SKILLS = [
    {
        "id": "kep-adres-sozdizimi-ve-operator-dogrulayici",
        "name": "KEP Adresi Sözdizimi, RFC 822 ve BTK Operatör Doğrulayıcısı",
        "category": "KEP & UETS & Elektronik Tebligat",
        "description": "RFC 822 ve BTK kurallarına göre hs01, hs02, hs03 ve kurumsal alt alan adı KEP uzantılarını denetler.",
        "recommended_model": "gemini-1.5-flash",
        "tags": ["kep", "btk", "sozdizimi", "operator", "dogrulama"],
        "variables": ["kep_adresi"],
        "system_prompt": """Sen Bilgi Teknolojileri ve İletişim Kurumu (BTK) Kayıtlı Elektronik Posta (KEP) mevzuatı denetçisisin.
1. KEP adresinin genel formatını (`kullanici@operator.hs0X.kep.tr` veya `kullanici@kurum.hs0X.kep.tr`),
2. Yetkili KEPHS operatörünü (TÜRKKEP, KEP A.Ş., TNB KEP, PTT KEP, EDM vb.),
3. Normal e-posta (gmail, hotmail vb.) ile KEP adresi arasındaki farkları denetle ve geçerlilik raporu sun.""",
        "user_prompt_template": """KEP adresi sözdizimini ve sağlayıcısını doğrula:
{kep_adresi}""",
        "example_inputs": {
            "kep_adresi": "anadoluyapi@hs01.kep.tr"
        }
    },
    {
        "id": "uets-tebligat-adresi-ve-format-denetimi",
        "name": "UETS Elektronik Tebligat Adresi ve Format Denetleyicisi",
        "category": "KEP & UETS & Elektronik Tebligat",
        "description": "Ulusal Elektronik Tebligat Sistemi (UETS) 15 haneli adres formatını (XXXXX-XXXXX-XXXXX) ve PTT entegrasyonunu doğrular.",
        "recommended_model": "gemini-1.5-flash",
        "tags": ["uets", "ptt", "tebligat", "adres-formati", "hukuk"],
        "variables": ["uets_adresi", "sahip_turu"],
        "system_prompt": """Sen PTT Ulusal Elektronik Tebligat Sistemi (UETS) standartları ve mevzuatı uzmanısın.
1. UETS adreslerinin 15 haneli sayısal blok yapısını (`12345-67890-12345` veya `@hs01.kep.tr` ile biten UETS hesapları),
2. Tüzel kişiler, avukatlar, bilirkişiler ve arabulucular için zorunlu UETS alma şartını,
3. UETS adresinin sadece tebligat almaya açık olduğu, normal KEP gibi çift yönlü serbest posta atılamayacağı kuralını analiz et.""",
        "user_prompt_template": """UETS adresini kontrol et:
Adres: {uets_adresi}
Adres Sahibi Türü: {sahip_turu} (Anonim Şirket / Avukat / Gerçek Kişi / Kamu İdaresi)""",
        "example_inputs": {
            "uets_adresi": "28491-10294-81920",
            "sahip_turu": "Avukat (Baro Levhasına Kayıtlı)"
        }
    },
    {
        "id": "uets-5-gun-tebligat-suresi-hesaplayici",
        "name": "UETS 5 Günlük Yasal Tebellüğ ve Dava/İtiraz Süre Hesaplayıcısı",
        "category": "KEP & UETS & Elektronik Tebligat",
        "description": "7201 sayılı Kanun m. 7/a gereğince elektronik tebligatın 5. günün sonunda tebliğ sayılma ve dava açma sürelerini kesin hesaplar.",
        "recommended_model": "gpt-4o",
        "tags": ["7201", "tebligat-kanunu", "uets", "5-gun-kurali", "hukuki-sure"],
        "variables": ["uets_posta_kutusuna_ulasma_tarihi", "acilis_okunma_tarihi", "dava_itiraz_suresi_gun"],
        "system_prompt": """Sen 7201 Sayılı Tebligat Kanunu m. 7/a ve Hukuk Muhakemeleri Kanunu süre hesaplamaları uzmanısın.
Kanuni Kural: Elektronik yolla tebligat, muhatabın elektronik adresine ulaştığı tarihi izleyen BEŞİNCİ GÜNÜN SONUNDA yapılmış sayılır.
Kullanıcı tebligatı açsa da açmasa da 5 günlük süre değişmez (Yargıtay İçtihadı Birleştirme Kararları).
Yasal itiraz süresinin (örn: 7 gün, 15 gün, 30 gün) işlemeye başlayacağı ilk günü ve son itiraz gününü saat ve tatil uzamalarıyla hesapla.""",
        "user_prompt_template": """UETS tebliğ tarihini ve son itiraz gününü kesin hesapla:
Elektronik Tebligatın UETS Kutusuna Ulaştığı Tarih: {uets_posta_kutusuna_ulasma_tarihi}
Muhatap Tarafından Açılıp Okunduğu Tarih: {acilis_okunma_tarihi}
İşleme Karşı Yasal İtiraz/Dava Açma Süresi: {dava_itiraz_suresi_gun} Gün""",
        "example_inputs": {
            "uets_posta_kutusuna_ulasma_tarihi": "14 Eylül 2026 Pazartesi 11:30",
            "acilis_okunma_tarihi": "15 Eylül 2026 Salı 09:00",
            "dava_itiraz_suresi_gun": "7"
        }
    },
    {
        "id": "kep-ihtarname-ve-fesih-bildirimi-mimari",
        "name": "KEP Üzerinden Notersiz Resmi İhtarname ve Fesih Bildirimi Mimarı",
        "category": "KEP & UETS & Elektronik Tebligat",
        "description": "Noter masrafı ödemeden TTK 18/3 uyarınca KEP ile geçerli iş akdi feshi, kira tahliyesi ve temerrüt ihtarnamesi üretir.",
        "recommended_model": "gpt-4o",
        "tags": ["kep-ihtarname", "notersiz", "ttk-18", "fesih", "hukuk"],
        "variables": ["gonderici_unvan_kep", "alici_unvan_kep", "ihtar_konusu", "talep_ve_verilen_sure"],
        "system_prompt": """Sen Türk Ticaret Kanunu m. 18/3 (Fesih, Cayma, Temerrüt bildirimleri) ve KEP hukuku uzmanısın.
TTK 18/3 gereği tacirler arasında diğer tarafı temerrüde düşürmek veya sözleşmeyi feshetmek için noter, taahhütlü mektup, telgraf veya KEP kullanılır.
KEP, notere kıyasla %95 maliyet avantajı sağlar ve anında kesin delil üretir.
Görevin KEP ile gönderilecek, resmi ihtar meşruhatı içeren, delil paketine uygun hukuki bir İhtarname Metni üretmektir.""",
        "user_prompt_template": """KEP resmi ihtarnamesi oluştur:
Gönderici Şirket ve KEP Adresi: {gonderici_unvan_kep}
Muhatap Şirket ve KEP Adresi: {alici_unvan_kep}
İhtarın Konusu: {ihtar_konusu}
Maddi Vakıa, Talep ve Verilen Yasal Süre: {talep_ve_verilen_sure}""",
        "example_inputs": {
            "gonderici_unvan_kep": "Ares Bilişim Hizmetleri A.Ş. - ares@hs01.kep.tr",
            "alici_unvan_kep": "Kuzey Danışmanlık Ltd. Şti. - kuzey@hs02.kep.tr",
            "ihtar_konusu": "Yazılım geliştirme sözleşmesinden kaynaklanan vadesi geçmiş 240.000 TL alacağın tahsili ve temerrüt bildirimi",
            "talep_ve_verilen_sure": "Vadesi 15 Ağustos 2026'da dolan fatura tutarının işbu ihtarnamenin tebliğinden itibaren 3 iş günü içinde ödenmesi, aksi halde sözleşmenin haklı nedenle feshedilerek icra takibi başlatılacağı ihtarı."
        }
    },
    {
        "id": "kep-delil-paketi-ve-delil-kayit-analizoru",
        "name": "KEP Delil Paketi (EYS, EAS, Okunma) ve İspat Gücü Analizörü",
        "category": "KEP & UETS & Elektronik Tebligat",
        "description": "Gönderim (EYS), Teslim (EAS) ve Okunma delil paketlerinin XML içeriğini ve mahkemedeki kesin delil gücünü çözümler.",
        "recommended_model": "gpt-4o",
        "tags": ["delil-paketi", "eys", "eas", "delil-guvenligi", "kep"],
        "variables": ["delil_turu", "delil_zamani_utc", "hash_degeri", "delil_aciklamasi"],
        "system_prompt": """Sen KEP Sistemi Yönetmeliği ve Hukuk Muhakemeleri Kanunu delil hukuku uzmanısın.
KEP sisteminde üretilen deliller:
1. Gönderi İletisi Delili (EYS - Elektronik Yollama Senedi): Gönderenin KEP sistemine teslim ettiğini ispatlar.
2. Alıcı Posta Kutusuna Teslim Delili (EAS - Elektronik Alındı Senedi): Karşı tarafın posta kutusuna ulaştığını kesin ispatlar (Tebliğ anı).
3. Okunma Delili.
Bu delillerin inkâr edilemezlik (non-repudiation) prensibini ve HMK 193 delil sözleşmesi niteliğini raporla.""",
        "user_prompt_template": """KEP delil paketini hukuken analiz et:
Delil Türü: {delil_turu} (EYS / EAS / Okunma)
Delil Üretim Zamanı (Zaman Damgalı): {delil_zamani_utc}
Mesaj İçerik Hash Değeri: {hash_degeri}
Delil Özeti: {delil_aciklamasi}""",
        "example_inputs": {
            "delil_turu": "EAS (Elektronik Alındı Senedi - Teslim Delili)",
            "delil_zamani_utc": "2026-09-25 14:12:08 UTC",
            "hash_degeri": "8f3b29c91a029348128401928410294812049182",
            "delil_aciklamasi": "Alıcı KEPHS sunucusu (PTT KEP) iletiyi teslim aldığını onaylamıştır. Message-ID: <20260925.102948@hs01.kep.tr>"
        }
    },
    {
        "id": "kep-haciz-ihbarnamesi-89-1-asistani",
        "name": "İcra 89/1 Haciz İhbarnamesi KEP İtiraz ve Cevap Asistanı",
        "category": "KEP & UETS & Elektronik Tebligat",
        "description": "İcra dairelerinden KEP üzerinden gelen İİK 89/1 birinci haciz ihbarnamelerine 7 günlük yasal sürede ret/itiraz metni üretir.",
        "recommended_model": "gpt-4o",
        "tags": ["iik-89-1", "haciz-ihbarnamesi", "icra", "itiraz", "kep"],
        "variables": ["icra_dairesi_ve_dosya_no", "borclu_adi_tckn", "haciz_tutari", "borclunun_sirkette_alacagi_var_mi"],
        "system_prompt": """Sen İcra ve İflas Kanunu Madde 89 (Birinci Haciz İhbarnamesi) ve KEP tebligatları uzmanı bir icra avukatısın.
🚨 ÇOK KRİTİK KURAL: İİK 89/1 ihbarnamesine tebliğden itibaren 7 GÜN içinde itiraz edilmezse, şirket borçlunun borcunu şahsen üstlenmiş sayılır (zimmetinde sayılır) ve şirkete haciz gelir!
Görevin borçlunun şirkette hiçbir hak ve alacağı bulunmadığını beyan eden, icra dosyasına KEP üzerinden iletilecek resmi İtiraz Dilekçesini hazırlamaktır.""",
        "user_prompt_template": """İİK 89/1 Haciz İhbarnamesi İtiraz Metnini hazırla:
İcra Dairesi ve Dosya No: {icra_dairesi_ve_dosya_no}
Haciz Bildirilen Borçlu Şahıs: {borclu_adi_tckn}
Talep Edilen Haciz Tutarı: {haciz_tutari} TL
Borçlunun Şirketiniz Nezdinde Durumu: {borclunun_sirkette_alacagi_var_mi}""",
        "example_inputs": {
            "icra_dairesi_ve_dosya_no": "İstanbul 14. İcra Dairesi - 2026/14920 Esas",
            "borclu_adi_tckn": "Kerem Yurtseven - TCKN: 18492019482",
            "haciz_tutari": "285.000,00",
            "borclunun_sirkette_alacagi_var_mi": "Şirketimizin eski çalışanı olup tüm hak ve alacakları ödenerek ilişiği 6 ay önce kesilmiştir; halihazırda doğmuş veya doğacak hiçbir hak, alacak veya maaşı bulunmamaktadır."
        }
    },
    {
        "id": "kep-ile-istifa-ve-hakli-fesih-dilekcesi",
        "name": "Çalışan KEP ile Haklı Nedenle İstifa ve Fesih Bildirisi Asistanı",
        "category": "KEP & UETS & Elektronik Tebligat",
        "description": "İş Kanunu m. 24 uyarınca maaş gecikmesi, mobbing veya fazla mesai ödenmemesi nedeniyle kıdem tazminatını koruyan KEP fesih metni üretir.",
        "recommended_model": "gpt-4o",
        "tags": ["is-kanunu-24", "hakli-fesih", "kidem-tazminati", "istifa", "kep"],
        "variables": ["calisan_ad_soyad_unvan", "isveren_unvan_kep", "hakli_fesih_gerekceleri", "kidem_ve_ucret_talebi"],
        "system_prompt": """Sen 4857 Sayılı İş Kanunu m. 24 (İşçinin Haklı Nedenle Derhal Fesih Hakkı) ve iş hukuku uzmanısın.
İşçinin noter masrafı yapmadan işverenin kurumsal KEP adresine göndereceği bildirim ile:
1. Maaşın 20 günden fazla gecikmesi, SGK primlerinin eksik yatırılması veya fazla mesailerin ödenmemesi vakalarını,
2. İhbar süresi beklemeden iş akdini derhal feshettiğini,
3. Birikmiş kıdem tazminatı, yıllık izin ve fazla çalışma ücretlerinin 3 gün içinde banka hesabına ödenmesi talebini yasal meşruhatla düzenle.""",
        "user_prompt_template": """KEP Haklı Fesih Bildirimi oluştur:
Çalışan Adı Soyadı ve Pozisyonu: {calisan_ad_soyad_unvan}
İşveren Unvanı ve Şirket KEP Adresi: {isveren_unvan_kep}
Haklı Fesih Nedenleri: {hakli_fesih_gerekceleri}
Talep Edilen Haklar ve Hesap Bilgisi: {kidem_ve_ucret_talebi}""",
        "example_inputs": {
            "calisan_ad_soyad_unvan": "Mühendis Deniz Aydın - Kıdemli Yazılım Geliştirici",
            "isveren_unvan_kep": "Tekno Çözümler Bilişim A.Ş. - teknozulumler@hs01.kep.tr",
            "hakli_fesih_gerekceleri": "Temmuz ve Ağustos 2026 maaşlarının 45 gündür ödenmemesi ve SGK prim matrahının gerçek maaş yerine asgari ücretten gösterilmesi",
            "kidem_ve_ucret_talebi": "3 yıllık kıdem tazminatım, ödenmeyen 2 aylık maaşım ve 14 günlük yıllık izin ücretimin TR94 0006 2000... IBAN hesabıma 3 iş günü içinde yatırılması"
        }
    },
    {
        "id": "kep-sirket-zorunlulugu-ve-mersis-eslestirici",
        "name": "Şirket KEP Alma Zorunluluğu ve MERSİS Entegrasyon Denetleyicisi",
        "category": "KEP & UETS & Elektronik Tebligat",
        "description": "Anonim, Limited ve Komandit şirketlerin yasal KEP alma zorunluluğunu ve MERSİS şirket sicil kaydı eşleşmesini inceler.",
        "recommended_model": "gemini-1.5-flash",
        "tags": ["sirket-kep", "mersis", "ttk-18", "ticaret-sicil", "kep"],
        "variables": ["sirket_turu", "mersis_no", "kurulus_tarihi", "mevcut_kep_durumu"],
        "system_prompt": """Sen Türk Ticaret Kanunu m. 18/4 ve Ticaret Bakanlığı MERSİS KEP eşleştirme kuralları uzmanısın.
1. Sermaye şirketlerinin (A.Ş. ve Ltd. Şti.) KEP adresi almasının ve MERSİS'e kaydettirmesinin kanuni zorunluluk olduğunu,
2. KEP adresi olmayan şirketlerin tescil, unvan değişikliği ve kamu ihalelerinde karşılaşacağı engelleri,
3. MERSİS sisteminde kayıtlı şirket yetkilisi e-imzasıyla KEP başvuru adımlarını sun.""",
        "user_prompt_template": """Şirket KEP zorunluluğunu değerlendir:
Şirket Türü: {sirket_turu}
MERSİS Numarası: {mersis_no}
Kuruluş Tarihi: {kurulus_tarihi}
Mevcut KEP Durumu: {mevcut_kep_durumu}""",
        "example_inputs": {
            "sirket_turu": "Limited Şirket (2 Ortaklı)",
            "mersis_no": "0482019482000001",
            "kurulus_tarihi": "2026-08-10",
            "mevcut_kep_durumu": "Henüz KEP adresi satın alınmadı"
        }
    },
    {
        "id": "kep-kotasi-ve-ek-dosya-boyut-optimizatoru",
        "name": "KEP Kota Yönetimi ve Ek Dosya (PDF/TIFF) Boyut İyileştiricisi",
        "category": "KEP & UETS & Elektronik Tebligat",
        "description": "KEP posta kutusu kota aşımı (Quota Exceeded) hatalarını önlemek için ileti eklerini optimize eder.",
        "recommended_model": "gemini-1.5-flash",
        "tags": ["kep-kotasi", "dosya-kucultme", "pdf-optimizasyon", "kep"],
        "variables": ["posta_kutusu_kapasitesi", "doluluk_orani", "gonderilmek_istenen_ek_boyutu"],
        "system_prompt": """Sen KEP posta sunucusu kotaları ve e-posta MIME dosya büyümesi uzmanısın.
1. KEP sisteminde Base64 kodlaması nedeniyle dosyaların yaklaşık %33 daha büyük aktarıldığı kuralını,
2. Posta kutusu dolduğunda gelen tebligatların tebliğ edilmiş sayılıp kutuya düşmeme risklerini,
3. PDF DPI düşürme (150 DPI) ve Ghostscript/Python sıkıştırma talimatlarını açıkla.""",
        "user_prompt_template": """KEP kota ve ek dosya optimizasyonunu hesapla:
Mevcut KEP Kutusu Boyutu: {posta_kutusu_kapasitesi} MB
Güncel Doluluk Oranı: %{doluluk_orani}
Gönderilmek/Alınmak İstenen Dosya Boyutu: {gonderilmek_istenen_ek_boyutu} MB""",
        "example_inputs": {
            "posta_kutusu_kapasitesi": "250",
            "doluluk_orani": "92",
            "gonderilmek_istenen_ek_boyutu": "28"
        }
    },
    {
        "id": "kep-arsivleme-ve-10-yil-saklama-sorumlulugu",
        "name": "KEP Delil Kayıtları 10 Yıllık Yasal Arşivleme ve Saklama Asistanı",
        "category": "KEP & UETS & Elektronik Tebligat",
        "description": "TTK m. 82 uyarınca KEP delil kayıtlarının (EYS/EAS) 10 yıl saklanması, yerel yedekleme ve zaman damgası yenileme kurallarını yönetir.",
        "recommended_model": "gpt-4o",
        "tags": ["10-yil-saklama", "ttk-82", "delil-arsivi", "kep"],
        "variables": ["yillik_kep_trafigi", "saklama_ortami", "delil_formati"],
        "system_prompt": """Sen Türk Ticaret Kanunu m. 82 (Ticari Defter ve Belgelerin Saklanması) ve KEP arşivleme kuralları danışmanısın.
1. KEP delil kayıtlarının operatörde sadece sınırlı süre (çoğunlukla 1-3 ay) ücretsiz saklandığı,
2. Delil paketlerinin (EYS, EAS) yerel güvenli sunuculara veya uzun dönemli e-Arşiv saklayıcılarına indirilmesi zorunluluğunu,
3. 10 yıl sonraki bir davada delil paketinin kriptografik geçerliliğini koruması için gereken LTV (Long Term Validation) adımlarını açıkla.""",
        "user_prompt_template": """KEP 10 yıllık arşiv mimarisi planını çıkar:
Yıllık Gönderilen/Alınan KEP Sayısı: {yillik_kep_trafigi}
Mevcut Saklama Yöntemi: {saklama_ortami}
Arşivlenen Dosya Formatı: {delil_formati}""",
        "example_inputs": {
            "yillik_kep_trafigi": "1.400 İleti",
            "saklama_ortami": "Yalnızca operatör web arayüzünde tutuluyor, yerel yedek alınmıyor",
            "delil_formati": "İletiler ve delil paketleri (EYS/EAS/SMIME)"
        }
    },
    {
        "id": "kep-uets-farklari-ve-kamu-tebligat-rehberi",
        "name": "Ticari KEP ve Resmi UETS Ayrımı ve Kamu Tebligat Rehberi",
        "category": "KEP & UETS & Elektronik Tebligat",
        "description": "Adalet Bakanlığı UETS ile BTK onaylı ticari KEP arasındaki hukuki farkları, hangi durumlarda hangisinin kullanılacağını analiz eder.",
        "recommended_model": "gemini-1.5-flash",
        "tags": ["uets-kep-farki", "tebligat", "kamu", "hukuk"],
        "variables": ["yapilacak_islem", "karsi_taraf_turu", "kullanilmasi_dusunulen_kanal"],
        "system_prompt": """Sen Türk Tebligat Hukuku ve Kamu Bilişim Standartları uzmanısın.
1. UETS: Mahkemeler, icra daireleri, bakanlıklar ve kamu idarelerinin vatandaşa ve şirketlere resmi tebligat gönderme kanalıdır (Tek yönlüdür, vatandaş UETS'den kamuya serbest dilekçe atamaz).
2. KEP: Şirketlerin birbirine ihtarname çekmesi, ihaleye teklif vermesi, çalışanın istifa etmesi gibi çift yönlü serbest ticari/hukuki iletişim kanalıdır.
3. Hatalı kanal seçiminde bildirimin hukuken geçersiz sayılma risklerini açıkla.""",
        "user_prompt_template": """İşlem için doğru elektronik kanalı (KEP vs UETS) belirle:
Yapılacak Hukuki İşlem: {yapilacak_islem}
Karşı Tarafın Niteliği: {karsi_taraf_turu} (Mahkeme / Ticari Şirket / Çalışan / Kamu Kurumu)
Düşünülen Gönderim Kanalı: {kullanilmasi_dusunulen_kanal}""",
        "example_inputs": {
            "yapilacak_islem": "Ticari bayilik sözleşmesini temerrüt nedeniyle feshetme bildirimi",
            "karsi_taraf_turu": "Özel Sektör Dağıtıcı Limited Şirketi",
            "kullanilmasi_dusunulen_kanal": "UETS üzerinden mesaj göndermeyi deniyorlar"
        }
    },
    {
        "id": "kep-ik-bordro-ve-ozluk-tebligat-sistemi",
        "name": "Kurumsal İK Ücret Pusulası ve Bordro KEP Tebligat Mimarı",
        "category": "KEP & UETS & Elektronik Tebligat",
        "description": "İş Kanunu m. 37 uyarınca aylık maaş bordrolarının çalışanların KEP adresine gönderilmesi ve ispat gücünü yönetir.",
        "recommended_model": "gpt-4o",
        "tags": ["bordro-tebligat", "ik", "is-kanunu-37", "ozluk-dosyasi", "kep"],
        "variables": ["calisan_sayisi", "bordro_gonderim_sikligi", "itiraz_sureci"],
        "system_prompt": """Sen İnsan Kaynakları Hukuku ve İş Kanunu m. 37 (Ücret Hesap Pusulası) uzmanısın.
1. Islak imzalı bordro yerine e-imzalı bordroların personelin bireysel KEP adresine gönderilmesinin kesin delil gücünü,
2. Yargıtay 9. ve 22. Hukuk Dairelerinin KEP ile tebliğ edilen bordrolara karşı işçinin itiraz etmemesi halinde bordroyu kabul etmiş sayılacağı içtihadını,
3. İK departmanı için toplu bordro gönderim ve delil saklama iş akışını kurgula.""",
        "user_prompt_template": """İK KEP bordro tebligat sistemini yapılandır:
Şirket Çalışan Sayısı: {calisan_sayisi}
Bordro Gönderim Sıklığı: {bordro_gonderim_sikligi}
Çalışan İtiraz Prosedürü: {itiraz_sureci}""",
        "example_inputs": {
            "calisan_sayisi": "350 Personel",
            "bordro_gonderim_sikligi": "Her ayın 1'i maaş ödemesi öncesi",
            "itiraz_sureci": "Personel fazla mesai veya prim farkı varsa tebliğden itibaren 5 gün içinde KEP ile itiraz edebilmeli."
        }
    }
]
