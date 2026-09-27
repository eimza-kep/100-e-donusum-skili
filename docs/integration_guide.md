# 🚀 E-Dönüşüm AI Becerileri Entegrasyon Kılavuzu

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

print("Sistem İstemi:\n", system_prompt)
print("Kullanıcı İstemi:\n", rendered_prompt)
```

---

## 4. Yerel Modeller & Ollama (DeepSeek / Llama 3)

Yerel LLM'lerde (Ollama) sistem istemini Modelfile içine gömebilirsiniz:

```dockerfile
FROM deepseek-r1:14b
SYSTEM """
Sen Türk Vergi Hukuku ve GİB E-Fatura UBL-TR 1.2.1 standartları konusunda uzman bir sistem mimarısın.
"""
```

CLI üzerinden mock veya yerel girdiyle çalıştırma:
```bash
python run_skill.py --run efatura-ubl-anomali-avcisi --mock
```

---

## 5. Webhook ve Otomatik ERP/Muhasebe Entegrasyonu

`skills.json` dosyasını ERP yazılımınızın (Logo, Mikro, Netsis, Zirve, Luca) mikroservisine bağlayarak her düzenlenen faturanın arka planda AI ile ön denetimden geçirilmesini sağlayabilirsiniz.
