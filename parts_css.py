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
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4), 0 2px 4px -2px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.5), 0 4px 6px -4px rgba(0, 0, 0, 0.5);
  --drawer-width: min(85vw, 320px);
  --header-height: 64px;
  --bottom-nav-height: 60px;
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
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.06);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-tap-highlight-color: transparent;
}

html, body {
  width: 100%;
  overflow-x: hidden;
  -webkit-text-size-adjust: 100%;
}

body {
  font-family: var(--font-sans);
  background-color: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.6;
  min-height: 100vh;
  min-height: 100dvh;
  display: flex;
  flex-direction: column;
  transition: background-color 0.25s, color 0.25s;
  -webkit-font-smoothing: antialiased;
}

/* Custom Scrollbar */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
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
  height: var(--header-height);
  background-color: var(--bg-secondary);
  border-bottom: 1px solid var(--border-color);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  padding: 0.6rem 1.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: var(--shadow-sm);
  gap: 0.75rem;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  min-width: 0;
}

.mobile-menu-btn {
  display: none;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  color: var(--text-primary);
  font-size: 1.25rem;
  cursor: pointer;
  flex-shrink: 0;
  transition: background-color 0.2s, border-color 0.2s;
}
.mobile-menu-btn:hover {
  background-color: var(--bg-card-hover);
  border-color: var(--accent);
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  text-decoration: none;
  min-width: 0;
}
.brand-logo {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #38bdf8, #6366f1);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 800;
  font-size: 1.2rem;
  box-shadow: 0 4px 12px rgba(56, 189, 248, 0.35);
  flex-shrink: 0;
}
.brand-text {
  min-width: 0;
}
.brand-text h1 {
  font-size: clamp(0.98rem, 0.9rem + 0.4vw, 1.15rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--text-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.brand-text p {
  font-size: 0.72rem;
  color: var(--text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.header-controls {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-shrink: 0;
}

.search-box {
  position: relative;
  width: 260px;
  transition: width 0.25s ease;
}
.search-box input {
  width: 100%;
  padding: 0.45rem 0.75rem 0.45rem 2.2rem;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  background-color: var(--bg-primary);
  color: var(--text-primary);
  font-size: 0.85rem;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.search-box input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px var(--accent-light);
}
.search-icon {
  position: absolute;
  left: 0.75rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
  pointer-events: none;
  font-size: 0.85rem;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  padding: 0.48rem 0.85rem;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  background-color: var(--bg-card);
  color: var(--text-primary);
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.18s ease;
  user-select: none;
  white-space: nowrap;
  min-height: 38px;
}
.btn:hover {
  background-color: var(--bg-card-hover);
  border-color: var(--accent);
}
.btn:active {
  transform: scale(0.97);
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
  width: 38px;
  height: 38px;
  padding: 0;
  border-radius: 8px;
  font-size: 1rem;
}
.btn-sm {
  padding: 0.32rem 0.6rem;
  font-size: 0.78rem;
  min-height: 32px;
}

/* Layout */
.app-container {
  display: flex;
  flex: 1;
  position: relative;
  width: 100%;
}

/* Backdrop Overlay for Mobile Drawer */
.sidebar-backdrop {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  height: 100dvh;
  background: rgba(0, 0, 0, 0.65);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  z-index: 998;
  opacity: 0;
  transition: opacity 0.25s ease;
}
.sidebar-backdrop.active {
  display: block;
  opacity: 1;
}

/* Sidebar */
aside {
  width: 290px;
  background-color: var(--bg-secondary);
  border-right: 1px solid var(--border-color);
  height: calc(100vh - var(--header-height));
  height: calc(100dvh - var(--header-height));
  position: sticky;
  top: var(--header-height);
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  padding: 1rem 0.75rem;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  flex-shrink: 0;
  z-index: 100;
  transition: transform 0.28s cubic-bezier(0.4, 0, 0.2, 1);
}

.sidebar-mobile-header {
  display: none;
  align-items: center;
  justify-content: space-between;
  padding: 0.5rem 0.75rem 1rem;
  border-bottom: 1px solid var(--border-color);
  margin-bottom: 0.75rem;
}
.sidebar-mobile-title {
  font-size: 1rem;
  font-weight: 700;
  color: var(--accent);
}
.sidebar-close-btn {
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: 1.6rem;
  line-height: 1;
  cursor: pointer;
  padding: 0.2rem 0.5rem;
}
.sidebar-close-btn:hover {
  color: var(--text-primary);
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
  padding: 0.62rem 0.75rem;
  border-radius: 8px;
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 0.86rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.15s ease;
  user-select: none;
  min-height: 40px;
}
.nav-item-left {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  min-width: 0;
}
.nav-item-left span:last-child {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
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
  flex-shrink: 0;
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
  padding: 2rem;
  max-width: 1240px;
  margin: 0 auto;
  width: 100%;
  min-width: 0;
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
  background: linear-gradient(135deg, rgba(56, 189, 248, 0.12), rgba(99, 102, 241, 0.12));
  border: 1px solid rgba(56, 189, 248, 0.3);
  border-radius: 16px;
  padding: clamp(1.2rem, 1rem + 1vw, 1.75rem);
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
  gap: 0.75rem;
}
.hero-title {
  font-size: clamp(1.25rem, 1rem + 1vw, 1.55rem);
  font-weight: 800;
  color: var(--text-primary);
  line-height: 1.3;
}
.hero-badge-group {
  display: flex;
  gap: 0.4rem;
  flex-wrap: wrap;
}
.hero-desc {
  color: var(--text-secondary);
  font-size: clamp(0.85rem, 0.8rem + 0.3vw, 0.95rem);
  line-height: 1.55;
}

/* Unit Dropdown Controls Bar */
.unit-controls-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 0.75rem 1.1rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
  gap: 0.75rem;
}
.unit-controls-left {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  flex-wrap: wrap;
}
.unit-controls-right {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
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
  max-width: 100%;
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
  margin-bottom: 1.15rem;
  box-shadow: var(--shadow-sm);
  transition: all 0.2s ease;
  overflow: hidden;
}
.main-topic-card:hover {
  border-color: rgba(56, 189, 248, 0.4);
}
.main-topic-header {
  padding: clamp(0.85rem, 0.8rem + 0.5vw, 1.15rem) clamp(1rem, 0.9rem + 0.5vw, 1.4rem);
  background: linear-gradient(135deg, var(--bg-card), var(--bg-secondary));
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  user-select: none;
  transition: background-color 0.2s;
  border-bottom: 1px solid transparent;
  gap: 0.75rem;
  min-height: 48px;
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
  gap: 0.65rem;
  flex-wrap: wrap;
  min-width: 0;
}
.main-topic-title {
  font-size: clamp(1rem, 0.95rem + 0.3vw, 1.15rem);
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.35;
}
.main-topic-toggle-btn {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--accent);
  background-color: var(--accent-light);
  padding: 0.3rem 0.6rem;
  border-radius: 6px;
  flex-shrink: 0;
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
  padding: clamp(0.85rem, 0.75rem + 0.5vw, 1.25rem);
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
  margin-bottom: 0.75rem;
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
  padding: clamp(0.75rem, 0.7rem + 0.3vw, 0.95rem) clamp(0.85rem, 0.8rem + 0.4vw, 1.15rem);
  background-color: var(--bg-secondary);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  user-select: none;
  font-weight: 600;
  font-size: clamp(0.88rem, 0.84rem + 0.2vw, 0.96rem);
  color: var(--text-primary);
  transition: background-color 0.15s;
  border-bottom: 1px solid transparent;
  gap: 0.5rem;
  min-height: 44px;
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
  gap: 0.5rem;
  flex: 1;
  min-width: 0;
}
.sub-topic-icon {
  color: var(--accent);
  font-size: 0.85rem;
  flex-shrink: 0;
}
.sub-topic-title-text {
  min-width: 0;
  word-break: break-word;
}
.sub-topic-badge {
  font-size: 0.7rem;
  font-weight: 600;
  padding: 0.15rem 0.45rem;
  border-radius: 6px;
  background-color: var(--accent-light);
  color: var(--accent);
  margin-left: auto;
  margin-right: 0.5rem;
  flex-shrink: 0;
}
.sub-topic-arrow {
  font-size: 0.8rem;
  color: var(--text-muted);
  transition: transform 0.25s ease;
  flex-shrink: 0;
}
.sub-topic-header.open .sub-topic-arrow {
  transform: rotate(180deg);
  color: var(--accent);
}

/* LEVEL 3: Detailed Description */
.sub-topic-detail {
  display: none;
  padding: clamp(0.9rem, 0.8rem + 0.5vw, 1.35rem);
  background-color: var(--bg-card);
  color: var(--text-secondary);
  font-size: clamp(0.85rem, 0.82rem + 0.2vw, 0.92rem);
  line-height: 1.65;
  animation: fadeIn 0.2s ease-in-out;
  overflow-wrap: break-word;
}
.sub-topic-detail.open {
  display: block;
}

/* Quick Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 210px), 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}
.stat-card {
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 1.15rem;
  display: flex;
  align-items: center;
  gap: 0.9rem;
  box-shadow: var(--shadow-sm);
  transition: transform 0.2s, border-color 0.2s;
}
.stat-card:hover {
  transform: translateY(-2px);
  border-color: var(--accent);
}
.stat-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.35rem;
  background-color: var(--accent-light);
  color: var(--accent);
  flex-shrink: 0;
}
.stat-info h3 {
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--text-primary);
  line-height: 1.2;
}
.stat-info p {
  font-size: 0.78rem;
  color: var(--text-muted);
}

/* Callout Boxes */
.def-box {
  background: linear-gradient(135deg, rgba(56, 189, 248, 0.08), rgba(56, 189, 248, 0.03));
  border-left: 4px solid var(--accent);
  padding: 1rem 1.15rem;
  border-radius: 0 10px 10px 0;
  margin: 1rem 0;
  font-size: 0.92rem;
  color: var(--text-primary);
  overflow-wrap: break-word;
}
.def-title {
  font-weight: 700;
  color: var(--accent);
  font-size: 0.8rem;
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
  padding: 0.95rem 1.15rem;
  border-radius: 0 10px 10px 0;
  margin: 1rem 0;
  font-size: 0.88rem;
  overflow-wrap: break-word;
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
  padding: 0.95rem 1.15rem;
  border-radius: 0 10px 10px 0;
  margin: 1rem 0;
  font-size: 0.88rem;
  overflow-wrap: break-word;
}
.alert-title {
  font-weight: 700;
  color: var(--danger);
  margin-bottom: 0.3rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

/* Responsive Tables */
.table-wrapper {
  width: 100%;
  max-width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin: 1.15rem 0;
  border-radius: 10px;
  border: 1px solid var(--border-color);
  background-color: var(--bg-card);
}
table {
  width: 100%;
  min-width: 580px;
  border-collapse: collapse;
  font-size: 0.86rem;
  text-align: left;
}
th {
  background-color: var(--bg-secondary);
  color: var(--text-primary);
  font-weight: 700;
  padding: 0.75rem 0.9rem;
  border-bottom: 2px solid var(--border-color);
  white-space: nowrap;
}
td {
  padding: 0.7rem 0.9rem;
  border-bottom: 1px solid var(--border-color);
  color: var(--text-secondary);
  vertical-align: top;
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
  padding: 0.9rem;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  font-family: var(--font-mono);
  font-size: 0.82rem;
  color: #38bdf8;
  margin: 0.9rem 0;
}
code {
  font-family: var(--font-mono);
  font-size: 0.85em;
  background-color: rgba(56, 189, 248, 0.1);
  color: var(--accent);
  padding: 0.12rem 0.35rem;
  border-radius: 4px;
}

/* Diagrams */
.diagram-container {
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 1.25rem 0.75rem;
  margin: 1.25rem 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  width: 100%;
  max-width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}
.diagram-container svg {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 0 auto;
}
.diagram-caption {
  font-size: 0.8rem;
  color: var(--text-muted);
  font-style: italic;
  text-align: center;
}

/* Diagram Reference & Google Photo Links Bar */
.diagram-ref-bar {
  width: 100%;
  max-width: 740px;
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 0.85rem 1rem;
  margin-top: 0.75rem;
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
  text-align: left;
}
.diagram-ref-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.6rem;
}
.diagram-ref-info {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--text-secondary);
  font-size: 0.82rem;
  font-weight: 500;
  flex-wrap: wrap;
}
.ref-tag {
  background-color: var(--accent-light);
  color: var(--accent);
  padding: 0.2rem 0.5rem;
  border-radius: 6px;
  font-weight: 700;
  font-size: 0.72rem;
  text-transform: uppercase;
  flex-shrink: 0;
}
.diagram-ref-actions {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.btn-ref {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.38rem 0.75rem;
  border-radius: 6px;
  text-decoration: none;
  font-size: 0.78rem;
  font-weight: 600;
  transition: all 0.15s ease;
  min-height: 32px;
}
.btn-ref-google {
  background: linear-gradient(135deg, #1e3a8a, #0284c7);
  color: #ffffff !important;
  border: 1px solid #38bdf8;
}
.btn-ref-google:hover {
  background: linear-gradient(135deg, #0284c7, #38bdf8);
  color: #0b0f19 !important;
  transform: translateY(-1px);
}
.btn-ref-wiki {
  background-color: var(--bg-secondary);
  color: var(--text-secondary) !important;
  border: 1px solid var(--border-color);
}
.btn-ref-wiki:hover {
  border-color: var(--accent);
  color: var(--text-primary) !important;
  transform: translateY(-1px);
}
.diagram-ref-tip {
  font-size: 0.82rem;
  color: var(--text-secondary);
  background-color: var(--bg-secondary);
  border-left: 3px solid var(--warning);
  padding: 0.45rem 0.75rem;
  border-radius: 0 6px 6px 0;
  line-height: 1.45;
}

/* Lists */
ul, ol {
  padding-left: 1.4rem;
  margin: 0.7rem 0;
  color: var(--text-secondary);
}
li {
  margin-bottom: 0.35rem;
}
li strong {
  color: var(--text-primary);
}

/* Grid Layouts */
.grid-2 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr));
  gap: 1.1rem;
  margin: 1.1rem 0;
}
.grid-3 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr));
  gap: 1rem;
  margin: 1.1rem 0;
}
.subcard {
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 1.15rem;
}
.subcard h4 {
  font-size: 0.96rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.45rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

/* Flashcards Section */
.flashcard-wrapper {
  max-width: 680px;
  margin: 1.5rem auto;
  perspective: 1000px;
  width: 100%;
}
.flashcard {
  position: relative;
  width: 100%;
  min-height: 270px;
  cursor: pointer;
  transform-style: preserve-3d;
  transition: transform 0.55s cubic-bezier(0.4, 0, 0.2, 1);
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
  -webkit-backface-visibility: hidden;
  border-radius: 16px;
  padding: clamp(1.2rem, 1rem + 1vw, 2rem);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border: 2px solid var(--border-color);
  box-shadow: var(--shadow-lg);
  overflow-y: auto;
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
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--accent);
}
.card-content {
  text-align: center;
  margin: auto 0;
}
.card-question {
  font-size: clamp(1.05rem, 0.95rem + 0.4vw, 1.25rem);
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.4;
}
.card-answer {
  font-size: clamp(0.88rem, 0.82rem + 0.3vw, 0.98rem);
  line-height: 1.6;
  color: var(--text-secondary);
}
.card-hint {
  font-size: 0.75rem;
  color: var(--text-muted);
  text-align: center;
}
.flashcard-nav {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  margin-top: 1.25rem;
  flex-wrap: wrap;
}

