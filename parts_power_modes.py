# -*- coding: utf-8 -*-

# ==============================================================================
# SECTION 1: RANDOM TOPICS GENERATOR
# ==============================================================================
TAB_RANDOM_TOPICS_HTML = """
<div id="random-topics" class="tab-pane">
  <div class="hero-banner power-banner">
    <div class="hero-header">
      <div class="hero-title">🎲 Random Topic Shuffler & Active Recall</div>
      <div class="hero-badge-group">
        <span class="badge badge-accent">All 5 Units</span>
        <span class="badge">140 Curated Concepts</span>
        <span class="badge badge-priority">Active Recall Drill</span>
      </div>
    </div>
    <p class="hero-desc">
      Eliminate predictable revision patterns! Click <strong>"Roll Random Topic"</strong> to challenge yourself with an unpredictable concept from anywhere in the syllabus. Test what you remember before clicking to view the full revision notes.
    </p>
  </div>

  <div class="random-topic-container">
    <!-- Chapter Filter Bar -->
    <div class="filter-bar">
      <button class="btn btn-primary" onclick="setRandomTopicUnit('all', this)">All Units (1–5)</button>
      <button class="btn" onclick="setRandomTopicUnit('unit4', this)">Unit 4: Virtualization (25%)</button>
      <button class="btn" onclick="setRandomTopicUnit('unit5', this)">Unit 5: Security (25%)</button>
      <button class="btn" onclick="setRandomTopicUnit('unit3', this)">Unit 3: Architecture (20%)</button>
      <button class="btn" onclick="setRandomTopicUnit('unit1', this)">Unit 1: Intro (15%)</button>
      <button class="btn" onclick="setRandomTopicUnit('unit2', this)">Unit 2: Service Models (15%)</button>
    </div>

    <!-- Active Topic Card Display -->
    <div class="random-topic-display" id="randomTopicDisplay">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem; flex-wrap: wrap; gap: 0.5rem;">
        <span class="badge badge-priority" id="rtUnitBadge">Unit 4: Virtualization</span>
        <span class="badge" id="rtMarksBadge">7 Marks Expected</span>
        <span class="badge badge-accent" id="rtYieldBadge">🔥 High-Yield Priority</span>
      </div>
      <h2 id="rtTitle" style="font-size: 1.35rem; color: var(--accent); margin-bottom: 1rem; line-height: 1.35;">
        Type 1 (Bare-Metal) vs Type 2 (Hosted) Hypervisors
      </h2>
      <div class="def-box" id="rtSummary">
        <strong>Exam Summary:</strong> Type 1 (Bare-Metal, e.g., ESXi, Hyper-V, KVM) runs directly on the raw physical hardware without any host OS, delivering direct hardware execution, high performance, and strict isolation. Type 2 (Hosted, e.g., VirtualBox, VMware Workstation) runs as a user application on top of an existing host OS (Windows/Linux), introducing double OS overhead and dependency on host kernel stability.
      </div>
      <div class="tip-box" id="rtAnalogy">
        <strong>💡 Real-World Analogy / Insight:</strong> Type 1 is like a purpose-built apartment complex constructed straight from the foundation. Type 2 is like running a hotel business inside rented rooms of a residential house.
      </div>
      <div class="diagram-ref-bar" style="margin-top: 1rem;" id="rtLinksBar">
        <div class="diagram-ref-top">
          <div class="diagram-ref-info">
            <span class="ref-tag">📸 Visual Search</span>
            <span id="rtDiagramDesc">View official diagrams & Google Image photos:</span>
          </div>
          <div class="diagram-ref-actions">
            <a href="https://www.google.com/search?tbm=isch&q=Type+1+vs+Type+2+Hypervisor+Architecture+Diagram" target="_blank" rel="noopener" class="btn-ref btn-ref-google" id="rtGoogleBtn">
              <span>🔍 Google Images Diagram</span>
              <span class="ext-icon">↗</span>
            </a>
            <button class="btn btn-sm btn-primary" onclick="jumpToRandomTopicUnit()" id="rtJumpBtn">
              <span>📖 Open Full Unit Notes</span>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Random Controls -->
    <div class="random-controls">
      <button class="btn btn-primary" style="padding: 0.75rem 1.5rem; font-size: 1rem;" onclick="rollNextRandomTopic()">
        <span>🎲 Roll Random Topic</span>
      </button>
      <button class="btn" style="padding: 0.75rem 1.25rem;" onclick="toggleTopicDetails()">
        <span id="rtToggleBtnText">👁️ Toggle Short Summary</span>
      </button>
      <span style="font-size: 0.85rem; color: var(--text-muted);" id="rtCounterText">Topics in pool: 35</span>
    </div>
  </div>
</div>
"""

