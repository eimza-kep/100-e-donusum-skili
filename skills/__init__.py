# -*- coding: utf-8 -*-
"""
100 E-Dönüşüm Skili Kütüphanesi
Yapay Zeka ve LLM Ajanları (Cursor, Claude, Antigravity, OpenAI, Ollama) İçin Hazır Beceriler.
"""

from .category_01_efatura import SKILLS as SKILLS_EFATURA
from .category_02_edefter import SKILLS as SKILLS_EDEFTER
from .category_03_eirsaliye import SKILLS as SKILLS_EIRSALIYE
from .category_04_eimza import SKILLS as SKILLS_EIMZA
from .category_05_kep import SKILLS as SKILLS_KEP
from .category_06_uyap import SKILLS as SKILLS_UYAP
from .category_07_smmm import SKILLS as SKILLS_SMMM
from .category_08_kvkk import SKILLS as SKILLS_KVKK

ALL_SKILLS = (
    SKILLS_EFATURA +
    SKILLS_EDEFTER +
    SKILLS_EIRSALIYE +
    SKILLS_EIMZA +
    SKILLS_KEP +
    SKILLS_UYAP +
    SKILLS_SMMM +
    SKILLS_KVKK
)

SKILLS_BY_ID = {s["id"]: s for s in ALL_SKILLS}

SKILLS_BY_CATEGORY = {
    "e-Fatura & e-Arşiv": SKILLS_EFATURA,
    "e-Defter & Berat": SKILLS_EDEFTER,
    "e-İrsaliye & Lojistik": SKILLS_EIRSALIYE,
    "e-İmza & Mali Mühür & PKI": SKILLS_EIMZA,
    "KEP & UETS & Elektronik Tebligat": SKILLS_KEP,
    "UYAP & Hukuk & LegalTech": SKILLS_UYAP,
    "Vergi, SMMM & Beyanname Denetim": SKILLS_SMMM,
    "KVKK, Dijital Kimlik & Siber Güvenlik": SKILLS_KVKK,
}

__all__ = [
    "ALL_SKILLS",
    "SKILLS_BY_ID",
    "SKILLS_BY_CATEGORY",
    "SKILLS_EFATURA",
    "SKILLS_EDEFTER",
    "SKILLS_EIRSALIYE",
    "SKILLS_EIMZA",
    "SKILLS_KEP",
    "SKILLS_UYAP",
    "SKILLS_SMMM",
    "SKILLS_KVKK",
]
