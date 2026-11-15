# -*- coding: utf-8 -*-

SVG_HYPERVISOR = """
<svg viewBox="0 0 740 320" xmlns="http://www.w3.org/2000/svg" style="font-family: inherit;">
  <!-- Type 1 Bare Metal -->
  <g transform="translate(10, 10)">
    <rect x="0" y="0" width="340" height="300" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="30" text-anchor="middle" fill="#38bdf8" font-size="16" font-weight="bold">Type 1: Bare-Metal Hypervisor</text>
    
    <!-- VMs Row -->
    <rect x="20" y="55" width="90" height="85" rx="6" fill="#0f172a" stroke="#64748b"/>
    <text x="65" y="75" text-anchor="middle" fill="#94a3b8" font-size="11" font-weight="bold">VM 1 (Linux)</text>
    <rect x="25" y="85" width="80" height="22" rx="4" fill="#334155"/>
    <text x="65" y="100" text-anchor="middle" fill="#f8fafc" font-size="10">App A</text>
    <rect x="25" y="112" width="80" height="22" rx="4" fill="#1e3a8a"/>
    <text x="65" y="127" text-anchor="middle" fill="#93c5fd" font-size="10">Guest OS</text>

    <rect x="125" y="55" width="90" height="85" rx="6" fill="#0f172a" stroke="#64748b"/>
    <text x="170" y="75" text-anchor="middle" fill="#94a3b8" font-size="11" font-weight="bold">VM 2 (Win)</text>
    <rect x="130" y="85" width="80" height="22" rx="4" fill="#334155"/>
    <text x="170" y="100" text-anchor="middle" fill="#f8fafc" font-size="10">App B</text>
    <rect x="130" y="112" width="80" height="22" rx="4" fill="#1e3a8a"/>
    <text x="170" y="127" text-anchor="middle" fill="#93c5fd" font-size="10">Guest OS</text>

    <rect x="230" y="55" width="90" height="85" rx="6" fill="#0f172a" stroke="#64748b"/>
    <text x="275" y="75" text-anchor="middle" fill="#94a3b8" font-size="11" font-weight="bold">VM 3 (Test)</text>
    <rect x="235" y="85" width="80" height="22" rx="4" fill="#334155"/>
    <text x="275" y="100" text-anchor="middle" fill="#f8fafc" font-size="10">App C</text>
    <rect x="235" y="112" width="80" height="22" rx="4" fill="#1e3a8a"/>
    <text x="275" y="127" text-anchor="middle" fill="#93c5fd" font-size="10">Guest OS</text>

    <!-- Hypervisor Layer -->
    <rect x="20" y="155" width="300" height="50" rx="8" fill="#0284c7"/>
    <text x="170" y="185" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">Type 1 Hypervisor (ESXi, Hyper-V, KVM, Xen)</text>

    <!-- Physical Hardware -->
    <rect x="20" y="220" width="300" height="60" rx="8" fill="#334155"/>
    <text x="170" y="248" text-anchor="middle" fill="#f8fafc" font-size="13" font-weight="bold">Physical Hardware (Bare Metal)</text>
    <text x="170" y="268" text-anchor="middle" fill="#94a3b8" font-size="11">CPU · RAM · Storage · Network Cards</text>
  </g>

  <!-- Type 2 Hosted -->
  <g transform="translate(390, 10)">
    <rect x="0" y="0" width="340" height="300" rx="12" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <text x="170" y="30" text-anchor="middle" fill="#a855f7" font-size="16" font-weight="bold">Type 2: Hosted Hypervisor</text>

    <!-- VMs Row -->
    <rect x="40" y="55" width="120" height="70" rx="6" fill="#0f172a" stroke="#64748b"/>
    <rect x="45" y="65" width="110" height="22" rx="4" fill="#334155"/>
    <text x="100" y="80" text-anchor="middle" fill="#f8fafc" font-size="11">App 1 · Guest OS</text>
    <rect x="180" y="55" width="120" height="70" rx="6" fill="#0f172a" stroke="#64748b"/>
    <rect x="185" y="65" width="110" height="22" rx="4" fill="#334155"/>
    <text x="240" y="80" text-anchor="middle" fill="#f8fafc" font-size="11">App 2 · Guest OS</text>

    <!-- Type 2 Hypervisor Layer -->
    <rect x="20" y="135" width="300" height="42" rx="6" fill="#7c3aed"/>
    <text x="170" y="161" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">Type 2 Hypervisor (VirtualBox, Workstation)</text>

    <!-- Host Operating System -->
    <rect x="20" y="185" width="300" height="42" rx="6" fill="#475569"/>
    <text x="170" y="211" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">Host OS (Windows 11, macOS, Ubuntu)</text>

    <!-- Physical Hardware -->
    <rect x="20" y="235" width="300" height="50" rx="6" fill="#1e293b" stroke="#475569"/>
    <text x="170" y="258" text-anchor="middle" fill="#f8fafc" font-size="12" font-weight="bold">Physical Hardware</text>
    <text x="170" y="274" text-anchor="middle" fill="#94a3b8" font-size="10">Laptop / Desktop Physical CPU, RAM, Disk</text>
  </g>
</svg>
"""