# ==============================================================================
# SECTION 2: IMP TOPICS (MOST IMPORTANT HIGH-YIELD CONCEPTS)
# ==============================================================================
TAB_IMP_TOPICS_HTML = """
<div id="imp-topics" class="tab-pane">
  <div class="hero-banner" style="border-color: rgba(239, 68, 68, 0.4); background: linear-gradient(135deg, rgba(239, 68, 68, 0.12), rgba(168, 85, 247, 0.12));">
    <div class="hero-header">
      <div class="hero-title">⭐ Master IMP Topics: 100% Exam-Guaranteed List</div>
      <div class="hero-badge-group">
        <span class="badge badge-priority">Top 30 Questions</span>
        <span class="badge badge-accent">Units 4 & 5 Focus (50% Marks)</span>
        <span class="badge">Model Blueprints</span>
      </div>
    </div>
    <p class="hero-desc">
      Historically proven examination questions curated from your GSFC University syllabus and lecture slide notes.
      Each topic card provides the <strong>Exact Mark Weightage</strong>, <strong>Expected Exam Question Format</strong>, <strong>Drawing Tips</strong>, and a <strong>Rapid 4-Bullet Answer Blueprint</strong>.
    </p>
  </div>

  <!-- IMP Filter Chips -->
  <div class="filter-bar">
    <button class="btn btn-primary" onclick="filterImpCards('all', this)">All IMPs (30)</button>
    <button class="btn" onclick="filterImpCards('tier1', this)">🔥 Tier 1: 50% Marks (Units 4 & 5)</button>
    <button class="btn" onclick="filterImpCards('tier2', this)">⭐ Tier 2: Unit 3 Architecture (20%)</button>
    <button class="btn" onclick="filterImpCards('tier3', this)">📌 Tier 3: Units 1 & 2 Foundations (30%)</button>
    <button class="btn" onclick="filterImpCards('7m', this)">7-Mark Questions</button>
    <button class="btn" onclick="filterImpCards('10m', this)">10-Mark Questions</button>
  </div>

  <!-- IMP Cards Container -->
  <div class="imp-grid" id="impGrid">
    
    <!-- IMP 1: Type 1 vs Type 2 Hypervisors -->
    <div class="imp-card tier-1" data-tier="tier1" data-marks="7m">
      <div class="imp-header">
        <div class="imp-title">1. Type 1 (Bare-Metal) vs Type 2 (Hosted) Hypervisors</div>
        <div class="imp-tags">
          <span class="badge badge-priority">Unit 4 · 7 Marks</span>
          <span class="badge" style="background-color: var(--danger-bg); color: var(--danger); font-weight: 700;">99% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"Differentiate between Type 1 and Type 2 Hypervisors with a neat diagram. Discuss their architectures, pros, cons, and give two examples of each."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>Architecture:</strong> Type 1 sits directly on bare-metal hardware (no host OS); Type 2 sits as an application on top of a host OS (Windows/Linux).</li>
          <li><strong>Performance & Overhead:</strong> Type 1 has near-native hardware speed and low latency; Type 2 suffers double OS context switching and high overhead.</li>
          <li><strong>Security & Isolation:</strong> Type 1 has strong VM isolation; Type 2 is vulnerable to host OS compromise (if host OS crashes, all VMs crash).</li>
          <li><strong>Examples:</strong> Type 1: VMware ESXi, Microsoft Hyper-V, KVM, Xen. Type 2: Oracle VirtualBox, VMware Workstation.</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <a href="https://www.google.com/search?tbm=isch&q=Type+1+vs+Type+2+Hypervisor+Architecture+Diagram" target="_blank" class="btn btn-sm">🔍 View Diagrams on Google</a>
        <button class="btn btn-sm btn-primary" onclick="switchTab('unit4'); setTimeout(() => { document.querySelector('#u4-t1 .main-topic-header').click(); }, 300);">📖 Open Unit 4 Notes</button>
      </div>
    </div>

    <!-- IMP 2: Hypervisor Core Components -->
    <div class="imp-card tier-1" data-tier="tier1" data-marks="7m">
      <div class="imp-header">
        <div class="imp-title">2. Three Core Modules of Hypervisors: Dispatcher, Allocator & Interpreter</div>
        <div class="imp-tags">
          <span class="badge badge-priority">Unit 4 · 7 Marks</span>
          <span class="badge" style="background-color: var(--danger-bg); color: var(--danger); font-weight: 700;">95% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"Explain the internal architecture of a hypervisor. Describe the roles of Dispatcher, Allocator, and Interpreter/Executor with a schematic diagram."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>Dispatcher:</strong> The traffic controller. Intercepts privileged CPU instructions and routes them to the Allocator or Interpreter.</li>
          <li><strong>Allocator:</strong> Decides how physical resources (CPU cores, RAM pages, disk blocks) are allocated to requesting VMs without collision.</li>
          <li><strong>Interpreter / Executor:</strong> Emulates sensitive instructions that cannot be executed directly by the hardware without violating isolation.</li>
          <li><strong>Popek-Goldberg Theorem:</strong> For a computer architecture to be virtualizable, all sensitive instructions must be a subset of privileged instructions.</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <a href="https://www.google.com/search?tbm=isch&q=Hypervisor+Dispatcher+Allocator+Interpreter+Architecture+Diagram" target="_blank" class="btn btn-sm">🔍 View Diagrams on Google</a>
        <button class="btn btn-sm btn-primary" onclick="switchTab('unit4');">📖 Open Unit 4 Notes</button>
      </div>
    </div>

    <!-- IMP 3: Docker Containers vs VMs -->
    <div class="imp-card tier-1" data-tier="tier1" data-marks="7m">
      <div class="imp-header">
        <div class="imp-title">3. Virtual Machines vs Docker Containers (Hardware vs OS Virtualization)</div>
        <div class="imp-tags">
          <span class="badge badge-priority">Unit 4 · 7/10 Marks</span>
          <span class="badge" style="background-color: var(--danger-bg); color: var(--danger); font-weight: 700;">99% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"Compare Virtual Machines and Containers on at least six parameters. Draw neat architectural diagrams for both."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>Virtualization Level:</strong> VM virtualizes physical hardware (CPU, RAM, NIC); Container virtualizes OS kernel using namespaces and cgroups.</li>
          <li><strong>Guest OS Requirement:</strong> VM requires a dedicated, full Guest OS per instance (~GBs); Container shares Host OS kernel (MBs).</li>
          <li><strong>Startup Time:</strong> VMs boot in minutes (full OS boot); Containers launch in milliseconds (instant process spawn).</li>
          <li><strong>Isolation & Density:</strong> VMs provide hard hardware-level boundary; Containers provide process-level isolation with 5–10x higher server density.</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <a href="https://www.google.com/search?tbm=isch&q=Docker+Containers+vs+Virtual+Machines+Architecture+Diagram" target="_blank" class="btn btn-sm">🔍 View Diagrams on Google</a>
        <button class="btn btn-sm btn-primary" onclick="switchTab('comparisons');">📊 View 7-Mark Comparison Table</button>
      </div>
    </div>

    <!-- IMP 4: OpenStack 9 Components -->
    <div class="imp-card tier-1" data-tier="tier1" data-marks="10m">
      <div class="imp-header">
        <div class="imp-title">4. OpenStack Architecture & 9 Core Components</div>
        <div class="imp-tags">
          <span class="badge badge-priority">Unit 4 · 10 Marks</span>
          <span class="badge" style="background-color: var(--danger-bg); color: var(--danger); font-weight: 700;">95% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"Explain the architecture of OpenStack with a diagram. Describe the functions of Keystone, Nova, Neutron, Swift, Glance, and Cinder."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>Compute & Identity:</strong> <strong>Nova</strong> provisions & manages virtual servers; <strong>Keystone</strong> provides unified authentication & authorization tokens.</li>
          <li><strong>Network & GUI:</strong> <strong>Neutron</strong> delivers SDN, IP addresses, subnets, and routing; <strong>Horizon</strong> provides the web graphical user interface.</li>
          <li><strong>Storage Trio:</strong> <strong>Glance</strong> (VM image repository), <strong>Cinder</strong> (persistent block storage volumes), <strong>Swift</strong> (distributed object storage for unstructured files).</li>
          <li><strong>Automation:</strong> <strong>Heat</strong> provides template-driven cloud application orchestration; <strong>Ceilometer</strong> tracks telemetry & billing meters.</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <a href="https://www.google.com/search?tbm=isch&q=OpenStack+Architecture+Nova+Neutron+Keystone+Glance+Diagram" target="_blank" class="btn btn-sm">🔍 View Diagrams on Google</a>
        <button class="btn btn-sm btn-primary" onclick="switchTab('unit4');">📖 Open Unit 4 Notes</button>
      </div>
    </div>

    <!-- IMP 5: Software Defined Networking (SDN) -->
    <div class="imp-card tier-1" data-tier="tier1" data-marks="7m">
      <div class="imp-header">
        <div class="imp-title">5. Software-Defined Networking (SDN) 3-Plane Architecture & OpenFlow</div>
        <div class="imp-tags">
          <span class="badge badge-priority">Unit 4 · 7 Marks</span>
          <span class="badge" style="background-color: var(--danger-bg); color: var(--danger); font-weight: 700;">95% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"What is SDN? Explain its 3-tier architecture with a neat diagram. Contrast the Data Plane, Control Plane, and Management Plane."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>Concept:</strong> Decouples the network control logic (Control Plane) from physical packet forwarding routers/switches (Data Plane).</li>
          <li><strong>Application Plane (Top):</strong> Network monitoring, security policies, and load balancing applications communicating via Northbound REST APIs.</li>
          <li><strong>Control Plane (Middle):</strong> The centralized SDN controller (the "brain") that calculates routing topologies and injects flow rules.</li>
          <li><strong>Data Plane (Bottom):</strong> High-speed hardware switches that simply forward packets according to flow tables via Southbound APIs (OpenFlow).</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <a href="https://www.google.com/search?tbm=isch&q=Software+Defined+Networking+SDN+Architecture+Three+Layers+Diagram" target="_blank" class="btn btn-sm">🔍 View Diagrams on Google</a>
        <button class="btn btn-sm btn-primary" onclick="switchTab('unit4');">📖 Open Unit 4 Notes</button>
      </div>
    </div>

    <!-- IMP 6: Storage Types (Block vs Object vs File) -->
    <div class="imp-card tier-1" data-tier="tier1" data-marks="7m">
      <div class="imp-header">
        <div class="imp-title">6. Cloud Storage Comparison: Block vs Object vs File Storage</div>
        <div class="imp-tags">
          <span class="badge badge-priority">Unit 4 · 7 Marks</span>
          <span class="badge" style="background-color: var(--danger-bg); color: var(--danger); font-weight: 700;">90% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"Compare Block Storage, Object Storage, and File Storage on use cases, structure, latency, protocols, and cloud services (AWS/Azure/GCP)."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>Block Storage (EBS, Persistent Disk):</strong> Data split into fixed raw blocks with unique addresses; ultra-low latency; ideal for OS boot disks and transactional databases (MySQL).</li>
          <li><strong>Object Storage (S3, Cloud Storage):</strong> Data stored as complete immutable objects with custom metadata and globally unique ID in a flat namespace; accessed via REST API (HTTP GET/PUT); infinite scale; ideal for media, backups, data lakes.</li>
          <li><strong>File Storage (EFS, Azure Files):</strong> Hierarchical folder/file structure; accessed via standard NFS/SMB network protocols; shared across multiple servers concurrently.</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <a href="https://www.google.com/search?tbm=isch&q=Block+vs+File+vs+Object+Storage+Cloud+Diagram" target="_blank" class="btn btn-sm">🔍 View Diagrams on Google</a>
        <button class="btn btn-sm btn-primary" onclick="switchTab('comparisons');">📊 View Comparison Table</button>
      </div>
    </div>

    <!-- IMP 7: CIA Triad in Cloud Computing -->
    <div class="imp-card tier-1" data-tier="tier1" data-marks="7m">
      <div class="imp-header">
        <div class="imp-title">7. The CIA Security Triad & Cloud Security Controls</div>
        <div class="imp-tags">
          <span class="badge badge-priority">Unit 5 · 7 Marks</span>
          <span class="badge" style="background-color: var(--danger-bg); color: var(--danger); font-weight: 700;">95% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"Explain the CIA Triad in the context of cloud security. What controls protect Confidentiality, Integrity, and Availability?"</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>Confidentiality:</strong> Preventing unauthorized exposure of sensitive customer data. Controls: AES-256 encryption at rest, TLS 1.3 in transit, IAM RBAC, MFA.</li>
          <li><strong>Integrity:</strong> Protecting data from unauthorized modification, deletion, or tampering. Controls: SHA-256 digital signatures, cryptographic checksums, WORM storage (S3 Object Lock).</li>
          <li><strong>Availability:</strong> Ensuring authorized users have uninterrupted access to cloud resources. Controls: Multi-AZ redundancy, DDoS mitigation (AWS Shield), auto-scaling groups, automated snapshots.</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <a href="https://www.google.com/search?tbm=isch&q=CIA+Triad+Information+Security+Cloud+Computing+Diagram" target="_blank" class="btn btn-sm">🔍 View Diagrams on Google</a>
        <button class="btn btn-sm btn-primary" onclick="switchTab('unit5');">📖 Open Unit 5 Notes</button>
      </div>
    </div>

    <!-- IMP 8: AWS IAM Policy Evaluation Logic -->
    <div class="imp-card tier-1" data-tier="tier1" data-marks="7m">
      <div class="imp-header">
        <div class="imp-title">8. AWS IAM Architecture & Policy Evaluation Flowchart (Prof. Amin Shaikh)</div>
        <div class="imp-tags">
          <span class="badge badge-priority">Unit 5 · 7 Marks</span>
          <span class="badge" style="background-color: var(--danger-bg); color: var(--danger); font-weight: 700;">99% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"Explain AWS IAM policy evaluation logic with a flowchart. Discuss the significance of the Explicit Deny Rule and Principle of Least Privilege."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>Default Decision:</strong> All requests begin with an implicit default DENY.</li>
          <li><strong>Golden Rule 1 (Explicit Deny):</strong> An explicit `\"Effect\": \"Deny\"` in ANY matching policy unconditionally overrides any number of `\"Allow\"` statements!</li>
          <li><strong>Golden Rule 2 (Explicit Allow):</strong> If no explicit deny exists, there must be at least one explicit `\"Effect\": \"Allow\"` for access to be granted; otherwise, it remains denied.</li>
          <li><strong>Principle of Least Privilege (PoLP):</strong> Grant users only the minimum permissions necessary to accomplish their assigned job role for the minimum required duration.</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <a href="https://www.google.com/search?tbm=isch&q=AWS+IAM+Policy+Evaluation+Logic+Flowchart+Diagram" target="_blank" class="btn btn-sm">🔍 View Diagrams on Google</a>
        <button class="btn btn-sm btn-primary" onclick="switchTab('unit5');">📖 Open Unit 5 Notes</button>
      </div>
    </div>

    <!-- IMP 9: Real-World Security Incidents -->
    <div class="imp-card tier-1" data-tier="tier1" data-marks="10m">
      <div class="imp-header">
        <div class="imp-title">9. Cloud Security Incident Case Studies (Capital One & Storm-0558)</div>
        <div class="imp-tags">
          <span class="badge badge-priority">Unit 5 · 10 Marks</span>
          <span class="badge" style="background-color: var(--danger-bg); color: var(--danger); font-weight: 700;">90% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"Analyze any two major real-world cloud security breaches. Discuss the root causes, attack vectors, and preventative controls."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>Capital One (2019):</strong> SSRF on misconfigured open-source WAF querying AWS IMDSv1 (`169.254.169.254`) &rarr; exfiltrated IAM role credentials &rarr; accessed 106M credit applications in S3. Fix: IMDSv2 (session token header required), restrictive IAM.</li>
          <li><strong>Microsoft Storm-0558 (2023):</strong> Stolen MSA signing key from crashed Windows kernel memory dump &rarr; forged OpenID tokens &rarr; breached 25 government email inboxes. Fix: Secure key rotation, HSM-enforced token signing.</li>
          <li><strong>Code Spaces (2014):</strong> Lack of MFA on AWS root account &rarr; hacker deleted all EBS volumes and S3 backups &rarr; company forced into complete liquidation. Fix: Never use root, enforce MFA.</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <button class="btn btn-sm btn-primary" onclick="switchTab('unit5');">📖 Open Unit 5 Incident Studies</button>
      </div>
    </div>

    <!-- IMP 10: Multi-Tenant Architecture & Database Isolation -->
    <div class="imp-card tier-2" data-tier="tier2" data-marks="7m">
      <div class="imp-header">
        <div class="imp-title">10. Multi-Tenant Architecture: Silo vs Bridge vs Pool Database Isolation</div>
        <div class="imp-tags">
          <span class="badge badge-accent">Unit 3 · 7 Marks</span>
          <span class="badge" style="background-color: var(--warning-bg); color: var(--warning); font-weight: 700;">95% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"What is Multi-Tenancy? Compare Silo, Bridge, and Pool data isolation patterns with respect to cost, security, performance, and blast radius."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>Definition:</strong> Software architecture where a single instance of an application serves multiple distinct customer organizations (tenants).</li>
          <li><strong>Silo Pattern:</strong> Separate physical database instance per tenant. Maximum isolation, zero cross-tenant blast radius, highest cost (used by Banks/Gov).</li>
          <li><strong>Bridge Pattern:</strong> Shared database engine, separate database schemas per tenant. Moderate isolation and cost.</li>
          <li><strong>Pool Pattern:</strong> Shared database and shared tables; data segregated logically via `tenant_id` column. Lowest cost, maximum resource efficiency, requires robust Row-Level Security (RLS).</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <a href="https://www.google.com/search?tbm=isch&q=Multi+Tenant+Database+Architecture+Silo+Bridge+Pool+Diagram" target="_blank" class="btn btn-sm">🔍 View Diagrams on Google</a>
        <button class="btn btn-sm btn-primary" onclick="switchTab('unit3');">📖 Open Unit 3 Notes</button>
      </div>
    </div>

    <!-- IMP 11: Multi-Server 3-Tier Web Architecture -->
    <div class="imp-card tier-2" data-tier="tier2" data-marks="7m">
      <div class="imp-header">
        <div class="imp-title">11. Multi-Server 3-Tier Enterprise Web Architecture</div>
        <div class="imp-tags">
          <span class="badge badge-accent">Unit 3 · 7 Marks</span>
          <span class="badge" style="background-color: var(--warning-bg); color: var(--warning); font-weight: 700;">90% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"Explain the 3-Tier Cloud Web Architecture with a diagram. Discuss the components of Presentation, Application, and Data Tiers."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>Tier 1 (Presentation / Web):</strong> Public-facing layer handling SSL termination, static content, and HTTP routing via Nginx behind an Elastic Load Balancer.</li>
          <li><strong>Tier 2 (Application / Business Logic):</strong> Private subnet compute nodes executing backend APIs, microservices, and asynchronous background worker queues.</li>
          <li><strong>Tier 3 (Database / Persistence):</strong> Isolated database subnet with Primary DB (read/write master) and secondary Read Replicas with automated failover.</li>
          <li><strong>High Availability Formula:</strong> $\\text{Availability} = \\frac{\\text{Uptime}}{\\text{Uptime} + \\text{Downtime}} \\times 100\\%$.</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <a href="https://www.google.com/search?tbm=isch&q=Three+Tier+Cloud+Web+Architecture+AWS+Diagram" target="_blank" class="btn btn-sm">🔍 View Diagrams on Google</a>
        <button class="btn btn-sm btn-primary" onclick="switchTab('unit3');">📖 Open Unit 3 Notes</button>
      </div>
    </div>

    <!-- IMP 12: NIST 5 Characteristics -->
    <div class="imp-card tier-3" data-tier="tier3" data-marks="5m">
      <div class="imp-header">
        <div class="imp-title">12. NIST 5 Essential Characteristics of Cloud Computing</div>
        <div class="imp-tags">
          <span class="badge">Unit 1 · 5/7 Marks</span>
          <span class="badge" style="background-color: var(--success-bg); color: var(--success); font-weight: 700;">99% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"Define Cloud Computing according to NIST SP 800-145 and explain all 5 essential characteristics."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>5-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>1. On-Demand Self-Service:</strong> Users provision servers/storage automatically without contacting human support.</li>
          <li><strong>2. Broad Network Access:</strong> Services accessible over standard networks via laptops, smartphones, tablets.</li>
          <li><strong>3. Resource Pooling:</strong> Multi-tenant shared infrastructure dynamically allocated to multiple consumers.</li>
          <li><strong>4. Rapid Elasticity:</strong> Resources scale outward and inward dynamically with real-time demand.</li>
          <li><strong>5. Measured Service:</strong> Automatic usage metering and pay-per-use billing based on actual consumption.</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <button class="btn btn-sm btn-primary" onclick="switchTab('unit1');">📖 Open Unit 1 Notes</button>
      </div>
    </div>

    <!-- IMP 13: Pizza-as-a-Service & SPI Taxonomy -->
    <div class="imp-card tier-3" data-tier="tier3" data-marks="7m">
      <div class="imp-header">
        <div class="imp-title">13. Cloud Service Models (SPI): IaaS vs PaaS vs SaaS & Pizza-as-a-Service</div>
        <div class="imp-tags">
          <span class="badge">Unit 2 · 7 Marks</span>
          <span class="badge" style="background-color: var(--success-bg); color: var(--success); font-weight: 700;">99% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"Explain the SPI service model taxonomy (IaaS, PaaS, SaaS) using the Pizza-as-a-Service analogy and a comparison table."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>Traditional On-Premises:</strong> "Made at home" — You manage all 9 layers (dough to dining table).</li>
          <li><strong>IaaS:</strong> "Take and bake" — Vendor manages hardware, servers, virtualization; You manage OS, runtime, and apps. (e.g., AWS EC2, GCP GCE).</li>
          <li><strong>PaaS:</strong> "Pizza delivered" — Vendor manages everything up to runtime/DB; You bring application code and data. (e.g., AWS Elastic Beanstalk, Google App Engine).</li>
          <li><strong>SaaS:</strong> "Dining out" — Vendor manages 100% of software, updates, servers, and data; You consume it via browser. (e.g., Google Docs, Microsoft 365).</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <button class="btn btn-sm btn-primary" onclick="switchTab('comparisons');">📊 View SPI Comparison Matrix</button>
      </div>
    </div>

    <!-- IMP 14: Fog Computing vs Cloud Computing -->
    <div class="imp-card tier-3" data-tier="tier3" data-marks="5m">
      <div class="imp-header">
        <div class="imp-title">14. Fog Computing vs Cloud Computing Architecture</div>
        <div class="imp-tags">
          <span class="badge">Unit 1 · 5/7 Marks</span>
          <span class="badge" style="background-color: var(--success-bg); color: var(--success); font-weight: 700;">90% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"What is Fog Computing? Why is it needed alongside Cloud Computing? Compare them on latency, location of nodes, and real-time processing."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>Concept:</strong> Decentralized computing extending cloud capabilities to the local network edge near IoT sensors.</li>
          <li><strong>Latency:</strong> Cloud has high latency (100–250 ms); Fog provides ultra-low sub-millisecond response (1–15 ms).</li>
          <li><strong>Bandwidth & Data Reduction:</strong> Fog filters and summarizes raw data locally, saving massive uplink WAN bandwidth.</li>
          <li><strong>Applications:</strong> Autonomous driving, manufacturing robotic line safety, smart healthcare telemetry, avionics.</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <a href="https://www.google.com/search?tbm=isch&q=Fog+Computing+Architecture+IoT+Edge+Cloud+Diagram" target="_blank" class="btn btn-sm">🔍 View Diagrams on Google</a>
        <button class="btn btn-sm btn-primary" onclick="switchTab('unit1');">📖 Open Unit 1 Notes</button>
      </div>
    </div>

  </div>
</div>
"""