/* Quiz Simulator */
.quiz-container {
  max-width: 820px;
  margin: 0 auto;
  width: 100%;
}
.quiz-progress-bar-container {
  height: 8px;
  background-color: var(--border-color);
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 1.25rem;
}
.quiz-progress-bar {
  height: 100%;
  background: linear-gradient(90deg, var(--accent), var(--success));
  width: 0%;
  transition: width 0.3s;
}
.quiz-filter {
  display: flex;
  gap: 0.45rem;
  margin-bottom: 1.25rem;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  padding-bottom: 0.35rem;
  scrollbar-width: none;
}
.quiz-filter::-webkit-scrollbar {
  display: none;
}
.quiz-filter .btn {
  flex-shrink: 0;
}

.quiz-card {
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 14px;
  padding: clamp(1rem, 0.9rem + 0.5vw, 1.5rem);
  margin-bottom: 1.25rem;
  box-shadow: var(--shadow-sm);
}
.quiz-card-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.85rem;
  font-size: 0.82rem;
  color: var(--text-muted);
  gap: 0.5rem;
}
.quiz-question-text {
  font-size: clamp(0.96rem, 0.92rem + 0.2vw, 1.05rem);
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 1.15rem;
  line-height: 1.45;
}
.quiz-options {
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
}
.quiz-option {
  padding: 0.72rem 0.95rem;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  background-color: var(--bg-secondary);
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.18s;
  display: flex;
  align-items: center;
  gap: 0.65rem;
  font-size: clamp(0.85rem, 0.82rem + 0.2vw, 0.92rem);
  min-height: 44px;
}
.quiz-option:hover {
  border-color: var(--accent);
  background-color: var(--accent-light);
  color: var(--text-primary);
}
.quiz-option:active {
  transform: scale(0.985);
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
  padding: 0.95rem;
  border-radius: 8px;
  background-color: var(--bg-secondary);
  border-left: 4px solid var(--accent);
  font-size: 0.86rem;
  color: var(--text-secondary);
  line-height: 1.55;
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
  padding: 0.9rem 1.15rem;
  background-color: var(--bg-card);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  user-select: none;
  font-weight: 600;
  color: var(--text-primary);
  font-size: clamp(0.88rem, 0.85rem + 0.2vw, 0.95rem);
  transition: background-color 0.2s;
  gap: 0.6rem;
  min-height: 48px;
}
.accordion-header:hover {
  background-color: var(--bg-card-hover);
}
.accordion-content {
  display: none;
  padding: 1.15rem;
  border-top: 1px solid var(--border-color);
  background-color: var(--bg-secondary);
  font-size: 0.88rem;
  color: var(--text-secondary);
  line-height: 1.6;
}
.accordion-content.open {
  display: block;
}
.accordion-icon {
  transition: transform 0.3s;
  flex-shrink: 0;
}
.accordion-header.open .accordion-icon {
  transform: rotate(180deg);
}

