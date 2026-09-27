# -*- coding: utf-8 -*-
"""
Dokümantasyon Üretici
Tüm 100 becerinin dokümantasyonunu ve kategori bazlı kılavuzlarını docs/ dizini altında otomatik oluşturur.
"""

import os
import sys
from skills import ALL_SKILLS, SKILLS_BY_CATEGORY

# Windows konsol desteği
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

DOCS_DIR = os.path.join(os.path.dirname(__file__), "docs")
os.makedirs(DOCS_DIR, exist_ok=True)

CAT_FILES = {
    "e-Fatura & e-Arşiv": "01_efatura_ve_earsiv.md",
    "e-Defter & Berat": "02_edefter_ve_berat.md",
    "e-İrsaliye & Lojistik": "03_eirsaliye_ve_lojistik.md",
    "e-İmza & Mali Mühür & PKI": "04_eimza_ve_malimuhur.md",
    "KEP & UETS & Elektronik Tebligat": "05_kep_ve_uets.md",
    "UYAP & Hukuk & LegalTech": "06_uyap_ve_hukuk.md",
    "Vergi, SMMM & Beyanname Denetim": "07_smmm_ve_beyanname.md",
    "KVKK, Dijital Kimlik & Siber Güvenlik": "08_kvkk_ve_guvenlik.md",
}

CAT_INTROS = {
    "e-Fatura & e-Arşiv": "GİB 509 Sıra No.lu VUK Genel Tebliği, UBL-TR 1.2.1 şeması, KDV tevkifatı, 8 günlük ticari fatura itirazı ve e-Arşiv limitleri.",
    "e-Defter & Berat": "1 Sıra No.lu Elektronik Defter Genel Tebliği, yevmiye-kebir balansı, berat SHA-256 hash hesabı, GİB zaman damgası ve ikincil kopya yükümlülükleri.",
    "e-İrsaliye & Lojistik": "Fiili sevk saati, karekodlu sevk irsaliyesi, yol denetimi kolluk ibrazı, Hal Kayıt Sistemi (HKS) künye entegrasyonu ve konsinye süreçleri.",
    "e-İmza & Mali Mühür & PKI": "5070 Sayılı Elektronik İmza Kanunu, TÜBİTAK Kamu SM / Özel ESHS altyapısı, PAdES/CAdES/XAdES standartları, AKİS kart sürücüleri ve PUK yönetimi.",
    "KEP & UETS & Elektronik Tebligat": "7201 Sayılı Tebligat Kanunu, UETS 5 günlük tebellüğ süresi, KEP delil paketleri (EYS/EAS), İİK 89/1 haciz itirazları ve İK bordro tebligatı.",
    "UYAP & Hukuk & LegalTech": "Adalet Bakanlığı UYAP Avukat/Vatandaş Portalı, UDF 1.8 XML doküman formatı, HMK m. 119 dava dilekçeleri, İcra Takip ve AAÜT vekalet ücreti hesaplamaları.",
    "Vergi, SMMM & Beyanname Denetim": "Gelir İdaresi BDP sistemi, 1 No'lu KDV, Muhtasar ve Prim Hizmet (MPHB), Geçici Vergi, VUK 298/A enflasyon düzeltmesi ve 5510 SGK teşvik analizleri.",
    "KVKK, Dijital Kimlik & Siber Güvenlik": "6698 Sayılı KVKK m. 11 veri sahibi başvuruları, VERBİS kayıt eşikleri, 72 saatlik veri ihlali bildirimi, e-fatura oltalama analizi ve Zero Trust mimarisi.",
}


def generate_category_docs():
    for cat_name, file_name in CAT_FILES.items():
        skills = SKILLS_BY_CATEGORY[cat_name]
        out_path = os.path.join(DOCS_DIR, file_name)

        lines = [
            f"# {cat_name} Becerileri",
            "",
            f"> **Kapsam:** {CAT_INTROS.get(cat_name, '')}",
            f"> **Toplam Beceri Sayısı:** {len(skills)} Adet",
            "",
            "## İçindekiler",
            ""
        ]

        for s in skills:
            lines.append(f"- [{s['name']} (`{s['id']}`)](#{s['id']})")
        lines.append("")
        lines.append("---")
        lines.append("")

        for idx, s in enumerate(skills, 1):
            lines.append(f"### <a id=\"{s['id']}\"></a> {idx}. {s['name']}")
            lines.append(f"**ID:** `{s['id']}`  ")
            lines.append(f"**Önerilen Model:** `{s['recommended_model']}`  ")
            lines.append(f"**Etiketler:** {', '.join([f'`{t}`' for t in s['tags']])}  ")
            lines.append("")
            lines.append(f"**Açıklama:**  \n{s['description']}")
            lines.append("")
            lines.append("#### Sistem İstemi (System Prompt):")
            lines.append("```text")
            lines.append(s["system_prompt"])
            lines.append("```")
            lines.append("")
            lines.append("#### Kullanıcı İstemi Şablonu (User Prompt Template):")
            lines.append("```text")
            lines.append(s["user_prompt_template"])
            lines.append("```")
            lines.append("")
            lines.append("#### Örnek Girdi Verileri (Example Inputs):")
            lines.append("```json")
            import json
            lines.append(json.dumps(s["example_inputs"], ensure_ascii=False, indent=2))
            lines.append("```")
            lines.append("")
            lines.append("---")
            lines.append("")

        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"✅ Kategori dokümanı oluşturuldu: {out_path}")


