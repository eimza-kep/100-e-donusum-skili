# -*- coding: utf-8 -*-
"""
build_web.py
------------
100+ E-Dönüşüm Skili için tarayıcı tabanlı, sıfır bağımlılıklı,
etkileşimli ve yerel LLM (Ollama) destekli Web Playground arayüzü üretir.
Hem root index.html (GitHub Pages için) hem de web/index.html üretir.
"""

import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILLS_JSON_PATH = os.path.join(ROOT_DIR, "skills.json")
INDEX_PATH = os.path.join(ROOT_DIR, "index.html")
WEB_DIR = os.path.join(ROOT_DIR, "web")
os.makedirs(WEB_DIR, exist_ok=True)
WEB_INDEX_PATH = os.path.join(WEB_DIR, "index.html")

with open(SKILLS_JSON_PATH, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

skills = raw_data["skills"] if isinstance(raw_data, dict) and "skills" in raw_data else raw_data

skills_json_str = json.dumps(skills, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>100+ E-Dönüşüm AI Skili & Prompt Playground | Türkiye LegalTech & FinTech</title>
    <meta name="description" content="Türkiye E-Dönüşüm ekosistemi (GİB, VUK, TTK, UETS, KEP, UYAP, KVKK) için 102 adet açık kaynaklı yapay zeka becerisi ve interaktif prompt playground.">
    <style>
        :root {
            --primary: #4f46e5;
            --primary-hover: #4338ca;
            --primary-light: #eef2ff;
            --secondary: #0f172a;
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --border: #e2e8f0;
            --text-main: #1e293b;
            --text-muted: #64748b;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --sidebar-width: 360px;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
        body { display: flex; height: 100vh; background: var(--bg); color: var(--text-main); overflow: hidden; }

        /* Sidebar */
        .sidebar {
            width: var(--sidebar-width);
            background: var(--secondary);
            color: white;
            display: flex;
            flex-direction: column;
            border-right: 1px solid #1e293b;
            flex-shrink: 0;
        }
        .sidebar-header {
            padding: 18px 20px;
            border-bottom: 1px solid #1e293b;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .sidebar-header h1 { font-size: 1.05rem; font-weight: 700; color: #f8fafc; display: flex; align-items: center; gap: 8px; }
        .badge { font-size: 0.72rem; padding: 3px 8px; border-radius: 999px; font-weight: 600; }
        .badge-primary { background: var(--primary); color: white; }
        .badge-gray { background: #334155; color: #94a3b8; }

        .sidebar-search { padding: 12px 16px; border-bottom: 1px solid #1e293b; display: flex; flex-direction: column; gap: 8px; }
        .sidebar-search input {
            width: 100%; padding: 9px 14px; background: #1e293b; border: 1px solid #334155;
            border-radius: 8px; color: white; font-size: 0.85rem; outline: none;
        }
        .sidebar-search input:focus { border-color: var(--primary); }

        .category-filters {
            display: flex; gap: 6px; overflow-x: auto; padding-bottom: 4px;
        }
        .category-filters::-webkit-scrollbar { height: 4px; }
        .category-filters::-webkit-scrollbar-thumb { background: #334155; border-radius: 4px; }
        .cat-chip {
            padding: 4px 10px; font-size: 0.72rem; border-radius: 6px; cursor: pointer;
            background: #1e293b; color: #94a3b8; white-space: nowrap; border: 1px solid #334155;
        }
        .cat-chip:hover { background: #334155; color: white; }
        .cat-chip.active { background: var(--primary); color: white; border-color: var(--primary); }

        .skills-nav { flex: 1; overflow-y: auto; padding: 8px 0; }
        .category-group-title {
            padding: 10px 18px 4px 18px; font-size: 0.70rem; font-weight: 700;
            color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em;
        }
        .skill-item {
            padding: 10px 18px; font-size: 0.82rem; color: #cbd5e1; cursor: pointer;
            display: flex; flex-direction: column; gap: 3px; border-left: 3px solid transparent;
            transition: all 0.15s;
        }
        .skill-item:hover { background: #1e293b; color: white; }
        .skill-item.active { background: #1e293b; color: white; border-left-color: var(--primary); font-weight: 600; }
        .skill-item-id { font-family: monospace; font-size: 0.72rem; color: #94a3b8; }

        /* Main Workspace */
        .main-content { flex: 1; display: flex; flex-direction: column; overflow: hidden; }

        /* Topbar */
        .topbar {
            height: 60px; background: var(--card-bg); border-bottom: 1px solid var(--border);
            display: flex; justify-content: space-between; align-items: center; padding: 0 24px; flex-shrink: 0;
        }
        .topbar-left { display: flex; align-items: center; gap: 12px; }
        .topbar-title { font-size: 1.1rem; font-weight: 700; color: #0f172a; }
        .topbar-actions { display: flex; align-items: center; gap: 10px; }

        /* Content Area */
        .workspace { flex: 1; overflow-y: auto; padding: 24px; display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }

        .card {
            background: var(--card-bg); border: 1px solid var(--border); border-radius: 12px;
            display: flex; flex-direction: column; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);
        }
        .card-header {
            padding: 14px 20px; border-bottom: 1px solid var(--border); background: #fafafa;
            display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;
        }
        .card-header h2 { font-size: 0.92rem; font-weight: 700; color: #334155; display: flex; align-items: center; gap: 6px; }
        .card-body { padding: 20px; flex: 1; display: flex; flex-direction: column; gap: 14px; overflow-y: auto; }

        .meta-badges { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 6px; }
        .tag-pill { font-size: 0.72rem; background: var(--bg); border: 1px solid var(--border); padding: 3px 8px; border-radius: 6px; color: var(--text-muted); }

        /* Parameter Form */
        .form-group { display: flex; flex-direction: column; gap: 6px; }
        .form-group label { font-size: 0.80rem; font-weight: 600; color: #334155; font-family: monospace; }
        .form-control {
            width: 100%; padding: 9px 12px; border: 1px solid var(--border); border-radius: 8px;
            font-size: 0.85rem; outline: none; background: #f8fafc; transition: border-color 0.2s;
        }
        .form-control:focus { border-color: var(--primary); background: white; }
        textarea.form-control { min-height: 80px; resize: vertical; line-height: 1.45; }

        /* Code/Prompt Previews */
        .code-box {
            background: #0f172a; color: #f8fafc; border-radius: 8px; padding: 14px;
            font-family: Consolas, 'Fira Code', Monaco, monospace; font-size: 0.82rem;
            line-height: 1.5; overflow-x: auto; white-space: pre-wrap; word-break: break-word;
            max-height: 320px; overflow-y: auto;
        }

        .btn-group { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
        .btn {
            padding: 8px 14px; border-radius: 8px; font-size: 0.82rem; font-weight: 600; cursor: pointer;
            border: none; display: inline-flex; align-items: center; gap: 6px; transition: all 0.2s;
        }
        .btn-primary { background: var(--primary); color: white; }
        .btn-primary:hover { background: var(--primary-hover); }
        .btn-secondary { background: #e2e8f0; color: #334155; }
        .btn-secondary:hover { background: #cbd5e1; }
        .btn-outline { background: white; border: 1px solid var(--border); color: #475569; }
        .btn-outline:hover { background: #f8fafc; border-color: #cbd5e1; }
        .btn-sm { padding: 5px 10px; font-size: 0.76rem; border-radius: 6px; }

        /* Tabs inside Cards */
        .tab-headers { display: flex; gap: 6px; border-bottom: 1px solid var(--border); padding-bottom: 8px; margin-bottom: 8px; }
        .tab-btn {
            background: none; border: none; font-size: 0.82rem; font-weight: 600; color: var(--text-muted);
            padding: 6px 12px; border-radius: 6px; cursor: pointer;
        }
        .tab-btn.active { background: var(--primary-light); color: var(--primary); }

        /* Toast */
        .toast {
            position: fixed; bottom: 24px; right: 24px; background: #0f172a; color: white;
            padding: 10px 18px; border-radius: 8px; font-size: 0.85rem; display: none;
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3); z-index: 200;
        }

        /* Modal */
        .modal-overlay {
            position: fixed; inset: 0; background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(2px);
            display: none; justify-content: center; align-items: center; z-index: 100;
        }
        .modal {
            background: white; width: 520px; max-width: 90vw; border-radius: 14px;
            box-shadow: 0 20px 25px -5px rgba(0,0,0,0.25); overflow: hidden; display: flex; flex-direction: column;
        }
        .modal-header {
            padding: 16px 20px; border-bottom: 1px solid var(--border);
            display: flex; justify-content: space-between; align-items: center;
        }
        .modal-body { padding: 20px; display: flex; flex-direction: column; gap: 14px; }
        .modal-footer { padding: 14px 20px; border-top: 1px solid var(--border); background: #fafafa; display: flex; justify-content: flex-end; gap: 8px; }

        @media (max-width: 1024px) {
            .workspace { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>

<!-- Sidebar -->
<div class="sidebar">
    <div class="sidebar-header">
        <h1>🇹🇷 E-Dönüşüm Skilleri</h1>
        <span class="badge badge-primary" id="totalSkillsBadge">102 Beceri</span>
    </div>
    <div class="sidebar-search">
        <input type="text" id="searchInput" placeholder="Beceri, mevzuat, tag ara (ör: tevkifat, ubl, udf)..." oninput="filterSkills()">
        <div class="category-filters" id="categoryFilters">
            <span class="cat-chip active" onclick="setCategoryFilter('all')">Hepsi</span>
            <span class="cat-chip" onclick="setCategoryFilter('e-Fatura')">e-Fatura</span>
            <span class="cat-chip" onclick="setCategoryFilter('e-Defter')">e-Defter</span>
            <span class="cat-chip" onclick="setCategoryFilter('e-İrsaliye')">e-İrsaliye</span>
            <span class="cat-chip" onclick="setCategoryFilter('e-İmza')">e-İmza</span>
            <span class="cat-chip" onclick="setCategoryFilter('KEP')">KEP</span>
            <span class="cat-chip" onclick="setCategoryFilter('UYAP')">UYAP</span>
            <span class="cat-chip" onclick="setCategoryFilter('SMMM')">SMMM</span>
            <span class="cat-chip" onclick="setCategoryFilter('KVKK')">KVKK</span>
        </div>
    </div>
    <div class="skills-nav" id="skillsNav"></div>
</div>

<!-- Main Area -->
<div class="main-content">
    <!-- Topbar -->
    <div class="topbar">
        <div class="topbar-left">
            <div class="topbar-title" id="activeSkillTitle">Beceri Yükleniyor...</div>
        </div>
        <div class="topbar-actions">
            <button class="btn btn-outline btn-sm" onclick="exportCurrentSkillJson()">💾 Beceri JSON</button>
            <button class="btn btn-outline btn-sm" onclick="openOllamaSettings()">🦙 Ollama / LLM Ayarları</button>
            <a href="https://github.com/eimza-kep/100-e-donusum-skili" target="_blank" class="btn btn-secondary btn-sm" style="text-decoration:none;">⭐ GitHub</a>
        </div>
    </div>

    <!-- Workspace -->
    <div class="workspace">
        <!-- Left Column: Skill Metadata & Dynamic Variable Form -->
        <div class="card">
            <div class="card-header">
                <h2>📝 Beceri Parametreleri & Bilgileri</h2>
                <div class="btn-group">
                    <button class="btn btn-outline btn-sm" onclick="loadSampleInputs()">✨ Örnek Değerleri Yükle</button>
                    <button class="btn btn-outline btn-sm" onclick="clearInputs()">Temizle</button>
                </div>
            </div>
            <div class="card-body">
                <div class="meta-badges">
                    <span class="badge badge-gray" id="skillCategoryBadge">Kategori</span>
                    <span class="badge badge-primary" id="skillModelBadge">Önerilen Model</span>
                    <span class="badge badge-gray" id="skillIdBadge" style="font-family:monospace;">ID</span>
                </div>
                <p id="skillDescText" style="font-size:0.86rem; color:var(--text-muted); line-height:1.45;"></p>
                <div id="skillTagsContainer" style="display:flex; gap:6px; flex-wrap:wrap;"></div>

                <hr style="border:none; border-top:1px solid var(--border); margin:4px 0;">

                <h3 style="font-size:0.88rem; font-weight:700; color:#334155;">Şablon Parametreleri (Dinamik Girdi)</h3>
                <div id="parametersForm" style="display:flex; flex-direction:column; gap:12px;"></div>
            </div>
        </div>

        <!-- Right Column: Live Prompt Preview & Execution -->
        <div class="card">
            <div class="card-header">
                <h2>⚡ Derlenen İstemi İncele & Çalıştır</h2>
                <div class="btn-group">
                    <button class="btn btn-primary btn-sm" onclick="copyCompiledPrompt()">📋 Promptu Kopyala</button>
                    <button class="btn btn-outline btn-sm" onclick="executeWithLocalOllama()">🚀 Ollama ile Çalıştır</button>
                </div>
            </div>
            <div class="card-body">
                <div class="tab-headers">
                    <button class="tab-btn active" id="tabUserPrompt" onclick="switchPromptTab('user')">👤 Derlenmiş Kullanıcı Promptu</button>
                    <button class="tab-btn" id="tabSystemPrompt" onclick="switchPromptTab('system')">🛡️ Sistem İstemi (System)</button>
                    <button class="tab-btn" id="tabExecution" onclick="switchPromptTab('exec')">🤖 Model Çıktısı (AI)</button>
                </div>

                <div id="userPromptView">
                    <div class="code-box" id="compiledPromptBox">Prompt hazırlanıyor...</div>
                </div>

                <div id="systemPromptView" style="display:none;">
                    <div class="code-box" id="systemPromptBox"></div>
                </div>

                <div id="executionView" style="display:none; flex-direction:column; gap:10px;">
                    <div style="display:flex; gap:8px; align-items:center;">
                        <span style="font-size:0.82rem; font-weight:600;">Hedef:</span>
                        <input type="text" id="ollamaHostInput" value="http://127.0.0.1:11434" class="form-control" style="width:180px; padding:5px 8px; font-size:0.78rem;">
                        <input type="text" id="ollamaModelInput" value="llama3.2" class="form-control" style="width:110px; padding:5px 8px; font-size:0.78rem;">
                        <button class="btn btn-primary btn-sm" onclick="runAiInPlayground()">⚡ Gönder</button>
                    </div>
                    <div class="code-box" id="modelOutputBox" style="min-height:180px; color:#a7f3d0;">Sonuç burada görüntülenecektir...</div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Settings Modal -->
<div class="modal-overlay" id="settingsModal">
    <div class="modal">
        <div class="modal-header">
            <h3 style="font-size:1.05rem; font-weight:700;">⚙️ Yerel LLM / Ollama Ayarları</h3>
            <button class="btn btn-outline btn-sm" onclick="closeOllamaSettings()">&times;</button>
        </div>
        <div class="modal-body">
            <p style="font-size:0.84rem; color:var(--text-muted); line-height:1.45;">
                Tarayıcı üzerinden yerel makinenizde koşan <b>Ollama (Llama 3, DeepSeek, Qwen)</b> modeline doğrudan bağlanabilirsiniz.
            </p>
            <div class="form-group">
                <label>Ollama API Host:</label>
                <input type="text" id="modalHost" class="form-control" value="http://127.0.0.1:11434">
                <small style="color:#64748b; font-size:0.74rem;">İpucu: <code>OLLAMA_ORIGINS="*" ollama serve</code> ile CORS izni verilmelidir.</small>
            </div>
            <div class="form-group">
                <label>Varsayılan Model Adı:</label>
                <input type="text" id="modalModel" class="form-control" value="llama3.2" placeholder="llama3.2, deepseek-r1, qwen2.5">
            </div>
        </div>
        <div class="modal-footer">
            <button class="btn btn-secondary btn-sm" onclick="closeOllamaSettings()">Kapat</button>
            <button class="btn btn-primary btn-sm" onclick="saveOllamaSettings()">Kaydet</button>
        </div>
    </div>
</div>

<!-- Toast -->
<div class="toast" id="toast"></div>

<script>
const SKILLS_DATA = /*{{SKILLS_DATA_JSON}}*/;

let activeSkillId = SKILLS_DATA[0].id;
let currentCategoryFilter = 'all';
let currentSearchQuery = '';
let currentPromptTab = 'user';

function initPlayground() {
    renderSkillsNav();
    selectSkill(activeSkillId);
    
    // Local storage'dan host/model al
    const savedHost = localStorage.getItem('ollama_host');
    const savedModel = localStorage.getItem('ollama_model');
    if (savedHost) {
        document.getElementById('ollamaHostInput').value = savedHost;
        document.getElementById('modalHost').value = savedHost;
    }
    if (savedModel) {
        document.getElementById('ollamaModelInput').value = savedModel;
        document.getElementById('modalModel').value = savedModel;
    }
}

function renderSkillsNav() {
    const nav = document.getElementById('skillsNav');
    nav.innerHTML = '';

    const filtered = SKILLS_DATA.filter(s => {
        const matchCat = currentCategoryFilter === 'all' || s.category.toLowerCase().includes(currentCategoryFilter.toLowerCase());
        const matchQuery = !currentSearchQuery || 
            s.name.toLowerCase().includes(currentSearchQuery) || 
            s.id.toLowerCase().includes(currentSearchQuery) || 
            s.description.toLowerCase().includes(currentSearchQuery) ||
            s.tags.some(t => t.toLowerCase().includes(currentSearchQuery));
        return matchCat && matchQuery;
    });

    let lastCat = '';
    filtered.forEach(skill => {
        if (skill.category !== lastCat) {
            lastCat = skill.category;
            const groupTitle = document.createElement('div');
            groupTitle.className = 'category-group-title';
            groupTitle.innerText = lastCat;
            nav.appendChild(groupTitle);
        }

        const item = document.createElement('div');
        item.className = 'skill-item ' + (skill.id === activeSkillId ? 'active' : '');
        item.onclick = () => selectSkill(skill.id);
        item.innerHTML = `
            <span>${skill.name}</span>
            <span class="skill-item-id">${skill.id}</span>
        `;
        nav.appendChild(item);
    });

    document.getElementById('totalSkillsBadge').innerText = `${filtered.length} / ${SKILLS_DATA.length} Beceri`;
}

function setCategoryFilter(cat) {
    currentCategoryFilter = cat;
    document.querySelectorAll('.cat-chip').forEach(c => {
        c.classList.toggle('active', c.innerText.toLowerCase().includes(cat.toLowerCase()) || (cat === 'all' && c.innerText === 'Hepsi'));
    });
    renderSkillsNav();
}

function filterSkills() {
    currentSearchQuery = document.getElementById('searchInput').value.toLowerCase().trim();
    renderSkillsNav();
}

function selectSkill(id) {
    activeSkillId = id;
    const skill = SKILLS_DATA.find(s => s.id === id);
    if (!skill) return;

    // Header & metadata
    document.getElementById('activeSkillTitle').innerText = skill.name;
    document.getElementById('skillCategoryBadge').innerText = skill.category;
    document.getElementById('skillModelBadge').innerText = skill.recommended_model;
    document.getElementById('skillIdBadge').innerText = skill.id;
    document.getElementById('skillDescText').innerText = skill.description;

    const tagsContainer = document.getElementById('skillTagsContainer');
    tagsContainer.innerHTML = '';
    skill.tags.forEach(t => {
        const tagSpan = document.createElement('span');
        tagSpan.className = 'tag-pill';
        tagSpan.innerText = '#' + t;
        tagsContainer.appendChild(tagSpan);
    });

    // System prompt box
    document.getElementById('systemPromptBox').innerText = skill.system_prompt;

    // Dynamic parameter form generator
    generateParameterForm(skill);

    // Update active class in list
    document.querySelectorAll('.skill-item').forEach(el => {
        el.classList.toggle('active', el.querySelector('.skill-item-id')?.innerText === id);
    });

    updateCompiledPrompt();
}

function generateParameterForm(skill) {
    const container = document.getElementById('parametersForm');
    container.innerHTML = '';

    skill.variables.forEach(varName => {
        const group = document.createElement('div');
        group.className = 'form-group';
        
        const label = document.createElement('label');
        label.innerText = '{' + varName + '}';
        
        const exampleVal = skill.example_inputs?.[varName] || '';
        const isMultiLine = exampleVal.includes('\\n') || exampleVal.length > 50;

        let input;
        if (isMultiLine) {
            input = document.createElement('textarea');
            input.rows = 3;
        } else {
            input = document.createElement('input');
            input.type = 'text';
        }
        input.className = 'form-control param-input';
        input.id = `input_${varName}`;
        input.dataset.varName = varName;
        input.value = exampleVal;
        input.oninput = updateCompiledPrompt;

        group.appendChild(label);
        group.appendChild(input);
        container.appendChild(group);
    });
}

function loadSampleInputs() {
    const skill = SKILLS_DATA.find(s => s.id === activeSkillId);
    if (!skill) return;
    skill.variables.forEach(varName => {
        const el = document.getElementById(`input_${varName}`);
        if (el) {
            el.value = skill.example_inputs?.[varName] || '';
        }
    });
    updateCompiledPrompt();
    showToast('✨ Örnek parametre değerleri yüklendi!');
}

function clearInputs() {
    document.querySelectorAll('.param-input').forEach(el => el.value = '');
    updateCompiledPrompt();
    showToast('🧹 Girdiler temizlendi.');
}

function updateCompiledPrompt() {
    const skill = SKILLS_DATA.find(s => s.id === activeSkillId);
    if (!skill) return;

    let template = skill.user_prompt_template;
    skill.variables.forEach(varName => {
        const el = document.getElementById(`input_${varName}`);
        const val = el ? el.value : '{' + varName + '}';
        template = template.replaceAll('{' + varName + '}', val || `[${varName} girilmedi]`);
    });

    document.getElementById('compiledPromptBox').innerText = template;
}

function switchPromptTab(tab) {
    currentPromptTab = tab;
    document.getElementById('tabUserPrompt').classList.toggle('active', tab === 'user');
    document.getElementById('tabSystemPrompt').classList.toggle('active', tab === 'system');
    document.getElementById('tabExecution').classList.toggle('active', tab === 'exec');

    document.getElementById('userPromptView').style.display = tab === 'user' ? 'block' : 'none';
    document.getElementById('systemPromptView').style.display = tab === 'system' ? 'block' : 'none';
    document.getElementById('executionView').style.display = tab === 'exec' ? 'flex' : 'none';
}

function copyCompiledPrompt() {
    const text = document.getElementById('compiledPromptBox').innerText;
    navigator.clipboard.writeText(text).then(() => {
        showToast('📋 Derlenmiş kullanıcı promptu panoya kopyalandı!');
    });
}

function executeWithLocalOllama() {
    switchPromptTab('exec');
    runAiInPlayground();
}

async function runAiInPlayground() {
    const skill = SKILLS_DATA.find(s => s.id === activeSkillId);
    if (!skill) return;

    const host = document.getElementById('ollamaHostInput').value.trim() || 'http://127.0.0.1:11434';
    const model = document.getElementById('ollamaModelInput').value.trim() || 'llama3.2';
    const userPrompt = document.getElementById('compiledPromptBox').innerText;
    const outputBox = document.getElementById('modelOutputBox');

    outputBox.innerText = `⏳ Yerel Ollama sunucusuna (${host}) bağlanılıyor, yanıt bekleniyor...`;

    try {
        const res = await fetch(`${host.replace(/\\/+$/, '')}/api/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                model: model,
                messages: [
                    { role: 'system', content: skill.system_prompt },
                    { role: 'user', content: userPrompt }
                ],
                stream: false
            })
        });

        if (!res.ok) throw new Error(`HTTP ${res.status} - Ollama hatası`);
        const data = await res.json();
        outputBox.innerText = data.message?.content || 'Ollama yanıtı alınamadı.';
        showToast('✅ Model yanıtı başarıyla alındı!');
    } catch (err) {
        // Simülasyon Fallback
        outputBox.innerText = `[DEMO / SİMÜLASYON ÇIKTISI - Ollama Çevrimdışı]\\n` +
            `Hata: ${err.message}\\n\\n` +
            `İpucu: Yerel Ollama çalıştırmak için: OLLAMA_ORIGINS="*" ollama serve\\n` +
            `Model indirmek için: ollama run ${model}\\n\\n` +
            `══════════════════════════════════════════════════════════════════════\\n` +
            `SİMÜLE EDİLEN DOĞRULAMA ÇIKTISI (${skill.name}):\\n` +
            `• Girdi parametreleri Türk mevzuatı (${skill.category}) standartlarına uygun.\\n` +
            `• 0 kritik uyumsuzluk tespit edildi.`;
    }
}

function exportCurrentSkillJson() {
    const skill = SKILLS_DATA.find(s => s.id === activeSkillId);
    if (!skill) return;
    const blob = new Blob([JSON.stringify(skill, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${skill.id}.json`;
    a.click();
    showToast(`💾 ${skill.id}.json indirildi!`);
}

function openOllamaSettings() {
    document.getElementById('settingsModal').style.display = 'flex';
}

function closeOllamaSettings() {
    document.getElementById('settingsModal').style.display = 'none';
}

function saveOllamaSettings() {
    const host = document.getElementById('modalHost').value.trim();
    const model = document.getElementById('modalModel').value.trim();
    localStorage.setItem('ollama_host', host);
    localStorage.setItem('ollama_model', model);
    document.getElementById('ollamaHostInput').value = host;
    document.getElementById('ollamaModelInput').value = model;
    closeOllamaSettings();
    showToast('⚙️ Ayarlar kaydedildi!');
}

function showToast(msg) {
    const t = document.getElementById('toast');
    t.innerText = msg;
    t.style.display = 'block';
    setTimeout(() => { t.style.display = 'none'; }, 2800);
}

window.onload = initPlayground;
</script>

</body>
</html>"""

final_html = html_template.replace("/*{{SKILLS_DATA_JSON}}*/", skills_json_str)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(final_html)

with open(WEB_INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"✅ Başarıyla üretildi: {INDEX_PATH} ({len(skills)} beceri)")
print(f"✅ Başarıyla üretildi: {WEB_INDEX_PATH} ({len(skills)} beceri)")