/* Mobile Sticky Bottom Navigation Bar */
.mobile-bottom-nav {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: var(--bottom-nav-height);
  background-color: var(--bg-secondary);
  border-top: 1px solid var(--border-color);
  z-index: 990;
  justify-content: space-around;
  align-items: center;
  padding: 0 0.5rem;
  padding-bottom: env(safe-area-inset-bottom);
  box-shadow: 0 -4px 15px rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}
.bottom-nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2px;
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: 0.68rem;
  font-weight: 600;
  cursor: pointer;
  flex: 1;
  height: 100%;
  transition: color 0.15s ease;
  user-select: none;
}
.bottom-nav-item .bnav-icon {
  font-size: 1.25rem;
  line-height: 1;
}
.bottom-nav-item:hover {
  color: var(--accent);
}
.bottom-nav-item.active {
  color: var(--accent);
}
.bottom-nav-item.active .bnav-icon {
  transform: translateY(-1px);
}

/* ============================================================ */
/* POWER MODES: RANDOM TOPICS, IMP LIST & QUESTION ROULETTE     */
/* ============================================================ */
.power-banner {
  border-color: rgba(56, 189, 248, 0.35);
  background: linear-gradient(135deg, rgba(56, 189, 248, 0.1), rgba(168, 85, 247, 0.1));
}