SVG_VM_VS_CONTAINER = """
<svg viewBox="0 0 740 310" xmlns="http://www.w3.org/2000/svg" style="font-family: inherit;">
  <!-- Virtual Machine -->
  <g transform="translate(10, 10)">
    <rect x="0" y="0" width="340" height="290" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="28" text-anchor="middle" fill="#38bdf8" font-size="15" font-weight="bold">Virtual Machines (Hardware Virtualization)</text>

    <!-- App + Libs + Full Guest OS -->
    <rect x="25" y="45" width="135" height="115" rx="6" fill="#0f172a" stroke="#475569"/>
    <rect x="35" y="55" width="115" height="22" rx="4" fill="#3b82f6"/>
    <text x="92" y="70" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">App 1 + Bins/Libs</text>
    <rect x="35" y="85" width="115" height="65" rx="4" fill="#1e3a8a"/>
    <text x="92" y="115" text-anchor="middle" fill="#bfdbfe" font-size="11" font-weight="bold">Guest OS</text>
    <text x="92" y="132" text-anchor="middle" fill="#93c5fd" font-size="9">(Full Kernel + Drivers ~GBs)</text>

    <rect x="180" y="45" width="135" height="115" rx="6" fill="#0f172a" stroke="#475569"/>
    <rect x="190" y="55" width="115" height="22" rx="4" fill="#3b82f6"/>
    <text x="247" y="70" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">App 2 + Bins/Libs</text>
    <rect x="190" y="85" width="115" height="65" rx="4" fill="#1e3a8a"/>
    <text x="247" y="115" text-anchor="middle" fill="#bfdbfe" font-size="11" font-weight="bold">Guest OS</text>
    <text x="247" y="132" text-anchor="middle" fill="#93c5fd" font-size="9">(Full Kernel + Drivers ~GBs)</text>

    <!-- Hypervisor -->
    <rect x="25" y="170" width="290" height="38" rx="6" fill="#0284c7"/>
    <text x="170" y="194" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">Hypervisor (VMware / Hyper-V / KVM)</text>

    <!-- Host OS / Hardware -->
    <rect x="25" y="215" width="290" height="30" rx="6" fill="#475569"/>
    <text x="170" y="235" text-anchor="middle" fill="#ffffff" font-size="11">Host Operating System</text>
    <rect x="25" y="250" width="290" height="28" rx="6" fill="#334155"/>
    <text x="170" y="269" text-anchor="middle" fill="#94a3b8" font-size="11">Server Hardware (CPU, RAM, NIC)</text>
  </g>

  <!-- Docker Container -->
  <g transform="translate(390, 10)">
    <rect x="0" y="0" width="340" height="290" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="28" text-anchor="middle" fill="#10b981" font-size="15" font-weight="bold">Docker Containers (OS Virtualization)</text>

    <!-- Containers (No Guest OS!) -->
    <rect x="20" y="50" width="90" height="85" rx="6" fill="#064e3b" stroke="#10b981"/>
    <rect x="25" y="58" width="80" height="26" rx="4" fill="#059669"/>
    <text x="65" y="75" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">App A</text>
    <rect x="25" y="90" width="80" height="35" rx="4" fill="#047857"/>
    <text x="65" y="112" text-anchor="middle" fill="#d1fae5" font-size="10">Bins / Libs</text>

    <rect x="125" y="50" width="90" height="85" rx="6" fill="#064e3b" stroke="#10b981"/>
    <rect x="130" y="58" width="80" height="26" rx="4" fill="#059669"/>
    <text x="170" y="75" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">App B</text>
    <rect x="130" y="90" width="80" height="35" rx="4" fill="#047857"/>
    <text x="170" y="112" text-anchor="middle" fill="#d1fae5" font-size="10">Bins / Libs</text>

    <rect x="230" y="50" width="90" height="85" rx="6" fill="#064e3b" stroke="#10b981"/>
    <rect x="235" y="58" width="80" height="26" rx="4" fill="#059669"/>
    <text x="275" y="75" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">App C</text>
    <rect x="235" y="90" width="80" height="35" rx="4" fill="#047857"/>
    <text x="275" y="112" text-anchor="middle" fill="#d1fae5" font-size="10">Bins / Libs</text>

    <!-- Container Engine -->
    <rect x="20" y="148" width="300" height="42" rx="6" fill="#0284c7"/>
    <text x="170" y="174" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">Docker Container Engine (dockerd)</text>

    <!-- Shared Host OS Kernel -->
    <rect x="20" y="198" width="300" height="42" rx="6" fill="#065f46"/>
    <text x="170" y="224" text-anchor="middle" fill="#a7f3d0" font-size="12" font-weight="bold">Host OS Kernel (Shared by all containers)</text>

    <!-- Server Hardware -->
    <rect x="20" y="248" width="300" height="30" rx="6" fill="#334155"/>
    <text x="170" y="268" text-anchor="middle" fill="#94a3b8" font-size="11">Server Hardware (Shared CPU, RAM, Network)</text>
  </g>
</svg>
"""

