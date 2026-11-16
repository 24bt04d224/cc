# -*- coding: utf-8 -*-
import os

from parts_css import CSS_CODE
from parts_unit1 import TAB_UNIT1_HTML
from parts_unit2 import TAB_UNIT2_HTML
from parts_unit3 import TAB_UNIT3_HTML
from parts_unit4 import TAB_UNIT4_HTML
from parts_unit5 import TAB_UNIT5_HTML
from parts_comparisons import TAB_COMPARISONS_HTML
from parts_quiz_flashcards import TAB_FLASHCARDS_HTML, TAB_QUIZ_HTML
from parts_qbank import TAB_QBANK_HTML
from parts_power_modes import TAB_RANDOM_TOPICS_HTML, TAB_IMP_TOPICS_HTML, TAB_RANDOM_QUESTIONS_HTML
from parts_u45_guaranteed import generate_u45_overview_card
from parts_js import JS_CODE

_RAW_OVERVIEW_HTML = """
<div id="overview" class="tab-pane active">
  <div class="hero-banner">
    <div class="hero-header">
      <div class="hero-title">BTCS701F: Cloud Computing — Master Exam Portal</div>
      <div class="hero-badge-group">
        <span class="badge badge-accent">B.Tech CSE · Sem VII</span>
        <span class="badge badge-priority">GSFC University</span>
        <span class="badge">Academic Year 2025–26</span>
      </div>
    </div>
    <p class="hero-desc">
      Welcome to your comprehensive, all-in-one Cloud Computing examination preparation portal.
      This platform consolidates 100% of your university syllabus (BTCS701F), complete lecture slide decks (Units 1–5),
      and dedicated AWS IAM slide notes by Prof. Amin Shaikh. Strictly focused on Cloud Computing theory, architecture, and university exams.
    </p>
  </div>

  <!-- Quick Stats Grid -->
  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-icon">📚</div>
      <div class="stat-info">
        <h3>5 Units</h3>
        <p>100% Syllabus Coverage</p>
      </div>
    </div>
    <div class="stat-card" style="border-color: rgba(239, 68, 68, 0.4);">
      <div class="stat-icon" style="color: var(--danger); background-color: var(--danger-bg);">⚡</div>
      <div class="stat-info">
        <h3 style="color: var(--danger);">50% Marks</h3>
        <p>Units 4 & 5 (Half the Exam!)</p>
      </div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">🎯</div>
      <div class="stat-info">
        <h3>52 MCQs</h3>
        <p>Interactive Exam Simulator</p>
      </div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">🗂️</div>
      <div class="stat-info">
        <h3>36 Cards</h3>
        <p>3D Flip Revision Cards</p>
      </div>
    </div>
  </div>

  <!-- High-Yield Exam Power Modes Card -->
  <div class="topic-card" style="border-color: rgba(56, 189, 248, 0.4); background: linear-gradient(135deg, rgba(56, 189, 248, 0.05), rgba(168, 85, 247, 0.05));">
    <div class="topic-header">
      <div class="topic-title">⚡ High-Yield Exam Power Modes (Rapid Revision Tools)</div>
      <span class="badge badge-accent">Interactive Revision</span>
    </div>
    <p style="color: var(--text-secondary); margin-bottom: 1.15rem; font-size: 0.92rem;">
      Accelerate your revision with active recall and targeted exam-readiness tools. Choose your study mode:
    </p>
    <div class="grid-3" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 0.85rem;">
      <div class="subcard" style="cursor: pointer; transition: transform 0.2s, border-color 0.2s; border-left: 4px solid var(--accent);" onclick="switchTab('random-topics')">
        <div style="font-size: 1.5rem; margin-bottom: 0.4rem;">🎲</div>
        <h4 style="color: var(--accent); margin-bottom: 0.4rem;">1. Random Topic Shuffler</h4>
        <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 0.75rem;">
          Shuffle through 140+ core curriculum topics across all 5 units for active recall drills. Includes real-world analogies & diagram links.
        </p>
        <span class="badge badge-accent">Launch Shuffler &rarr;</span>
      </div>

      <div class="subcard" style="cursor: pointer; transition: transform 0.2s, border-color 0.2s; border-left: 4px solid var(--danger);" onclick="switchTab('imp-topics')">
        <div style="font-size: 1.5rem; margin-bottom: 0.4rem;">⭐</div>
        <h4 style="color: var(--danger); margin-bottom: 0.4rem;">2. Master IMP Topics (Top 30)</h4>
        <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 0.75rem;">
          100% exam-guaranteed questions. Units 4 & 5 (50% marks) prioritized with exact question formats, marks, and 4-point blueprints.
        </p>
        <span class="badge badge-priority">View IMP List &rarr;</span>
      </div>

      <div class="subcard" style="cursor: pointer; transition: transform 0.2s, border-color 0.2s; border-left: 4px solid var(--success);" onclick="switchTab('random-questions')">
        <div style="font-size: 1.5rem; margin-bottom: 0.4rem;">❓</div>
        <h4 style="color: var(--success); margin-bottom: 0.4rem;">3. Question Roulette (All Units)</h4>
        <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 0.75rem;">
          Cross-chapter exam simulator with 2M, 5M, 7M, and 10M questions. Hidden answers with instant model answer reveals & grading tips.
        </p>
        <span class="badge" style="background: var(--success-bg); color: var(--success);">Start Roulette &rarr;</span>
      </div>
    </div>
  </div>

  <!-- Exam Blueprint Card -->
  <div class="topic-card">
    <div class="topic-header">
      <div class="topic-title">Official Syllabus Blueprint & Marks Distribution</div>
      <span class="topic-tag">Strategic Roadmap</span>
    </div>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Unit</th>
            <th>Unit Title</th>
            <th>Weightage</th>
            <th>Contact Hours</th>
            <th>Study Priority</th>
            <th>Key High-Yield Focus Topics</th>
          </tr>
        </thead>
        <tbody>
          <tr style="background-color: rgba(239, 68, 68, 0.08);">
            <td><strong>Unit 4</strong></td>
            <td><strong>Virtualization Technologies & Cloud Tools</strong></td>
            <td><strong style="color: var(--danger);">25%</strong></td>
            <td>10 Hours</td>
            <td><span class="badge badge-priority">FIRST PRIORITY</span></td>
            <td>Type 1 vs 2 Hypervisors, Dispatcher/Allocator/Interpreter, Docker vs VMs, OpenStack 9 components, CloudStack hierarchy, Block/Object/File storage, SDN, CDN.</td>
          </tr>
          <tr style="background-color: rgba(239, 68, 68, 0.08);">
            <td><strong>Unit 5</strong></td>
            <td><strong>Security, Privacy & Cloud Management</strong></td>
            <td><strong style="color: var(--danger);">25%</strong></td>
            <td>10 Hours</td>
            <td><span class="badge badge-priority">SECOND PRIORITY</span></td>
            <td>CIA Triad, AWS IAM (Users, Groups, Roles, Policies, Explicit Deny Rule), VM Security, Scalability vs Elasticity, 7 Real-World Security Incidents.</td>
          </tr>
          <tr>
            <td><strong>Unit 3</strong></td>
            <td><strong>Cloud Deployment Models & Architecture</strong></td>
            <td><strong>20%</strong></td>
            <td>9 Hours</td>
            <td><span class="badge badge-accent">HIGH PRIORITY</span></td>
            <td>Public/Private/Hybrid/Community, Multi-Tenant, Multi-Server, Distributed Architectures, AWS vs Azure vs GCP.</td>
          </tr>
          <tr>
            <td><strong>Unit 1</strong></td>
            <td><strong>Introduction to Cloud Computing</strong></td>
            <td><strong>15%</strong></td>
            <td>9 Hours</td>
            <td><span class="badge">FOUNDATIONAL</span></td>
            <td>5 NIST Characteristics, Benefits vs Challenges, Pizza-as-a-Service, Infrastructure Management, Criteria for Provider.</td>
          </tr>
          <tr>
            <td><strong>Unit 2</strong></td>
            <td><strong>Cloud Service Models (SPI)</strong></td>
            <td><strong>15%</strong></td>
            <td>7 Hours</td>
            <td><span class="badge">FOUNDATIONAL</span></td>
            <td>IaaS (EC2, GCE, Azure VMs), PaaS (App Engine, Beanstalk), SaaS (Google Docs, M365), Shared Responsibility Matrix.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="tip-box">
      <div class="tip-title">Top Scoring Strategy for University Exam</div>
      <p>
        Notice that <strong>Unit 4 + Unit 5 alone account for 50% of your total examination marks</strong>!
        Always prepare Units 4 & 5 first, master the side-by-side comparison tables (for 7-mark questions), and practice the 52 interactive MCQs.
      </p>
    </div>
  </div>

  <!-- Course Learning Outcomes (Blooms Taxonomy) -->
  <div class="topic-card">
    <div class="topic-header">
      <div class="topic-title">Course Learning Outcomes (Blooms Taxonomy)</div>
      <span class="topic-tag">University Curriculum</span>
    </div>
    <div class="grid-2">
      <div class="subcard">
        <h4>CO1 & CO2 (Remember & Understand)</h4>
        <p>Understand cloud computing models, multi-tier architectures, and the principles/practices of different service models (IaaS, PaaS, SaaS).</p>
      </div>
      <div class="subcard">
        <h4>CO3 & CO4 (Apply & Analyze)</h4>
        <p>Gain practical knowledge of cloud deployment models, master virtualization concepts, hypervisors, containers, and cloud management platforms (OpenStack, CloudStack).</p>
      </div>
      <div class="subcard" style="grid-column: 1 / -1;">
        <h4>CO5 (Evaluate & Secure)</h4>
        <p>Master cloud security mechanisms, privacy governance, IAM evaluation, and dynamic cloud resource management (scalability and elasticity) in multi-tenant environments.</p>
      </div>
    </div>
  </div>
</div>
"""