.random-topic-container {
  max-width: 900px;
  margin: 0 auto;
}

.random-topic-display {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: var(--shadow-md);
  transition: transform 0.2s ease, border-color 0.2s ease;
}

.random-topic-display:hover {
  border-color: var(--accent);
}

.random-controls {
  display: flex;
  gap: 0.75rem;
  align-items: center;
  flex-wrap: wrap;
  margin-top: 1.25rem;
}

/* IMP Topics Grid & Cards */
.imp-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 1.25rem;
  margin-top: 1.25rem;
}

.imp-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 1.25rem;
  box-shadow: var(--shadow-sm);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.imp-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
  border-color: var(--accent);
}

.imp-card.tier-1 {
  border-left: 4px solid var(--danger);
}

.imp-card.tier-2 {
  border-left: 4px solid var(--purple);
}

.imp-card.tier-3 {
  border-left: 4px solid var(--accent);
}

.imp-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
  flex-wrap: wrap;
}

.imp-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.35;
  flex: 1;
  min-width: 220px;
}

.imp-tags {
  display: flex;
  gap: 0.35rem;
  flex-wrap: wrap;
}

/* Roulette Question Mode */
.roulette-container {
  max-width: 850px;
  margin: 0 auto;
}

.roulette-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 14px;
  padding: 1.75rem;
  box-shadow: var(--shadow-md);
  transition: all 0.25s ease;
}