SVG_OPENSTACK = """
<svg viewBox="0 0 740 380" xmlns="http://www.w3.org/2000/svg" style="font-family: inherit;">
  <rect x="10" y="10" width="720" height="360" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="370" y="38" text-anchor="middle" fill="#38bdf8" font-size="17" font-weight="bold">OpenStack Architecture & Core Components</text>

  <!-- Horizon Dashboard at Top -->
  <rect x="160" y="55" width="420" height="40" rx="8" fill="#0284c7"/>
  <text x="370" y="80" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">Horizon (Web Dashboard GUI) & REST APIs</text>

  <!-- Central Authentication: Keystone -->
  <rect x="250" y="115" width="240" height="45" rx="8" fill="#e11d48"/>
  <text x="370" y="137" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">Keystone (Identity & Token)</text>
  <text x="370" y="152" text-anchor="middle" fill="#fecdd3" font-size="10">Authentication & Access Control</text>

  <!-- Core Services Grid -->
  <!-- Nova (Compute) -->
  <g transform="translate(40, 185)">
    <rect x="0" y="0" width="145" height="70" rx="8" fill="#2563eb"/>
    <text x="72" y="28" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">Nova</text>
    <text x="72" y="48" text-anchor="middle" fill="#bfdbfe" font-size="11">Compute Engine</text>
    <text x="72" y="62" text-anchor="middle" fill="#dbeafe" font-size="9">Manages VMs Lifecycle</text>
  </g>

  <!-- Neutron (Networking) -->
  <g transform="translate(205, 185)">
    <rect x="0" y="0" width="155" height="70" rx="8" fill="#059669"/>
    <text x="77" y="28" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">Neutron</text>
    <text x="77" y="48" text-anchor="middle" fill="#a7f3d0" font-size="11">Virtual Networking</text>
    <text x="77" y="62" text-anchor="middle" fill="#d1fae5" font-size="9">Subnets, Routers, Ports</text>
  </g>

  <!-- Glance (Image) -->
  <g transform="translate(380, 185)">
    <rect x="0" y="0" width="145" height="70" rx="8" fill="#d97706"/>
    <text x="72" y="28" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">Glance</text>
    <text x="72" y="48" text-anchor="middle" fill="#fef3c7" font-size="11">Image Registry</text>
    <text x="72" y="62" text-anchor="middle" fill="#fef9c3" font-size="9">VM Disk Images / OS</text>
  </g>

  <!-- Cinder (Block Storage) -->
  <g transform="translate(545, 185)">
    <rect x="0" y="0" width="155" height="70" rx="8" fill="#7c3aed"/>
    <text x="77" y="28" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">Cinder</text>
    <text x="77" y="48" text-anchor="middle" fill="#ede9fe" font-size="11">Block Storage</text>
    <text x="77" y="62" text-anchor="middle" fill="#f5f3ff" font-size="9">Persistent Disks for VMs</text>
  </g>

  <!-- Bottom Row: Swift, Heat, Octavia -->
  <g transform="translate(80, 275)">
    <rect x="0" y="0" width="170" height="60" rx="8" fill="#0891b2"/>
    <text x="85" y="25" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">Swift (Object Storage)</text>
    <text x="85" y="45" text-anchor="middle" fill="#cffafe" font-size="10">Unstructured Blobs & Backups</text>
  </g>

  <g transform="translate(285, 275)">
    <rect x="0" y="0" width="170" height="60" rx="8" fill="#ca8a04"/>
    <text x="85" y="25" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">Heat (Orchestration)</text>
    <text x="85" y="45" text-anchor="middle" fill="#fef08a" font-size="10">Template-based Automation</text>
  </g>

  <g transform="translate(490, 275)">
    <rect x="0" y="0" width="170" height="60" rx="8" fill="#4f46e5"/>
    <text x="85" y="25" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">Octavia (Load Balancer)</text>
    <text x="85" y="45" text-anchor="middle" fill="#c7d2fe" font-size="10">LBaaS Traffic Distribution</text>
  </g>

  <!-- Connective Arrows -->
  <path d="M 370 95 L 370 115" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4"/>
  <path d="M 370 160 L 112 185" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4"/>
  <path d="M 370 160 L 282 185" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4"/>
  <path d="M 370 160 L 452 185" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4"/>
  <path d="M 370 160 L 622 185" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4"/>
</svg>
"""

SVG_SDN = """
<svg viewBox="0 0 720 300" xmlns="http://www.w3.org/2000/svg" style="font-family: inherit;">
  <rect x="10" y="10" width="700" height="280" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="360" y="32" text-anchor="middle" fill="#38bdf8" font-size="16" font-weight="bold">Software-Defined Networking (SDN) 3-Tier Architecture</text>

  <!-- Layer 1: Application Layer -->
  <rect x="40" y="50" width="640" height="50" rx="8" fill="#0369a1"/>
  <text x="360" y="73" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">1. Application Layer (Network Applications & Business Logic)</text>
  <text x="360" y="90" text-anchor="middle" fill="#bae6fd" font-size="11">Firewall rules, QoS, Traffic engineering policies, Cloud management portal</text>

  <!-- Northbound API -->
  <rect x="260" y="108" width="200" height="22" rx="4" fill="#334155" stroke="#38bdf8"/>
  <text x="360" y="123" text-anchor="middle" fill="#38bdf8" font-size="10" font-weight="bold">Northbound REST APIs</text>

  <!-- Layer 2: Control Layer -->
  <rect x="40" y="138" width="640" height="52" rx="8" fill="#0284c7"/>
  <text x="360" y="162" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">2. Control Layer (SDN Controller - Central Intelligence Brain)</text>
  <text x="360" y="180" text-anchor="middle" fill="#e0f2fe" font-size="11">Maintains global network view, calculates shortest routing paths, installs flow rules</text>

  <!-- Southbound API -->
  <rect x="250" y="198" width="220" height="22" rx="4" fill="#334155" stroke="#10b981"/>
  <text x="360" y="213" text-anchor="middle" fill="#34d399" font-size="10" font-weight="bold">Southbound APIs (OpenFlow, NETCONF)</text>

  <!-- Layer 3: Infrastructure Layer -->
  <rect x="40" y="228" width="640" height="50" rx="8" fill="#0f766e"/>
  <text x="360" y="250" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">3. Infrastructure / Data Layer (Packet Forwarding Plane)</text>
  <text x="360" y="268" text-anchor="middle" fill="#ccfbf1" font-size="11">Physical & Virtual Switches, Routers, Hardware forwarding tables (no independent routing decisions)</text>
</svg>
"""

