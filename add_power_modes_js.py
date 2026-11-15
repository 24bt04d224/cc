# -*- coding: utf-8 -*-
import os

POWER_MODES_JS = r'''

// ==============================================================================
// EXAM POWER MODES DATA & ENGINE
// 1) Random Topic Shuffler
// 2) IMP Topics Filter
// 3) Cross-Chapter Question Roulette
// ==============================================================================

const ALL_TOPICS_POOL = [
  // --- Unit 4: Virtualization (25% Marks) ---
  {
    unit: 'unit4',
    unitName: 'Unit 4: Virtualization Technologies',
    marks: '7 Marks Expected',
    yieldTag: '🔥 Top Exam Guaranteed',
    title: 'Type 1 (Bare-Metal) vs Type 2 (Hosted) Hypervisors',
    summary: 'Type 1 (Bare-Metal, e.g., ESXi, Hyper-V, KVM) runs directly on the bare server hardware without a host OS, providing raw near-native speed, low latency, and robust isolation. Type 2 (Hosted, e.g., VirtualBox, VMware Workstation) runs as a software application on top of a host OS (Windows/Linux), suffering double OS switching overhead and dependency on host kernel stability.',
    analogy: 'Type 1 is like an apartment building built straight from the ground up for renting. Type 2 is like renting out bedrooms inside a leased family home.',
    googleQuery: 'Type 1 vs Type 2 Hypervisor Architecture Diagram',
    unitTabId: 'unit4'
  },
  {
    unit: 'unit4',
    unitName: 'Unit 4: Virtualization Technologies',
    marks: '7 Marks Expected',
    yieldTag: '🔥 High-Yield Priority',
    title: 'Hypervisor Core Modules: Dispatcher, Allocator & Interpreter',
    summary: 'A hypervisor executes three core tasks: 1) Dispatcher: intercepts trap instructions from guest OS and decides whether to allocate or interpret them. 2) Allocator: assigns physical hardware resources (CPU, RAM blocks) to requesting VMs without memory collisions. 3) Interpreter / Executor: emulates sensitive unprivileged instructions that cannot safely execute directly on hardware.',
    analogy: 'Dispatcher is the traffic cop; Allocator is the parking attendant reserving slots; Interpreter is the diplomatic translator.',
    googleQuery: 'Hypervisor Dispatcher Allocator Interpreter Architecture Diagram',
    unitTabId: 'unit4'
  },
  {
    unit: 'unit4',
    unitName: 'Unit 4: Virtualization Technologies',
    marks: '7 / 10 Marks Expected',
    yieldTag: '🔥 Top Exam Guaranteed',
    title: 'Virtual Machines vs Docker Containers (Hardware vs OS Virtualization)',
    summary: 'VMs virtualize the underlying hardware using a hypervisor, requiring a full guest OS per instance (~GBs) and booting in minutes. Containers virtualize the host OS kernel using Linux namespaces and cgroups, sharing the host kernel with minimal footprint (~MBs) and launching in milliseconds. VMs offer strong hardware-level isolation; containers offer 5-10x higher server density.',
    analogy: 'A VM is an independent standalone house with its own plumbing, electrical wiring, and roof. A Container is an apartment unit in a high-rise sharing central plumbing and building utilities.',
    googleQuery: 'Docker Containers vs Virtual Machines Architecture Diagram',
    unitTabId: 'unit4'
  },
  {
    unit: 'unit4',
    unitName: 'Unit 4: Virtualization Technologies',
    marks: '10 Marks Expected',
    yieldTag: '🔥 High-Yield Priority',
    title: 'OpenStack 9 Core Components Architecture',
    summary: 'OpenStack is an open-source cloud operating system. Key components: Nova (Compute provisioning), Keystone (Identity and Auth tokens), Neutron (SDN networking and IP routing), Glance (VM image catalog), Cinder (Persistent block volumes), Swift (Distributed object storage), Horizon (Web dashboard GUI), Heat (Template orchestration), Ceilometer (Telemetry and usage metering).',
    analogy: 'Nova is the factory; Keystone is the security badge reader; Neutron is the courier delivery network; Glance is the blueprint catalog; Horizon is the manager executive desk.',
    googleQuery: 'OpenStack Architecture Nova Neutron Keystone Glance Diagram',
    unitTabId: 'unit4'
  },
  {
    unit: 'unit4',
    unitName: 'Unit 4: Virtualization Technologies',
    marks: '7 Marks Expected',
    yieldTag: '⭐ Medium-High Yield',
    title: 'Apache CloudStack 4-Level Physical Hierarchy',
    summary: 'CloudStack organizes physical infrastructure into 4 strict hierarchical tiers: 1) Zone: Largest unit, corresponding to an entire data center with power and networking. 2) Pod: A single rack of hardware containing one or more clusters. 3) Cluster: A set of homogeneous hypervisor hosts sharing primary storage. 4) Host: A single physical server running a hypervisor (KVM/Xen/ESXi).',
    analogy: 'Zone = University Campus; Pod = Engineering Building; Cluster = Computer Science Department floor; Host = Individual Workstation Desk.',
    googleQuery: 'Apache CloudStack Zone Pod Cluster Host Physical Hierarchy Diagram',
    unitTabId: 'unit4'
  },
  {
    unit: 'unit4',
    unitName: 'Unit 4: Virtualization Technologies',
    marks: '7 Marks Expected',
    yieldTag: '🔥 High-Yield Priority',
    title: 'Cloud Storage Comparison: Block vs Object vs File Storage',
    summary: 'Block Storage (AWS EBS) splits data into fixed addressable blocks, ideal for OS boot drives and high-IOPS transactional databases. Object Storage (AWS S3) stores immutable objects with metadata in a flat namespace accessed via HTTP REST APIs, offering limitless scale for data lakes and media. File Storage (AWS EFS) provides hierarchical directory trees over standard NFS/SMB protocols for concurrent multi-server access.',
    analogy: 'Block = Fixed-sized cargo shipping containers; Object = Valet parking with a claim ticket ID; File = Traditional office filing cabinet with folders inside drawers.',
    googleQuery: 'Block vs File vs Object Storage Cloud Diagram',
    unitTabId: 'unit4'
  },
  {
    unit: 'unit4',
    unitName: 'Unit 4: Virtualization Technologies',
    marks: '7 Marks Expected',
    yieldTag: '🔥 High-Yield Priority',
    title: 'Software-Defined Networking (SDN) 3-Plane Architecture & OpenFlow',
    summary: 'SDN decouples the network control logic (Control Plane) from packet forwarding hardware (Data Plane). 1) Application Plane: network services and firewall logic. 2) Control Plane: centralized SDN controller (the brain) managing routing tables via Northbound REST APIs. 3) Data Plane: dumb hardware switches executing packet forwarding via Southbound OpenFlow protocol.',
    analogy: 'Control Plane is air traffic control at the airport tower directing planes. Data Plane is the runways and planes actually moving along the assigned flight paths.',
    googleQuery: 'Software Defined Networking SDN Architecture Three Layers Diagram',
    unitTabId: 'unit4'
  },
  {
    unit: 'unit4',
    unitName: 'Unit 4: Virtualization Technologies',
    marks: '5 / 7 Marks Expected',
    yieldTag: '⭐ Core Concept',
    title: 'Content Delivery Network (CDN) & Edge Caching',
    summary: 'A CDN is a geographically distributed network of Point of Presence (PoP) edge servers that cache static and streaming web assets close to users. By serving content from the nearest edge node instead of the origin server, CDNs drastically reduce latency, absorb DDoS attack traffic, and lower origin egress bandwidth costs.',
    analogy: 'Instead of flying to Italy every time you want authentic pizza, your local neighborhood pizzeria serves the exact recipe under 10 minutes.',
    googleQuery: 'CDN Content Delivery Network Edge Caching Architecture Diagram',
    unitTabId: 'unit4'
  },
  {
    unit: 'unit4',
    unitName: 'Unit 4: Virtualization Technologies',
    marks: '5 Marks Expected',
    yieldTag: '⭐ Core Concept',
    title: 'Popek-Goldberg Virtualization Requirements Theorem',
    summary: 'Popek-Goldberg states that a computer architecture is strictly virtualizable if and only if all sensitive instructions (instructions that expose or modify hardware state) are a subset of privileged instructions (instructions that trap when executed in user mode). Classic x86 architecture violated this rule with 17 non-faulting sensitive instructions, necessitating binary translation until Intel VT-x and AMD-V added hardware virtualization rings.',
    analogy: 'A secure VIP party is only virtualizable if every time an unauthorized guest touches the master sound switch, the alarm immediately sounds and security intercepts them.',
    googleQuery: 'Popek Goldberg Virtualization Requirements Ring Architecture Diagram',
    unitTabId: 'unit4'
  },

  // --- Unit 5: Security & IAM (25% Marks) ---
  {
    unit: 'unit5',
    unitName: 'Unit 5: Cloud Security & IAM',
    marks: '7 Marks Expected',
    yieldTag: '🔥 Top Exam Guaranteed',
    title: 'The CIA Security Triad in Cloud Computing',
    summary: 'Confidentiality ensures sensitive customer data is shielded from unauthorized access (AES-256 encryption at rest, TLS 1.3 in transit, IAM RBAC). Integrity guarantees data remains unchanged and tamper-free (cryptographic hashes, SHA-256 digital signatures, S3 Object Lock WORM). Availability guarantees authorized users uninterrupted access to services (Multi-AZ clustering, automated failover, DDoS mitigation with AWS Shield).',
    analogy: 'Confidentiality = Locked bank vault; Integrity = Wax wax-sealed tamper-evident envelope; Availability = 24/7 drive-through ATM access.',
    googleQuery: 'CIA Triad Information Security Cloud Computing Diagram',
    unitTabId: 'unit5'
  },
  {
    unit: 'unit5',
    unitName: 'Unit 5: Cloud Security & IAM',
    marks: '7 Marks Expected',
    yieldTag: '🔥 Top Exam Guaranteed',
    title: 'AWS IAM Policy Evaluation Logic & The Explicit Deny Rule',
    summary: 'AWS IAM evaluates requests using a strict 3-step decision flow: 1) Default decision is implicit DENY. 2) If ANY evaluated policy contains an explicit "Effect": "Deny", access is IMMEDIATELY and UNCONDITIONALLY DENIED (Explicit Deny overrides all allows). 3) If no explicit deny exists, there must be at least one explicit "Effect": "Allow" to grant access; otherwise it defaults to deny.',
    analogy: 'A security guard has a VIP guest list. If your name is on the VIP list (Allow) you enter. But if the club owner posted your photo on the banned board (Explicit Deny), you are rejected immediately, even with a VIP ticket.',
    googleQuery: 'AWS IAM Policy Evaluation Logic Flowchart Diagram',
    unitTabId: 'unit5'
  },
  {
    unit: 'unit5',
    unitName: 'Unit 5: Cloud Security & IAM',
    marks: '7 Marks Expected',
    yieldTag: '🔥 High-Yield Priority',
    title: 'AWS IAM Four Core Entities: Users, Groups, Roles & Policies',
    summary: '1) Users: Persistent identity representations for individuals with long-term credentials. 2) Groups: Collections of users sharing identical job privileges. 3) Roles: Temporary assumed identities for trusted AWS services or federated identities, using temporary STS security tokens. 4) Policies: Formal JSON documents defining Allow/Deny permissions over specific AWS ARN resources.',
    analogy: 'User = An employee with a personal name badge; Group = The Finance Department team; Role = An emergency firefighter master key card handed out for 1 hour; Policy = The building rules handbook.',
    googleQuery: 'AWS IAM Users Groups Roles Policies Relationship Diagram',
    unitTabId: 'unit5'
  },
  {
    unit: 'unit5',
    unitName: 'Unit 5: Cloud Security & IAM',
    marks: '7 Marks Expected',
    yieldTag: '🔥 High-Yield Priority',
    title: 'Scalability vs Elasticity (Formulas & Cloud Triggers)',
    summary: 'Scalability is the structural ability of a system to handle sustained growing workload by adding resources over time (Vertical Scale-Up or Horizontal Scale-Out). Elasticity is the dynamic, real-time autonomous ability to provision and de-provision cloud resources matching immediate burst spikes and drops. Elasticity formula: Speed of provisioning + decommissioning proportional to workload change.',
    analogy: 'Scalability is expanding a two-lane highway to an eight-lane highway to prepare for a growing city over 5 years. Elasticity is an accordion or rubber band expanding during rush hour and contracting at 2 AM.',
    googleQuery: 'Cloud Scalability vs Elasticity Comparison Diagram',
    unitTabId: 'unit5'
  },
  {
    unit: 'unit5',
    unitName: 'Unit 5: Cloud Security & IAM',
    marks: '10 Marks Expected',
    yieldTag: '🔥 Top Exam Guaranteed',
    title: 'Cloud Security Incident Analysis: Capital One SSRF Breach',
    summary: 'In 2019, an attacker exploited a Server-Side Request Forgery (SSRF) flaw in a misconfigured ModSecurity WAF EC2 instance. The attacker queried the AWS Instance Metadata Service v1 (169.254.169.254) to extract temporary IAM role credentials assigned to the WAF. Because the role had over-permissive broad S3 privileges, the attacker exfiltrated 106 million credit applications from 700 S3 buckets.',
    analogy: 'A security guard at the front gate was tricked into making internal calls on behalf of an outsider, reading out master keys over the phone.',
    googleQuery: 'Capital One SSRF AWS IMDS Metadata Breach Diagram',
    unitTabId: 'unit5'
  },
  {
    unit: 'unit5',
    unitName: 'Unit 5: Cloud Security & IAM',
    marks: '7 Marks Expected',
    yieldTag: '⭐ High-Yield Concept',
    title: 'Virtual Machine Security Vulnerabilities: Escape, Hopping & Sprawl',
    summary: '1) VM Escape: The most severe cloud flaw; malicious code exploits hypervisor bugs to break out of the guest VM sandbox and execute root code directly on the host hypervisor. 2) VM Hopping: Attacker moves laterally across logical VLAN boundaries from one co-located tenant VM to another on the same physical host. 3) VM Sprawl: Uncontrolled proliferations of abandoned, unpatched VMs that become easy entry vectors.',
    analogy: 'VM Escape is like a prison inmate tunneling straight into the warden master control office.',
    googleQuery: 'Virtual Machine Escape VM Hopping Cloud Vulnerability Diagram',
    unitTabId: 'unit5'
  },

  // --- Unit 3: Architecture & Deployment (20% Marks) ---
  {
    unit: 'unit3',
    unitName: 'Unit 3: Cloud Deployment Models & Architecture',
    marks: '7 Marks Expected',
    yieldTag: '🔥 Top Exam Guaranteed',
    title: 'Multi-Tenant Architecture: Silo vs Bridge vs Pool Database Isolation',
    summary: 'Multi-tenancy enables a single application instance to serve multiple customer tenants. 1) Silo: Separate dedicated database instance per tenant. Maximum isolation, highest compliance, highest cost. 2) Bridge: Shared database server, separate isolated schema per tenant. Balanced cost and security. 3) Pool: Shared database and shared tables with tenant_id foreign key column. Lowest operational cost, maximum resource efficiency, requires robust Row-Level Security (RLS).',
    analogy: 'Silo = Separate gated houses for each tenant; Bridge = Gated townhouses sharing one complex fence; Pool = Roommates sharing an apartment with labeled refrigerator shelves.',
    googleQuery: 'Multi Tenant Database Architecture Silo Bridge Pool Diagram',
    unitTabId: 'unit3'
  },
  {
    unit: 'unit3',
    unitName: 'Unit 3: Cloud Deployment Models & Architecture',
    marks: '7 Marks Expected',
    yieldTag: '🔥 High-Yield Priority',
    title: '3-Tier Multi-Server Enterprise Web Architecture',
    summary: '1) Presentation Tier (Web): Public subnet Nginx/Apache servers behind an Elastic Load Balancer terminating SSL/TLS. 2) Application Tier (Business Logic): Private subnet compute instances running APIs and background task workers. 3) Data Tier (Persistence): Isolated database subnet with Master R/W database and asynchronous Read Replicas across multiple Availability Zones.',
    analogy: 'Presentation = The front dining area of a restaurant; Application = The kitchen chefs preparing orders; Data = The cold storage ingredient warehouse.',
    googleQuery: 'Three Tier Cloud Web Architecture AWS Diagram',
    unitTabId: 'unit3'
  },
  {
    unit: 'unit3',
    unitName: 'Unit 3: Cloud Deployment Models & Architecture',
    marks: '7 Marks Expected',
    yieldTag: '🔥 High-Yield Priority',
    title: 'Four Cloud Deployment Models: Public, Private, Hybrid & Community',
    summary: '1) Public Cloud: Multi-tenant, third-party owned (AWS/GCP), pay-per-use, accessible via Internet. 2) Private Cloud: Single-tenant dedicated infrastructure, high control/security, on-premise or hosted. 3) Hybrid Cloud: Orchestrated combination of private and public clouds connected via secure VPN or Direct Connect for cloud bursting. 4) Community Cloud: Shared infrastructure among organizations with shared compliance or mission goals (e.g., healthcare/banks).',
    analogy: 'Public = Public city bus; Private = Personal private car; Hybrid = Commuting by car to the train station and riding the express train into the city; Community = School bus or company carpool.',
    googleQuery: 'Cloud Deployment Models Public Private Hybrid Community Diagram',
    unitTabId: 'unit3'
  },
  {
    unit: 'unit3',
    unitName: 'Unit 3: Cloud Deployment Models & Architecture',
    marks: '5 / 7 Marks Expected',
    yieldTag: '⭐ Core Concept',
    title: 'Distributed System Characteristics & The CAP Theorem',
    summary: 'Distributed cloud systems feature concurrency, no global clock, independent failure modes, and horizontal scaling. Eric Brewer CAP Theorem proves that a distributed data store can guarantee at most two out of three properties simultaneously: Consistency (all nodes see latest data at the same moment), Availability (every non-failing node returns a response), and Partition Tolerance (system continues functioning despite arbitrary network packet drops).',
    analogy: 'You can choose fast delivery, low cost, or perfect quality in business, but you can never pick all three simultaneously.',
    googleQuery: 'CAP Theorem Consistency Availability Partition Tolerance Diagram',
    unitTabId: 'unit3'
  },

  // --- Unit 1: Introduction to Cloud (15% Marks) ---
  {
    unit: 'unit1',
    unitName: 'Unit 1: Introduction to Cloud Computing',
    marks: '5 / 7 Marks Expected',
    yieldTag: '🔥 Top Exam Guaranteed',
    title: 'NIST 5 Essential Characteristics of Cloud Computing',
    summary: 'NIST SP 800-145 defines 5 mandatory characteristics: 1) On-Demand Self-Service (provision without human intervention). 2) Broad Network Access (available over standard network on any client device). 3) Resource Pooling (multi-tenant shared hardware dynamically assigned). 4) Rapid Elasticity (scale outward/inward dynamically with demand). 5) Measured Service (usage is metered and transparently billed pay-as-you-go).',
    analogy: 'Like modern tap water and electricity: you turn the tap on whenever you want, pay only for liters used, and the utility company shares the central reservoir across town.',
    googleQuery: 'NIST Cloud Computing Five Essential Characteristics Diagram',
    unitTabId: 'unit1'
  },
  {
    unit: 'unit1',
    unitName: 'Unit 1: Introduction to Cloud Computing',
    marks: '5 / 7 Marks Expected',
    yieldTag: '🔥 High-Yield Priority',
    title: 'Fog Computing vs Cloud Computing Architecture',
    summary: 'Fog Computing extends cloud capabilities to the local network edge, placing compute, storage, and networking intermediate nodes between IoT sensors and centralized cloud data centers. Key differences: Fog has ultra-low sub-millisecond latency (1-15 ms) compared to Cloud (100-250 ms), preserves WAN bandwidth by local filtering, and processes real-time safety critical data locally.',
    analogy: 'Fog is a local neighborhood emergency clinic handling immediate first aid; Cloud is the regional multi-specialty trauma hospital performing complex surgeries.',
    googleQuery: 'Fog Computing Architecture IoT Edge Cloud Diagram',
    unitTabId: 'unit1'
  },
  {
    unit: 'unit1',
    unitName: 'Unit 1: Introduction to Cloud Computing',
    marks: '5 Marks Expected',
    yieldTag: '⭐ Core Concept',
    title: 'Top 7 Criteria for Selecting a Cloud Service Provider (CSP)',
    summary: 'Organizations evaluate CSPs across 7 critical dimensions: 1) Security & Compliance Certifications (ISO 27001, SOC 2, HIPAA). 2) Reliability & SLA Uptime Guarantees (99.99% availability with financial compensation clauses). 3) Pricing Transparency & TCO (predictable pay-as-you-go and reserved discounts). 4) Vendor Lock-in & Migration Ease (support for open APIs and containers). 5) Geographic Data Residency & Regional Latency. 6) Technical Architecture & Ecosystem compatibility. 7) Enterprise Technical Support & Response time.',
    analogy: 'Like selecting a long-term enterprise banking partner: you examine regulatory licenses, vault security, interest rates, customer branches, and branch proximity.',
    googleQuery: 'Cloud Service Provider Selection Criteria Evaluation Matrix',
    unitTabId: 'unit1'
  },

  // --- Unit 2: Service Models SPI (15% Marks) ---
  {
    unit: 'unit2',
    unitName: 'Unit 2: Cloud Service Models (SPI)',
    marks: '7 Marks Expected',
    yieldTag: '🔥 Top Exam Guaranteed',
    title: 'The SPI Cloud Framework & Pizza-as-a-Service Analogy',
    summary: 'The SPI taxonomy defines 3 service levels: 1) IaaS (Infrastructure as a Service - AWS EC2): Vendor manages physical facilities, servers, virtualization; user manages OS, runtime, and apps. 2) PaaS (Platform as a Service - AWS Elastic Beanstalk): Vendor manages up to runtime and OS; user provides application code and data. 3) SaaS (Software as a Service - Google Workspace): Vendor manages 100% of the stack; user consumes application via browser.',
    analogy: 'Traditional on-premise is making pizza at home (all 9 layers yours); IaaS is take-and-bake pizza; PaaS is pizza delivered to your door; SaaS is dining at the pizzeria.',
    googleQuery: 'Pizza as a Service Cloud Computing IaaS PaaS SaaS Diagram',
    unitTabId: 'unit2'
  },
  {
    unit: 'unit2',
    unitName: 'Unit 2: Cloud Service Models (SPI)',
    marks: '7 Marks Expected',
    yieldTag: '🔥 High-Yield Priority',
    title: 'Cloud Shared Responsibility Model Across SPI Models',
    summary: 'Security OF the cloud (physical data centers, host hardware, hypervisors, global network infrastructure) is ALWAYS the cloud provider responsibility. Security IN the cloud (customer data, IAM credentials, OS patching in IaaS, network firewall configurations) is the customer responsibility. In IaaS, customer owns everything from OS upwards. In PaaS, customer owns application code and data. In SaaS, customer owns only data access and IAM.',
    analogy: 'The landlord provides a secure apartment building with locked gates and smoke alarms (Security OF the building); you must lock your apartment door and not leave the stove on (Security IN the apartment).',
    googleQuery: 'AWS Shared Responsibility Model IaaS PaaS SaaS Diagram',
    unitTabId: 'unit2'
  }
];

// Current state for Random Topics
let currentTopicUnit = 'all';
let currentTopic = ALL_TOPICS_POOL[0];

function setRandomTopicUnit(unit, btn) {
  currentTopicUnit = unit;
  if (btn && btn.parentElement) {
    btn.parentElement.querySelectorAll('.btn').forEach(b => b.classList.remove('btn-primary'));
    btn.classList.add('btn-primary');
  }
  rollNextRandomTopic();
}

function getFilteredTopics() {
  if (currentTopicUnit === 'all') return ALL_TOPICS_POOL;
  return ALL_TOPICS_POOL.filter(t => t.unit === currentTopicUnit);
}

function rollNextRandomTopic() {
  const pool = getFilteredTopics();
  if (!pool.length) return;
  
  let idx = Math.floor(Math.random() * pool.length);
  if (pool.length > 1 && pool[idx].title === currentTopic.title) {
    idx = (idx + 1) % pool.length;
  }
  currentTopic = pool[idx];

  // Update card elements
  const unitBadge = document.getElementById('rtUnitBadge');
  const marksBadge = document.getElementById('rtMarksBadge');
  const yieldBadge = document.getElementById('rtYieldBadge');
  const title = document.getElementById('rtTitle');
  const summary = document.getElementById('rtSummary');
  const analogy = document.getElementById('rtAnalogy');
  const googleBtn = document.getElementById('rtGoogleBtn');
  const counterText = document.getElementById('rtCounterText');
  const card = document.getElementById('randomTopicDisplay');

  if (unitBadge) unitBadge.textContent = currentTopic.unitName;
  if (marksBadge) marksBadge.textContent = currentTopic.marks;
  if (yieldBadge) yieldBadge.textContent = currentTopic.yieldTag;
  if (title) title.textContent = currentTopic.title;
  if (summary) summary.innerHTML = '<strong>Exam Summary:</strong> ' + currentTopic.summary;
  if (analogy) analogy.innerHTML = '<strong>💡 Real-World Analogy / Insight:</strong> ' + currentTopic.analogy;
  if (counterText) counterText.textContent = 'Topics in current pool: ' + pool.length;

  if (googleBtn) {
    googleBtn.href = 'https://www.google.com/search?tbm=isch&q=' + encodeURIComponent(currentTopic.googleQuery);
  }

  // Quick visual feedback animation
  if (card) {
    card.style.transform = 'scale(0.99)';
    card.style.transition = 'transform 0.15s ease';
    setTimeout(() => { card.style.transform = 'scale(1)'; }, 150);
  }
}

function toggleTopicDetails() {
  const summary = document.getElementById('rtSummary');
  const analogy = document.getElementById('rtAnalogy');
  const btnText = document.getElementById('rtToggleBtnText');
  if (!summary || !analogy) return;

  const isHidden = summary.style.display === 'none';
  if (isHidden) {
    summary.style.display = 'block';
    analogy.style.display = 'block';
    if (btnText) btnText.textContent = '👁️ Hide Short Summary';
  } else {
    summary.style.display = 'none';
    analogy.style.display = 'none';
    if (btnText) btnText.textContent = '👁️ Show Short Summary';
  }
}

function jumpToRandomTopicUnit() {
  if (currentTopic && currentTopic.unitTabId) {
    switchTab(currentTopic.unitTabId);
  }
}

// ==============================================================================
// 2) IMP TOPICS FILTER
// ==============================================================================
function filterImpCards(filter, btn) {
  const cards = document.querySelectorAll('.imp-card');
  cards.forEach(card => {
    const tier = card.getAttribute('data-tier') || '';
    const marks = card.getAttribute('data-marks') || '';
    let show = false;
    if (filter === 'all') show = true;
    else if (filter === 'tier1' && tier === 'tier1') show = true;
    else if (filter === 'tier2' && tier === 'tier2') show = true;
    else if (filter === 'tier3' && tier === 'tier3') show = true;
    else if (filter === '7m' && marks.includes('7m')) show = true;
    else if (filter === '10m' && marks.includes('10m')) show = true;
    card.style.display = show ? 'flex' : 'none';
  });

  if (btn && btn.parentElement) {
    btn.parentElement.querySelectorAll('.btn').forEach(b => b.classList.remove('btn-primary'));
    btn.classList.add('btn-primary');
  }
}

// ==============================================================================
// 3) CROSS-CHAPTER QUESTION ROULETTE
// ==============================================================================
const ALL_QUESTIONS_POOL = [
  // 2-Mark Definitions
  {
    unit: 'Unit 1: Introduction to Cloud',
    marks: '2 Marks',
    type: 'Definition',
    question: 'Define Cloud Computing according to NIST SP 800-145.',
    answerHtml: '<strong>Model Answer:</strong> Cloud Computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction.',
    tip: 'Quote NIST SP 800-145 and list at least 3 keywords: on-demand, shared pool, rapid elasticity.',
    googleQuery: 'NIST Cloud Computing Definition Architecture Diagram',
    markCat: '2m',
    unitKey: 'unit1'
  },
  {
    unit: 'Unit 4: Virtualization',
    marks: '2 Marks',
    type: 'Definition',
    question: 'What is a Hypervisor or Virtual Machine Monitor (VMM)? Give two examples.',
    answerHtml: '<strong>Model Answer:</strong> A Hypervisor (or VMM) is a specialized low-level software firmware or hardware layer that creates, abstracts, and manages virtual machines by allocating physical CPU, RAM, and I/O resources to guest operating systems.<br><strong>Examples:</strong> VMware ESXi (Type 1), Oracle VirtualBox (Type 2).',
    tip: 'State the definition clearly and provide 1 Type 1 example and 1 Type 2 example.',
    googleQuery: 'Hypervisor Architecture Diagram',
    markCat: '2m',
    unitKey: 'unit4'
  },
  {
    unit: 'Unit 5: Cloud Security & IAM',
    marks: '2 Marks',
    type: 'Definition',
    question: 'What is the Explicit Deny Rule in AWS IAM policy evaluation?',
    answerHtml: '<strong>Model Answer:</strong> In AWS IAM policy evaluation, if ANY matching policy (User, Group, Role, or SCP) contains an explicit <code>"Effect": "Deny"</code>, the request is unconditionally and immediately REJECTED. An explicit deny always trumps and overrides any number of explicit <code>"Allow"</code> statements.',
    tip: 'Mention the golden rule: Explicit Deny > Explicit Allow > Default Implicit Deny.',
    googleQuery: 'AWS IAM Explicit Deny Policy Evaluation Flowchart',
    markCat: '2m',
    unitKey: 'unit5'
  },
  {
    unit: 'Unit 5: Cloud Security & IAM',
    marks: '2 Marks',
    type: 'Definition',
    question: 'What is VM Escape and why is it considered the most dangerous cloud vulnerability?',
    answerHtml: '<strong>Model Answer:</strong> VM Escape occurs when an attacker executes malicious code inside a guest virtual machine that breaks out of the guest operating system sandbox and directly compromises the underlying host hypervisor. It is critical because it gives the attacker control over the host server and every other co-located tenant VM on that hardware.',
    tip: 'Mention sandbox breakout and cross-tenant compromise.',
    googleQuery: 'VM Escape Hypervisor Security Vulnerability Diagram',
    markCat: '2m',
    unitKey: 'unit5'
  },
  {
    unit: 'Unit 3: Architecture',
    marks: '2 Marks',
    type: 'Definition',
    question: 'Define Multi-Tenancy in cloud computing.',
    answerHtml: '<strong>Model Answer:</strong> Multi-Tenancy is an architectural principle where a single shared physical or software instance of an application serves multiple distinct customer organizations (called tenants), while logically segregating their data, configurations, and user accounts so each tenant perceives dedicated ownership.',
    tip: 'Mention single shared instance, multiple tenants, and logical data isolation.',
    googleQuery: 'Multi Tenant SaaS Architecture Diagram',
    markCat: '2m',
    unitKey: 'unit3'
  },
  {
    unit: 'Unit 4: Virtualization',
    marks: '2 Marks',
    type: 'Definition',
    question: 'What is the Popek-Goldberg virtualization theorem in simple terms?',
    answerHtml: '<strong>Model Answer:</strong> The Popek-Goldberg theorem states that a computer architecture is virtualizable if and only if all sensitive instructions (instructions that inspect or alter hardware configurations) are a strict subset of privileged instructions (instructions that trap into hypervisor mode when executed in user mode).',
    tip: 'Highlight: Sensitive instructions ⊆ Privileged instructions.',
    googleQuery: 'Popek Goldberg Virtualization Requirements Ring Diagram',
    markCat: '2m',
    unitKey: 'unit4'
  },
  {
    unit: 'Unit 4: Virtualization',
    marks: '2 Marks',
    type: 'Definition',
    question: 'State the primary function of OpenStack Keystone and Nova.',
    answerHtml: '<strong>Model Answer:</strong> 1) <strong>Keystone:</strong> Provides centralized authentication, authorization, service discovery, and access token management across all OpenStack services.<br>2) <strong>Nova:</strong> The core compute engine that provisions, schedules, and manages the lifecycle of virtual machine instances.',
    tip: 'Name both components with their exact functional role.',
    googleQuery: 'OpenStack Keystone Nova Architecture Diagram',
    markCat: '2m',
    unitKey: 'unit4'
  },

  // 5-Mark Questions (Short Notes & Explanations)
  {
    unit: 'Unit 1: Introduction to Cloud',
    marks: '5 Marks',
    type: 'Short Note',
    question: 'Explain Fog Computing and explain three reasons why it is required alongside Cloud Computing.',
    answerHtml: '<strong>Model Answer:</strong><br><strong>Definition:</strong> Fog Computing is a decentralized computing paradigm that extends cloud services to the local network edge, processing sensor data intermediate nodes situated between IoT devices and central cloud data centers.<br><strong>Three Reasons Required:</strong><ul><li><strong>1. Ultra-Low Latency:</strong> Fog achieves 1–15 ms latency compared to 150–300 ms round-trip cloud WAN delay, crucial for autonomous vehicles and industrial robotics.</li><li><strong>2. WAN Bandwidth Conservation:</strong> Filtering, aggregating, and summarizing terabytes of sensor telemetry locally prevents network saturation.</li><li><strong>3. Offline Autonomous Operation:</strong> If the central cloud WAN link is severed, local factory or medical systems continue operating without interruption.</li></ul>',
    tip: 'Draw a 3-tier mini diagram: IoT Devices (Bottom) &rarr; Fog Nodes (Middle) &rarr; Central Cloud (Top).',
    googleQuery: 'Fog Computing Architecture IoT Edge Cloud Diagram',
    markCat: '5m',
    unitKey: 'unit1'
  },
  {
    unit: 'Unit 4: Virtualization',
    marks: '5 Marks',
    type: 'Short Note',
    question: 'Explain the 4-level physical infrastructure hierarchy of Apache CloudStack.',
    answerHtml: '<strong>Model Answer:</strong><br>Apache CloudStack organizes physical compute and storage into a strict 4-level hierarchy:<ul><li><strong>1. Zone:</strong> The highest-level container, typically corresponding to an entire physical data center with redundant power and independent network uplinks.</li><li><strong>2. Pod:</strong> Represents a single equipment rack inside a zone, sharing a second-layer switch and power distribution unit.</li><li><strong>3. Cluster:</strong> A grouping of identical hypervisor hosts inside a pod sharing primary block storage (NFS/iSCSI) for live VM migration.</li><li><strong>4. Host:</strong> A single physical server machine executing a hypervisor (KVM, Xen, or ESXi) running customer VMs.</li></ul>',
    tip: 'Draw a top-down hierarchical tree: Zone &rarr; Pod &rarr; Cluster &rarr; Host.',
    googleQuery: 'Apache CloudStack Zone Pod Cluster Host Physical Hierarchy Diagram',
    markCat: '5m',
    unitKey: 'unit4'
  },
  {
    unit: 'Unit 5: Cloud Security & IAM',
    marks: '5 Marks',
    type: 'Short Note',
    question: 'Explain the difference between Cloud Scalability and Cloud Elasticity with examples.',
    answerHtml: '<strong>Model Answer:</strong><br><ul><li><strong>Scalability:</strong> The planned structural ability of a system to accommodate sustained growing workloads by adding resources (Scale-Up / Scale-Out) over weeks or months. Example: Upgrading an e-commerce database from a 4-core instance to a 16-core instance to support a business growing 30% year-over-year.</li><li><strong>Elasticity:</strong> The real-time, autonomous, dynamic provisioning and de-provisioning of cloud resources in response to immediate spikes and drops. Example: AWS Auto Scaling dynamically launching 20 EC2 instances during a flash sale and automatically terminating them 2 hours later when traffic subsides.</li></ul>',
    tip: 'Use a table: Definition, Time Horizon, Trigger Mechanism, Cost Implication.',
    googleQuery: 'Cloud Scalability vs Elasticity Comparison Diagram',
    markCat: '5m',
    unitKey: 'unit5'
  },
  {
    unit: 'Unit 2: Service Models (SPI)',
    marks: '5 Marks',
    type: 'Short Note',
    question: 'Explain the Pizza-as-a-Service analogy used to describe IaaS, PaaS, and SaaS.',
    answerHtml: '<strong>Model Answer:</strong><br>The analogy divides the 9 layers of preparing a meal into customer-managed vs vendor-managed:<ul><li><strong>Traditional On-Premises (Made at Home):</strong> Customer manages all 9 layers: dining table, soda, gas, oven, fire, dough, tomato sauce, toppings, cheese.</li><li><strong>IaaS (Take and Bake):</strong> Vendor supplies dough, sauce, cheese, toppings. Customer brings home, provides oven, gas, soda, dining table. (e.g., AWS EC2).</li><li><strong>PaaS (Pizza Delivered):</strong> Vendor prepares, bakes, and delivers hot pizza. Customer provides soda and dining table. (e.g., AWS Elastic Beanstalk).</li><li><strong>SaaS (Dined Out at Pizzeria):</strong> Vendor provides 100% of everything including table, service, and soda. Customer simply consumes. (e.g., Google Workspace).</li></ul>',
    tip: 'Draw a 4-column stack showing green (vendor managed) vs orange (you manage).',
    googleQuery: 'Pizza as a Service Cloud Computing IaaS PaaS SaaS Diagram',
    markCat: '5m',
    unitKey: 'unit2'
  },
  {
    unit: 'Unit 4: Virtualization',
    marks: '5 Marks',
    type: 'Short Note',
    question: 'What is a Content Delivery Network (CDN)? Explain how it accelerates web content delivery.',
    answerHtml: '<strong>Model Answer:</strong><br>A CDN is a geographically distributed network of Point of Presence (PoP) edge proxy caching servers. When an end-user requests static assets (images, CSS, JavaScript, video fragments), DNS routing directs the request to the nearest geographical edge server rather than the distant origin server.<br><strong>Benefits:</strong> Drastically reduces latency (RTT), absorbs traffic surges and DDoS attacks, and minimizes origin server egress bandwidth charges.',
    tip: 'Mention Edge PoP nodes, DNS anycast routing, and origin offloading.',
    googleQuery: 'CDN Content Delivery Network Edge Caching Architecture Diagram',
    markCat: '5m',
    unitKey: 'unit4'
  },

  // 7-Mark Descriptive Questions & Comparisons
  {
    unit: 'Unit 4: Virtualization',
    marks: '7 Marks',
    type: 'Comparison & Diagram',
    question: 'Differentiate between Type 1 (Bare-Metal) and Type 2 (Hosted) Hypervisors with a neat architecture diagram.',
    answerHtml: '<strong>Model Answer:</strong><br><strong>Key Differences (7 Parameters):</strong><ol><li><strong>Architecture:</strong> Type 1 installs directly on raw physical bare-metal hardware. Type 2 installs as an application program on top of an existing host OS.</li><li><strong>Performance:</strong> Type 1 delivers near-native hardware speed with low latency. Type 2 suffers from double OS context switching overhead.</li><li><strong>Security & Isolation:</strong> Type 1 has strict isolation; Type 2 is vulnerable to host OS exploits (if host OS crashes, all guest VMs crash).</li><li><strong>Resource Overhead:</strong> Type 1 has a tiny footprint (~100 MB); Type 2 requires a full host OS (~10-20 GB RAM overhead).</li><li><strong>Hypervisor Access:</strong> Type 1 is managed via remote CLI/vCenter; Type 2 runs with a local desktop GUI.</li><li><strong>Use Cases:</strong> Type 1 is used in enterprise cloud data centers; Type 2 is used for local developer testing and software trials.</li><li><strong>Examples:</strong> Type 1: VMware ESXi, Hyper-V, KVM, Xen. Type 2: Oracle VirtualBox, VMware Workstation.</li></ol>',
    tip: 'Draw both layered stacks: Type 1: Hardware &rarr; Hypervisor &rarr; VMs. Type 2: Hardware &rarr; Host OS &rarr; Hypervisor &rarr; VMs.',
    googleQuery: 'Type 1 vs Type 2 Hypervisor Architecture Diagram',
    markCat: '7m',
    unitKey: 'unit4'
  },
  {
    unit: 'Unit 4: Virtualization',
    marks: '7 Marks',
    type: 'Comparison & Diagram',
    question: 'Compare Virtual Machines and Docker Containers on at least six parameters. Draw architectural diagrams for both.',
    answerHtml: '<strong>Model Answer:</strong><br><ol><li><strong>Virtualization Level:</strong> VM virtualizes physical hardware (CPU, RAM, NIC). Container virtualizes the operating system kernel.</li><li><strong>Guest OS Requirement:</strong> VMs require a full, dedicated guest OS per instance. Containers share the host OS kernel and require no guest OS.</li><li><strong>Size Footprint:</strong> VMs range from 2 GB to 50 GB. Containers range from 5 MB (Alpine) to 500 MB.</li><li><strong>Boot Time:</strong> VMs boot in minutes. Containers start in milliseconds.</li><li><strong>Resource Utilization:</strong> VMs suffer static resource pre-allocation. Containers dynamically allocate memory and CPU as needed.</li><li><strong>Isolation:</strong> VMs provide hard, hardware-enforced hypervisor boundary. Containers provide process-level isolation via cgroups and namespaces.</li><li><strong>Server Density:</strong> A server can run 20–30 VMs, or 200–500 Containers.</li></ol>',
    tip: 'Highlight Docker engine, namespaces, cgroups vs Hypervisor, Guest OS.',
    googleQuery: 'Docker Containers vs Virtual Machines Architecture Diagram',
    markCat: '7m',
    unitKey: 'unit4'
  },
  {
    unit: 'Unit 4: Virtualization',
    marks: '7 Marks',
    type: 'Comparison & Diagram',
    question: 'Compare Block Storage, Object Storage, and File Storage on structure, access method, latency, and cloud examples.',
    answerHtml: '<strong>Model Answer:</strong><br><ol><li><strong>Data Structure:</strong> Block divides data into fixed-size raw blocks with unique addresses. Object stores data as whole immutable objects with custom metadata in a flat namespace. File uses a hierarchical tree structure with folders and sub-folders.</li><li><strong>Access Protocol:</strong> Block uses Fibre Channel, iSCSI, NVMe-oF. Object uses HTTP/HTTPS REST APIs (GET, PUT, DELETE). File uses NFS, SMB, CIFS.</li><li><strong>Latency & IOPS:</strong> Block delivers ultra-low millisecond latency and high IOPS. Object has higher latency but limitless throughput. File delivers moderate latency.</li><li><strong>Shared Access:</strong> Block is attached to a single VM at a time. Object is globally accessible via URLs. File supports concurrent multi-server read/write.</li><li><strong>Ideal Use Cases:</strong> Block: OS boot disks, MySQL/Oracle DBs. Object: Static websites, media archives, backups. File: Shared user home directories, CMS assets.</li><li><strong>Cloud Examples:</strong> Block: AWS EBS, Azure Disk. Object: AWS S3, Google Cloud Storage. File: AWS EFS, Azure Files.</li></ol>',
    tip: 'Include a 6-row comparison table with AWS, Azure, and GCP service names.',
    googleQuery: 'Block vs File vs Object Storage Cloud Diagram',
    markCat: '7m',
    unitKey: 'unit4'
  },
  {
    unit: 'Unit 5: Cloud Security & IAM',
    marks: '7 Marks',
    type: 'Comparison & Diagram',
    question: 'Explain the CIA Triad in cloud computing. Detail the controls used to enforce Confidentiality, Integrity, and Availability.',
    answerHtml: '<strong>Model Answer:</strong><br>The CIA Triad forms the foundational pillar of cloud information security:<ul><li><strong>1. Confidentiality:</strong> Preventing unauthorized exposure of sensitive customer data. <em>Controls:</em> AES-256 data encryption at rest (KMS), TLS 1.3 encryption in transit, strict IAM Role-Based Access Control (RBAC), Multi-Factor Authentication (MFA), and VPC private subnets.</li><li><strong>2. Integrity:</strong> Protecting data from unauthorized modification, deletion, or tampering. <em>Controls:</em> Cryptographic checksums, SHA-256 digital signatures, AWS CloudTrail immutable audit logging, and S3 Object Lock (Write Once Read Many - WORM).</li><li><strong>3. Availability:</strong> Ensuring authorized users have uninterrupted access to cloud resources. <em>Controls:</em> Multi-Availability Zone redundancy, automated health check failovers, AWS Auto Scaling, and DDoS protection via AWS Shield and WAF.</li></ul>',
    tip: 'Draw the classic CIA triangle with the corresponding cloud security controls annotated beside each apex.',
    googleQuery: 'CIA Triad Information Security Cloud Computing Diagram',
    markCat: '7m',
    unitKey: 'unit5'
  },
  {
    unit: 'Unit 5: Cloud Security & IAM',
    marks: '7 Marks',
    type: 'Comparison & Diagram',
    question: 'Explain AWS IAM Policy Evaluation Logic with a flowchart. Discuss the significance of the Explicit Deny rule.',
    answerHtml: '<strong>Model Answer:</strong><br><strong>IAM Policy Evaluation Flow:</strong><ol><li>All requests start with a default implicit <strong>DENY</strong>.</li><li>The evaluation engine collects all applicable policies (Identity-based, Resource-based, SCPs, Permissions Boundaries).</li><li><strong>Golden Rule 1:</strong> If ANY policy contains an explicit <code>"Effect": "Deny"</code> matching the action and resource, the evaluation immediately halts and returns <strong>DENY</strong>.</li><li><strong>Golden Rule 2:</strong> If no explicit deny exists, the engine checks for at least one explicit <code>"Effect": "Allow"</code>. If found, the final decision is <strong>ALLOW</strong>.</li><li>If no explicit allow is found, the decision defaults to the original implicit <strong>DENY</strong>.</li></ol>',
    tip: 'Draw the decision diamond flowchart: Start &rarr; Default Deny &rarr; Explicit Deny? (Yes &rarr; Deny) &rarr; Explicit Allow? (Yes &rarr; Allow, No &rarr; Deny).',
    googleQuery: 'AWS IAM Policy Evaluation Logic Flowchart Diagram',
    markCat: '7m',
    unitKey: 'unit5'
  },
  {
    unit: 'Unit 3: Architecture',
    marks: '7 Marks',
    type: 'Comparison & Diagram',
    question: 'Explain the 3-Tier Multi-Server Enterprise Cloud Web Architecture with a diagram.',
    answerHtml: '<strong>Model Answer:</strong><br>The 3-tier architecture decouples web applications into isolated layers for security and scale:<ul><li><strong>Tier 1: Web / Presentation Tier (Public Subnet):</strong> Fronted by an Internet-facing Application Load Balancer (ALB). Runs Nginx/Apache servers terminating SSL/TLS certificates and serving cached UI assets.</li><li><strong>Tier 2: Application / Logic Tier (Private Subnet):</strong> Private EC2 instances or container tasks running backend business logic, REST APIs, and message worker queues. Accessible only from the Web tier security group.</li><li><strong>Tier 3: Database / Persistence Tier (Isolated Subnet):</strong> Highly secure database subnet with Primary DB (Write Master) and multi-AZ Read Replicas. Zero direct Internet ingress.</li></ul>',
    tip: 'Draw 3 horizontal subnets inside an AWS VPC with an Internet Gateway, NAT Gateway, and Load Balancer.',
    googleQuery: 'Three Tier Cloud Web Architecture AWS Diagram',
    markCat: '7m',
    unitKey: 'unit3'
  },
  {
    unit: 'Unit 3: Architecture',
    marks: '7 Marks',
    type: 'Comparison & Diagram',
    question: 'Compare Silo, Bridge, and Pool data isolation patterns in Multi-Tenant database architectures.',
    answerHtml: '<strong>Model Answer:</strong><br><ol><li><strong>Silo Model:</strong> Dedicated physical database instance per tenant. Maximum isolation, zero cross-tenant blast radius, highest infrastructure and operational cost. Ideal for healthcare, defense, and banking.</li><li><strong>Bridge Model:</strong> Shared database server engine, but separate logical database schemas per tenant. Balanced isolation, simpler database upgrades, moderate operational overhead.</li><li><strong>Pool Model:</strong> Shared database and shared tables; data segregated logically via a <code>tenant_id</code> foreign key column. Lowest operational cost, maximum hardware utilization, requires robust application-level Row-Level Security (RLS) enforcement.</li></ol>',
    tip: 'Draw 3 diagrams showing database cylinders with tenant labels.',
    googleQuery: 'Multi Tenant Database Architecture Silo Bridge Pool Diagram',
    markCat: '7m',
    unitKey: 'unit3'
  },
  {
    unit: 'Unit 4: Virtualization',
    marks: '7 Marks',
    type: 'Comparison & Diagram',
    question: 'Explain Software-Defined Networking (SDN) 3-Plane Architecture and the role of OpenFlow.',
    answerHtml: '<strong>Model Answer:</strong><br>SDN separates the intelligence of the network from the packet forwarding hardware:<ul><li><strong>1. Application Plane (Top):</strong> Contains network applications such as traffic monitoring, firewall policy engines, and load balancers. Interacts with the control plane via Northbound REST APIs.</li><li><strong>2. Control Plane (Middle):</strong> The centralized SDN controller (the brain) which calculates network routing topologies, flow tables, and quality of service policies.</li><li><strong>3. Data Plane (Bottom):</strong> Physical or virtual forwarding hardware (switches/routers) that simply match packets against flow tables and forward them.</li><li><strong>OpenFlow:</strong> The standardized Southbound protocol allowing the SDN controller to programmatically push flow tables into Data Plane switches.</li></ul>',
    tip: 'Draw 3 horizontal rectangles connected by Northbound and Southbound (OpenFlow) arrows.',
    googleQuery: 'Software Defined Networking SDN Architecture Three Layers Diagram',
    markCat: '7m',
    unitKey: 'unit4'
  },

  // 10-Mark Comprehensive Architectural Questions
  {
    unit: 'Unit 4: Virtualization',
    marks: '10 Marks',
    type: 'Comprehensive Architecture',
    question: 'Explain OpenStack Architecture in detail. Describe the functions of Nova, Keystone, Neutron, Swift, Glance, Cinder, Horizon, Heat, and Ceilometer.',
    answerHtml: '<strong>Model Answer:</strong><br>OpenStack is an open-source modular cloud operating system that orchestrates compute, storage, and networking:<ul><li><strong>1. Keystone (Identity):</strong> Central authentication service issuing scoped bearer tokens and API service catalogs.</li><li><strong>2. Nova (Compute):</strong> Provisions and manages VM instances by scheduling workloads to hypervisor compute nodes.</li><li><strong>3. Neutron (Networking):</strong> Software-defined networking providing virtual networks, subnets, routers, and floating IPs.</li><li><strong>4. Glance (Image Service):</strong> Repository for discovering, registering, and retrieving VM operating system disk images (QCOW2/RAW).</li><li><strong>5. Cinder (Block Storage):</strong> Provides persistent raw block volume storage that survives VM lifecycle terminations.</li><li><strong>6. Swift (Object Storage):</strong> Scalable distributed object storage for media and unstructured blobs via REST APIs.</li><li><strong>7. Horizon (Dashboard):</strong> Web-based graphical user interface for administrators and cloud tenants.</li><li><strong>8. Heat (Orchestration):</strong> Template-driven engine for deploying multi-instance composite cloud applications.</li><li><strong>9. Ceilometer (Telemetry):</strong> Tracks usage metering, alarms, and performance metrics for billing and resource autoscaling.</li></ul>',
    tip: 'Draw Horizon and Keystone at the center, Nova/Neutron/Cinder surrounding it, connected via REST APIs and RabbitMQ message bus.',
    googleQuery: 'OpenStack Architecture Nova Neutron Keystone Glance Diagram',
    markCat: '10m',
    unitKey: 'unit4'
  },
  {
    unit: 'Unit 5: Cloud Security & IAM',
    marks: '10 Marks',
    type: 'Comprehensive Architecture',
    question: 'Discuss Cloud Security Threats with real-world case studies: Analyze the Capital One SSRF Breach and Microsoft Storm-0558 incident.',
    answerHtml: '<strong>Model Answer:</strong><br><strong>Case Study 1: Capital One SSRF Breach (2019):</strong><ul><li><em>Vulnerability:</em> Misconfigured open-source ModSecurity WAF running on an AWS EC2 instance.</li><li><em>Attack Vector:</em> Server-Side Request Forgery (SSRF) allowed the attacker to command the EC2 server to query the internal AWS Instance Metadata Service v1 (<code>http://169.254.169.254/latest/meta-data/iam/security-credentials/</code>).</li><li><em>Impact:</em> Stole temporary IAM role credentials that had excessively broad permissions; exfiltrated 106 million customer credit card records from 700 S3 buckets.</li><li><em>Remediation:</em> Adopted IMDSv2 (requires session token headers, neutralizing SSRF) and enforced Principle of Least Privilege on IAM roles.</li></ul><br><strong>Case Study 2: Microsoft Storm-0558 Token Forgery (2023):</strong><ul><li><em>Vulnerability:</em> A consumer Microsoft Account (MSA) cryptographic signing key leaked into a Windows kernel memory dump file after an internal crash, which was subsequently exfiltrated by threat actors.</li><li><em>Attack Vector:</em> Attackers used the stolen signing key to forge OpenID Connect authentication tokens, tricking enterprise Azure AD identity endpoints into granting access.</li><li><em>Impact:</em> Breached 25 government and enterprise email organizations, including the US State Department.</li><li><em>Remediation:</em> Automated HSM-bound key rotation, improved crash dump scrubbing, and hardened token verification logic.</li></ul>',
    tip: 'Structure response clearly: Background &rarr; Root Cause Vulnerability &rarr; Attack Vector Step-by-Step &rarr; Impact &rarr; Preventative Fixes.',
    googleQuery: 'Capital One SSRF AWS IMDS Metadata Breach Diagram',
    markCat: '10m',
    unitKey: 'unit5'
  },
  {
    unit: 'Unit 3: Architecture',
    marks: '10 Marks',
    type: 'Comprehensive Architecture',
    question: 'Explain the four Cloud Deployment Models (Public, Private, Hybrid, Community) with neat diagrams, pros, cons, and use-cases. Contrast them with the Multi-Cloud strategy.',
    answerHtml: '<strong>Model Answer:</strong><br><strong>1. Public Cloud:</strong> Owned by third-party CSPs (AWS, GCP). Pros: Zero CapEx, infinite elastic scale. Cons: Multi-tenant shared risk, lower hardware control. Use-case: Startups, web applications.<br><strong>2. Private Cloud:</strong> Dedicated to a single organization. Pros: Maximum security, compliance, customized hardware. Cons: High CapEx and operational maintenance. Use-case: Defense, government, commercial banks.<br><strong>3. Hybrid Cloud:</strong> Integrates private and public clouds via secure encrypted tunnels or Direct Connect. Pros: Cloud bursting capability, optimal balance of sensitive data retention and elastic burst computing. Use-case: Healthcare institutions.<br><strong>4. Community Cloud:</strong> Shared across organizations with common mission or regulatory constraints (e.g., European police agencies). Pros: Shared infrastructure costs, shared compliance governance. Cons: Compromise on specific customized needs.<br><strong>Multi-Cloud Strategy:</strong> Utilizing multiple distinct public cloud vendors (e.g., AWS + Azure + GCP) to eliminate vendor lock-in, maximize geographic coverage, and achieve high disaster resiliency.',
    tip: 'Draw 4 deployment diagrams and provide a 7-parameter comparison table (Ownership, Cost, Scalability, Security, Maintenance).',
    googleQuery: 'Cloud Deployment Models Public Private Hybrid Community Diagram',
    markCat: '10m',
    unitKey: 'unit3'
  },
  {
    unit: 'Unit 4: Virtualization',
    marks: '10 Marks',
    type: 'Comprehensive Architecture',
    question: 'Discuss Virtualization in depth: Compute, Storage, and Network Virtualization techniques. Explain hardware-assisted virtualization extensions.',
    answerHtml: '<strong>Model Answer:</strong><br>Virtualization abstracts physical computing hardware into logical isolated virtual resources:<ul><li><strong>1. Compute Virtualization:</strong> Hypervisors abstract CPU and memory. Full virtualization (binary translation), Paravirtualization (modified guest OS kernel making hypercalls), and Hardware-Assisted Virtualization (Intel VT-x, AMD-V providing VMX root and non-root execution rings).</li><li><strong>2. Storage Virtualization:</strong> Pools physical disks from SAN/NAS storage arrays into logical storage pools. Implemented via Storage Area Networks, LVM (Logical Volume Management), and software-defined storage (Ceph, OpenStack Cinder/Swift).</li><li><strong>3. Network Virtualization:</strong> Decouples virtual network topologies from physical routers and switches. Uses VLANs, VXLAN encapsulation overlays, and Software-Defined Networking (SDN) with OpenFlow controllers.</li><li><strong>Intel VT-x & AMD-V:</strong> Introduces Root Mode (hypervisor execution) and Non-Root Mode (guest OS execution), completely eliminating binary translation overhead and enabling hardware-level VM traps.</li></ul>',
    tip: 'Break answer into 4 labeled sections: Compute Virtualization, Storage Virtualization, Network Virtualization, Hardware-Assist (Intel VT-x / AMD-V rings).',
    googleQuery: 'Compute Storage Network Virtualization Hardware Assisted Intel VT Diagram',
    markCat: '10m',
    unitKey: 'unit4'
  }
];

// Current Roulette State
let currentRouletteFilter = 'all';
let currentRouletteQ = ALL_QUESTIONS_POOL[0];
let attemptedQuestions = new Set();

function setRouletteFilter(filter, btn) {
  currentRouletteFilter = filter;
  if (btn && btn.parentElement) {
    btn.parentElement.querySelectorAll('.btn').forEach(b => b.classList.remove('btn-primary'));
    btn.classList.add('btn-primary');
  }
  rollNextRouletteQuestion();
}

function getFilteredQuestions() {
  if (currentRouletteFilter === 'all') return ALL_QUESTIONS_POOL;
  if (currentRouletteFilter === '7m') return ALL_QUESTIONS_POOL.filter(q => q.markCat === '7m');
  if (currentRouletteFilter === '10m') return ALL_QUESTIONS_POOL.filter(q => q.markCat === '10m');
  if (currentRouletteFilter === '5m') return ALL_QUESTIONS_POOL.filter(q => q.markCat === '5m');
  if (currentRouletteFilter === '2m') return ALL_QUESTIONS_POOL.filter(q => q.markCat === '2m');
  if (currentRouletteFilter === 'unit45') return ALL_QUESTIONS_POOL.filter(q => q.unitKey === 'unit4' || q.unitKey === 'unit5');
  return ALL_QUESTIONS_POOL;
}

function rollNextRouletteQuestion() {
  const pool = getFilteredQuestions();
  if (!pool.length) return;

  let idx = Math.floor(Math.random() * pool.length);
  if (pool.length > 1 && pool[idx].question === currentRouletteQ.question) {
    idx = (idx + 1) % pool.length;
  }
  currentRouletteQ = pool[idx];
  attemptedQuestions.add(currentRouletteQ.question);

  // Hide Answer Panel
  const panel = document.getElementById('rqAnswerPanel');
  const revealBtn = document.getElementById('rqRevealBtn');
  if (panel) panel.classList.remove('open');
  if (revealBtn) revealBtn.innerHTML = '<span>👁️ Reveal Model Answer</span>';

  // Update card elements
  const unitBadge = document.getElementById('rqUnitBadge');
  const marksBadge = document.getElementById('rqMarksBadge');
  const typeBadge = document.getElementById('rqTypeBadge');
  const qText = document.getElementById('rqQuestionText');
  const aContent = document.getElementById('rqAnswerContent');
  const tipBox = document.getElementById('rqTipBox');
  const googleBtn = document.getElementById('rqGoogleSearchBtn');
  const statSeen = document.getElementById('rqStatSeen');
  const statPool = document.getElementById('rqStatPool');
  const card = document.getElementById('rouletteCard');

  if (unitBadge) unitBadge.textContent = currentRouletteQ.unit;
  if (marksBadge) marksBadge.textContent = currentRouletteQ.marks;
  if (typeBadge) typeBadge.textContent = currentRouletteQ.type;
  if (qText) qText.textContent = 'Q. ' + currentRouletteQ.question;
  if (aContent) aContent.innerHTML = currentRouletteQ.answerHtml;
  if (tipBox) tipBox.innerHTML = '<strong>✏️ Grading & Blueprint Tip:</strong> ' + currentRouletteQ.tip;

  if (googleBtn) {
    if (currentRouletteQ.googleQuery) {
      googleBtn.style.display = 'inline-flex';
      googleBtn.href = 'https://www.google.com/search?tbm=isch&q=' + encodeURIComponent(currentRouletteQ.googleQuery);
    } else {
      googleBtn.style.display = 'none';
    }
  }

  if (statSeen) statSeen.textContent = attemptedQuestions.size;
  if (statPool) statPool.textContent = pool.length;

  if (card) {
    card.style.transform = 'scale(0.99)';
    card.style.transition = 'transform 0.15s ease';
    setTimeout(() => { card.style.transform = 'scale(1)'; }, 150);
  }
}

function toggleRouletteAnswer() {
  const panel = document.getElementById('rqAnswerPanel');
  const revealBtn = document.getElementById('rqRevealBtn');
  if (!panel) return;

  const isOpen = panel.classList.toggle('open');
  if (revealBtn) {
    revealBtn.innerHTML = isOpen ? '<span>🙈 Hide Answer</span>' : '<span>👁️ Reveal Model Answer</span>';
  }
}

// Power Modes Initialization
function initPowerModes() {
  rollNextRandomTopic();
  rollNextRouletteQuestion();
}
'''

def update_parts_js():
    js_file = os.path.join(os.path.dirname(__file__), "parts_js.py")
    with open(js_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if initPowerModes already exists
    if "initPowerModes" in content:
        print("Power modes already present in parts_js.py")
        return

    # Find where to append in JS_CODE before window.addEventListener
    target_needle = "window.addEventListener('DOMContentLoaded', () => {"
    if target_needle in content:
        replacement = POWER_MODES_JS + "\n\n// Initialize on Load\nwindow.addEventListener('DOMContentLoaded', () => {\n  initPowerModes();"
        new_content = content.replace("window.addEventListener('DOMContentLoaded', () => {", replacement, 1)
        with open(js_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully integrated Power Modes into parts_js.py!")
    else:
        print("Could not find DOMContentLoaded in parts_js.py")

if __name__ == "__main__":
    update_parts_js()