.roulette-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.roulette-question {
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--text-primary);
  line-height: 1.45;
  margin-bottom: 1.25rem;
  padding-left: 0.75rem;
  border-left: 3px solid var(--accent);
}

.answer-panel {
  display: none;
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 1.25rem;
  margin-top: 1.25rem;
  animation: fadeIn 0.25s ease;
}

.answer-panel.open {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-4px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ============================================================ */
/* MEDIA QUERIES & ADVANCED MOBILE-FIRST APP STYLING           */
/* ============================================================ */

/* Tablet & Mobile (< 900px) */
@media (max-width: 900px) {
  .mobile-menu-btn {
    display: inline-flex;
  }
  
  .sidebar-mobile-header {
    display: flex;
  }

  /* Aside becomes an off-canvas slide-out drawer */
  aside {
    position: fixed;
    top: 0;
    left: 0;
    width: var(--drawer-width);
    height: 100vh;
    height: 100dvh;
    z-index: 1000;
    transform: translateX(-100%);
    box-shadow: none;
    border-right: 1px solid var(--border-color);
    background-color: var(--bg-secondary);
    padding-bottom: calc(2rem + env(safe-area-inset-bottom, 0px));
  }
  aside.drawer-open {
    transform: translateX(0);
    box-shadow: 16px 0 40px rgba(0, 0, 0, 0.7);
  }

  main {
    padding: 1rem 0.85rem;
    padding-bottom: calc(var(--bottom-nav-height) + 2rem + env(safe-area-inset-bottom, 0px));
    max-width: 100vw;
    overflow-x: hidden;
  }

  .mobile-bottom-nav {
    display: flex;
  }

  .search-box {
    width: 180px;
  }
  .search-box input:focus {
    width: 220px;
  }

  .unit-controls-bar {
    flex-direction: column;
    align-items: stretch;
    gap: 0.6rem;
  }
  .unit-controls-left, .unit-controls-right {
    width: 100%;
    justify-content: space-between;
  }
}

/* Small Tablets & Phones (< 640px) */
@media (max-width: 640px) {
  :root {
    --header-height: 56px;
    --bottom-nav-height: 58px;
  }

  body {
    font-size: 14px;
    line-height: 1.55;
  }

  /* Compact Non-Overflowing Header */
  header {
    padding: 0.4rem 0.65rem;
    height: var(--header-height);
    gap: 0.4rem;
    max-width: 100vw;
    overflow: hidden;
  }

  .header-left {
    gap: 0.45rem;
    flex: 1;
    min-width: 0;
  }

  .mobile-menu-btn {
    width: 36px;
    height: 36px;
    font-size: 1.15rem;
    border-radius: 7px;
  }

  .brand {
    gap: 0.5rem;
    min-width: 0;
  }

  .brand-logo {
    width: 32px;
    height: 32px;
    font-size: 0.95rem;
    border-radius: 7px;
  }

  .brand-text h1 {
    font-size: 0.92rem;
    font-weight: 700;
  }

  .brand-text p {
    display: none;
  }

  .header-controls {
    gap: 0.35rem;
  }

  .search-box {
    width: 110px;
  }
  .search-box input {
    font-size: 0.78rem;
    padding: 0.35rem 0.5rem 0.35rem 1.65rem;
    height: 34px;
    border-radius: 6px;
  }
  .search-box input:focus {
    width: 145px;
  }
  .search-icon {
    left: 0.5rem;
    font-size: 0.72rem;
  }

  .btn-icon {
    width: 34px;
    height: 34px;
    font-size: 0.95rem;
    border-radius: 6px;
  }

  .btn-print-hide {
    display: none !important;
  }

  /* Fluid Content & Clean Margins */
  main {
    padding: 0.75rem 0.5rem;
    padding-bottom: calc(var(--bottom-nav-height) + 1.8rem + env(safe-area-inset-bottom, 0px));
  }

  .hero-banner {
    padding: 1rem 0.85rem;
    border-radius: 12px;
    margin-bottom: 1.25rem;
  }
  .hero-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
    margin-bottom: 0.65rem;
  }
  .hero-title {
    font-size: 1.18rem;
    line-height: 1.3;
  }
  .hero-desc {
    font-size: 0.82rem;
    line-height: 1.5;
  }
  .hero-badge-group {
    gap: 0.3rem;
  }
  .hero-badge-group .badge {
    font-size: 0.7rem;
    padding: 0.2rem 0.5rem;
  }

  /* Stats Grid */
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 0.55rem;
    margin-bottom: 1.25rem;
  }
  .stat-card {
    padding: 0.75rem;
    gap: 0.5rem;
    border-radius: 10px;
  }
  .stat-icon {
    width: 32px;
    height: 32px;
    font-size: 1rem;
    border-radius: 8px;
  }
  .stat-info h3 {
    font-size: 1.05rem;
  }
  .stat-info p {
    font-size: 0.68rem;
  }

  /* Cards Padding Reduction */
  .topic-card {
    padding: 0.85rem 0.75rem;
    border-radius: 12px;
    margin-bottom: 1.25rem;
  }
  .topic-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.4rem;
    margin-bottom: 0.85rem;
  }
  .topic-title {
    font-size: 1.05rem;
  }

  /* 2-Tier Topic Dropdowns */
  .main-topic-card {
    border-radius: 10px;
    margin-bottom: 0.65rem;
  }
  .main-topic-header {
    padding: 0.75rem 0.85rem;
    gap: 0.4rem;
  }
  .main-topic-title-area {
    gap: 0.4rem;
  }
  .main-topic-title {
    font-size: 0.94rem;
    line-height: 1.35;
  }
  /* Hide verbose 'Expand Topic' text on phones, keep clean arrow */
  .main-topic-toggle-btn span:first-child {
    display: none;
  }
  .main-topic-toggle-btn {
    padding: 0.25rem 0.45rem;
    border-radius: 5px;
  }
  .main-topic-body {
    padding: 0.65rem 0.5rem;
  }

  .sub-topic-card {
    border-radius: 8px;
    margin-bottom: 0.45rem;
  }
  .sub-topic-header {
    padding: 0.65rem 0.75rem;
    min-height: 40px;
  }
  .sub-topic-title-text {
    font-size: 0.86rem;
    line-height: 1.35;
  }
  .sub-topic-badge {
    font-size: 0.65rem;
    padding: 0.12rem 0.35rem;
    margin-left: 0.25rem;
    margin-right: 0.25rem;
  }
  .sub-topic-detail {
    padding: 0.75rem 0.65rem;
    font-size: 0.85rem;
    line-height: 1.55;
  }

  /* Callout Boxes */
  .def-box, .tip-box {
    padding: 0.75rem 0.85rem;
    margin: 0.75rem 0;
    font-size: 0.84rem;
    border-radius: 0 8px 8px 0;
  }

  /* Horizontal Filter Bar as Mobile Scrollable Chips */
  .filter-bar {
    display: flex;
    gap: 0.45rem;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    padding-bottom: 0.4rem;
    margin-bottom: 1rem;
    scrollbar-width: none;
    flex-wrap: nowrap;
    width: 100%;
  }
  .filter-bar::-webkit-scrollbar {
    display: none;
  }
  .filter-bar .btn {
    flex-shrink: 0;
    border-radius: 999px;
    padding: 0.35rem 0.75rem;
    font-size: 0.78rem;
    min-height: 34px;
    white-space: nowrap;
  }

  /* Unit Controls Bar */
  .unit-controls-bar {
    padding: 0.65rem 0.75rem;
    margin-bottom: 1rem;
    gap: 0.5rem;
  }
  .unit-controls-left {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.45rem;
    width: 100%;
  }
  .unit-controls-left .btn {
    width: 100%;
    font-size: 0.76rem;
    padding: 0.4rem 0.5rem;
    min-height: 34px;
  }
  .unit-controls-right {
    width: 100%;
  }
  .topic-select {
    width: 100%;
    font-size: 0.8rem;
    padding: 0.4rem 0.65rem;
  }

  /* Tables: Mobile Scroll Hint & Compact Padding */
  .table-wrapper {
    margin: 0.85rem 0;
    border-radius: 8px;
    position: relative;
  }
  .table-wrapper::before {
    content: '👉 Swipe table horizontally to view all columns';
    display: block;
    font-size: 0.7rem;
    color: var(--accent);
    background: var(--accent-light);
    padding: 0.25rem 0.5rem;
    border-bottom: 1px solid var(--border-color);
    font-weight: 600;
    text-align: center;
  }
  table {
    min-width: 500px;
    font-size: 0.78rem;
  }
  th {
    padding: 0.55rem 0.65rem;
  }
  td {
    padding: 0.5rem 0.65rem;
  }

  /* Diagrams on Mobile: Maintain Readable Size with Horizontal Scroll */
  .diagram-container {
    padding: 0.85rem 0.5rem;
    margin: 0.85rem 0;
    border-radius: 10px;
    align-items: flex-start;
  }
  .diagram-container::before {
    content: '📐 Swipe diagram horizontally to view full architecture';
    display: block;
    font-size: 0.7rem;
    color: var(--accent);
    margin-bottom: 0.4rem;
    font-weight: 600;
    width: 100%;
    text-align: center;
  }
  .diagram-container svg {
    min-width: 540px;
    max-width: none;
    height: auto;
  }
  .diagram-ref-bar {
    padding: 0.65rem 0.75rem;
    border-radius: 8px;
  }
  .diagram-ref-top {
    flex-direction: column;
    align-items: stretch;
    gap: 0.5rem;
  }
  .diagram-ref-actions {
    flex-direction: column;
    align-items: stretch;
    gap: 0.4rem;
  }
  .diagram-ref-actions .btn, .diagram-ref-actions .btn-ref {
    width: 100%;
    text-align: center;
    justify-content: center;
  }

  /* Code Blocks */
  pre {
    padding: 0.65rem 0.75rem;
    font-size: 0.76rem;
    border-radius: 8px;
    margin: 0.65rem 0;
  }

  /* Power Modes: Random Topics */
  .random-topic-display {
    padding: 1rem 0.85rem;
    border-radius: 10px;
  }
  .random-controls {
    flex-direction: column;
    align-items: stretch;
    gap: 0.5rem;
  }
  .random-controls .btn {
    width: 100%;
    padding: 0.65rem 1rem !important;
    font-size: 0.9rem !important;
  }
  #rtCounterText {
    text-align: center;
  }

  /* Power Modes: IMP Topics Cards */
  .imp-grid {
    grid-template-columns: 1fr;
    gap: 0.85rem;
  }
  .imp-card {
    padding: 1rem 0.85rem;
    border-radius: 10px;
  }
  .imp-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.35rem;
  }
  .imp-title {
    font-size: 0.96rem;
  }
  .imp-tags {
    gap: 0.25rem;
  }
  .imp-tags .badge {
    font-size: 0.7rem;
    padding: 0.15rem 0.45rem;
  }
  .imp-card > div:last-child {
    display: grid !important;
    grid-template-columns: 1fr !important;
    gap: 0.4rem !important;
  }
  .imp-card > div:last-child .btn {
    width: 100%;
    text-align: center;
    justify-content: center;
  }

  /* Power Modes: Question Roulette */
  .roulette-card {
    padding: 1rem 0.85rem;
    border-radius: 10px;
  }
  .roulette-meta {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.4rem;
  }
  .roulette-question {
    font-size: 1rem;
    line-height: 1.4;
    padding-left: 0.5rem;
    margin-bottom: 1rem;
  }
  .roulette-card > div:nth-of-type(2) {
    display: grid !important;
    grid-template-columns: 1fr !important;
    gap: 0.45rem !important;
  }
  .roulette-card > div:nth-of-type(2) .btn {
    width: 100%;
    text-align: center;
    justify-content: center;
    padding: 0.55rem 0.85rem;
  }
  .answer-panel {
    padding: 0.85rem 0.75rem;
    border-radius: 8px;
    font-size: 0.84rem;
  }

  /* Flashcards */
  .flashcard-container {
    padding: 0;
  }
  .flashcard {
    min-height: 250px;
  }
  .flashcard-front, .flashcard-back {
    padding: 1rem 0.85rem;
    border-radius: 12px;
  }
  .card-question {
    font-size: 1.05rem;
  }
  .card-answer {
    font-size: 0.85rem;
  }
  .flashcard-nav {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.45rem;
    width: 100%;
  }
  .flashcard-nav .btn {
    width: 100%;
    font-size: 0.78rem;
    padding: 0.45rem 0.5rem;
    min-height: 38px;
  }
  .flashcard-nav #fcCounter {
    grid-column: 1 / -1;
    text-align: center;
  }

  /* Sticky Mobile Bottom Navigation Bar */
  .mobile-bottom-nav {
    height: calc(var(--bottom-nav-height) + env(safe-area-inset-bottom, 0px));
    padding-bottom: env(safe-area-inset-bottom, 0px);
    background-color: rgba(21, 29, 47, 0.94);
  }
  [data-theme="light"] .mobile-bottom-nav {
    background-color: rgba(255, 255, 255, 0.94);
  }
  .bottom-nav-item {
    padding: 4px 0;
    font-size: 0.65rem;
  }
  .bottom-nav-item .bnav-icon {
    font-size: 1.2rem;
  }
}

/* Extra Small Phones (< 380px, e.g. iPhone SE, compact Androids) */
@media (max-width: 380px) {
  header {
    padding: 0.35rem 0.5rem;
  }
  .brand-logo {
    display: none;
  }
  .brand-text h1 {
    font-size: 0.86rem;
  }
  .search-box {
    width: 95px;
  }
  .search-box input:focus {
    width: 125px;
  }
  .mobile-menu-btn {
    width: 32px;
    height: 32px;
    font-size: 1rem;
  }
  .btn-icon {
    width: 32px;
    height: 32px;
  }
  .stats-grid {
    grid-template-columns: 1fr;
  }
}

/* Print Optimization */
@media print {
  header, aside, .mobile-bottom-nav, .sidebar-backdrop, .btn, .flashcard-nav, 
  .quiz-filter, .search-box, .quiz-progress-bar-container, .unit-controls-bar {
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
