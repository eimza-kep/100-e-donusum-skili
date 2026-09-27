#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
100 E-Dönüşüm Skili CLI & Otomasyon Yöneticisi
Yapay Zeka ve LLM Ajanları (Cursor, Claude, Antigravity, OpenAI, Ollama) İçin Beceri Çalıştırıcı ve Dışa Aktarıcı.
"""

import sys
import os
import json
import argparse
import re

# Windows cp1254/cp1252 konsol kodlama koruması
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
if hasattr(sys.stderr, 'reconfigure'):
    try:
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from skills import ALL_SKILLS, SKILLS_BY_ID, SKILLS_BY_CATEGORY


def print_header():
    print("=" * 80)
    print("   🚀 100 E-DÖNÜŞÜM YAPAY ZEKA SKİLİ & HAZIR PROMPT KÜTÜPHANESİ")
    print("   Türkiye E-Dönüşüm Ekosistemi (GİB, VUK, TTK, UETS, KEP, UYAP, KVKK)")
    print("=" * 80)


def list_categories():
    print_header()
    print("\n📁 KATEGORİ LİSTESİ:")
    print("-" * 80)
    total = 0
    for idx, (cat, skills) in enumerate(SKILLS_BY_CATEGORY.items(), 1):
        print(f" {idx}. [{len(skills):2d} Beceri] {cat}")
        total += len(skills)
    print("-" * 80)
    print(f" Toplam: {len(SKILLS_BY_CATEGORY)} Kategori, {total} Beceri\n")


def list_skills(category_filter=None):
    print_header()
    if category_filter:
        skills = [s for s in ALL_SKILLS if category_filter.lower() in s["category"].lower()]
        title = f"'{category_filter}' Kategorisindeki Beceriler ({len(skills)} adet)"
    else:
        skills = ALL_SKILLS
        title = f"Tüm Beceriler ({len(skills)} adet)"

    print(f"\n📋 {title}:")
    print("-" * 80)
    print(f"{'No':<4} {'ID':<38} {'Model':<12} {'Kategori'}")
    print("-" * 80)
    for idx, s in enumerate(skills, 1):
        cat_short = s["category"][:22]
        print(f"{idx:<4} {s['id']:<38} {s['recommended_model']:<12} {cat_short}")
    print("-" * 80)
    print(f"Toplam {len(skills)} beceri listelendi.\n")


def search_skills(query):
    print_header()
    q = query.lower()
    matches = []
    for s in ALL_SKILLS:
        searchable = f"{s['id']} {s['name']} {s['category']} {s['description']} {' '.join(s['tags'])}".lower()
        if q in searchable:
            matches.append(s)

    print(f"\n🔍 '{query}' Arama Sonuçları ({len(matches)} eşleşme):")
    print("-" * 80)
    for idx, s in enumerate(matches, 1):
        print(f"\n[{idx}] {s['name']} (ID: {s['id']})")
        print(f"    Kategori : {s['category']} | Model: {s['recommended_model']}")
        print(f"    Açıklama : {s['description']}")
        print(f"    Etiketler: {', '.join(s['tags'])}")
    print("-" * 80 + "\n")


def show_skill(skill_id):
    skill = SKILLS_BY_ID.get(skill_id)
    if not skill:
        print(f"❌ HATA: '{skill_id}' ID'li beceri bulunamadı!")
        print("Tüm listeyi görmek için: python run_skill.py --list")
        sys.exit(1)

    print("=" * 80)
    print(f"🎯 BECERİ: {skill['name']}")
    print(f"🔑 ID: {skill['id']}")
    print(f"📁 Kategori: {skill['category']} | Önerilen Model: {skill['recommended_model']}")
    print(f"🏷️  Etiketler: {', '.join(skill['tags'])}")
    print("=" * 80)
    print(f"\n📖 AÇIKLAMA:\n{skill['description']}")
    print("\n⚙️  DEĞİŞKENLER (Variables):")
    for var in skill["variables"]:
        sample_val = skill["example_inputs"].get(var, "")
        print(f"  • {var} (Örnek: \"{sample_val}\")")

    print("\n🧠 SİSTEM PROMPTU (System Prompt):")
    print("-" * 40)
    print(skill["system_prompt"])
    print("-" * 40)

    print("\n💬 KULLANICI PROMPT ŞABLONU (User Prompt Template):")
    print("-" * 40)
    print(skill["user_prompt_template"])
    print("-" * 40)

    print("\n🧪 ÖRNEK GİRDİLERLE DOLDURULMUŞ PROMPT:")
    print("-" * 40)
    rendered = skill["user_prompt_template"].format(**skill["example_inputs"])
    print(rendered)
    print("-" * 40 + "\n")


def run_skill(skill_id, mock=False, inputs_json=None):
    skill = SKILLS_BY_ID.get(skill_id)
    if not skill:
        print(f"❌ HATA: '{skill_id}' ID'li beceri bulunamadı!")
        sys.exit(1)

    if inputs_json:
        try:
            inputs = json.loads(inputs_json)
        except Exception as e:
            print(f"❌ HATA: Girdi JSON'ı geçersiz: {e}")
            sys.exit(1)
    else:
        inputs = skill["example_inputs"]

    rendered_user_prompt = skill["user_prompt_template"].format(**inputs)

    print("=" * 80)
    print(f"⚡ ÇALIŞTIRILIYOR: {skill['name']} ({skill['id']})")
    print(f"🤖 Hedef Model: {skill['recommended_model']}")
    print("=" * 80)
    print("\n[1] SİSTEM PROMPTU ENJEKSİYONU:")
    print(skill["system_prompt"][:250] + "...\n")
    print("[2] HAZIRLANAN KULLANICI GİRDİSİ:")
    print(rendered_user_prompt)
    print("\n" + "=" * 80)

    if mock:
        print("💡 [MOCK ÇALIŞTIRMA MODU] LLM Yanıt Simülasyonu:")
        print("-" * 80)
        print(f"✅ Girdi Doğrulandı: {len(inputs)} parametre başarıyla işlendi.")
        print(f"✅ Denetim Tamamlandı: {skill['name']} analiz kuralları başarıyla uygulandı.")
        print(f"📊 Özet Rapor: GİB / VUK / TTK mevzuat kriterlerine göre 0 anomali tespit edildi.")
        print("-" * 80)
    else:
        print("ℹ️  Gerçek LLM API çağrısı için ortam değişkenlerini (OPENAI_API_KEY, ANTHROPIC_API_KEY) ayarlayabilir")
        print("    veya prompt çıktısını doğrudan Cursor / Claude / Antigravity arayüzüne yapıştırabilirsiniz.")
        print("    (Örnek simülasyonu görmek için '--mock' bayrağını ekleyiniz.)\n")


def export_json(output_path="skills.json"):
    data = {
        "title": "100 E-Dönüşüm Yapay Zeka Skili & Hazır Prompt Kütüphanesi",
        "version": "1.0.0",
        "organization": "eimza-kep",
        "repository": "https://github.com/eimza-kep/100-e-donusum-skili",
        "total_skills": len(ALL_SKILLS),
        "categories": list(SKILLS_BY_CATEGORY.keys()),
        "skills": ALL_SKILLS
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ Başarıyla dışa aktarıldı: {output_path} ({len(ALL_SKILLS)} beceri)")


def export_claude(output_path="claude_skills.xml"):
    lines = ["<skills>"]
    for s in ALL_SKILLS:
        lines.append(f'  <skill id="{s["id"]}">')
        lines.append(f'    <name>{s["name"]}</name>')
        lines.append(f'    <category>{s["category"]}</category>')
        lines.append(f'    <description>{s["description"]}</description>')
        lines.append(f'    <tags>{", ".join(s["tags"])}</tags>')
        lines.append('    <system_prompt>')
        for l in s["system_prompt"].strip().split("\n"):
            lines.append(f'      {l}')
        lines.append('    </system_prompt>')
        lines.append('    <template>')
        for l in s["user_prompt_template"].strip().split("\n"):
            lines.append(f'      {l}')
        lines.append('    </template>')
        lines.append('  </skill>')
    lines.append("</skills>")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✅ Claude XML formatında dışa aktarıldı: {output_path}")


def export_cursor(output_path=".cursorrules"):
    lines = [
        "# E-Dönüşüm AI Kuralları & 100 Beceri Referansı",
        "# eimza-kep/100-e-donusum-skili",
        "",
        "You are an expert E-Transformation (e-Dönüşüm), Turkish Tax Code (VUK), Commercial Code (TTK),",
        "Civil Procedure (HMK), Enforcement Law (İİK), and Data Protection (KVKK) AI Assistant.",
        "",
        "Available Skill Categories:",
    ]
    for cat, skills in SKILLS_BY_CATEGORY.items():
        lines.append(f"- **{cat}** ({len(skills)} skills):")
        for s in skills[:3]:
            lines.append(f"  • `{s['id']}`: {s['name']}")
        if len(skills) > 3:
            lines.append(f"  • ... ve {len(skills) - 3} beceri daha (Bkz: skills.json)")

    lines.extend([
        "",
        "## Core Principles:",
        "1. Always cite exact article numbers: VUK m. 227, TTK m. 82, 5070 m. 5, HMK m. 119, KVKK m. 10.",
        "2. For e-Invoice/UBL-TR 1.2.1, ensure strict schema compliance (UUID, Schematron, CAC/CBC).",
        "3. Never provide legal or tax advice without disclaimers.",
        "4. Always support cryptographic verification (X.509, SHA-256, TSA, PAdES/CAdES/XAdES).",
        "",
        "# For full skill catalogue, refer to skills/ directory or skills.json"
    ])

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✅ Cursor rules dosyası oluşturuldu: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="100 E-Dönüşüm Yapay Zeka Skili & Hazır Prompt Kütüphanesi CLI"
    )
    parser.add_argument("--list", action="store_true", help="Tüm becerileri listeler")
    parser.add_argument("--categories", action="store_true", help="Tüm kategorileri ve beceri sayılarını listeler")
    parser.add_argument("--category", type=str, help="Belirli bir kategorideki becerileri filtreler")
    parser.add_argument("--search", type=str, help="Becerilerde anahtar kelime araması yapar")
    parser.add_argument("--skill", type=str, help="Belirtilen becerinin tüm detaylarını görüntüler")
    parser.add_argument("--run", type=str, help="Belirtilen beceriyi örnek verilerle çalıştırır")
    parser.add_argument("--mock", action="store_true", help="Mock simülasyon yanıtı üretir")
    parser.add_argument("--inputs", type=str, help="JSON formatında özel girdi parametreleri")
    parser.add_argument("--export-json", nargs="?", const="skills.json", help="Becerileri JSON olarak dışa aktarır")
    parser.add_argument("--export-claude", nargs="?", const="claude_skills.xml", help="Claude XML formatında dışa aktarır")
    parser.add_argument("--export-cursor", nargs="?", const=".cursorrules", help="Cursor .cursorrules formatında dışa aktarır")

    args = parser.parse_args()

    if args.categories:
        list_categories()
    elif args.list:
        list_skills(args.category)
    elif args.category:
        list_skills(args.category)
    elif args.search:
        search_skills(args.search)
    elif args.skill:
        show_skill(args.skill)
    elif args.run:
        run_skill(args.run, mock=args.mock, inputs_json=args.inputs)
    elif args.export_json:
        export_json(args.export_json)
    elif args.export_claude:
        export_claude(args.export_claude)
    elif args.export_cursor:
        export_cursor(args.export_cursor)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