SVG_CIA_TRIAD = """
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="font-family: inherit;">
  <rect x="10" y="10" width="580" height="300" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="300" y="38" text-anchor="middle" fill="#38bdf8" font-size="17" font-weight="bold">The CIA Triad of Cloud Security</text>

  <!-- Central Circle -->
  <circle cx="300" cy="180" r="48" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
  <text x="300" y="178" text-anchor="middle" fill="#f8fafc" font-size="13" font-weight="bold">DATA</text>
  <text x="300" y="194" text-anchor="middle" fill="#38bdf8" font-size="11">SECURITY</text>

  <!-- Confidentiality (Top) -->
  <g transform="translate(180, 60)">
    <rect x="0" y="0" width="240" height="55" rx="8" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
    <text x="120" y="25" text-anchor="middle" fill="#bfdbfe" font-size="13" font-weight="bold">🔒 Confidentiality</text>
    <text x="120" y="43" text-anchor="middle" fill="#93c5fd" font-size="10">Encryption · Access Control · MFA</text>
  </g>

  <!-- Integrity (Bottom Left) -->
  <g transform="translate(30, 220)">
    <rect x="0" y="0" width="220" height="60" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
    <text x="110" y="26" text-anchor="middle" fill="#a7f3d0" font-size="13" font-weight="bold">🛡️ Integrity</text>
    <text x="110" y="44" text-anchor="middle" fill="#6ee7b7" font-size="10">SHA-256 Hashing · TLS · Digital Sigs</text>
  </g>

  <!-- Availability (Bottom Right) -->
  <g transform="translate(350, 220)">
    <rect x="0" y="0" width="220" height="60" rx="8" fill="#701a75" stroke="#ec4899" stroke-width="2"/>
    <text x="110" y="26" text-anchor="middle" fill="#fbcfe8" font-size="13" font-weight="bold">⚡ Availability</text>
    <text x="110" y="44" text-anchor="middle" fill="#f472b6" font-size="10">Redundancy · DDoS Shield · Auto-Scale</text>
  </g>

  <!-- Connecting Lines -->
  <line x1="300" y1="115" x2="300" y2="132" stroke="#38bdf8" stroke-width="2"/>
  <line x1="225" y1="195" x2="252" y2="188" stroke="#10b981" stroke-width="2"/>
  <line x1="375" y1="195" x2="348" y2="188" stroke="#ec4899" stroke-width="2"/>
</svg>
"""

SVG_IAM_EVAL = """
<svg viewBox="0 0 720 280" xmlns="http://www.w3.org/2000/svg" style="font-family: inherit;">
  <rect x="10" y="10" width="700" height="260" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <text x="360" y="34" text-anchor="middle" fill="#f59e0b" font-size="16" font-weight="bold">AWS IAM Policy Evaluation Logic Flow</text>

  <!-- Step 1: Default Deny -->
  <g transform="translate(30, 60)">
    <rect x="0" y="0" width="130" height="70" rx="8" fill="#334155" stroke="#64748b"/>
    <text x="65" y="28" text-anchor="middle" fill="#f8fafc" font-size="12" font-weight="bold">Step 1</text>
    <text x="65" y="48" text-anchor="middle" fill="#cbd5e1" font-size="11">Default State:</text>
    <text x="65" y="62" text-anchor="middle" fill="#ef4444" font-size="11" font-weight="bold">Implicit Deny</text>
  </g>

  <!-- Step 2: Explicit Deny Check -->
  <g transform="translate(200, 60)">
    <polygon points="70,0 140,45 70,90 0,45" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <text x="70" y="42" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">Is there an</text>
    <text x="70" y="56" text-anchor="middle" fill="#ef4444" font-size="11" font-weight="bold">Explicit DENY?</text>
  </g>

  <!-- Result: Denied (from Step 2) -->
  <g transform="translate(200, 185)">
    <rect x="15" y="0" width="110" height="55" rx="6" fill="#991b1b" stroke="#ef4444"/>
    <text x="70" y="25" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">ACCESS</text>
    <text x="70" y="44" text-anchor="middle" fill="#fecaca" font-size="13" font-weight="bold">DENIED ❌</text>
  </g>

  <!-- Step 3: Explicit Allow Check -->
  <g transform="translate(390, 60)">
    <polygon points="70,0 140,45 70,90 0,45" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="70" y="42" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">Is there an</text>
    <text x="70" y="56" text-anchor="middle" fill="#10b981" font-size="11" font-weight="bold">Explicit ALLOW?</text>
  </g>

  <!-- Result: Allowed (from Step 3 Yes) -->
  <g transform="translate(570, 75)">
    <rect x="0" y="0" width="120" height="55" rx="6" fill="#065f46" stroke="#10b981"/>
    <text x="60" y="25" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">ACCESS</text>
    <text x="60" y="44" text-anchor="middle" fill="#a7f3d0" font-size="13" font-weight="bold">ALLOWED ✔️</text>
  </g>

  <!-- Result: Denied (from Step 3 No - back to default deny) -->
  <g transform="translate(405, 185)">
    <rect x="0" y="0" width="110" height="55" rx="6" fill="#991b1b" stroke="#ef4444"/>
    <text x="55" y="25" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">ACCESS</text>
    <text x="55" y="44" text-anchor="middle" fill="#fecaca" font-size="13" font-weight="bold">DENIED ❌</text>
  </g>

  <!-- Connectors -->
  <path d="M 160 95 L 200 95" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>
  <path d="M 270 150 L 270 185" stroke="#ef4444" stroke-width="2"/>
  <text x="280" y="170" fill="#ef4444" font-size="11" font-weight="bold">YES</text>

  <path d="M 340 105 L 390 105" stroke="#94a3b8" stroke-width="2"/>
  <text x="360" y="98" fill="#94a3b8" font-size="11">NO</text>

  <path d="M 530 105 L 570 105" stroke="#10b981" stroke-width="2"/>
  <text x="545" y="98" fill="#10b981" font-size="11" font-weight="bold">YES</text>

  <path d="M 460 150 L 460 185" stroke="#ef4444" stroke-width="2"/>
  <text x="470" y="170" fill="#ef4444" font-size="11">NO</text>
</svg>
"""

