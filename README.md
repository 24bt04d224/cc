# ☁️ BTCS701F: Cloud Computing — Master Exam Portal

[![GSFC University](https://img.shields.io/badge/University-GSFC%20University-blue)](https://www.gsfcuniversity.ac.in/)
[![Course](https://img.shields.io/badge/Course-BTCS701F%3A%20Cloud%20Computing-emerald)](https://github.com/24bt04d224/cc)
[![Live Portal](https://img.shields.io/badge/Live%20Website-GitHub%20Pages-brightgreen)](https://24bt04d224.github.io/cc/)
[![MCQ Simulator](https://img.shields.io/badge/Exam%20MCQs-52%20Questions-purple)](https://24bt04d224.github.io/cc/)
[![Flashcards](https://img.shields.io/badge/Revision%20Cards-36%20Cards-orange)](https://24bt04d224.github.io/cc/)

A comprehensive, self-contained Cloud Computing examination preparation and study portal built for **B.Tech Computer Science & Engineering (Semester VII)** students at **GSFC University**.

🌐 **Live Website Link:** **[https://24bt04d224.github.io/cc/](https://24bt04d224.github.io/cc/)**

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

- 📑 **2-Tier Interactive Dropdown Accordions:** Main heads expand to sub-topics, which expand to in-depth revision notes and diagrams.
- 🎨 **Inline SVG Architecture Diagrams:** 10 hand-crafted vector diagrams (Hypervisors, Containers vs VMs, OpenStack Nova/Neutron/Keystone, SDN planes, AWS IAM flow, Pizza-as-a-Service, Multi-Tenant Database Isolation, 3-Tier Web Architecture).
- ⚖️ **7-Mark Side-by-Side Comparison Matrices:** 8 full-credit exam comparison tables ready for long-answer questions.
- 🎯 **52-Question Exam MCQ Simulator:** Instant grading, score tracking, unit filters, and detailed explanations for every question.
- 🗂️ **36 Interactive 3D-Flip Flashcards:** Rapid-fire memory drills for formulas, definitions, and key exam concepts.
- 📝 **University Question Bank:** Curated model answers categorized by marks (2M, 5M, 7M, 10M).
- 🔍 **Live Global Search:** Instant keyword lookup with automatic accordion opening.
- 🌓 **Dark / Light Theme Toggle:** Clean contrast tuned for long study sessions.
- 📱 **100% Mobile & Offline Ready:** Zero external CSS/JS dependencies.

---

## 🚀 How to Enable GitHub Pages (Free Hosting)

1. Open this repository on GitHub: [github.com/24bt04d224/cc](https://github.com/24bt04d224/cc)
2. Go to **Settings** ➔ **Pages** (in the left sidebar).
3. Under **Build and deployment**:
   - **Source:** Select `Deploy from a branch`
   - **Branch:** Select `main` and folder `/(root)`
   - Click **Save**.
4. Within 1 minute, your website will be live at:
   👉 **[https://24bt04d224.github.io/cc/](https://24bt04d224.github.io/cc/)**

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
