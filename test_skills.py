# -*- coding: utf-8 -*-
"""
100 E-Dönüşüm Skili Test Paketi
Tüm becerilerin şema bütünlüğünü, değişken eşleşmelerini ve prompt şablonlarını doğrular.
"""

import unittest
import re
from skills import ALL_SKILLS, SKILLS_BY_ID, SKILLS_BY_CATEGORY


class TestEDonusumSkills(unittest.TestCase):

    def test_total_skill_count(self):
        """Toplam tam 100 beceri olduğunu doğrula."""
        self.assertEqual(len(ALL_SKILLS), 100, f"Beklenen: 100 beceri, Bulunan: {len(ALL_SKILLS)}")

    def test_category_count(self):
        """8 ana kategori olduğunu doğrula."""
        self.assertEqual(len(SKILLS_BY_CATEGORY), 8)

    def test_unique_ids(self):
        """Tüm beceri ID'lerinin benzersiz olduğunu doğrula."""
        ids = [s["id"] for s in ALL_SKILLS]
        self.assertEqual(len(ids), len(set(ids)), "Tekrar eden beceri ID'si bulundu!")

    def test_schema_integrity(self):
        """Her becerinin zorunlu şema alanlarını taşıdığını doğrula."""
        required_fields = [
            "id",
            "name",
            "category",
            "description",
            "recommended_model",
            "tags",
            "variables",
            "system_prompt",
            "user_prompt_template",
            "example_inputs"
        ]
        for s in ALL_SKILLS:
            for field in required_fields:
                self.assertIn(field, s, f"Skill '{s.get('id', 'Bilinmeyen')}' içinde '{field}' alanı eksik!")
                self.assertTrue(s[field], f"Skill '{s['id']}' içindeki '{field}' boş olamaz!")

    def test_variable_matching_and_interpolation(self):
        """Template içindeki {degisken} yer tutucularının variables listesi ve example_inputs ile tam eşleştiğini doğrula."""
        for s in ALL_SKILLS:
            skill_id = s["id"]
            template = s["user_prompt_template"]
            variables = s["variables"]
            examples = s["example_inputs"]

            # Regex ile template içindeki {degisken_adi} alanlarını bul
            placeholders = re.findall(r"\{([a-zA-Z0-9_]+)\}", template)
            placeholder_set = set(placeholders)
            variable_set = set(variables)

            self.assertEqual(
                placeholder_set,
                variable_set,
                f"Skill '{skill_id}': Template'teki yer tutucular ({placeholder_set}) ile variables ({variable_set}) uyuşmuyor!"
            )

            # example_inputs tüm değişkenleri içeriyor mu?
            for var in variables:
                self.assertIn(
                    var,
                    examples,
                    f"Skill '{skill_id}': '{var}' değişkeni example_inputs içinde tanımlı değil!"
                )

            # İnterpolasyonun sorunsuz çalıştığını test et
            try:
                rendered_prompt = template.format(**examples)
                self.assertTrue(len(rendered_prompt) > 20, f"Skill '{skill_id}': Üretilen prompt çok kısa!")
            except Exception as e:
                self.fail(f"Skill '{skill_id}' prompt interpolasyon hatası verdi: {e}")

    def test_content_quality(self):
        """Sistem promptlarının ve açıklamaların yeterli derinlikte olduğunu doğrula."""
        for s in ALL_SKILLS:
            skill_id = s["id"]
            self.assertGreater(len(s["system_prompt"]), 50, f"Skill '{skill_id}' sistem promptu çok kısa!")
            self.assertGreater(len(s["description"]), 20, f"Skill '{skill_id}' açıklaması çok kısa!")
            self.assertGreaterEqual(len(s["tags"]), 2, f"Skill '{skill_id}' en az 2 etiket içermeli!")


if __name__ == "__main__":
    unittest.main()