SVG_PIZZA = """
<svg viewBox="0 0 740 280" xmlns="http://www.w3.org/2000/svg" style="font-family: inherit;">
  <rect x="10" y="10" width="720" height="260" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="370" y="32" text-anchor="middle" fill="#38bdf8" font-size="15" font-weight="bold">"Pizza-as-a-Service" Analogy (Cloud Service Models)</text>

  <!-- Column 1: On-Premises -->
  <g transform="translate(30, 50)">
    <rect x="0" y="0" width="150" height="205" rx="8" fill="#0f172a" stroke="#64748b"/>
    <text x="75" y="24" text-anchor="middle" fill="#f8fafc" font-size="12" font-weight="bold">Traditional On-Prem</text>
    <text x="75" y="38" text-anchor="middle" fill="#94a3b8" font-size="10">"Made at Home"</text>
    
    <rect x="10" y="48" width="130" height="145" rx="6" fill="#1e3a8a"/>
    <text x="75" y="68" text-anchor="middle" fill="#bfdbfe" font-size="10">Dining Table (You)</text>
    <text x="75" y="85" text-anchor="middle" fill="#bfdbfe" font-size="10">Soda & Drinks (You)</text>
    <text x="75" y="102" text-anchor="middle" fill="#bfdbfe" font-size="10">Gas & Oven (You)</text>
    <text x="75" y="119" text-anchor="middle" fill="#bfdbfe" font-size="10">Pizza Dough (You)</text>
    <text x="75" y="136" text-anchor="middle" fill="#bfdbfe" font-size="10">Tomato Sauce (You)</text>
    <text x="75" y="153" text-anchor="middle" fill="#bfdbfe" font-size="10">Toppings (You)</text>
    <text x="75" y="170" text-anchor="middle" fill="#bfdbfe" font-size="10">Cheese (You)</text>
    <text x="75" y="185" text-anchor="middle" fill="#38bdf8" font-size="9" font-weight="bold">YOU MANAGE ALL 100%</text>
  </g>

  <!-- Column 2: IaaS -->
  <g transform="translate(200, 50)">
    <rect x="0" y="0" width="150" height="205" rx="8" fill="#0f172a" stroke="#38bdf8"/>
    <text x="75" y="24" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">IaaS (EC2 / VMs)</text>
    <text x="75" y="38" text-anchor="middle" fill="#94a3b8" font-size="10">"Take and Bake"</text>
    
    <rect x="10" y="48" width="130" height="65" rx="4" fill="#1e3a8a"/>
    <text x="75" y="68" text-anchor="middle" fill="#bfdbfe" font-size="10">Dining Table (You)</text>
    <text x="75" y="85" text-anchor="middle" fill="#bfdbfe" font-size="10">Drinks (You)</text>
    <text x="75" y="102" text-anchor="middle" fill="#bfdbfe" font-size="10">Oven (You)</text>

    <rect x="10" y="118" width="130" height="75" rx="4" fill="#0284c7"/>
    <text x="75" y="136" text-anchor="middle" fill="#ffffff" font-size="10">Dough (Vendor)</text>
    <text x="75" y="153" text-anchor="middle" fill="#ffffff" font-size="10">Sauce (Vendor)</text>
    <text x="75" y="170" text-anchor="middle" fill="#ffffff" font-size="10">Cheese (Vendor)</text>
    <text x="75" y="185" text-anchor="middle" fill="#e0f2fe" font-size="9" font-weight="bold">VENDOR: HW & HYPERVISOR</text>
  </g>

  <!-- Column 3: PaaS -->
  <g transform="translate(370, 50)">
    <rect x="0" y="0" width="150" height="205" rx="8" fill="#0f172a" stroke="#10b981"/>
    <text x="75" y="24" text-anchor="middle" fill="#10b981" font-size="12" font-weight="bold">PaaS (Beanstalk/GAE)</text>
    <text x="75" y="38" text-anchor="middle" fill="#94a3b8" font-size="10">"Pizza Delivered"</text>

    <rect x="10" y="48" width="130" height="42" rx="4" fill="#1e3a8a"/>
    <text x="75" y="66" text-anchor="middle" fill="#bfdbfe" font-size="10">Dining Table (You)</text>
    <text x="75" y="82" text-anchor="middle" fill="#bfdbfe" font-size="10">Drinks (You)</text>

    <rect x="10" y="95" width="130" height="98" rx="4" fill="#059669"/>
    <text x="75" y="115" text-anchor="middle" fill="#ffffff" font-size="10">Delivered Hot (Vendor)</text>
    <text x="75" y="132" text-anchor="middle" fill="#ffffff" font-size="10">Cooked Oven (Vendor)</text>
    <text x="75" y="149" text-anchor="middle" fill="#ffffff" font-size="10">Dough & Cheese (Vendor)</text>
    <text x="75" y="166" text-anchor="middle" fill="#ffffff" font-size="10">OS & Runtime (Vendor)</text>
    <text x="75" y="185" text-anchor="middle" fill="#d1fae5" font-size="9" font-weight="bold">YOU MANAGE CODE ONLY</text>
  </g>

  <!-- Column 4: SaaS -->
  <g transform="translate(540, 50)">
    <rect x="0" y="0" width="150" height="205" rx="8" fill="#0f172a" stroke="#a855f7"/>
    <text x="75" y="24" text-anchor="middle" fill="#a855f7" font-size="12" font-weight="bold">SaaS (M365/Docs)</text>
    <text x="75" y="38" text-anchor="middle" fill="#94a3b8" font-size="10">"Dining Out"</text>

    <rect x="10" y="48" width="130" height="145" rx="6" fill="#7c3aed"/>
    <text x="75" y="70" text-anchor="middle" fill="#ffffff" font-size="10">Restaurant Table (Vendor)</text>
    <text x="75" y="88" text-anchor="middle" fill="#ffffff" font-size="10">Drinks & Service (Vendor)</text>
    <text x="75" y="106" text-anchor="middle" fill="#ffffff" font-size="10">Kitchen & Oven (Vendor)</text>
    <text x="75" y="124" text-anchor="middle" fill="#ffffff" font-size="10">Pizza & Toppings (Vendor)</text>
    <text x="75" y="142" text-anchor="middle" fill="#ffffff" font-size="10">All App & Data (Vendor)</text>
    <text x="75" y="160" text-anchor="middle" fill="#ffffff" font-size="10">Software & DB (Vendor)</text>
    <text x="75" y="185" text-anchor="middle" fill="#f5f3ff" font-size="9" font-weight="bold">VENDOR MANAGES ALL 100%</text>
  </g>
</svg>
"""