# ==============================================================================
# SECTION 3: RANDOM QUESTION ROULETTE (FROM ANY CHAPTER)
# ==============================================================================
TAB_RANDOM_QUESTIONS_HTML = """
<div id="random-questions" class="tab-pane">
  <div class="hero-banner power-banner" style="border-color: rgba(56, 189, 248, 0.4); background: linear-gradient(135deg, rgba(56, 189, 248, 0.12), rgba(16, 185, 129, 0.12));">
    <div class="hero-header">
      <div class="hero-title">❓ Cross-Chapter Random Question Roulette</div>
      <div class="hero-badge-group">
        <span class="badge badge-accent">Units 1 to 5</span>
        <span class="badge">2M / 5M / 7M / 10M</span>
        <span class="badge badge-priority">Exam Simulation</span>
      </div>
    </div>
    <p class="hero-desc">
      Test your actual exam readiness! Pull sudden questions of any mark weightage from random chapters. Try framing the answer in your mind or on paper first, then click <strong>"Reveal Model Answer"</strong> to evaluate yourself against university grading criteria.
    </p>
  </div>

  <div class="roulette-container">
    <!-- Filters Bar -->
    <div class="filter-bar">
      <button class="btn btn-primary" onclick="setRouletteFilter('all', this)">All Marks (2M/5M/7M/10M)</button>
      <button class="btn" onclick="setRouletteFilter('7m', this)">7-Mark Questions</button>
      <button class="btn" onclick="setRouletteFilter('10m', this)">10-Mark Questions</button>
      <button class="btn" onclick="setRouletteFilter('5m', this)">5-Mark Questions</button>
      <button class="btn" onclick="setRouletteFilter('2m', this)">2-Mark Definitions</button>
      <button class="btn" onclick="setRouletteFilter('unit45', this)">Units 4 & 5 Only (50%)</button>
    </div>

    <!-- Active Question Display Card -->
    <div class="roulette-card" id="rouletteCard">
      <div class="roulette-meta">
        <div style="display: flex; gap: 0.5rem; align-items: center;">
          <span class="badge badge-priority" id="rqUnitBadge">Unit 4: Virtualization</span>
          <span class="badge badge-accent" id="rqMarksBadge">7 Marks</span>
        </div>
        <span class="badge" id="rqTypeBadge">Descriptive & Diagram</span>
      </div>

      <div class="roulette-question" id="rqQuestionText">
        Q. Differentiate between Type 1 (Bare-Metal) and Type 2 (Hosted) Hypervisors with a neat architecture diagram. Discuss why Type 1 hypervisors are preferred in enterprise cloud data centers.
      </div>

      <!-- Action Buttons -->
      <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
        <button class="btn btn-primary" onclick="toggleRouletteAnswer()" id="rqRevealBtn">
          <span>👁️ Reveal Model Answer</span>
        </button>
        <button class="btn" onclick="rollNextRouletteQuestion()">
          <span>🔄 Next Random Question</span>
        </button>
        <a href="https://www.google.com/search?tbm=isch&q=Type+1+vs+Type+2+Hypervisor+Architecture+Diagram" target="_blank" class="btn" id="rqGoogleSearchBtn">
          <span>🔍 View Diagram on Google</span>
        </a>
      </div>

      <!-- Hidden Model Answer Panel -->
      <div class="answer-panel" id="rqAnswerPanel">
        <h4 style="color: var(--success); margin-bottom: 0.6rem; display: flex; align-items: center; gap: 0.4rem;">
          <span>✔️</span> Official Model Answer & Grading Blueprint
        </h4>
        <div id="rqAnswerContent">
          <!-- Answer will be populated dynamically by JavaScript -->
        </div>
        <div class="tip-box" style="margin-top: 1rem;" id="rqTipBox">
          <strong>✏️ Diagram & Grading Tip:</strong> 2 Marks reserved for the diagram; 3 Marks for architecture differences; 2 Marks for enterprise justification (low latency, high isolation).
        </div>
      </div>
    </div>

    <!-- Statistics Tracker -->
    <div class="stats-grid" style="grid-template-columns: repeat(3, 1fr); margin-top: 1.5rem;">
      <div class="stat-card" style="padding: 0.85rem; text-align: center; justify-content: center;">
        <div>
          <h3 id="rqStatSeen" style="font-size: 1.35rem; color: var(--accent);">1</h3>
          <p style="font-size: 0.75rem;">Questions Attempted</p>
        </div>
      </div>
      <div class="stat-card" style="padding: 0.85rem; text-align: center; justify-content: center;">
        <div>
          <h3 id="rqStatPool" style="font-size: 1.35rem; color: var(--purple);">35</h3>
          <p style="font-size: 0.75rem;">Total Question Pool</p>
        </div>
      </div>
      <div class="stat-card" style="padding: 0.85rem; text-align: center; justify-content: center;">
        <div>
          <h3 style="font-size: 1.35rem; color: var(--success);">100%</h3>
          <p style="font-size: 0.75rem;">Syllabus Aligned</p>
        </div>
      </div>
    </div>
  </div>
</div>
"""