OVERVIEW_HTML = _RAW_OVERVIEW_HTML.replace('<!-- High-Yield Exam Power Modes Card -->', generate_u45_overview_card() + '\n  <!-- High-Yield Exam Power Modes Card -->')


FULL_HTML = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>BTCS701F: Cloud Computing — Master Exam Portal (GSFC University)</title>
  <style>
{CSS_CODE}
  </style>
</head>
<body>

  <!-- Backdrop for Mobile Slide-Out Drawer -->
  <div class="sidebar-backdrop" id="sidebarBackdrop" onclick="closeMobileNav()"></div>

  <!-- Top Header Navigation -->
  <header>
    <div class="header-left">
      <button class="mobile-menu-btn" onclick="toggleMobileNav()" title="Open Navigation Menu" aria-label="Toggle navigation menu">☰</button>
      <a href="#" class="brand" onclick="switchTab('overview'); return false;">
        <div class="brand-logo">CC</div>
        <div class="brand-text">
          <h1><span>Cloud Computing</span> <span class="hide-mobile">(BTCS701F)</span></h1>
          <p>GSFC University · Master Exam Portal · 100% CC Aligned</p>
        </div>
      </a>
    </div>

    <div class="header-controls">
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="globalSearchInput" placeholder="Search topics, IAM..." oninput="handleLiveSearch(this.value)">
      </div>

      <button class="btn btn-icon" id="themeToggleBtn" onclick="toggleTheme()" title="Toggle Dark/Light Mode">🌙</button>
      <button class="btn btn-primary btn-print-hide" onclick="window.print()" title="Print / Save Notes as PDF">🖨️ Print Notes</button>
    </div>
  </header>

  <div class="app-container">
    <!-- Sidebar Navigation -->
    <aside>
      <div class="sidebar-mobile-header">
        <div class="sidebar-mobile-title">Course Navigation</div>
        <button class="sidebar-close-btn" onclick="closeMobileNav()" aria-label="Close menu">&times;</button>
      </div>

      <div class="sidebar-title">Core Navigation</div>
      
      <div class="nav-item active" id="nav-overview" onclick="switchTab('overview')">
        <div class="nav-item-left">
          <span>🏠</span>
          <span>Roadmap & Syllabus</span>
        </div>
        <span class="badge">Blueprint</span>
      </div>

      <div class="sidebar-title">🎯 Exam Power Modes</div>
      
      <div class="nav-item" id="nav-random-topics" onclick="switchTab('random-topics')">
        <div class="nav-item-left">
          <span>🎲</span>
          <span>Random Topics</span>
        </div>
        <span class="badge badge-accent">Recall</span>
      </div>

      <div class="nav-item" id="nav-imp-topics" onclick="switchTab('imp-topics')">
        <div class="nav-item-left">
          <span>⭐</span>
          <span>IMP Topics (Top 30)</span>
        </div>
        <span class="badge badge-priority">100% Exam</span>
      </div>

      <div class="nav-item" id="nav-u45-guaranteed" onclick="switchTab('qbank'); filterQBank('u45', null);">
        <div class="nav-item-left">
          <span>🔥</span>
          <span>Units 4 & 5 (21 Qs)</span>
        </div>
        <span class="badge badge-priority">50% Marks</span>
      </div>

      <div class="nav-item" id="nav-random-questions" onclick="switchTab('random-questions')">
        <div class="nav-item-left">
          <span>❓</span>
          <span>Question Roulette</span>
        </div>
        <span class="badge">Cross-Unit</span>
      </div>

      <div class="sidebar-title">High-Weightage Units (50%)</div>
      
      <div class="nav-item" id="nav-unit4" onclick="switchTab('unit4')">
        <div class="nav-item-left">
          <span>📕</span>
          <span>Unit 4: Virtualization</span>
        </div>
        <span class="badge badge-priority">25%</span>
      </div>

      <div class="nav-item" id="nav-unit5" onclick="switchTab('unit5')">
        <div class="nav-item-left">
          <span>🔒</span>
          <span>Unit 5: Security & IAM</span>
        </div>
        <span class="badge badge-priority">25%</span>
      </div>

      <div class="sidebar-title">Foundational Units (50%)</div>

      <div class="nav-item" id="nav-unit3" onclick="switchTab('unit3')">
        <div class="nav-item-left">
          <span>📙</span>
          <span>Unit 3: Architecture</span>
        </div>
        <span class="badge">20%</span>
      </div>

      <div class="nav-item" id="nav-unit1" onclick="switchTab('unit1')">
        <div class="nav-item-left">
          <span>📘</span>
          <span>Unit 1: Intro to Cloud</span>
        </div>
        <span class="badge">15%</span>
      </div>

      <div class="nav-item" id="nav-unit2" onclick="switchTab('unit2')">
        <div class="nav-item-left">
          <span>📗</span>
          <span>Unit 2: Service Models</span>
        </div>
        <span class="badge">15%</span>
      </div>

      <div class="sidebar-title">Exam Master Tools</div>

      <div class="nav-item" id="nav-comparisons" onclick="switchTab('comparisons')">
        <div class="nav-item-left">
          <span>📊</span>
          <span>Comparison Matrices</span>
        </div>
        <span class="badge badge-accent">7 Marks</span>
      </div>

      <div class="nav-item" id="nav-quiz" onclick="switchTab('quiz')">
        <div class="nav-item-left">
          <span>🎯</span>
          <span>Exam MCQ Simulator</span>
        </div>
        <span class="badge badge-priority">52 MCQs</span>
      </div>

      <div class="nav-item" id="nav-flashcards" onclick="switchTab('flashcards')">
        <div class="nav-item-left">
          <span>🗂️</span>
          <span>Interactive Flashcards</span>
        </div>
        <span class="badge">36 Cards</span>
      </div>

      <div class="nav-item" id="nav-qbank" onclick="switchTab('qbank')">
        <div class="nav-item-left">
          <span>📝</span>
          <span>University Question Bank</span>
        </div>
        <span class="badge">2/5/7/10M</span>
      </div>
    </aside>

    <!-- Main Content Panes -->
    <main>
      {OVERVIEW_HTML}
      {TAB_RANDOM_TOPICS_HTML}
      {TAB_IMP_TOPICS_HTML}
      {TAB_RANDOM_QUESTIONS_HTML}
      {TAB_UNIT1_HTML}
      {TAB_UNIT2_HTML}
      {TAB_UNIT3_HTML}
      {TAB_UNIT4_HTML}
      {TAB_UNIT5_HTML}
      {TAB_COMPARISONS_HTML}
      {TAB_QUIZ_HTML}
      {TAB_FLASHCARDS_HTML}
      {TAB_QBANK_HTML}
    </main>
  </div>

  <!-- Mobile Sticky Bottom Navigation Bar -->
  <nav class="mobile-bottom-nav">
    <button class="bottom-nav-item active" id="bnav-overview" onclick="switchTab('overview')">
      <span class="bnav-icon">🏠</span>
      <span class="bnav-label">Home</span>
    </button>
    <button class="bottom-nav-item" id="bnav-units" onclick="toggleMobileNav()">
      <span class="bnav-icon">📚</span>
      <span class="bnav-label">Units</span>
    </button>
    <button class="bottom-nav-item" id="bnav-comparisons" onclick="switchTab('comparisons')">
      <span class="bnav-icon">📊</span>
      <span class="bnav-label">Compare</span>
    </button>
    <button class="bottom-nav-item" id="bnav-quiz" onclick="switchTab('quiz')">
      <span class="bnav-icon">🎯</span>
      <span class="bnav-label">MCQs</span>
    </button>
    <button class="bottom-nav-item" id="bnav-flashcards" onclick="switchTab('flashcards')">
      <span class="bnav-icon">🗂️</span>
      <span class="bnav-label">Cards</span>
    </button>
  </nav>

  <script>
{JS_CODE}
  </script>
</body>
</html>
"""

output_path = os.path.join(os.path.dirname(__file__), "index.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(FULL_HTML)

print(f"Portal successfully built! File created at: {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")