# ==================== NEW UNIT 3 ARCHITECTURAL SVGS ====================

SVG_DEPLOYMENT_MODELS = """
<svg viewBox="0 0 740 330" xmlns="http://www.w3.org/2000/svg" style="font-family: inherit;">
  <rect x="10" y="10" width="720" height="310" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="370" y="34" text-anchor="middle" fill="#38bdf8" font-size="16" font-weight="bold">The 4 Cloud Deployment Models & Hybrid Cloud Bursting</text>

  <!-- Public Cloud Box -->
  <g transform="translate(30, 55)">
    <rect x="0" y="0" width="150" height="240" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="10" y="12" width="130" height="32" rx="6" fill="#0284c7"/>
    <text x="75" y="32" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">Public Cloud</text>
    <text x="75" y="65" text-anchor="middle" fill="#94a3b8" font-size="10">Owned by 3rd Party</text>
    <text x="75" y="80" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">AWS / Azure / GCP</text>
    
    <rect x="15" y="95" width="120" height="60" rx="6" fill="#1e293b"/>
    <text x="75" y="115" text-anchor="middle" fill="#f8fafc" font-size="10">Multi-Tenant</text>
    <text x="75" y="132" text-anchor="middle" fill="#cbd5e1" font-size="9">Shared Hardware</text>
    <text x="75" y="145" text-anchor="middle" fill="#38bdf8" font-size="9">Pay-as-you-go</text>

    <rect x="15" y="165" width="120" height="60" rx="6" fill="#0369a1"/>
    <text x="75" y="185" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">Target Audience</text>
    <text x="75" y="200" text-anchor="middle" fill="#e0f2fe" font-size="9">Startups, Netflix, Spotify</text>
    <text x="75" y="213" text-anchor="middle" fill="#bae6fd" font-size="8">Infinite Scalability</text>
  </g>

  <!-- Private Cloud Box -->
  <g transform="translate(200, 55)">
    <rect x="0" y="0" width="150" height="240" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="10" y="12" width="130" height="32" rx="6" fill="#7c3aed"/>
    <text x="75" y="32" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">Private Cloud</text>
    <text x="75" y="65" text-anchor="middle" fill="#94a3b8" font-size="10">Dedicated to 1 Org</text>
    <text x="75" y="80" text-anchor="middle" fill="#a855f7" font-size="11" font-weight="bold">OpenStack / VMware</text>

    <rect x="15" y="95" width="120" height="60" rx="6" fill="#1e293b"/>
    <text x="75" y="115" text-anchor="middle" fill="#f8fafc" font-size="10">Single-Tenant</text>
    <text x="75" y="132" text-anchor="middle" fill="#cbd5e1" font-size="9">Total Data Privacy</text>
    <text x="75" y="145" text-anchor="middle" fill="#a855f7" font-size="9">Heavy CapEx</text>

    <rect x="15" y="165" width="120" height="60" rx="6" fill="#6d28d9"/>
    <text x="75" y="185" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">Target Audience</text>
    <text x="75" y="200" text-anchor="middle" fill="#ede9fe" font-size="9">UIDAI Aadhaar, Banks</text>
    <text x="75" y="213" text-anchor="middle" fill="#ddd6fe" font-size="8">Defense / High Compliance</text>
  </g>

  <!-- Hybrid Cloud Box -->
  <g transform="translate(370, 55)">
    <rect x="0" y="0" width="165" height="240" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect x="10" y="12" width="145" height="32" rx="6" fill="#059669"/>
    <text x="82" y="32" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">Hybrid Cloud</text>
    <text x="82" y="65" text-anchor="middle" fill="#94a3b8" font-size="10">Private + Public Bound</text>
    <text x="82" y="80" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">VPN / Direct Connect</text>

    <rect x="15" y="95" width="135" height="60" rx="6" fill="#1e293b"/>
    <text x="82" y="115" text-anchor="middle" fill="#f8fafc" font-size="10">Data Portability</text>
    <text x="82" y="130" text-anchor="middle" fill="#cbd5e1" font-size="9">Sensitive Data on-prem</text>
    <text x="82" y="145" text-anchor="middle" fill="#10b981" font-size="9" font-weight="bold">Cloud Bursting Surge</text>

    <rect x="15" y="165" width="135" height="60" rx="6" fill="#047857"/>
    <text x="82" y="185" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">Target Audience</text>
    <text x="82" y="200" text-anchor="middle" fill="#d1fae5" font-size="9">Enterprises with legacy</text>
    <text x="82" y="213" text-anchor="middle" fill="#a7f3d0" font-size="8">Gradual cloud migration</text>
  </g>

  <!-- Community Cloud Box -->
  <g transform="translate(555, 55)">
    <rect x="0" y="0" width="155" height="240" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="10" y="12" width="135" height="32" rx="6" fill="#d97706"/>
    <text x="77" y="32" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">Community Cloud</text>
    <text x="77" y="65" text-anchor="middle" fill="#94a3b8" font-size="10">Shared by Domain Orgs</text>
    <text x="77" y="80" text-anchor="middle" fill="#f59e0b" font-size="11" font-weight="bold">Shared Requirements</text>

    <rect x="15" y="95" width="125" height="60" rx="6" fill="#1e293b"/>
    <text x="77" y="115" text-anchor="middle" fill="#f8fafc" font-size="10">Cost Sharing</text>
    <text x="77" y="132" text-anchor="middle" fill="#cbd5e1" font-size="9">Joint Governance</text>
    <text x="77" y="145" text-anchor="middle" fill="#fbbf24" font-size="9">Shared Compliance</text>

    <rect x="15" y="165" width="125" height="60" rx="6" fill="#b45309"/>
    <text x="77" y="185" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">Target Audience</text>
    <text x="77" y="200" text-anchor="middle" fill="#fef3c7" font-size="9">Gov Agencies, Hospitals</text>
    <text x="77" y="213" text-anchor="middle" fill="#fde68a" font-size="8">University Research Labs</text>
  </g>
</svg>
"""

