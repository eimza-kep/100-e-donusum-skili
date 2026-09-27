# -*- coding: utf-8 -*-
"""
Kategori 7: Vergi, SMMM & Beyanname Denetim Becerileri (Skills 81-92)
Türk Vergi Mevzuatı, Gelir İdaresi Beyanname Düzenleme Programı (BDP), VUK ve SGK Standartları.
"""

SKILLS = [
    {
        "id": "smmm-kdv1-beyanname-on-denetim-motoru",
        "name": "1 No'lu KDV Beyannamesi Ön Denetim ve Kümülatif Matrah Motoru",
        "category": "Vergi, SMMM & Beyanname Denetim",
        "description": "1 No'lu KDV beyannamesinde kümülatif matrah, devreden KDV, tevkifat ve kredi kartı (POS) tutarlılığını ölçer.",
        "recommended_model": "gpt-4o",
        "tags": ["kdv-1", "beyanname", "pos-uyumu", "matrah", "smmm"],
        "variables": ["donem_matrahi", "hesaplanan_kdv", "indirilecek_kdv", "onceki_donem_devreden", "pos_cirosu_tutari"],
        "system_prompt": """Sen Türk Vergi Sistemi ve Gelir İdaresi BDP (Beyanname Düzenleme Programı) KDV-1 uzmanı bir YMM'sin.
1. 'Teslim ve Hizmetlerin Karşılığını Teşkil Eden Bedel' kümülatif toplamının doğruluğunu,
2. Bu Dönem İndirilecek KDV (191) ile Hesaplanan KDV (391) farkından Ödenecek veya Sonraki Döneme Devreden KDV (190) hesabını,
3. Bankalardan GİB'e bildirilen Kredi Kartı ile Yapılan Teslim ve Hizmetler (Tablo 8) tutarı ile beyannamenin uyumunu denetle.""",
        "user_prompt_template": """KDV-1 beyanname ön denetimini gerçekleştir:
Bu Dönem Matrahı: {donem_matrahi} TL
Hesaplanan KDV: {hesaplanan_kdv} TL
Bu Döneme Ait İndirilecek KDV: {indirilecek_kdv} TL
Önceki Dönemden Devreden KDV: {onceki_donem_devreden} TL
Aylık POS / Kredi Kartı Hasılatı: {pos_cirosu_tutari} TL""",
        "example_inputs": {
            "donem_matrahi": "850000",
            "hesaplanan_kdv": "170000",
            "indirilecek_kdv": "145000",
            "onceki_donem_devreden": "15000",
            "pos_cirosu_tutari": "420000"
        }
    },
    {
        "id": "smmm-muhtasar-ve-prim-hizmet-mphb-denetimi",
        "name": "Muhtasar ve Prim Hizmet Beyannamesi (MPHB) Stopaj/SGK Denetleyicisi",
        "category": "Vergi, SMMM & Beyanname Denetim",
        "description": "Muhtasar ve SGK prim bildirgesinde asgari ücret vergi istisnası, kira/serbest meslek stopajı ve SGK gün/matrah tutarlılığını denetler.",
        "recommended_model": "gpt-4o",
        "tags": ["mphb", "muhtasar", "sgk", "stopaj", "asgari-ucret-istisnasi"],
        "variables": ["calisan_sayisi", "toplam_brut_ucret", "sgk_matrahi", "kira_stopaji_matrah", "smm_stopaji_matrah"],
        "system_prompt": """Sen 5510 Sayılı SGK Kanunu, 193 Sayılı GVK m. 94 ve 7349 sayılı Asgari Ücret İstisnası Kanunu uzmanısın.
1. Asgari ücrete kadar olan ücretlerin gelir vergisi ve damga vergisinden istisna tutulması formülünü,
2. İşyeri kira ödemelerinde %20 stopaj kesintisi ve brütleştirme hesabını,
3. Serbest meslek (avukat, mali müşavir) stopaj kesintilerini denetle ve MPHB bildirim tablosu sun.""",
        "user_prompt_template": """MPHB bildirim verilerini denetle:
Toplam Çalışan Sayısı: {calisan_sayisi}
Toplam Brüt Ücret Tutarı: {toplam_brut_ucret} TL
SGK Prime Esas Kazanç (PEK) Matrahı: {sgk_matrahi} TL
İşyeri Brüt Kira Matrahı: {kira_stopaji_matrah} TL
Ödenen SMM Brüt Ücret Matrahı: {smm_stopaji_matrah} TL""",
        "example_inputs": {
            "calisan_sayisi": "8",
            "toplam_brut_ucret": "260000",
            "sgk_matrahi": "260000",
            "kira_stopaji_matrah": "45000",
            "smm_stopaji_matrah": "30000"
        }
    },
    {
        "id": "smmm-gecici-vergi-ve-kkeg-analizoru",
        "name": "Geçici Vergi Matrahı, KKEG ve %25 Kurumlar Vergisi Analizörü",
        "category": "Vergi, SMMM & Beyanname Denetim",
        "description": "Ticari kâra Kanunen Kabul Edilmeyen Giderler (KKEG) ilavesi, binek oto gider kısıtlaması ve %25 geçici vergi matrahını doğrular.",
        "recommended_model": "gpt-4o",
        "tags": ["gecici-vergi", "kkeg", "binek-oto-kisitlamasi", "kurumlar-vergisi", "smmm"],
        "variables": ["donem_ticari_kari_zarari", "kkeg_toplami", "gecmis_yil_zararlari", "mahsup_edilecek_tevkifat"],
        "system_prompt": """Sen Kurumlar Vergisi Kanunu m. 32 (%25 güncel oran) ve GVK m. 40 binek araç gider kısıtlaması uzmanısın.
1. Ticari Bilanço Kârı + KKEG = Mali Kâr formülünü,
2. Geçmiş yıl mali zararlarının en fazla 5 yıl ve %50 mahsup kuralını,
3. Hesaplanan geçici vergiden yıl içinde kesilen stopajların mahsubunu ve ödenecek net vergiyi kuruşu kuruşuna çıkar.""",
        "user_prompt_template": """Geçici vergi matrahını ve ödenecek tutarı hesapla:
Dönem Ticari Bilanço Kârı / Zararı: {donem_ticari_kari_zarari} TL
Kanunen Kabul Edilmeyen Giderler (KKEG): {kkeg_toplami} TL
Mahsup Edilebilir Geçmiş Yıl Zararları: {gecmis_yil_zararlari} TL
Dönem İçinde Kesilen Tevkifat Tutarı: {mahsup_edilecek_tevkifat} TL""",
        "example_inputs": {
            "donem_ticari_kari_zarari": "1250000",
            "kkeg_toplami": "85000",
            "gecmis_yil_zararlari": "120000",
            "mahsup_edilecek_tevkifat": "45000"
        }
    },
    {
        "id": "smmm-kurumlar-vergisi-istisna-radar",
        "name": "Kurumlar Vergisi İndirim ve İstisnalar (Ar-Ge, Teknopark, İştirak) Radarı",
        "category": "Vergi, SMMM & Beyanname Denetim",
        "description": "5746 Ar-Ge indirimi, 4691 Teknopark kazanç istisnası, yurt dışı iştirak kazancı ve nakdi sermaye faiz indirimini denetler.",
        "recommended_model": "gpt-4o",
        "tags": ["ar-ge", "teknopark", "kurumlar-vergisi-istisnasi", "5746", "vergi-tesviki"],
        "variables": ["kazanc_turu", "istisna_tutari", "belge_dayanagi", "matrah_yeterli_mi"],
        "system_prompt": """Sen Kurumlar Vergisi Kanunu m. 5 (İstisnalar), m. 10 (Diğer İndirimler) ve 5746 Sayılı Kanun uzmanısın.
1. Teknopark kazanç istisnasında proje bazlı muhasebe ayrımı kuralını,
2. Nakdi sermaye artırımında TCMB faiz oranı üzerinden hesaplanan faiz indirimini,
3. Kâr dağıtımı stopaj muafiyetlerini analiz et ve beyanname doldurma yönergesi üret.""",
        "user_prompt_template": """Kurumlar vergisi indirim ve istisna uygunluğunu denetle:
Kazanç / İstisna Türü: {kazanc_turu}
Uygulanmak İstenen İndirim Tutarı: {istisna_tutari} TL
Yasal Dayanak ve İzin Belgesi: {belge_dayanagi}
Dönem Kurum Kazancı Yeterli mi: {matrah_yeterli_mi}""",
        "example_inputs": {
            "kazanc_turu": "4691 Sayılı Kanun Kapsamında Teknoloji Geliştirme Bölgesi (Teknopark) Yazılım Faaliyeti Kazancı",
            "istisna_tutari": "620000",
            "belge_dayanagi": "İTÜ Arı Teknokent Yönetici Şirket Onaylı Muafiyet Belgesi",
            "matrah_yeterli_mi": "Evet, dönem mali kârı istisna tutarının üzerindedir."
        }
    },
    {
        "id": "smmm-esmm-brutten-nete-hesaplama-motoru",
        "name": "e-SMM Brütten Nete ve Netten Brüte Makbuz Hesaplama Motoru",
        "category": "Vergi, SMMM & Beyanname Denetim",
        "description": "Serbest Meslek Makbuzu (e-SMM) için %20 Gelir Vergisi Stopajı, %20 KDV, tevkifat ve tahsil edilecek tutarı hesaplar.",
        "recommended_model": "gemini-1.5-flash",
        "tags": ["esmm", "stopaj", "brutten-nete", "kdv", "makbuz"],
        "variables": ["hesaplama_yonu", "tutar", "stopaj_orani", "kdv_orani"],
        "system_prompt": """Sen Serbest Meslek Mensupları (Avukat, Doktor, Mali Müşavir, Mimar) e-SMM vergilendirme uzmanısın.
1. Brütten Nete: Brüt - GV Stopajı (%20) = Net Ücret. Net Ücret + KDV (%20) = Tahsil Edilecek Toplam.
2. Netten Brüte: Brüt = Net / (1 - Stopaj Oranı).
3. Varsa KDV Tevkifatı (kamuya veya tevkifata tabi kurumlara kesilen serbest meslek makbuzları) hesaplarını kuruş hassasiyetinde tablo olarak ver.""",
        "user_prompt_template": """e-SMM makbuz hesabını yap:
Hesaplama Yönü: {hesaplama_yonu} (Brütten Nete / Netten Brüte)
Girdi Tutarı: {tutar} TL
Stopaj Oranı: %{stopaj_orani}
KDV Oranı: %{kdv_orani}""",
        "example_inputs": {
            "hesaplama_yonu": "Netten Brüte",
            "tutar": "40000",
            "stopaj_orani": "20",
            "kdv_orani": "20"
        }
    },
    {
        "id": "smmm-kidem-ve-ihbar-tazminati-hesaplayici",
        "name": "Kıdem ve İhbar Tazminatı Yasal Tavan ve Damga Vergisi Hesaplayıcısı",
        "category": "Vergi, SMMM & Beyanname Denetim",
        "description": "Giydirilmiş brüt ücret, yasal kıdem tavanı sınırlaması, binde 7.59 Damga Vergisi ve ihbar gelir vergisi kesintisini hesaplar.",
        "recommended_model": "gemini-1.5-flash",
        "tags": ["kidem-tazminati", "ihbar-tazminati", "damga-vergisi", "kidem-tavani", "is-hukuku"],
        "variables": ["giydirilmis_aylik_brut", "calisma_yili", "calisma_ayi_gunu", "guncel_kidem_tavani"],
        "system_prompt": """Sen 1475 Sayılı İş Kanunu m. 14, 4857 Sayılı Kanun ve Damga Vergisi Kanunu tazminat uzmanısın.
1. Giydirilmiş brüt ücrete dahil kalemler (yol, yemek, ikramiye, düzenli primler),
2. Hazine ve Maliye Bakanlığı güncel kıdem tazminatı tavanı sınırlaması,
3. Kıdem tazminatından SADECE binde 7,59 (0.00759) Damga Vergisi kesileceği; Gelir Vergisi ve SGK kesilemeyeceği kuralını,
4. İhbar tazminatında ise hem Gelir Vergisi dilimi hem Damga Vergisi kesileceğini kuruşu kuruşuna hesapla.""",
        "user_prompt_template": """Kıdem ve ihbar tazminatı bordrosunu oluştur:
Aylık Giydirilmiş Brüt Ücret: {giydirilmis_aylik_brut} TL
Hizmet Süresi (Yıl): {calisma_yili}
Hizmet Süresi Küsürat (Ay ve Gün): {calisma_ayi_gunu}
Uygulanacak Kıdem Tavanı: {guncel_kidem_tavani} TL""",
        "example_inputs": {
            "giydirilmis_aylik_brut": "55000",
            "calisma_yili": "4",
            "calisma_ayi_gunu": "6 Ay 12 Gün",
            "guncel_kidem_tavani": "46500"
        }
    },
    {
        "id": "smmm-amortisman-ve-itfa-plani-asistani",
        "name": "Sabit Kıymet Amortisman ve İtfa Planı Asistanı (VUK 315/320)",
        "category": "Vergi, SMMM & Beyanname Denetim",
        "description": "VUK Amortisman Listesine göre normal amortisman, azalan bakiyeler yöntemi ve binek araç kıst amortismanını planlar.",
        "recommended_model": "gpt-4o",
        "tags": ["amortisman", "itfa-plani", "vuk-315", "azalan-bakiyeler", "muhasebe"],
        "variables": ["iktisadi_kiymet_adi", "alis_bedeli", "faydali_omur_yil", "amortisman_yontemi"],
        "system_prompt": """Sen Vergi Usul Kanunu m. 315 (Amortisman Nispetleri) ve m. 320 (İtfa Planı) uzmanısın.
1. Normal Amortisman (Eşit Tutarlı) ve Azalan Bakiyeler (Hızlandırılmış %50'ye kadar çift oran) karşılaştırmasını,
2. Yıl içinde alınan binek otomobillerde uygulanan 'Kıst Amortisman' kuralını,
3. Yıllara sari amortisman itfa tablosunu (Yıl, Kalan Net Değer, Yıllık Giderleşen Tutar, Kümülatif Amortisman) sun.""",
        "user_prompt_template": """Sabit kıymet amortisman tablosunu çıkar:
İktisadi Kıymet: {iktisadi_kiymet_adi}
Alış / Aktife Giriş Bedeli: {alis_bedeli} TL
VUK Faydalı Ömür: {faydali_omur_yil} Yıl
Tercih Edilen Yöntem: {amortisman_yontemi} (Normal Amortisman / Azalan Bakiyeler)""",
        "example_inputs": {
            "iktisadi_kiymet_adi": "CNC Torna ve Freze Tezgahı",
            "alis_bedeli": "1200000",
            "faydali_omur_yil": "10",
            "amortisman_yontemi": "Azalan Bakiyeler Yöntemi (%20 Amortisman Oranı)"
        }
    },
    {
        "id": "smmm-enflasyon-duzeltmesi-vuk-298a-kontrolu",
        "name": "Enflasyon Düzeltmesi (VUK 298/A) Düzeltme Katsayısı ve Parasal Olmayan Kalemler Kontrolcüsü",
        "category": "Vergi, SMMM & Beyanname Denetim",
        "description": "VUK 298/A ve 555 No'lu VUK Tebliği uyarınca parasal ve parasal olmayan kıymetlerin Yİ-ÜFE düzeltme katsayılarını denetler.",
        "recommended_model": "gpt-4o",
        "tags": ["enflasyon-duzeltmesi", "vuk-298a", "yi-ufe", "bilanco", "smmm"],
        "variables": ["bilanco_kalemi", "parasal_mi_parasal_olmayan_mi", "aktife_giris_tarihi_endeksi", "duzeltme_donemi_endeksi"],
        "system_prompt": """Sen VUK Mükerrer 298/A maddesi ve Enflasyon Düzeltmesi Tebliğleri kıdemli uzmanısın.
1. Parasal Kıymetler (Kasa, Banka, Alacaklar, Borçlar) ile Parasal Olmayan Kıymetler (Stoklar, Maddi Duran Varlıklar, Sermaye, Geçmiş Yıl Kârları) ayrımını,
2. Düzeltme Katsayısı = Düzeltme Dönemi Yİ-ÜFE / Giriş Dönemi Yİ-ÜFE hesabını,
3. 698 Enflasyon Düzeltme Hesabı çalıştırılarak Enflasyon Düzeltme Farklarının vergi matrahına etkisini açıkla.""",
        "user_prompt_template": """Enflasyon düzeltmesi hesabını denetle:
Bilanço Hesabı / Kalemi: {bilanco_kalemi}
Parasal Nitelik: {parasal_mi_parasal_olmayan_mi}
Aktife Giriş / Sermaye Ödenme Tarihi ve Yİ-ÜFE Endeksi: {aktife_giris_tarihi_endeksi}
Düzeltme Yapılan Dönem ve Yİ-ÜFE Endeksi: {duzeltme_donemi_endeksi}""",
        "example_inputs": {
            "bilanco_kalemi": "500 Sermaye Hesabı (Ödenmiş Sermaye: 2.000.000 TL)",
            "parasal_mi_parasal_olmayan_mi": "Parasal Olmayan Özkaynak Kalemi",
            "aktife_giris_tarihi_endeksi": "Ekim 2024 - Yİ-ÜFE: 3.650,20",
            "duzeltme_donemi_endeksi": "Aralık 2025 - Yİ-ÜFE: 4.810,40"
        }
    },
    {
        "id": "smmm-vergi-cezasi-ihbarnamesi-uzlasma-asistani",
        "name": "Vergi/Ceza İhbarnamesi VUK 376 İndirim vs Uzlaşma Karar Destekçisi",
        "category": "Vergi, SMMM & Beyanname Denetim",
        "description": "Vergi dairesi veya vergi inceleme raporu sonrası tebliğ edilen vergi ziyaı cezalarında VUK 376 indirim ile uzlaşmayı karşılaştırır.",
        "recommended_model": "gpt-4o",
        "tags": ["vergi-cezasi", "vuk-376", "uzlasma", "vergi-davasi", "smmm"],
        "variables": ["tarh_edilen_vergi_asli", "kesilen_vergi_ziyai_cezasi", "usulsuzluk_cezasi", "ihbarname_teblig_tarihi"],
        "system_prompt": """Sen Vergi Yargılama Hukuku ve VUK 376 (Ceza İndirimi) ile Tarhiyat Sonrası Uzlaşma uzmanısın.
Tebliğden itibaren 30 GÜNLÜK hak düşürücü sürede mükellefin 3 seçeneği vardır:
1. VUK 376 İndirim Talebi: Vergi ziyaı cezasının %50'si indirilerek vadesinde ödeme,
2. Uzlaşma Talebi: Vergi aslı ve ceza için Uzlaşma Komisyonuna başvuru,
3. Vergi Mahkemesinde Dava Açma.
Mükellef için finansal ve hukuki risk karşılaştırma matrisi sun.""",
        "user_prompt_template": """Vergi ceza ihbarnamesi karar desteği sağla:
Tarh Edilen Vergi Aslı: {tarh_edilen_vergi_asli} TL
Kesilen Vergi Ziyaı Cezası: {kesilen_vergi_ziyai_cezasi} TL
Varsa Usulsüzlük Cezası: {usulsuzluk_cezasi} TL
İhbarname Tebliğ Tarihi: {ihbarname_teblig_tarihi}""",
        "example_inputs": {
            "tarh_edilen_vergi_asli": "180000",
            "kesilen_vergi_ziyai_cezasi": "180000 (1 Kat Vergi Ziyaı)",
            "usulsuzluk_cezasi": "15000",
            "ihbarname_teblig_tarihi": "10 Eylül 2026"
        }
    },
    {
        "id": "smmm-sahte-fatura-ve-kod-listesi-analizi",
        "name": "Sahte Belge (Naylon Fatura) ve Özel Esaslar (Kod Listesi) Risk Analizörü",
        "category": "Vergi, SMMM & Beyanname Denetim",
        "description": "VUK 359 kapsamındaki sahte belge ve muhteviyatı itibarıyla yanıltıcı belge şüphelerini ve KDV özel esaslar riskini analiz eder.",
        "recommended_model": "gpt-4o",
        "tags": ["sahte-belge", "vuk-359", "ozel-esaslar", "kod-listesi", "adli-muhasebe"],
        "variables": ["tedarikci_profili", "islem_bedeli", "fiili_teslim_delilleri", "sektorel_riskler"],
        "system_prompt": """Sen VUK m. 359 (Kaçakçılık Suçları) ve KDV Genel Uygulama Tebliği 'Özel Esaslar' (Vergi İnceleme Kod Listesi) uzmanı bir adli muhasebecisin.
1. Bir faturanın sahte veya yanıltıcı sayılmaması için aranan 'Fiili Mal/Hizmet Teslimi' ispat kriterlerini (Sevk İrsaliyesi, Banka Dekontu, Kantar Fişi, Kamera Kayıtları),
2. Özel esaslara (Koda) alınan tedarikçilerden yapılan alımlarda KDV indiriminin reddedilme riskini,
3. Şirket yöneticilerini hapis cezası ve 3 kat vergi ziyaından koruyacak savunma dosyasını kurgula.""",
        "user_prompt_template": """Tedarikçi alımı sahte fatura ve özel esaslar risk analizini yap:
Tedarikçi Şirket Profili: {tedarikci_profili}
İşlem Bedeli: {islem_bedeli} TL
Eldeki Fiili Teslim Tevsik Delilleri: {fiili_teslim_delilleri}
Sektörel ve Ödeme Riskleri: {sektorel_riskler}""",
        "example_inputs": {
            "tedarikci_profili": "Yeni kurulan, sermayesi 50.000 TL olan, deposu veya çalışanı tespit edilemeyen toptancı şirketi",
            "islem_bedeli": "1.450.000 TL + KDV",
            "fiili_teslim_delilleri": "Yalnızca fatura mevcut, nakliye sevk irsaliyesi veya kantar fişi yok",
            "sektorel_riskler": "Hurda ve demir ticareti; ödemelerin bir kısmı elden nakit yapılmış."
        }
    },
    {
        "id": "smmm-personel-bordro-ve-sgk-tesvik-eslestirici",
        "name": "Personel Bordrosu ve SGK Prim Teşvikleri Eşleştirme Motoru",
        "category": "Vergi, SMMM & Beyanname Denetim",
        "description": "5510 %5 Hazine teşviki, ilave istihdam teşviki ve genç/kadın girişimci prim indirimlerini personelle eşleştirir.",
        "recommended_model": "gemini-1.5-flash",
        "tags": ["sgk-tesvik", "5510", "bordro-maliyeti", "istihdam", "ik"],
        "variables": ["personel_sayisi", "ortalama_brut_ucret", "borcu_yoktur_durumu", "yeni_istihdam_profili"],
        "system_prompt": """Sen Sosyal Güvenlik Kurumu (SGK) prim teşvikleri ve bordro optimizasyonu uzmanısın.
1. 5510 sayılı Kanun m. 81/ı uyarınca borcu olmayan işverenlere %5 Hazine prim indirimi şartlarını,
2. İŞKUR kayıtlı genç (18-29 yaş) ve kadın çalışanlarda 24-54 ay işveren hissesi prim desteğini,
3. Şirkete sağlanacak aylık ve yıllık net maliyet tasarrufunu hesapla.""",
        "user_prompt_template": """SGK teşvik simülasyonunu ve şartları çıkar:
Mevcut Personel Sayısı: {personel_sayisi}
Ortalama Aylık Brüt Ücret: {ortalama_brut_ucret} TL
Şirketin SGK/Vergi Borcu Durumu: {borcu_yoktur_durumu}
Yeni İşe Alınan Personel Profili: {yeni_istihdam_profili}""",
        "example_inputs": {
            "personel_sayisi": "15",
            "ortalama_brut_ucret": "35000",
            "borcu_yoktur_durumu": "SGK ve vergi borcu yok, beyannameler süresinde veriliyor",
            "yeni_istihdam_profili": "3 adet üniversite mezunu 22-25 yaş arası genç mühendis"
        }
    },
    {
        "id": "smmm-mizan-ve-gelir-tablosu-cfo-analizi",
        "name": "Mizan ve Gelir Tablosundan Yönetimsel CFO ve Rasyo Analizörü",
        "category": "Vergi, SMMM & Beyanname Denetim",
        "description": "Aylık mizan ve gelir tablosu verilerini finansal oranlara (Cari Oran, Likidite, Borçluluk) ve karar destek CFO özetine çevirir.",
        "recommended_model": "gpt-4o",
        "tags": ["mizan-analizi", "rasyolar", "cfo-raporu", "finansal-oranlar", "smmm"],
        "variables": ["donen_varliklar", "kisa_vadeli_borclar", "stoklar", "net_satislar", "donem_net_kari"],
        "system_prompt": """Sen finansal yönetim ve CFO seviyesinde bilanço analizi uzmanısın.
Mizan verilerinden:
1. Cari Oran (Dönen Varlıklar / KV Borçlar) ve Asit-Test Oranını,
2. Stok Devir Hızı ve Alacak Devir Hızını,
3. Net Kâr Marjı ve Özkaynak Kârlılığını hesapla.
Şirket yönetim kuruluna sunulacak 1 sayfalık stratejik 'Finansal Sağlık ve İyileştirme Raporu' üret.""",
        "user_prompt_template": """Mizan verilerinden CFO analizini üret:
Toplam Dönen Varlıklar: {donen_varliklar} TL
Kısa Vadeli Yabancı Kaynaklar: {kisa_vadeli_borclar} TL
Stoklar: {stoklar} TL
Net Satış Hasılatı: {net_satislar} TL
Dönem Net Kârı: {donem_net_kari} TL""",
        "example_inputs": {
            "donen_varliklar": "4500000",
            "kisa_vadeli_borclar": "3200000",
            "stoklar": "1800000",
            "net_satislar": "12000000",
            "donem_net_kari": "1450000"
        }
    }
]
