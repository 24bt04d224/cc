# -*- coding: utf-8 -*-

CSS_CODE = """
:root {
  --bg-primary: #0b0f19;
  --bg-secondary: #151d2f;
  --bg-card: #1e293b;
  --bg-card-hover: #27354a;
  --border-color: #334155;
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  --accent: #38bdf8;
  --accent-hover: #0284c7;
  --accent-light: rgba(56, 189, 248, 0.12);
  --success: #10b981;
  --success-bg: rgba(16, 185, 129, 0.15);
  --warning: #f59e0b;
  --warning-bg: rgba(245, 158, 11, 0.15);
  --danger: #ef4444;
  --danger-bg: rgba(239, 68, 68, 0.15);
  --purple: #a855f7;
  --purple-bg: rgba(168, 85, 247, 0.15);
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4), 0 2px 4px -2px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.5), 0 4px 6px -4px rgba(0, 0, 0, 0.5);
}

[data-theme="light"] {
  --bg-primary: #f8fafc;
  --bg-secondary: #ffffff;
  --bg-card: #ffffff;
  --bg-card-hover: #f1f5f9;
  --border-color: #e2e8f0;
  --text-primary: #0f172a;
  --text-secondary: #475569;
  --text-muted: #94a3b8;
  --accent: #0284c7;
  --accent-hover: #0369a1;
  --accent-light: rgba(2, 132, 199, 0.08);
  --success: #059669;
  --success-bg: rgba(5, 150, 105, 0.1);
  --warning: #d97706;
  --warning-bg: rgba(217, 119, 6, 0.1);
  --danger: #dc2626;
  --danger-bg: rgba(220, 38, 38, 0.1);
  --purple: #7c3aed;
  --purple-bg: rgba(124, 58, 237, 0.1);
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: var(--font-sans);
  background-color: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.6;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  transition: background-color 0.25s, color 0.25s;
}

/* Custom Scrollbar */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}
::-webkit-scrollbar-track {
  background: var(--bg-primary);
}
::-webkit-scrollbar-thumb {
  background: var(--border-color);
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: var(--accent);
}

/* Header */
header {
  position: sticky;
  top: 0;
  z-index: 100;
  background-color: var(--bg-secondary);
  border-bottom: 1px solid var(--border-color);
  backdrop-filter: blur(10px);
  padding: 0.75rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: var(--shadow-sm);
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  text-decoration: none;
}
.brand-logo {
  width: 42px;
  height: 42px;
  background: linear-gradient(135deg, #38bdf8, #6366f1);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 800;
  font-size: 1.3rem;
  box-shadow: 0 4px 12px rgba(56, 189, 248, 0.35);
}
.brand-text h1 {
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--text-primary);
}
.brand-text p {
  font-size: 0.75rem;
  color: var(--text-muted);
}

.header-controls {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.search-box {
  position: relative;
  width: 280px;
}
.search-box input {
  width: 100%;
  padding: 0.5rem 0.75rem 0.5rem 2.25rem;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  background-color: var(--bg-primary);
  color: var(--text-primary);
  font-size: 0.85rem;
  outline: none;
  transition: all 0.2s;
}
.search-box input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px var(--accent-light);
  width: 320px;
}
.search-icon {
  position: absolute;
  left: 0.75rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
  pointer-events: none;
  font-size: 0.9rem;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.5rem 0.85rem;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  background-color: var(--bg-card);
  color: var(--text-primary);
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.btn:hover {
  background-color: var(--bg-card-hover);
  border-color: var(--accent);
}
.btn-primary {
  background: linear-gradient(135deg, var(--accent), var(--accent-hover));
  color: white;
  border: none;
}
.btn-primary:hover {
  opacity: 0.95;
  transform: translateY(-1px);
}
.btn-icon {
  padding: 0.5rem;
  border-radius: 8px;
}
.btn-sm {
  padding: 0.35rem 0.65rem;
  font-size: 0.78rem;
}

/* Layout */
.app-container {
  display: flex;
  flex: 1;
}

/* Sidebar */
aside {
  width: 290px;
  background-color: var(--bg-secondary);
  border-right: 1px solid var(--border-color);
  height: calc(100vh - 65px);
  position: sticky;
  top: 65px;
  overflow-y: auto;
  padding: 1.25rem 0.75rem;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  flex-shrink: 0;
}

.sidebar-title {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  font-weight: 700;
  padding: 0.6rem 0.75rem 0.25rem;
  margin-top: 0.6rem;
}
.sidebar-title:first-child {
  margin-top: 0;
}

.nav-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.6rem 0.75rem;
  border-radius: 8px;
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 0.86rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.15s ease;
  user-select: none;
}
.nav-item-left {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}
.nav-item:hover {
  background-color: var(--accent-light);
  color: var(--accent);
}
.nav-item.active {
  background-color: var(--accent);
  color: #ffffff;
  font-weight: 600;
}
.nav-item.active .badge {
  background-color: rgba(255, 255, 255, 0.25);
  color: #ffffff;
}

.badge {
  font-size: 0.7rem;
  font-weight: 700;
  padding: 0.15rem 0.45rem;
  border-radius: 12px;
  background-color: var(--bg-primary);
  color: var(--text-muted);
}
.badge-priority {
  background-color: var(--danger-bg);
  color: var(--danger);
  border: 1px solid rgba(239, 68, 68, 0.25);
}
.badge-accent {
  background-color: var(--accent-light);
  color: var(--accent);
  border: 1px solid rgba(56, 189, 248, 0.3);
}

/* Main Content Area */
main {
  flex: 1;
  padding: 2.25rem;
  max-width: 1240px;
  margin: 0 auto;
  width: 100%;
}

.tab-pane {
  display: none;
  animation: fadeIn 0.2s ease-in-out;
}
.tab-pane.active {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Banner */
.hero-banner {
  background: linear-gradient(135deg, rgba(56, 189, 248, 0.15), rgba(99, 102, 241, 0.15));
  border: 1px solid rgba(56, 189, 248, 0.35);
  border-radius: 16px;
  padding: 1.75rem;
  margin-bottom: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.hero-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}
.hero-title {
  font-size: 1.55rem;
  font-weight: 800;
  color: var(--text-primary);
}
.hero-badge-group {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.hero-desc {
  color: var(--text-secondary);
  font-size: 0.95rem;
}

/* Unit Dropdown Controls Bar */
.unit-controls-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 0.75rem 1.25rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
  gap: 0.75rem;
}
.unit-controls-left {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}
.unit-controls-right {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.topic-select {
  padding: 0.45rem 0.85rem;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  background-color: var(--bg-primary);
  color: var(--text-primary);
  font-size: 0.85rem;
  outline: none;
  cursor: pointer;
}
.topic-select:focus {
  border-color: var(--accent);
}

/* 2-Tier Hierarchical Dropdown Structure */

/* LEVEL 1: Main Head / Main Topic Dropdown */
.main-topic-card {
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 14px;
  margin-bottom: 1.25rem;
  box-shadow: var(--shadow-sm);
  transition: all 0.2s ease;
  overflow: hidden;
}
.main-topic-card:hover {
  border-color: rgba(56, 189, 248, 0.4);
}
.main-topic-header {
  padding: 1.15rem 1.4rem;
  background: linear-gradient(135deg, var(--bg-card), var(--bg-secondary));
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  user-select: none;
  transition: background-color 0.2s;
  border-bottom: 1px solid transparent;
}
.main-topic-header:hover {
  background-color: var(--bg-card-hover);
}
.main-topic-header.open {
  border-bottom-color: var(--border-color);
}
.main-topic-title-area {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}
.main-topic-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text-primary);
}
.main-topic-toggle-btn {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--accent);
  background-color: var(--accent-light);
  padding: 0.3rem 0.65rem;
  border-radius: 6px;
  transition: transform 0.2s;
}
.main-topic-arrow {
  display: inline-block;
  transition: transform 0.3s ease;
}
.main-topic-header.open .main-topic-arrow {
  transform: rotate(180deg);
}

.main-topic-body {
  display: none;
  padding: 1.25rem;
  background-color: var(--bg-primary);
  animation: fadeIn 0.2s ease-in-out;
}
.main-topic-body.open {
  display: block;
}

/* LEVEL 2: Sub-Topic Dropdown */
.sub-topic-card {
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  margin-bottom: 0.85rem;
  overflow: hidden;
  transition: border-color 0.2s;
}
.sub-topic-card:last-child {
  margin-bottom: 0;
}
.sub-topic-card:hover {
  border-color: rgba(56, 189, 248, 0.4);
}
.sub-topic-header {
  padding: 0.9rem 1.15rem;
  background-color: var(--bg-secondary);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  user-select: none;
  font-weight: 600;
  font-size: 0.96rem;
  color: var(--text-primary);
  transition: background-color 0.15s;
  border-bottom: 1px solid transparent;
}
.sub-topic-header:hover {
  background-color: var(--bg-card-hover);
  color: var(--accent);
}
.sub-topic-header.open {
  border-bottom-color: var(--border-color);
  background-color: var(--bg-card);
}
.sub-topic-title-area {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  flex: 1;
}
.sub-topic-icon {
  color: var(--accent);
  font-size: 0.85rem;
}
.sub-topic-badge {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 0.15rem 0.5rem;
  border-radius: 6px;
  background-color: var(--accent-light);
  color: var(--accent);
  margin-left: auto;
  margin-right: 0.75rem;
}
.sub-topic-arrow {
  font-size: 0.8rem;
  color: var(--text-muted);
  transition: transform 0.25s ease;
}
.sub-topic-header.open .sub-topic-arrow {
  transform: rotate(180deg);
  color: var(--accent);
}

/* LEVEL 3: Detailed Description */
.sub-topic-detail {
  display: none;
  padding: 1.35rem;
  background-color: var(--bg-card);
  color: var(--text-secondary);
  font-size: 0.92rem;
  line-height: 1.65;
  animation: fadeIn 0.2s ease-in-out;
}
.sub-topic-detail.open {
  display: block;
}

/* Quick Stats Bar */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}
.stat-card {
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 1.25rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  box-shadow: var(--shadow-sm);
  transition: transform 0.2s, border-color 0.2s;
}
.stat-card:hover {
  transform: translateY(-2px);
  border-color: var(--accent);
}
.stat-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  background-color: var(--accent-light);
  color: var(--accent);
  flex-shrink: 0;
}
.stat-info h3 {
  font-size: 1.45rem;
  font-weight: 800;
  color: var(--text-primary);
}
.stat-info p {
  font-size: 0.8rem;
  color: var(--text-muted);
}

/* Callout Boxes */
.def-box {
  background: linear-gradient(135deg, rgba(56, 189, 248, 0.08), rgba(56, 189, 248, 0.03));
  border-left: 4px solid var(--accent);
  padding: 1.1rem 1.25rem;
  border-radius: 0 10px 10px 0;
  margin: 1.1rem 0;
  font-size: 0.95rem;
  color: var(--text-primary);
}
.def-title {
  font-weight: 700;
  color: var(--accent);
  font-size: 0.82rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.35rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.tip-box {
  background: var(--warning-bg);
  border-left: 4px solid var(--warning);
  padding: 1rem 1.25rem;
  border-radius: 0 10px 10px 0;
  margin: 1.1rem 0;
  font-size: 0.9rem;
}
.tip-title {
  font-weight: 700;
  color: var(--warning);
  margin-bottom: 0.3rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.alert-box {
  background: var(--danger-bg);
  border-left: 4px solid var(--danger);
  padding: 1rem 1.25rem;
  border-radius: 0 10px 10px 0;
  margin: 1.1rem 0;
  font-size: 0.9rem;
}
.alert-title {
  font-weight: 700;
  color: var(--danger);
  margin-bottom: 0.3rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

/* Tables */
.table-wrapper {
  overflow-x: auto;
  margin: 1.25rem 0;
  border-radius: 10px;
  border: 1px solid var(--border-color);
}
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
  text-align: left;
}
th {
  background-color: var(--bg-secondary);
  color: var(--text-primary);
  font-weight: 700;
  padding: 0.85rem 1rem;
  border-bottom: 2px solid var(--border-color);
  white-space: nowrap;
}
td {
  padding: 0.75rem 1rem;
  border-bottom: 1px solid var(--border-color);
  color: var(--text-secondary);
}
tr:last-child td {
  border-bottom: none;
}
tr:hover td {
  background-color: var(--accent-light);
  color: var(--text-primary);
}

/* Code and JSON Blocks */
pre {
  background-color: #090d16;
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 1rem;
  overflow-x: auto;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  color: #38bdf8;
  margin: 1rem 0;
}
code {
  font-family: var(--font-mono);
  font-size: 0.85em;
  background-color: rgba(56, 189, 248, 0.1);
  color: var(--accent);
  padding: 0.15rem 0.35rem;
  border-radius: 4px;
}

/* Diagrams */
.diagram-container {
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 1.5rem;
  margin: 1.5rem 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}
.diagram-container svg {
  max-width: 100%;
  height: auto;
}
.diagram-caption {
  font-size: 0.82rem;
  color: var(--text-muted);
  font-style: italic;
  text-align: center;
}

/* Lists */
ul, ol {
  padding-left: 1.5rem;
  margin: 0.75rem 0;
  color: var(--text-secondary);
}
li {
  margin-bottom: 0.4rem;
}
li strong {
  color: var(--text-primary);
}

/* Grid Layouts */
.grid-2 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.25rem;
  margin: 1.25rem 0;
}
.grid-3 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.1rem;
  margin: 1.25rem 0;
}
.subcard {
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 1.25rem;
}
.subcard h4 {
  font-size: 1rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

/* Flashcards Section */
.flashcard-wrapper {
  max-width: 680px;
  margin: 2rem auto;
  perspective: 1000px;
}
.flashcard {
  position: relative;
  width: 100%;
  min-height: 290px;
  cursor: pointer;
  transform-style: preserve-3d;
  transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  border-radius: 16px;
}
.flashcard.flipped {
  transform: rotateY(180deg);
}
.flashcard-front, .flashcard-back {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 16px;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border: 2px solid var(--border-color);
  box-shadow: var(--shadow-lg);
}
.flashcard-front {
  background: linear-gradient(135deg, var(--bg-card), var(--bg-secondary));
  border-color: var(--accent);
}
.flashcard-back {
  background: linear-gradient(135deg, var(--bg-secondary), var(--bg-card));
  transform: rotateY(180deg);
  border-color: var(--purple);
}
.card-unit-badge {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--accent);
}
.card-content {
  text-align: center;
  margin: auto 0;
}
.card-question {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-primary);
}
.card-answer {
  font-size: 1rem;
  line-height: 1.6;
  color: var(--text-secondary);
}
.card-hint {
  font-size: 0.78rem;
  color: var(--text-muted);
  text-align: center;
}
.flashcard-nav {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-top: 1.5rem;
}

/* Quiz Simulator */
.quiz-container {
  max-width: 820px;
  margin: 0 auto;
}
.quiz-progress-bar-container {
  height: 8px;
  background-color: var(--border-color);
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 1.5rem;
}
.quiz-progress-bar {
  height: 100%;
  background: linear-gradient(90deg, var(--accent), var(--success));
  width: 0%;
  transition: width 0.3s;
}
.quiz-filter {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}
.quiz-card {
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 14px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: var(--shadow-sm);
}
.quiz-card-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
  font-size: 0.85rem;
  color: var(--text-muted);
}
.quiz-question-text {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 1.25rem;
}
.quiz-options {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}
.quiz-option {
  padding: 0.75rem 1rem;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  background-color: var(--bg-secondary);
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.92rem;
}
.quiz-option:hover {
  border-color: var(--accent);
  background-color: var(--accent-light);
  color: var(--text-primary);
}
.quiz-option.correct {
  background-color: var(--success-bg) !important;
  border-color: var(--success) !important;
  color: var(--text-primary) !important;
  font-weight: 600;
}
.quiz-option.incorrect {
  background-color: var(--danger-bg) !important;
  border-color: var(--danger) !important;
  color: var(--text-primary) !important;
}
.quiz-explanation {
  display: none;
  margin-top: 1rem;
  padding: 1rem;
  border-radius: 8px;
  background-color: var(--bg-secondary);
  border-left: 4px solid var(--accent);
  font-size: 0.88rem;
  color: var(--text-secondary);
}

/* Accordion Question Bank */
.accordion-item {
  border: 1px solid var(--border-color);
  border-radius: 10px;
  margin-bottom: 0.75rem;
  overflow: hidden;
  background-color: var(--bg-card);
}
.accordion-header {
  padding: 1rem 1.25rem;
  background-color: var(--bg-card);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  user-select: none;
  font-weight: 600;
  color: var(--text-primary);
  font-size: 0.95rem;
  transition: background-color 0.2s;
}
.accordion-header:hover {
  background-color: var(--bg-card-hover);
}
.accordion-content {
  display: none;
  padding: 1.25rem;
  border-top: 1px solid var(--border-color);
  background-color: var(--bg-secondary);
  font-size: 0.9rem;
  color: var(--text-secondary);
}
.accordion-content.open {
  display: block;
}
.accordion-icon {
  transition: transform 0.3s;
}
.accordion-header.open .accordion-icon {
  transform: rotate(180deg);
}

/* Responsive */
@media (max-width: 900px) {
  .app-container {
    flex-direction: column;
  }
  aside {
    width: 100%;
    height: auto;
    position: static;
    border-right: none;
    border-bottom: 1px solid var(--border-color);
    padding: 0.75rem;
  }
  .search-box {
    width: 180px;
  }
  .search-box input:focus {
    width: 220px;
  }
  main {
    padding: 1rem;
  }
  .unit-controls-bar {
    flex-direction: column;
    align-items: stretch;
  }
  .unit-controls-left, .unit-controls-right {
    width: 100%;
    justify-content: space-between;
  }
}

/* Print Optimization */
@media print {
  header, aside, .btn, .flashcard-nav, .quiz-filter, .search-box, .quiz-progress-bar-container, .unit-controls-bar {
    display: none !important;
  }
  body, main {
    background: #ffffff !important;
    color: #000000 !important;
    padding: 0 !important;
  }
  .tab-pane {
    display: block !important;
    page-break-after: always;
  }
  .main-topic-card, .sub-topic-card, .table-wrapper, .accordion-item {
    border: 1px solid #cccccc !important;
    box-shadow: none !important;
    break-inside: avoid;
  }
  .main-topic-body, .sub-topic-detail, .accordion-content {
    display: block !important;
  }
}
"""