SVG_MULTI_TENANT_PATTERNS = """
<svg viewBox="0 0 740 310" xmlns="http://www.w3.org/2000/svg" style="font-family: inherit;">
  <rect x="10" y="10" width="720" height="290" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="370" y="34" text-anchor="middle" fill="#38bdf8" font-size="16" font-weight="bold">Multi-Tenant Database Isolation Patterns (Pool vs Bridge vs Silo)</text>

  <!-- Pattern 1: Pool Pattern -->
  <g transform="translate(30, 55)">
    <rect x="0" y="0" width="205" height="225" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="10" y="12" width="185" height="28" rx="4" fill="#0284c7"/>
    <text x="102" y="30" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">1. Pool (Shared DB/Table)</text>

    <rect x="15" y="50" width="175" height="85" rx="4" fill="#1e293b" stroke="#475569"/>
    <text x="102" y="70" text-anchor="middle" fill="#38bdf8" font-size="10" font-weight="bold">Single Shared Table</text>
    <text x="102" y="88" text-anchor="middle" fill="#94a3b8" font-size="9">Row 1: [tenant_1, Rahul, Ahmd]</text>
    <text x="102" y="104" text-anchor="middle" fill="#94a3b8" font-size="9">Row 2: [tenant_2, Priya, Vado]</text>
    <text x="102" y="120" text-anchor="middle" fill="#94a3b8" font-size="9">Row 3: [tenant_1, Amit, Surat]</text>

    <rect x="15" y="145" width="175" height="70" rx="4" fill="#0369a1"/>
    <text x="102" y="165" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">Evaluation</text>
    <text x="102" y="180" text-anchor="middle" fill="#e0f2fe" font-size="9">Cost: Lowest | Isolation: Low</text>
    <text x="102" y="195" text-anchor="middle" fill="#bae6fd" font-size="8">Isolation via Row-Level Security</text>
  </g>

  <!-- Pattern 2: Bridge Pattern -->
  <g transform="translate(265, 55)">
    <rect x="0" y="0" width="205" height="225" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect x="10" y="12" width="185" height="28" rx="4" fill="#059669"/>
    <text x="102" y="30" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">2. Bridge (Separate Schemas)</text>

    <rect x="15" y="50" width="175" height="85" rx="4" fill="#1e293b" stroke="#475569"/>
    <text x="102" y="68" text-anchor="middle" fill="#34d399" font-size="10" font-weight="bold">Shared DB Engine</text>
    <rect x="25" y="76" width="155" height="22" rx="3" fill="#064e3b"/>
    <text x="102" y="91" text-anchor="middle" fill="#a7f3d0" font-size="9">Schema_Tenant_A (Tables)</text>
    <rect x="25" y="103" width="155" height="22" rx="3" fill="#064e3b"/>
    <text x="102" y="118" text-anchor="middle" fill="#a7f3d0" font-size="9">Schema_Tenant_B (Tables)</text>

    <rect x="15" y="145" width="175" height="70" rx="4" fill="#047857"/>
    <text x="102" y="165" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">Evaluation</text>
    <text x="102" y="180" text-anchor="middle" fill="#d1fae5" font-size="9">Cost: Moderate | Isolation: Medium</text>
    <text x="102" y="195" text-anchor="middle" fill="#a7f3d0" font-size="8">Good balance for standard SaaS</text>
  </g>

  <!-- Pattern 3: Silo Pattern -->
  <g transform="translate(500, 55)">
    <rect x="0" y="0" width="205" height="225" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="10" y="12" width="185" height="28" rx="4" fill="#7c3aed"/>
    <text x="102" y="30" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">3. Silo (Database-per-Tenant)</text>

    <rect x="15" y="50" width="175" height="85" rx="4" fill="#1e293b" stroke="#475569"/>
    <rect x="25" y="58" width="155" height="32" rx="4" fill="#581c87"/>
    <text x="102" y="75" text-anchor="middle" fill="#f3e8ff" font-size="9" font-weight="bold">DB_Instance_Tenant_A</text>
    <rect x="25" y="96" width="155" height="32" rx="4" fill="#581c87"/>
    <text x="102" y="113" text-anchor="middle" fill="#f3e8ff" font-size="9" font-weight="bold">DB_Instance_Tenant_B</text>

    <rect x="15" y="145" width="175" height="70" rx="4" fill="#6d28d9"/>
    <text x="102" y="165" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">Evaluation</text>
    <text x="102" y="180" text-anchor="middle" fill="#ede9fe" font-size="9">Cost: Highest | Isolation: Maximum</text>
    <text x="102" y="195" text-anchor="middle" fill="#ddd6fe" font-size="8">For Banks & Gov (Zero Leakage)</text>
  </g>
</svg>
"""