def generate_integration_guide():
    out_path = os.path.join(DOCS_DIR, "integration_guide.md")
    content = """# 🚀 E-Dönüşüm AI Becerileri Entegrasyon Kılavuzu

Bu kılavuz, `100-e-donusum-skili` kütüphanesindeki becerilerin Cursor, Claude, OpenAI, Antigravity ve yerel modeller (Ollama / vLLM) ile nasıl entegre edileceğini açıklar.

---

## 1. Cursor IDE Entegrasyonu

Repository kök dizininde oluşturulan `.cursorrules` dosyası Cursor tarafından otomatik algılanır.

### Kurulum:
```bash
python run_skill.py --export-cursor
```

### Prompt Kullanımı:
Cursor chat penceresinde doğrudan beceri ID'sini ve değişkenleri yazabilirsiniz:
```text
@skills/category_01_efatura.py dosyasındaki 'efatura-kdv-tevkifat-denetleyici' becerisini kullanarak 
aşağıdaki fatura satırını tevkifat mevzuatına göre denetle:
Hizmet Türü: Güvenlik Hizmeti
Matrah: 120.000 TL
KDV: %20
Uygulanan Tevkifat: 9/10
```

---

## 2. Claude Projects & System Prompts

Claude Projects içine `claude_skills.xml` dosyasını "Project Knowledge" olarak ekleyebilirsiniz.

### Dışa Aktarma:
```bash
python run_skill.py --export-claude
```

Claude bu XML dosyasındaki tüm sistem istemlerini ve şablonları doğrudan referans alarak e-dönüşüm kurallarına harfiyen uyar.

---

## 3. Python SDK & API Entegrasyonu

Kendi yazılımınızda veya backend servisinizde doğrudan Python paketi olarak çağırabilirsiniz:

```python
from skills import SKILLS_BY_ID

# Beceriyi ID ile çek
skill = SKILLS_BY_ID["efatura-8-gun-ticari-fatura-itiraz-yoneticisi"]

# Girdileri hazırla
inputs = {
    "fatura_teblig_tarihi": "2026-09-20",
    "bugunun_tarihi": "2026-09-27",
    "itiraz_kanali": "KEP (Kayıtlı Elektronik Posta)",
    "itiraz_gerekcesi": "Sözleşmeye aykırı fiyat farkı ve hatalı teslimat",
    "fatura_tutari": "180.000 TL"
}

# Şablonu render et
rendered_prompt = skill["user_prompt_template"].format(**inputs)
system_prompt = skill["system_prompt"]

print("Sistem İstemi:\\n", system_prompt)
print("Kullanıcı İstemi:\\n", rendered_prompt)
```

---

## 4. Yerel Modeller & Ollama (DeepSeek / Llama 3)

Yerel LLM'lerde (Ollama) sistem istemini Modelfile içine gömebilirsiniz:

```dockerfile
FROM deepseek-r1:14b
SYSTEM \"\"\"
Sen Türk Vergi Hukuku ve GİB E-Fatura UBL-TR 1.2.1 standartları konusunda uzman bir sistem mimarısın.
\"\"\"
```

CLI üzerinden mock veya yerel girdiyle çalıştırma:
```bash
python run_skill.py --run efatura-ubl-anomali-avcisi --mock
```

---

## 5. Webhook ve Otomatik ERP/Muhasebe Entegrasyonu

`skills.json` dosyasını ERP yazılımınızın (Logo, Mikro, Netsis, Zirve, Luca) mikroservisine bağlayarak her düzenlenen faturanın arka planda AI ile ön denetimden geçirilmesini sağlayabilirsiniz.
"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Entegrasyon kılavuzu oluşturuldu: {out_path}")


if __name__ == "__main__":
    generate_category_docs()
    generate_integration_guide()
