# ☁️ BTCS701F: Cloud Computing — Master Exam Portal

[![GSFC University](https://img.shields.io/badge/University-GSFC%20University-blue)](https://www.gsfcuniversity.ac.in/)
[![Course](https://img.shields.io/badge/Course-BTCS701F%3A%20Cloud%20Computing-emerald)](https://github.com/24bt04d224/cc)
[![Vercel Deployment](https://img.shields.io/badge/Live%20on-Vercel-black?logo=vercel)](https://cc1-black.vercel.app/)
[![MCQ Simulator](https://img.shields.io/badge/Exam%20MCQs-52%20Questions-purple)](https://cc1-black.vercel.app/)
[![Flashcards](https://img.shields.io/badge/Revision%20Cards-36%20Cards-orange)](https://cc1-black.vercel.app/)

A comprehensive, self-contained Cloud Computing examination preparation and study portal built for **B.Tech Computer Science & Engineering (Semester VII)** students at **GSFC University**.

🚀 **Official Live Website (Vercel):** **[https://cc1-black.vercel.app/](https://cc1-black.vercel.app/)**
🔥 **Units 4 & 5 Guaranteed Questions (21 Qs):** **[https://cc1-black.vercel.app/unit4_5_imp_questions](https://cc1-black.vercel.app/unit4_5_imp_questions)**
📱 **Instant Mobile Shortlink:** **[https://tinyurl.com/25vbsf4t](https://tinyurl.com/25vbsf4t)**


---

## 📖 Course Coverage & Marks Distribution

| Unit | Title | Weightage | Focus & High-Yield Concepts |
| :---: | :--- | :---: | :--- |
| **Unit 1** | **Introduction to Cloud Computing** | 15% | 5 NIST Characteristics, 12 Benefits vs 10 Challenges, 9 Architecture Layers, CloudWatch 95% CPU Case, CSP Selection Criteria, Fog Computing. |
| **Unit 2** | **Cloud Service Models (SPI)** | 15% | IaaS (EC2 10-step launch, GCE, Azure VMs), PaaS (App Engine, Beanstalk Web vs Worker tiers), SaaS (Google Docs, M365), Shared Responsibility Model. |
| **Unit 3** | **Cloud Deployment Models & Architecture** | 20% | Public/Private/Hybrid/Community, Multi-Cloud, Cloud Bursting, Multi-Tenant Database Isolation (Pool/Bridge/Silo), Multi-Server 3-Tier Architecture. |
| **Unit 4** | **Virtualization Technologies & Cloud Tools** | **25%** | **Priority #1:** Type 1 vs Type 2 Hypervisors, Dispatcher/Allocator/Interpreter, Docker vs VMs, OpenStack 9 components, CloudStack hierarchy, Storage types (Block/Object/File), SDN 3 layers. |
| **Unit 5** | **Security, Privacy & Cloud Management** | **25%** | **Priority #2:** CIA Triad, AWS IAM (JSON policy syntax, Explicit Deny Rule), VM Security, 7 Real-World Security Incidents (Capital One, Storm-0558, S3 leaks, Uber, Code Spaces, Marriott, Target). |

> ⚠️ **Key Exam Strategy:** **Unit 4 + Unit 5 alone account for 50% of your examination marks.** Master these two units first!

---

## ✨ Features

- 🎲 **Random Topic Shuffler & Active Recall:** Eliminate predictable study patterns with an interactive topic roller across all 140 syllabus concepts, complete with real-world analogies and Google Images diagram links.
- ⭐ **Master IMP Topics (Top 30 Guaranteed):** Curated high-yield examination priority list (Units 4 & 5 - 50% Marks focus) featuring exact question formats, mark allocations, and 4-point blueprints.
- ❓ **Cross-Chapter Question Roulette:** Interactive exam simulator testing 2M definitions, 5M short notes, 7M comparisons, and 10M architectural questions with hidden model answers and instant reveals.
- 📸 **Google Images Diagram Reference Bars:** Every major architecture diagram features direct 1-click visual search buttons to official Google Image search diagrams and Wikipedia references.
- 📱 **100% Responsive & Mobile Optimized:** Touch-first navigation with an off-canvas slide-out drawer (`☰`), sticky bottom thumb-bar (`🏠 Units 📊 MCQs 🗂️`), and iOS/Android viewport-fit support.
- 📑 **2-Tier Interactive Dropdown Accordions:** Main heads expand to sub-topics, which expand to in-depth revision notes and diagrams.
- 🎨 **Inline SVG Architecture Diagrams:** 12 hand-crafted vector diagrams (Hypervisors, Containers vs VMs, OpenStack Nova/Neutron/Keystone, SDN planes, AWS IAM flow, Pizza-as-a-Service, Multi-Tenant Database Isolation, 3-Tier Web Architecture, NIST Roles, Fog Computing).
- ⚖️ **7-Mark Side-by-Side Comparison Matrices:** 8 full-credit exam comparison tables ready for long-answer questions.
- 🎯 **52-Question Exam MCQ Simulator:** Instant grading, score tracking, unit filters, and detailed explanations for every question.
- 🗂️ **36 Interactive 3D-Flip Flashcards:** Rapid-fire memory drills for formulas, definitions, and key exam concepts.
- 📝 **University Question Bank:** Curated model answers categorized by marks (2M, 5M, 7M, 10M).
- 🔍 **Live Global Search:** Instant keyword lookup with automatic accordion opening.
- 🌓 **Dark / Light Theme Toggle:** Clean contrast tuned for long study sessions.
- 📱 **Self-Contained & Offline Ready:** Zero external CSS/JS dependencies.

---

## 🚀 Deploying Live with Free Domains

### Option A: GitHub Pages (Automatic CI/CD via GitHub Actions)
1. Open [github.com/24bt04d224/cc/settings/pages](https://github.com/24bt04d224/cc/settings/pages).
2. Under **Build and deployment**:
   - **Source:** Select `GitHub Actions` (or `Deploy from a branch` -> `main` / `root`).
   - Click **Save**.
3. Within 30–60 seconds, your site is published at:
   👉 **[https://24bt04d224.github.io/cc/](https://24bt04d224.github.io/cc/)**

### Option B: Vercel (1-Click Deployment)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2F24bt04d224%2Fcc)
1. Click the button above or visit: **[Deploy to Vercel](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2F24bt04d224%2Fcc)**
2. Sign in with GitHub and click **Deploy**.
3. Live in 15 seconds at: `https://cc-...vercel.app`

### Option C: Instant Live Mirror
- Mobile Quicklink: **[tinyurl.com/263ku7h8](https://tinyurl.com/263ku7h8)**
- Direct HTTPS Mirror: **[files.catbox.moe/e7k04r.html](https://files.catbox.moe/e7k04r.html)**

---

## 🛠️ Local Development & Regeneration

To regenerate or modify the portal content:
```bash
# Run portal test
python test_portal.py

# Recompile the portal
python generate_portal.py
```

---
*Created for GSFC University BTCS701F Cloud Computing Course.*