SVG_THREE_TIER_ARCHITECTURE = """
<svg viewBox="0 0 740 320" xmlns="http://www.w3.org/2000/svg" style="font-family: inherit;">
  <rect x="10" y="10" width="720" height="300" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="370" y="34" text-anchor="middle" fill="#38bdf8" font-size="16" font-weight="bold">Multi-Server 3-Tier Enterprise Web Architecture</text>

  <!-- Client Devices -->
  <g transform="translate(30, 60)">
    <rect x="0" y="0" width="110" height="225" rx="8" fill="#0f172a" stroke="#64748b"/>
    <text x="55" y="30" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">Clients</text>
    <rect x="10" y="50" width="90" height="35" rx="4" fill="#1e293b"/>
    <text x="55" y="72" text-anchor="middle" fill="#f8fafc" font-size="10">Browsers</text>
    <rect x="10" y="95" width="90" height="35" rx="4" fill="#1e293b"/>
    <text x="55" y="117" text-anchor="middle" fill="#f8fafc" font-size="10">Mobile Apps</text>
    <rect x="10" y="140" width="90" height="35" rx="4" fill="#1e293b"/>
    <text x="55" y="162" text-anchor="middle" fill="#f8fafc" font-size="10">IoT / APIs</text>
    <text x="55" y="200" text-anchor="middle" fill="#94a3b8" font-size="9">HTTPS :443</text>
  </g>

  <!-- Load Balancer -->
  <g transform="translate(170, 115)">
    <rect x="0" y="0" width="105" height="110" rx="8" fill="#e11d48"/>
    <text x="52" y="30" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">Elastic LB</text>
    <text x="52" y="50" text-anchor="middle" fill="#ffe4e6" font-size="9">Layer 7 / Layer 4</text>
    <text x="52" y="70" text-anchor="middle" fill="#ffffff" font-size="9">Round Robin</text>
    <text x="52" y="85" text-anchor="middle" fill="#ffffff" font-size="9">Health Checks</text>
  </g>

  <!-- Tier 1: Web Tier -->
  <g transform="translate(305, 55)">
    <rect x="0" y="0" width="115" height="235" rx="8" fill="#0f172a" stroke="#0284c7"/>
    <text x="57" y="25" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Tier 1: Web Tier</text>
    <rect x="10" y="40" width="95" height="48" rx="4" fill="#0369a1"/>
    <text x="57" y="62" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">Web Server 1</text>
    <text x="57" y="78" text-anchor="middle" fill="#bae6fd" font-size="8">Nginx / SSL</text>

    <rect x="10" y="98" width="95" height="48" rx="4" fill="#0369a1"/>
    <text x="57" y="120" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">Web Server 2</text>
    <text x="57" y="136" text-anchor="middle" fill="#bae6fd" font-size="8">Nginx / SSL</text>

    <rect x="10" y="156" width="95" height="48" rx="4" fill="#0369a1"/>
    <text x="57" y="178" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">Web Server 3</text>
    <text x="57" y="194" text-anchor="middle" fill="#bae6fd" font-size="8">Auto-Scaled</text>
  </g>

  <!-- Tier 2: App Tier -->
  <g transform="translate(450, 55)">
    <rect x="0" y="0" width="115" height="235" rx="8" fill="#0f172a" stroke="#10b981"/>
    <text x="57" y="25" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">Tier 2: App Tier</text>
    <rect x="10" y="40" width="95" height="48" rx="4" fill="#059669"/>
    <text x="57" y="62" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">App Worker 1</text>
    <text x="57" y="78" text-anchor="middle" fill="#d1fae5" font-size="8">Business Logic</text>

    <rect x="10" y="98" width="95" height="48" rx="4" fill="#059669"/>
    <text x="57" y="120" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">App Worker 2</text>
    <text x="57" y="136" text-anchor="middle" fill="#d1fae5" font-size="8">Business Logic</text>

    <rect x="10" y="156" width="95" height="48" rx="4" fill="#047857"/>
    <text x="57" y="178" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">Redis Cache</text>
    <text x="57" y="194" text-anchor="middle" fill="#a7f3d0" font-size="8">Session Store</text>
  </g>

  <!-- Tier 3: Data Tier -->
  <g transform="translate(595, 55)">
    <rect x="0" y="0" width="120" height="235" rx="8" fill="#0f172a" stroke="#a855f7"/>
    <text x="60" y="25" text-anchor="middle" fill="#c084fc" font-size="11" font-weight="bold">Tier 3: Data Tier</text>
    
    <rect x="10" y="45" width="100" height="65" rx="4" fill="#7c3aed"/>
    <text x="60" y="70" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">Primary DB</text>
    <text x="60" y="86" text-anchor="middle" fill="#ede9fe" font-size="8">Read / Write Master</text>
    <text x="60" y="98" text-anchor="middle" fill="#ddd6fe" font-size="8">(PostgreSQL/MySQL)</text>

    <rect x="10" y="135" width="100" height="65" rx="4" fill="#581c87"/>
    <text x="60" y="160" text-anchor="middle" fill="#f3e8ff" font-size="10" font-weight="bold">Replica DB</text>
    <text x="60" y="176" text-anchor="middle" fill="#e9d5ff" font-size="8">Read-Only Slave</text>
    <text x="60" y="188" text-anchor="middle" fill="#d8b4fe" font-size="8">Async Replication</text>
  </g>

  <!-- Connecting Lines -->
  <line x1="140" y1="170" x2="170" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <line x1="275" y1="170" x2="305" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <line x1="420" y1="170" x2="450" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <line x1="565" y1="170" x2="595" y2="170" stroke="#94a3b8" stroke-width="2"/>
</svg>
"""
