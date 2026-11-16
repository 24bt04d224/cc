# -*- coding: utf-8 -*-
import json
from parts_u45_guaranteed import generate_u45_js_roulette_items

U45_JS_DATA = json.dumps(generate_u45_js_roulette_items())

_RAW_JS_CODE = """
// State Management
let currentTheme = localStorage.getItem('cc_theme') || 'dark';
document.documentElement.setAttribute('data-theme', currentTheme);

// Tab Navigation
function switchTab(tabId) {
  document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.bottom-nav-item').forEach(el => el.classList.remove('active'));
  
  const targetTab = document.getElementById(tabId);
  const targetNav = document.getElementById('nav-' + tabId);
  const targetBottomNav = document.getElementById('bnav-' + tabId);
  
  if (targetTab) targetTab.classList.add('active');
  if (targetNav) targetNav.classList.add('active');
  if (targetBottomNav) {
    targetBottomNav.classList.add('active');
  } else if (tabId.startsWith('unit')) {
    const unitsBnav = document.getElementById('bnav-units');
    if (unitsBnav) unitsBnav.classList.add('active');
  }
  
  closeMobileNav();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Mobile Drawer Navigation
function toggleMobileNav() {
  const sidebar = document.querySelector('aside');
  const backdrop = document.getElementById('sidebarBackdrop');
  if (!sidebar) return;
  const isOpen = sidebar.classList.contains('drawer-open');
  if (isOpen) {
    closeMobileNav();
  } else {
    sidebar.classList.add('drawer-open');
    if (backdrop) backdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
}

function closeMobileNav() {
  const sidebar = document.querySelector('aside');
  const backdrop = document.getElementById('sidebarBackdrop');
  if (sidebar) sidebar.classList.remove('drawer-open');
  if (backdrop) backdrop.classList.remove('active');
  document.body.style.overflow = '';
}

// Theme Toggle
function toggleTheme() {
  currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', currentTheme);
  localStorage.setItem('cc_theme', currentTheme);
  const btn = document.getElementById('themeToggleBtn');
  if (btn) btn.innerHTML = currentTheme === 'dark' ? '🌙' : '☀️';
}

// Level 1: Main Head Dropdown Toggle
function toggleMainTopic(header) {
  header.classList.toggle('open');
  const body = header.nextElementSibling;
  body.classList.toggle('open');
}

// Level 2: Sub-Topic Dropdown Toggle
function toggleSubTopic(header) {
  header.classList.toggle('open');
  const detail = header.nextElementSibling;
  detail.classList.toggle('open');
}

// Expand All in Unit
function expandAllInUnit(unitId) {
  const unit = document.getElementById(unitId);
  if (!unit) return;
  unit.querySelectorAll('.main-topic-header').forEach(h => h.classList.add('open'));
  unit.querySelectorAll('.main-topic-body').forEach(b => b.classList.add('open'));
  unit.querySelectorAll('.sub-topic-header').forEach(h => h.classList.add('open'));
  unit.querySelectorAll('.sub-topic-detail').forEach(d => d.classList.add('open'));
}

// Collapse All in Unit
function collapseAllInUnit(unitId) {
  const unit = document.getElementById(unitId);
  if (!unit) return;
  unit.querySelectorAll('.main-topic-header').forEach(h => h.classList.remove('open'));
  unit.querySelectorAll('.main-topic-body').forEach(b => b.classList.remove('open'));
  unit.querySelectorAll('.sub-topic-header').forEach(h => h.classList.remove('open'));
  unit.querySelectorAll('.sub-topic-detail').forEach(d => d.classList.remove('open'));
}

// Jump to Specific Main Topic from Dropdown Selector
function jumpToTopic(unitId, selectElem) {
  const topicId = selectElem.value;
  if (!topicId) return;
  
  const targetCard = document.getElementById(topicId);
  if (targetCard) {
    const header = targetCard.querySelector('.main-topic-header');
    const body = targetCard.querySelector('.main-topic-body');
    if (header && !header.classList.contains('open')) {
      header.classList.add('open');
      if (body) body.classList.add('open');
    }
    targetCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

// Flashcards Data & Controller (36 Cards)
const flashcardsData = [
  // --- Unit 1 Flashcards ---
  { unit: "Unit 1", q: "What is Cloud Computing?", a: "The on-demand delivery of computing services (servers, storage, databases, networking, software, AI) over the Internet on a pay-as-you-go basis without maintaining physical infrastructure." },
  { unit: "Unit 1", q: "Name the 5 NIST Essential Characteristics of Cloud Computing.", a: "1. <strong>On-Demand Self-Service</strong><br>2. <strong>Broad Network Access</strong><br>3. <strong>Resource Pooling</strong><br>4. <strong>Rapid Elasticity</strong><br>5. <strong>Measured Service</strong>." },
  { unit: "Unit 1", q: "What is Vendor Lock-in and why does it occur?", a: "When an organization becomes dependent on a specific cloud provider's proprietary APIs, database engines, and tooling, making migrating to another vendor difficult and costly." },
  { unit: "Unit 1", q: "What is the core formula for selecting a Cloud Service Provider?", a: "<code>Sustenance = Technology Strength + Business Skills</code> (Must evaluate SLAs, compliance audits, financial health, and data security)." },
  { unit: "Unit 1", q: "What is Fog Computing and where is it used?", a: "A decentralized model bringing data processing and analytics closer to local IoT devices (Fog Nodes) rather than sending all raw data to a centralized cloud. Used in factories, oil pipelines, and avionics." },
  { unit: "Unit 1", q: "What is Virtualization and the Apartment Building Analogy?", a: "Creating virtual versions of physical hardware. <strong>Building</strong> = Physical Server, <strong>Apartments</strong> = Virtual Machines (VMs), <strong>Families</strong> = Different Operating Systems, <strong>Shared Utilities</strong> = CPU/RAM." },

  // --- Unit 2 Flashcards ---
  { unit: "Unit 2", q: "Explain the 'Pizza-as-a-Service' Analogy.", a: "<strong>On-Premises:</strong> Made at home (manage everything)<br><strong>IaaS:</strong> Take and bake (vendor gives dough/sauce, you bake)<br><strong>PaaS:</strong> Pizza delivered (ready hot; you provide table)<br><strong>SaaS:</strong> Dining out (vendor manages 100%)." },
  { unit: "Unit 2", q: "What is Amazon EC2 and an EC2 Instance?", a: "Amazon Elastic Compute Cloud provides resizable virtual compute capacity. An <strong>EC2 Instance</strong> is a virtual server running on AWS infrastructure." },
  { unit: "Unit 2", q: "What is an AMI (Amazon Machine Image)?", a: "A pre-configured template containing the OS, application software, and configuration files used to launch an EC2 instance." },
  { unit: "Unit 2", q: "What are the 6 states of the EC2 Instance Lifecycle?", a: "<code>Launch &rarr; Pending &rarr; Running &rarr; Stopping &rarr; Stopped &rarr; Shutting-Down &rarr; Terminated</code>." },
  { unit: "Unit 2", q: "Differentiate Web Server vs Worker Environment in AWS Elastic Beanstalk.", a: "<strong>Web Server Environment:</strong> Handles front-facing public HTTP/HTTPS traffic.<br><strong>Worker Environment:</strong> Pulls background, asynchronous batch tasks from an Amazon SQS queue." },
  { unit: "Unit 2", q: "What are the 4 layers in SaaS Architecture?", a: "1. <strong>Client Layer</strong> (Browsers, mobile apps)<br>2. <strong>Application Layer</strong> (Business logic, REST APIs)<br>3. <strong>Data Layer</strong> (Databases, file storage)<br>4. <strong>Infrastructure Layer</strong> (VMs, containers, networks)." },

  // --- Unit 3 Flashcards ---
  { unit: "Unit 3", q: "What is a Private Cloud and give 2 real Indian examples?", a: "Cloud infrastructure dedicated exclusively to a single organization (e.g. <strong>UIDAI Aadhaar</strong> for 1.4B resident biometric data, and <strong>Indian Bank / SBI</strong> for core banking compliance)." },
  { unit: "Unit 3", q: "What is Cloud Bursting in a Hybrid Cloud setup?", a: "A dynamic deployment pattern where an application runs primarily in a private cloud/datacenter, but automatically bursts excess workload into a public cloud during unexpected peak demand spikes." },
  { unit: "Unit 3", q: "Compare Pool Pattern vs Silo Pattern in Multi-Tenant Databases.", a: "<strong>Pool:</strong> Shared DB and shared tables partitioned by <code>tenant_id</code> (Lowest cost).<br><strong>Silo:</strong> Dedicated database instance per tenant (Highest isolation, maximum compliance, highest cost)." },
  { unit: "Unit 3", q: "What is the mathematical formula for High Availability (HA)?", a: "<code>Availability (%) = [Uptime / (Uptime + Downtime)] &times; 100</code>.<br>Example: 999 hrs uptime with 1 hr downtime = 99.9% availability." },
  { unit: "Unit 3", q: "Differentiate Layer 4 vs Layer 7 Load Balancing.", a: "<strong>Layer 4 (NLB):</strong> Routes at Transport Layer based on IP & TCP/UDP ports without inspecting packet contents.<br><strong>Layer 7 (ALB):</strong> Routes at Application Layer based on HTTP URLs, headers, and cookies." },
  { unit: "Unit 3", q: "Which cloud provider offers BigQuery and what is its core specialty?", a: "<strong>Google Cloud Platform (GCP)</strong>. BigQuery is a serverless, highly-scalable multi-cloud data warehouse engineered for lightning-fast SQL queries on petabytes of data." },

  // --- Unit 4 Flashcards ---
  { unit: "Unit 4", q: "What is a Type 1 Hypervisor?", a: "A bare-metal hypervisor that runs directly on physical hardware without a host OS (e.g. VMware ESXi, Hyper-V, KVM, Xen). Offers maximum performance and strong isolation." },
  { unit: "Unit 4", q: "What is a Type 2 Hypervisor?", a: "A hosted hypervisor that runs as an application inside an existing host operating system (e.g. VirtualBox, VMware Workstation). Ideal for testing and software development." },
  { unit: "Unit 4", q: "Name the 3 modules in the Hypervisor Reference Model.", a: "1. <strong>Dispatcher</strong> (Directs incoming instructions)<br>2. <strong>Allocator</strong> (Allocates CPU/RAM/Disk resources)<br>3. <strong>Interpreter</strong> (Interprets privileged CPU instructions safely)." },
  { unit: "Unit 4", q: "What is the primary difference between a VM and a Docker Container?", a: "A Virtual Machine virtualizes hardware and boots a <strong>full Guest OS</strong> (GBs in size). A Container virtualizes the OS and <strong>shares the host OS kernel</strong> (MBs in size, near-instant boot)." },
  { unit: "Unit 4", q: "What is Nova in OpenStack?", a: "Nova is the <strong>Compute Engine</strong> in OpenStack responsible for provisioning, scheduling, and managing the lifecycle of virtual machine instances." },
  { unit: "Unit 4", q: "What is Neutron in OpenStack?", a: "Neutron is the <strong>Networking Service</strong> providing virtual networks, subnets, routers, floating IPs, and security groups." },
  { unit: "Unit 4", q: "What is Keystone in OpenStack?", a: "Keystone is the <strong>Identity & Token Service</strong> that handles centralized user authentication, access authorization, and the service catalog." },
  { unit: "Unit 4", q: "What is Cinder vs Swift in OpenStack?", a: "<strong>Cinder:</strong> Persistent Block Storage for VM disks.<br><strong>Swift:</strong> Highly scalable Object Storage for unstructured files/backups." },
  { unit: "Unit 4", q: "What is the 5-tier Apache CloudStack hierarchy?", a: "From top to bottom: <strong>Region &rarr; Zone &rarr; Pod &rarr; Cluster &rarr; Host</strong>." },
  { unit: "Unit 4", q: "Which storage type is best for OS boot drives and DBs?", a: "<strong>Block Storage</strong> (e.g. AWS EBS, Azure Managed Disks) because of low latency, addressable blocks, and high IOPS." },
  { unit: "Unit 4", q: "Which storage type uses Buckets and HTTP APIs?", a: "<strong>Object Storage</strong> (e.g. AWS S3, Azure Blob, Google Cloud Storage). Stores data + custom metadata + globally unique key." },
  { unit: "Unit 4", q: "What are the 3 layers of Software-Defined Networking (SDN)?", a: "1. <strong>Application Layer</strong> (Policies, Apps)<br>2. <strong>Control Layer</strong> (SDN Controller - Central Intelligence)<br>3. <strong>Infrastructure Layer</strong> (Packet Forwarding Switches)." },

  // --- Unit 5 Flashcards ---
  { unit: "Unit 5", q: "What are the 4 Pillars of Cloud Security?", a: "1. <strong>Infrastructure Security</strong><br>2. <strong>Data Security</strong><br>3. <strong>Network Security</strong><br>4. <strong>Application Security</strong>." },
  { unit: "Unit 5", q: "What does the CIA Triad represent?", a: "<strong>Confidentiality</strong> (prevent unauthorized access), <strong>Integrity</strong> (prevent unauthorized alteration/tampering), and <strong>Availability</strong> (ensure reliable access)." },
  { unit: "Unit 5", q: "What is the Cardinal Rule of AWS IAM Policy Evaluation?", a: "<strong>Explicit Deny overrides Allow!</strong> If even ONE matching policy has a Deny effect, the final decision is unconditionally DENIED." },
  { unit: "Unit 5", q: "What is the Principle of Least Privilege?", a: "Users, roles, and programs should be granted only the absolute minimum permissions necessary to perform their specific job tasks." },
  { unit: "Unit 5", q: "Differentiate Authentication vs Authorization.", a: "<strong>Authentication:</strong> 'Who are you?' (verifies identity via passwords/MFA).<br><strong>Authorization:</strong> 'What can you do?' (determines permissions via policies)." },
  { unit: "Unit 5", q: "What was the core vulnerability in Storm-0558 (2023)?", a: "An inactive Microsoft consumer signing key (MSA key) leaked via crash dump was used to forge authentication tokens for enterprise Exchange Online inboxes." }
];

let currentCardIndex = 0;

function updateFlashcardUI() {
  const card = flashcardsData[currentCardIndex];
  document.getElementById('fcUnitBadge').innerText = card.unit;
  document.getElementById('fcQuestion').innerHTML = card.q;
  document.getElementById('fcAnswer').innerHTML = card.a;
  document.getElementById('fcCounter').innerText = `Card ${currentCardIndex + 1} of ${flashcardsData.length}`;
  document.getElementById('activeFlashcard').classList.remove('flipped');
}

function flipCard() {
  document.getElementById('activeFlashcard').classList.toggle('flipped');
}

function nextCard() {
  currentCardIndex = (currentCardIndex + 1) % flashcardsData.length;
  updateFlashcardUI();
}

function prevCard() {
  currentCardIndex = (currentCardIndex - 1 + flashcardsData.length) % flashcardsData.length;
  updateFlashcardUI();
}

function shuffleCards() {
  for (let i = flashcardsData.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [flashcardsData[i], flashcardsData[j]] = [flashcardsData[j], flashcardsData[i]];
  }
  currentCardIndex = 0;
  updateFlashcardUI();
}

// 52-Question Comprehensive Exam Simulator (100% Course Syllabus)
const quizQuestions = [
  // ==================== UNIT 1 QUESTIONS (1 to 10) ====================
  {
    category: "unit1",
    q: "Q1. What is Cloud Computing?",
    options: ["Physical hardware purchase", "Delivery of computing services over the Internet", "Only data storage", "Operating system"],
    answer: 1,
    explanation: "Cloud Computing is the delivery of computing services (servers, storage, databases, networking, software) over the Internet on a pay-as-you-go basis."
  },
  {
    category: "unit1",
    q: "Q2. Which is a major characteristic of Cloud Computing?",
    options: ["Resource Pooling", "No Internet required", "Fixed resources only", "Manual billing only"],
    answer: 0,
    explanation: "Resource Pooling is one of the 5 NIST essential characteristics, where physical and virtual resources are dynamically pooled to serve multiple consumers."
  },
  {
    category: "unit1",
    q: "Q3. Which pricing model is commonly used in cloud computing?",
    options: ["Fixed hardware purchase", "Pay-as-you-go", "One-time hardware ownership", "No billing"],
    answer: 1,
    explanation: "Cloud computing follows a utility-based Pay-As-You-Go pricing model, converting heavy upfront CapEx into flexible ongoing OpEx."
  },
  {
    category: "unit1",
    q: "Q4. What is Vendor Lock-in?",
    options: ["Physical server failure", "Difficulty migrating between providers", "Automatic scaling", "Data backup"],
    answer: 1,
    explanation: "Vendor Lock-in occurs when an organization becomes dependent on a single cloud vendor's proprietary APIs and tools, making migration expensive and difficult."
  },
  {
    category: "unit1",
    q: "Q5. Which AWS tool is used for infrastructure monitoring?",
    options: ["CloudWatch", "Word", "Excel", "S3 only"],
    answer: 0,
    explanation: "Amazon CloudWatch is AWS's monitoring service that tracks metrics (CPU, RAM, disk, network), collects logs, and triggers automated scaling alarms."
  },
  {
    category: "unit1",
    q: "Q6. Which software creates and manages Virtual Machines?",
    options: ["Compiler", "Hypervisor", "Browser", "Database"],
    answer: 1,
    explanation: "A Hypervisor (Virtual Machine Monitor / VMM) is software or firmware that creates, isolates, and manages multiple virtual machines on a single physical host."
  },
  {
    category: "unit1",
    q: "Q7. Which hypervisor runs directly on physical hardware?",
    options: ["Type 2", "Type 1", "Hosted only", "Application hypervisor"],
    answer: 1,
    explanation: "A Type 1 (Bare-Metal) Hypervisor (e.g. VMware ESXi, Hyper-V, KVM) runs directly on bare-metal hardware without requiring a host operating system."
  },
  {
    category: "unit1",
    q: "Q8. What is a VM?",
    options: ["Physical data centre", "Software-based computer", "Network cable", "Cloud provider"],
    answer: 1,
    explanation: "A Virtual Machine (VM) is an isolated software-based emulation of a physical computer equipped with virtual CPU, memory, storage, and guest OS."
  },
  {
    category: "unit1",
    q: "Q9. Which service model provides virtualized infrastructure?",
    options: ["SaaS", "PaaS", "IaaS", "None"],
    answer: 2,
    explanation: "Infrastructure as a Service (IaaS) provides virtualized raw infrastructure including VMs, storage disks, and virtual private networks."
  },
  {
    category: "unit1",
    q: "Q10. Amazon EC2 belongs to which model?",
    options: ["SaaS", "IaaS", "PaaS", "Community Cloud"],
    answer: 1,
    explanation: "Amazon EC2 (Elastic Compute Cloud) is AWS's flagship IaaS offering, providing resizable virtual compute instances in the cloud."
  },

  // ==================== UNIT 2 QUESTIONS (11 to 20) ====================
  {
    category: "unit2",
    q: "Q11. What is an AMI?",
    options: ["Application Management Interface", "Amazon Machine Image", "Automatic Memory Integration", "Amazon Monitoring Instance"],
    answer: 1,
    explanation: "An Amazon Machine Image (AMI) is a pre-configured template containing the operating system, applications, and settings required to launch an EC2 instance."
  },
  {
    category: "unit2",
    q: "Q12. Google Compute Engine is provided by:",
    options: ["Microsoft", "Amazon", "Google Cloud", "Oracle"],
    answer: 2,
    explanation: "Google Compute Engine (GCE) is Google Cloud Platform's (GCP) Infrastructure as a Service offering delivering scalable virtual machines."
  },
  {
    category: "unit2",
    q: "Q13. Which service model provides a ready-to-use development platform?",
    options: ["IaaS", "PaaS", "SaaS", "Traditional IT"],
    answer: 1,
    explanation: "Platform as a Service (PaaS) provides developers with a configured development environment, runtime, and database services so they can focus on writing code."
  },
  {
    category: "unit2",
    q: "Q14. Which is a PaaS service?",
    options: ["Amazon EC2", "Google App Engine", "Google Docs", "Microsoft Word desktop"],
    answer: 1,
    explanation: "Google App Engine (GAE) is a premier PaaS platform where developers deploy web applications without managing servers or operating systems."
  },
  {
    category: "unit2",
    q: "Q15. AWS Elastic Beanstalk is used for:",
    options: ["Only file storage", "Application deployment and management", "Word processing", "Physical hardware manufacturing"],
    answer: 1,
    explanation: "AWS Elastic Beanstalk is a managed PaaS service that automatically handles provisioning, load balancing, auto-scaling, and health monitoring for deployed applications."
  },
  {
    category: "unit2",
    q: "Q16. Which environment tier handles background processing in Elastic Beanstalk?",
    options: ["Web Server Environment", "Worker Environment", "Client Environment", "Storage Environment"],
    answer: 1,
    explanation: "In AWS Elastic Beanstalk, the Worker Environment handles asynchronous background jobs by pulling tasks from an Amazon SQS message queue."
  },
  {
    category: "unit2",
    q: "Q17. Which model provides complete ready-made software?",
    options: ["IaaS", "PaaS", "SaaS", "Virtualization"],
    answer: 2,
    explanation: "Software as a Service (SaaS) delivers complete, ready-to-use applications over the Internet accessed via a web browser or mobile client."
  },
  {
    category: "unit2",
    q: "Q18. Google Docs is an example of:",
    options: ["IaaS", "PaaS", "SaaS", "Hypervisor"],
    answer: 2,
    explanation: "Google Docs is a cloud-native SaaS application allowing real-time multi-user document creation and editing without local software installation."
  },
  {
    category: "unit2",
    q: "Q19. Which layer includes databases and file storage in the SaaS architecture from your PPT?",
    options: ["Client Layer", "Application Layer", "Data Layer", "Infrastructure Layer"],
    answer: 2,
    explanation: "The 4-layer SaaS architecture includes: Client Layer (UI), Application Layer (Logic/APIs), Data Layer (Databases/Storage), and Infrastructure Layer (VMs/Network)."
  },
  {
    category: "unit2",
    q: "Q20. Who mainly manages the operating system in IaaS?",
    options: ["Cloud customer", "Cloud provider", "End user only", "Internet provider"],
    answer: 0,
    explanation: "Under IaaS Shared Responsibility, the cloud provider manages physical hardware and hypervisors, while the cloud customer is responsible for managing the guest OS."
  },

  // ==================== UNIT 3 QUESTIONS (21 to 32) ====================
  {
    category: "unit3",
    q: "Q21. Which cloud model is dedicated to a single organization?",
    options: ["Public", "Private", "Community", "Multi-Cloud"],
    answer: 1,
    explanation: "A Private Cloud is dedicated exclusively to a single organization (e.g. UIDAI Aadhaar, Indian Bank), providing maximum data privacy and complete infrastructure control."
  },
  {
    category: "unit3",
    q: "Q22. Which deployment model combines public and private cloud?",
    options: ["Community", "Multi-Cloud", "Hybrid", "Public"],
    answer: 2,
    explanation: "A Hybrid Cloud combines two or more distinct cloud environments (commonly private and public) bound together to enable data portability and Cloud Bursting."
  },
  {
    category: "unit3",
    q: "Q23. Which model uses services from multiple cloud providers?",
    options: ["Private", "Public", "Hybrid", "Multi-Cloud"],
    answer: 3,
    explanation: "The Multi-Cloud model uses services from two or more independent cloud vendors (e.g. AWS + Azure + GCP) to diversify risk and avoid vendor lock-in."
  },
  {
    category: "unit3",
    q: "Q24. Which architecture serves multiple customers using one application instance?",
    options: ["Multi-Server", "Multi-Tenant", "Distributed", "Centralized"],
    answer: 1,
    explanation: "Multi-Tenant Architecture runs a single application instance serving multiple customers (tenants) on shared infrastructure while strictly isolating each tenant's data."
  },
  {
    category: "unit3",
    q: "Q25. Which database pattern provides the highest tenant isolation?",
    options: ["Pool", "Bridge", "Silo", "Shared table"],
    answer: 2,
    explanation: "The Silo Pattern provisions a separate, dedicated database instance for each tenant, ensuring zero possibility of cross-tenant query leakage."
  },
  {
    category: "unit3",
    q: "Q26. Which scaling method adds more machines?",
    options: ["Vertical", "Horizontal", "Diagonal only", "Static"],
    answer: 1,
    explanation: "Horizontal Scaling (Scale Out) adds more physical or virtual machines into the server cluster; Vertical Scaling (Scale Up) upgrades CPU/RAM on an existing machine."
  },
  {
    category: "unit3",
    q: "Q27. Which component distributes incoming requests across servers?",
    options: ["Database", "Firewall", "Load Balancer", "DNS record"],
    answer: 2,
    explanation: "A Load Balancer distributes incoming network and application traffic across a pool of healthy backend servers to prevent overload and ensure high availability."
  },
  {
    category: "unit3",
    q: "Q28. Which layer represents the user side of cloud architecture?",
    options: ["Back End", "Front End", "Storage", "Compute"],
    answer: 1,
    explanation: "The Front End represents client devices, web browsers, mobile applications, and user interfaces through which users interact with cloud services."
  },
  {
    category: "unit3",
    q: "Q29. Which provider offers BigQuery?",
    options: ["AWS", "Azure", "Google Cloud", "Oracle only"],
    answer: 2,
    explanation: "BigQuery is Google Cloud Platform's serverless, highly scalable multi-cloud data warehouse engineered for petabyte-scale SQL analytics."
  },
  {
    category: "unit3",
    q: "Q30. A collection of independent computers working together is called:",
    options: ["Single-Tenant", "Private Cloud", "Distributed System", "Single Server"],
    answer: 2,
    explanation: "A Distributed System is a collection of autonomous, independent computers connected by a network that coordinate actions to appear to users as a single coherent system."
  },
  {
    category: "unit3",
    q: "Q31. Which load balancing algorithm sends requests in sequence?",
    options: ["IP Hash", "Round Robin", "Least Connections", "Response Time"],
    answer: 1,
    explanation: "The Round Robin algorithm distributes incoming requests cyclically and sequentially across servers (Request 1 &rarr; Server 1, Request 2 &rarr; Server 2, Request 3 &rarr; Server 3, Request 4 &rarr; Server 1)."
  },
  {
    category: "unit3",
    q: "Q32. What does fault tolerance mean?",
    options: [
      "Increase server cost",
      "Stop all requests",
      "Continue functioning despite component failures",
      "Store only one backup"
    ],
    answer: 2,
    explanation: "Fault Tolerance is the ability of an architectural system to continue functioning with zero downtime and zero data loss even when one or more components fail."
  },

  // ==================== UNIT 4 QUESTIONS (33 to 42) ====================
  {
    category: "unit4",
    q: "Q33. Which hypervisor runs directly on bare-metal physical hardware without an underlying host operating system?",
    options: ["Type 1", "Type 2", "Hosted", "Application"],
    answer: 0,
    explanation: "Type 1 (Bare-Metal, e.g. VMware ESXi, Hyper-V, KVM) runs directly on physical server hardware, delivering high performance and hardware-enforced isolation."
  },
  {
    category: "unit4",
    q: "Q34. Which Docker component is a declarative text document containing build instructions to assemble an image?",
    options: ["Docker Container", "Dockerfile", "Docker Hub", "Docker Daemon"],
    answer: 1,
    explanation: "A Dockerfile contains instructions (FROM, RUN, COPY, CMD) used by the Docker daemon to assemble an immutable container image."
  },
  {
    category: "unit4",
    q: "Q35. Which OpenStack core component is responsible for managing virtual machine lifecycle (compute)?",
    options: ["Neutron", "Keystone", "Nova", "Swift"],
    answer: 2,
    explanation: "Nova is the compute engine in OpenStack that provisions, starts, stops, and schedules virtual machines."
  },
  {
    category: "unit4",
    q: "Q36. Which cloud storage type is best suited for virtual machine operating system boot disks and relational databases?",
    options: ["Object Storage", "File Storage", "Block Storage", "Archive Storage"],
    answer: 2,
    explanation: "Block storage (e.g. AWS EBS) provides low-latency, raw addressable block volumes with high IOPS essential for OS boot disks."
  },
  {
    category: "unit4",
    q: "Q37. In Software-Defined Networking (SDN), which layer contains the SDN Controller and decides how traffic is managed?",
    options: ["Application Layer", "Control Layer", "Infrastructure Layer", "Physical Layer"],
    answer: 1,
    explanation: "The Control Layer houses the centralized SDN Controller, maintaining global network topology and calculating flow table routing rules."
  },
  {
    category: "unit4",
    q: "Q38. In the Hypervisor Reference Model, which component receives instructions from VMs and directs them?",
    options: ["Allocator", "Dispatcher", "Interpreter", "Scheduler"],
    answer: 1,
    explanation: "The Dispatcher acts as the entry point of the monitor, receiving VM instructions and rerouting them to the Allocator or Interpreter."
  },
  {
    category: "unit4",
    q: "Q39. What is the fundamental architectural difference between Docker containers and Virtual Machines?",
    options: [
      "Containers run a full guest OS kernel, while VMs do not",
      "Containers share the host OS kernel, while VMs run full independent guest OSs",
      "VMs cannot run on Linux servers",
      "Containers require dedicated physical hardware"
    ],
    answer: 1,
    explanation: "Containers share the host operating system kernel and isolate processes via cgroups and namespaces, making them lightweight and fast to boot."
  },
  {
    category: "unit4",
    q: "Q40. In OpenStack, which service provides Identity, authentication, and token management?",
    options: ["Glance", "Keystone", "Cinder", "Horizon"],
    answer: 1,
    explanation: "Keystone is the OpenStack Identity service providing authentication, authorization, and service catalog endpoints."
  },
  {
    category: "unit4",
    q: "Q41. What is the correct top-to-bottom resource hierarchy in Apache CloudStack?",
    options: [
      "Region > Zone > Pod > Cluster > Host",
      "Zone > Region > Cluster > Pod > Host",
      "Pod > Zone > Region > Host > Cluster",
      "Host > Cluster > Pod > Zone > Region"
    ],
    answer: 0,
    explanation: "CloudStack strictly follows the 5-tier physical hierarchy: Region > Zone (Datacenter) > Pod (Rack) > Cluster (Shared storage pool) > Host (Hypervisor server)."
  },
  {
    category: "unit4",
    q: "Q42. In a Content Delivery Network (CDN), what occurs when a user requests an asset already present in the local edge cache?",
    options: ["Cache Miss", "Cache Invalidation", "Cache Hit", "Origin Fetch"],
    answer: 2,
    explanation: "A Cache Hit occurs when the requested resource is found in the edge server's cache, serving it immediately without contacting the origin server."
  },

  // ==================== UNIT 5 QUESTIONS (43 to 52) ====================
  {
    category: "unit5",
    q: "Q43. Authentication answers which fundamental security question?",
    options: ["What are you allowed to do?", "Who are you?", "Where is the data stored?", "How much does it cost?"],
    answer: 1,
    explanation: "Authentication verifies identity ('Who are you?'), whereas Authorization evaluates permissions ('What are you permitted to do?')."
  },
  {
    category: "unit5",
    q: "Q44. In AWS IAM policy evaluation logic, which rule takes precedence unconditionally?",
    options: ["Explicit Allow overrides Deny", "Explicit Deny overrides Allow", "Implicit Allow overrides Deny", "Role policy overrides User policy"],
    answer: 1,
    explanation: "The explicit Deny rule is cardinal: an explicit Deny unconditionally overrides any number of explicit Allows in AWS IAM."
  },
  {
    category: "unit5",
    q: "Q45. What does the 'I' in the CIA Triad stand for?",
    options: ["Identity", "Integrity", "Isolation", "Infrastructure"],
    answer: 1,
    explanation: "CIA stands for Confidentiality, Integrity (accuracy and tamper-resistance), and Availability."
  },
  {
    category: "unit5",
    q: "Q46. Increasing a virtual machine's RAM from 4 GB to 16 GB is an example of which type of scaling?",
    options: ["Horizontal Scaling (Scale Out)", "Vertical Scaling (Scale Up)", "Elasticity", "Diagonal Scaling"],
    answer: 1,
    explanation: "Vertical scaling (Scale Up) increases compute, RAM, or storage specifications on an existing node."
  },
  {
    category: "unit5",
    q: "Q47. Which major incident involved forged authentication tokens using a leaked consumer cryptographic signing key in 2023?",
    options: ["Capital One Breach", "Storm-0558", "Midnight Blizzard", "SolarWinds"],
    answer: 1,
    explanation: "Storm-0558 was the Microsoft cloud compromise where a stolen MSA key was used to forge OpenID authentication tokens for Exchange Online."
  },
  {
    category: "unit5",
    q: "Q48. What was the primary exploit vector in the 2019 Capital One cloud breach on AWS?",
    options: [
      "SQL Injection into MySQL database",
      "SSRF vulnerability in a misconfigured WAF querying EC2 Instance Metadata Service",
      "Phishing password attack on root user",
      "Hardware hypervisor escape exploit"
    ],
    answer: 1,
    explanation: "An SSRF flaw in a WAF allowed the attacker to query the AWS IMDSv1 service at 169.254.169.254 to steal IAM role credentials and exfiltrate S3 data."
  },
  {
    category: "unit5",
    q: "Q49. Which regulation specifically protects the privacy and personal data of European Union citizens with strict breach notifications?",
    options: ["HIPAA", "PCI DSS", "GDPR", "ISO 27017"],
    answer: 2,
    explanation: "GDPR (General Data Protection Regulation) is the EU legal framework protecting personal data and privacy."
  },
  {
    category: "unit5",
    q: "Q50. What is the Principle of Least Privilege in cloud IAM?",
    options: [
      "Granting users full AdministratorAccess to avoid tickets",
      "Granting only the bare minimum permissions necessary to complete assigned duties",
      "Denying all access to cloud systems permanently",
      "Sharing a single set of root credentials among team members"
    ],
    answer: 1,
    explanation: "The Principle of Least Privilege dictates granting identities only the minimum permissions necessary for their immediate legitimate functions."
  },
  {
    category: "unit5",
    q: "Q51. What is an IAM Role in AWS?",
    options: [
      "A permanent user account with a console password",
      "An assumable identity with specific permissions providing temporary security credentials",
      "A collection of IAM users",
      "A network firewall rule"
    ],
    answer: 1,
    explanation: "An IAM Role is an assumable identity that provides temporary credentials via AWS STS, commonly used by applications and EC2 instances."
  },
  {
    category: "unit5",
    q: "Q52. Which cloud security term describes the legal concept that data is governed by the laws of the nation where it physically resides?",
    options: ["Data Residency", "Data Sovereignty", "Data Multi-Tenancy", "Data Isolation"],
    answer: 1,
    explanation: "Data Sovereignty refers to data being subject to the legal governance and subpoena authority of the country where it is physically stored."
  }
];

let userAnswers = {};
let activeQuizFilter = 'all';

function renderQuiz() {
  const container = document.getElementById('quizQuestionsList');
  if (!container) return;
  
  const filtered = quizQuestions.filter(q => activeQuizFilter === 'all' || q.category === activeQuizFilter);
  
  container.innerHTML = filtered.map((item, idx) => {
    const originalIndex = quizQuestions.indexOf(item);
    const isAnswered = userAnswers[originalIndex] !== undefined;
    const selectedOption = userAnswers[originalIndex];
    
    return `
      <div class="quiz-card" id="qcard-${originalIndex}">
        <div class="quiz-card-header">
          <span>Question ${idx + 1} of ${filtered.length}</span>
          <span class="badge ${item.category === 'unit1' || item.category === 'unit2' ? 'badge-accent' : (item.category === 'unit4' || item.category === 'unit5' ? 'badge-priority' : '')}">
            ${item.category.toUpperCase()}
          </span>
        </div>
        <div class="quiz-question-text">${item.q}</div>
        <div class="quiz-options">
          ${item.options.map((opt, optIdx) => {
            let extraClass = '';
            if (isAnswered) {
              if (optIdx === item.answer) extraClass = 'correct';
              else if (optIdx === selectedOption) extraClass = 'incorrect';
            }
            return `
              <div class="quiz-option ${extraClass}" onclick="handleOptionSelect(${originalIndex}, ${optIdx})">
                <span style="font-weight: 700; width: 20px;">${String.fromCharCode(65 + optIdx)}.</span>
                <span>${opt}</span>
              </div>
            `;
          }).join('')}
        </div>
        <div class="quiz-explanation" id="exp-${originalIndex}" style="display: ${isAnswered ? 'block' : 'none'};">
          <strong>${selectedOption === item.answer ? '✔️ Correct!' : '❌ Incorrect.'}</strong> ${item.explanation}
        </div>
      </div>
    `;
  }).join('');
  
  updateScoreAndProgress();
}

function handleOptionSelect(qIdx, optIdx) {
  if (userAnswers[qIdx] !== undefined) return; // Prevent re-answering
  userAnswers[qIdx] = optIdx;
  renderQuiz();
}

function updateScoreAndProgress() {
  const answeredCount = Object.keys(userAnswers).length;
  let correctCount = 0;
  for (const [qIdx, chosen] of Object.entries(userAnswers)) {
    if (chosen === quizQuestions[qIdx].answer) {
      correctCount++;
    }
  }
  
  const scoreBadge = document.getElementById('liveScoreBadge');
  if (scoreBadge) {
    scoreBadge.innerText = `Score: ${correctCount} / ${answeredCount} (${answeredCount > 0 ? Math.round((correctCount/answeredCount)*100) : 0}%)`;
  }
  
  const progBar = document.getElementById('quizProgressBar');
  if (progBar) {
    progBar.style.width = `${(answeredCount / quizQuestions.length) * 100}%`;
  }
}

function filterQuiz(cat, btn) {
  activeQuizFilter = cat;
  document.querySelectorAll('.quiz-filter .btn').forEach(b => b.classList.remove('btn-primary'));
  if (btn) btn.classList.add('btn-primary');
  renderQuiz();
}

function resetQuiz() {
  userAnswers = {};
  renderQuiz();
}

// Question Bank Accordions
function toggleAccordion(header) {
  header.classList.toggle('open');
  const content = header.nextElementSibling;
  content.classList.toggle('open');
}

function toggleAllAccordions() {
  const headers = document.querySelectorAll('.accordion-header');
  const allOpen = Array.from(headers).every(h => h.classList.contains('open'));
  headers.forEach(h => {
    if (allOpen) {
      h.classList.remove('open');
      h.nextElementSibling.classList.remove('open');
    } else {
      h.classList.add('open');
      h.nextElementSibling.classList.add('open');
    }
  });
}

function filterQBank(markFilter, btn) {
  document.querySelectorAll('.accordion-item').forEach(item => {
    const isU45 = item.getAttribute('data-u45') === 'true';
    if (markFilter === 'all') {
      item.style.display = 'block';
    } else if (markFilter === 'u45') {
      item.style.display = isU45 ? 'block' : 'none';
    } else if (item.getAttribute('data-marks') === markFilter) {
      item.style.display = 'block';
    } else {
      item.style.display = 'none';
    }
  });
  if (btn) {
    btn.parentElement.querySelectorAll('.btn').forEach(b => b.classList.remove('btn-primary'));
    btn.classList.add('btn-primary');
  }
}

// Global Live Search Across All Tabs and Accordions
function handleLiveSearch(query) {
  const q = query.trim().toLowerCase();
  if (!q) {
    document.querySelectorAll('.main-topic-card, .sub-topic-card, .accordion-item').forEach(el => el.style.display = 'block');
    return;
  }
  
  document.querySelectorAll('.main-topic-card').forEach(mainCard => {
    let mainMatches = false;
    mainCard.querySelectorAll('.sub-topic-card').forEach(subCard => {
      const text = subCard.innerText.toLowerCase();
      if (text.includes(q)) {
        subCard.style.display = 'block';
        // Auto expand matching subtopic
        const subHeader = subCard.querySelector('.sub-topic-header');
        const subDetail = subCard.querySelector('.sub-topic-detail');
        if (subHeader) subHeader.classList.add('open');
        if (subDetail) subDetail.classList.add('open');
        mainMatches = true;
      } else {
        subCard.style.display = 'none';
      }
    });

    if (mainMatches) {
      mainCard.style.display = 'block';
      const mainHeader = mainCard.querySelector('.main-topic-header');
      const mainBody = mainCard.querySelector('.main-topic-body');
      if (mainHeader) mainHeader.classList.add('open');
      if (mainBody) mainBody.classList.add('open');
    } else {
      mainCard.style.display = 'none';
    }
  });

  document.querySelectorAll('.accordion-item').forEach(item => {
    const text = item.innerText.toLowerCase();
    if (text.includes(q)) {
      item.style.display = 'block';
      const header = item.querySelector('.accordion-header');
      const content = item.querySelector('.accordion-content');
      if (header) header.classList.add('open');
      if (content) content.classList.add('open');
    } else {
      item.style.display = 'none';
    }
  });
}

// Initialize on Load


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
    const isU45 = card.getAttribute('data-u45') === 'true';
    let show = false;
    if (filter === 'all') show = true;
    else if (filter === 'u45' && (isU45 || tier === 'tier1')) show = true;
    else if (filter === 'tier1' && (tier === 'tier1' || isU45)) show = true;
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
const U45_GUARANTEED_ITEMS = __U45_ITEMS_PLACEHOLDER__;

const ALL_QUESTIONS_POOL = [
  ...U45_GUARANTEED_ITEMS,
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

  // --- 10-Mark Comprehensive Architectural Questions (8 Master Questions) ---
  {
    unit: 'Unit 4: Virtualization',
    marks: '10 Marks',
    type: 'Comprehensive Architecture',
    question: 'Comprehensive Virtualization Architecture: Explain Full Virtualization, Paravirtualization, and Hardware-Assisted Virtualization with neat diagrams. Explain Popek-Goldberg Theorem, Intel VT-x VMX Root/Non-Root modes, and discuss Compute, Storage, and Network Virtualization.',
    answerHtml: `<strong>Model Answer & Master Blueprint:</strong><br>
    <strong>1. Popek-Goldberg Virtualization Theorem (1974):</strong>
    An architecture is strictly virtualizable if and only if all sensitive instructions (modify hardware state or read hardware configurations) are a subset of privileged instructions (instructions that trap when executed in user mode): <code>Sensitive ⊆ Privileged</code>. Classical x86 had 17 sensitive unprivileged instructions (e.g. <code>POPF, SGDT, SMSW</code>) that failed silently, creating the x86 virtualization hole.<br><br>
    <strong>2. Three CPU Virtualization Models:</strong>
    <ul>
      <li><strong>Full Virtualization:</strong> Unmodified Guest OS runs in Ring 1; Hypervisor in Ring 0 uses dynamic <em>Binary Translation</em> to intercept sensitive instructions. 100% OS compatibility, but 5–15% CPU overhead.</li>
      <li><strong>Paravirtualization:</strong> Guest OS kernel source code is modified with <em>Hypercalls</em> (software traps) directed to the hypervisor. Near-native speed, but requires hypervisor-aware OS (Xen PV).</li>
      <li><strong>Hardware-Assisted Virtualization (Intel VT-x / AMD-V):</strong> CPU silicon introduces <em>VMX Root Mode</em> (Hypervisor) and <em>VMX Non-Root Mode</em> (Guest OS). Traps trigger a hardware <strong>VM-Exit</strong>; hypervisor resumes guest execution via <code>VMRESUME</code> (<strong>VM-Entry</strong>). Extended Page Tables (EPT) handle hardware memory address translation.</li>
    </ul>
    <strong>3. Three Virtualization Domains:</strong>
    <ul>
      <li><strong>Compute:</strong> Hypervisors abstract CPU cores into vCPUs and manage memory overcommit via dynamic ballooning drivers.</li>
      <li><strong>Storage:</strong> Pooling physical SAN/NAS disk arrays into elastic virtual volumes via LVM, Ceph, and OpenStack Cinder.</li>
      <li><strong>Network:</strong> Decouples physical routers and cables using Virtual Switches (Open vSwitch), VLANs, and 24-bit VXLAN overlay encapsulation.</li>
    </ul>`,
    tip: 'Score breakdown: 2M Popek-Goldberg theorem & x86 hole; 3M Three CPU virtualization techniques with diagrams; 2M Intel VT-x VMX Root/Non-Root and VM-Exit/VM-Entry; 2M Compute, Storage, Network domains; 1M Comparison table.',
    googleQuery: 'Compute Storage Network Virtualization Hardware Assisted Intel VT Diagram',
    markCat: '10m',
    unitKey: 'unit4'
  },
  {
    unit: 'Unit 4: Virtualization',
    marks: '10 Marks',
    type: 'Comprehensive Architecture',
    question: 'OpenStack Cloud Operating System: Detail the architecture of OpenStack, all 9 Core Components, internal daemons, and trace the complete 12-Step VM Provisioning Workflow.',
    answerHtml: `<strong>Model Answer & Master Blueprint:</strong><br>
    <strong>1. Architectural Philosophy:</strong>
    OpenStack is a modular open-source IaaS cloud operating system. All microservices communicate asynchronously via the <strong>RabbitMQ AMQP message bus</strong>, store state in a shared <strong>MariaDB/MySQL</strong> database, and expose uniform RESTful APIs.<br><br>
    <strong>2. The 9 Core Components:</strong>
    <ol>
      <li><strong>Keystone (Identity):</strong> Issues authentication tokens (Fernet/UUID), manages user RBAC, and maintains the dynamic API Service Catalog.</li>
      <li><strong>Nova (Compute Fabric):</strong> Provisions and manages VM lifecycles via <code>nova-api</code>, <code>nova-scheduler</code>, <code>nova-conductor</code>, and <code>nova-compute</code>.</li>
      <li><strong>Neutron (Networking):</strong> Software-Defined Networking (SDN) managing virtual networks, subnets, routers, and floating IPs via ML2 and Open vSwitch.</li>
      <li><strong>Glance (Image Registry):</strong> Stores and retrieves base operating system templates (QCOW2, RAW, VMDK).</li>
      <li><strong>Cinder (Block Storage):</strong> Provisions persistent raw block storage volumes attached to instances over iSCSI or Ceph RBD.</li>
      <li><strong>Swift (Object Storage):</strong> Highly scalable distributed object storage ring for unstructured files and media blobs via REST APIs.</li>
      <li><strong>Horizon (Dashboard):</strong> Django-based web management GUI for administrators and self-service tenants.</li>
      <li><strong>Heat (Orchestration):</strong> Template-driven composite cloud application deployment based on YAML Heat Orchestration Templates (HOT).</li>
      <li><strong>Ceilometer (Telemetry):</strong> Collects resource usage meters and performance counters, triggering autoscaling alarms via Aodh.</li>
    </ol>
    <strong>3. 12-Step VM Provisioning Workflow:</strong><br>
    User requests VM via Horizon/CLI &rarr; Authenticated by <strong>Keystone</strong> &rarr; Request arrives at <code>nova-api</code> &rarr; Logged in MariaDB via <code>nova-conductor</code> &rarr; <code>nova-scheduler</code> evaluates filters (RAMFilter, CoreFilter) to select optimal host node &rarr; RPC message published to RabbitMQ &rarr; Target <code>nova-compute</code> receives task &rarr; <strong>Neutron</strong> allocates vNIC, IP, and security groups &rarr; <strong>Glance</strong> streams base QCOW2 image &rarr; <strong>Cinder</strong> attaches persistent block storage &rarr; Local hypervisor (KVM via libvirt) spawns VM &rarr; Status updated to ACTIVE in MariaDB.`,
    tip: 'Score breakdown: 2M Architecture & RabbitMQ/DB bus; 4M 9 Core Components and their internal daemons; 3M 12-Step VM creation sequence; 1M HA Deployment tiering (Controller, Compute, Storage nodes).',
    googleQuery: 'OpenStack Architecture Nova Neutron Keystone Glance Diagram',
    markCat: '10m',
    unitKey: 'unit4'
  },
  {
    unit: 'Unit 3: Architecture',
    marks: '10 Marks',
    type: 'Comprehensive Architecture',
    question: 'Multi-Tenant Architecture: Analyze Silo, Bridge, and Pool Data Isolation Models, explain Row-Level Security (RLS) implementation, and detail mitigation engineering for the Noisy Neighbor Problem.',
    answerHtml: `<strong>Model Answer & Master Blueprint:</strong><br>
    <strong>1. Definition & Economics:</strong>
    Multi-Tenancy is an architectural model where a single software instance runs on shared cloud servers to serve multiple independent customer organizations (tenants), while logically segregating their data, custom configurations, and user accounts. Reduces operational Cost of Goods Sold (COGS) by 70–90% compared to running separate VM clusters per tenant.<br><br>
    <strong>2. The 3 Database Isolation Models:</strong>
    <ul>
      <li><strong>Silo Model (Dedicated DB per Tenant):</strong> Maximum isolation, zero cross-tenant blast radius, customized DB settings, highest infrastructure cost. Ideal for Banks, Defense, and Healthcare.</li>
      <li><strong>Bridge Model (Shared Engine, Dedicated Schemas):</strong> Balanced cost and security. Schema boundaries isolate tenant tables on a shared database server engine.</li>
      <li><strong>Pool Model (Shared DB, Shared Tables):</strong> Lowest cost, maximum server utilization, instantaneous tenant onboarding. Every table contains a <code>tenant_id</code> discriminator column. Requires strict Row-Level Security (RLS).</li>
    </ul>
    <strong>3. Row-Level Security (RLS) Enforcement:</strong><br>
    Enabled via native PostgreSQL policy: <code>CREATE POLICY tenant_iso ON orders FOR ALL USING (tenant_id = current_setting('app.tenant_id')::UUID);</code>. Application sets the tenant context upon DB connection; queries automatically filter rows belonging strictly to that tenant.<br><br>
    <strong>4. Noisy Neighbor Mitigation Engineering:</strong><br>
    (1) Token-Bucket & Leaky-Bucket per-tenant API rate limiting, (2) Linux Cgroup quotas restricting CPU and memory hogging, (3) Partitioned database connection pools via PgBouncer, (4) Automated "Whale Migration" promoting heavy tenants from Pool to dedicated Silo instances.`,
    tip: 'Score breakdown: 2M Definition & COGS economics; 3M Silo vs Bridge vs Pool with diagrams; 2M Row-Level Security SQL implementation; 2M Noisy Neighbor causes and mitigation algorithms; 1M 7-parameter comparison table.',
    googleQuery: 'Multi Tenant Database Architecture Silo Bridge Pool Diagram',
    markCat: '10m',
    unitKey: 'unit3'
  },
  {
    unit: 'Unit 5: Cloud Security & IAM',
    marks: '10 Marks',
    type: 'Comprehensive Architecture',
    question: 'Cloud Security Forensics & Real-World Breaches: Analyze the Capital One SSRF on IMDSv1, Microsoft Storm-0558 Token Forgery, Code Spaces Root Liquidation, and formulate a Layered Defense-in-Depth Architecture.',
    answerHtml: `<strong>Model Answer & Master Blueprint:</strong><br>
    <strong>1. Case Study 1: Capital One SSRF Breach (2019) — AWS:</strong><br>
    Attacker exploited a Server-Side Request Forgery (SSRF) flaw in a misconfigured ModSecurity WAF running on an EC2 instance. The WAF was coerced into querying the AWS Instance Metadata Service v1 at <code>http://169.254.169.254/latest/meta-data/iam/security-credentials/</code>. The service returned temporary IAM role credentials with excessive <code>s3:*</code> privileges, allowing the exfiltration of 106 million customer credit records from 700 S3 buckets.<br>
    <em>Fix:</em> Adopted IMDSv2 (requires session token headers, neutralizing SSRF) and enforced Least Privilege IAM roles.<br><br>
    <strong>2. Case Study 2: Microsoft Storm-0558 Token Forgery (2023) — Azure:</strong><br>
    A private Microsoft Account (MSA) consumer signing key leaked into a Windows kernel memory dump following an internal crash. Threat actors used the stolen key to forge OpenID Connect authentication tokens that were erroneously accepted by Azure AD enterprise endpoints, compromising 25 government email organizations.<br>
    <em>Fix:</em> Automated HSM-bound key rotation, crash dump sanitization, and strict separation of consumer vs enterprise token validation.<br><br>
    <strong>3. Case Study 3: Code Spaces Complete Liquidation (2014) — AWS:</strong><br>
    Attackers compromised the AWS Root Account (lacked MFA). After demanding an extortion ransom that was refused, attackers deleted all EBS volumes, S3 buckets, and backup replicas, forcing the company into complete bankruptcy within 12 hours.<br>
    <em>Fix:</em> Never use root for operations, enforce physical FIDO2 hardware MFA, lock root keys in a corporate vault, and maintain cross-account WORM-locked AWS Backup Vaults.<br><br>
    <strong>4. Layered Cloud Defense-in-Depth Blueprint:</strong><br>
    Perimeter (CloudFront CDN, AWS Shield DDoS, WAF) &rarr; Network (VPC Private Subnets, Security Groups, Flow Logs) &rarr; Host (IMDSv2, CIS hardened AMIs) &rarr; IAM (Least privilege, temporary STS tokens, permission boundaries) &rarr; Data (AES-256 KMS encryption, S3 Block Public Access) &rarr; Monitoring (CloudTrail immutable logs, GuardDuty ML threat detection).`,
    tip: 'Score breakdown: 2M Cloud attack surface & Shared Responsibility; 4M Capital One & Storm-0558 post-mortems; 2M Code Spaces & Root risks; 2M Layered Defense-in-Depth table.',
    googleQuery: 'Capital One SSRF AWS IMDS Metadata Breach Diagram',
    markCat: '10m',
    unitKey: 'unit5'
  },
  {
    unit: 'Unit 5: Cloud Security & IAM',
    marks: '10 Marks',
    type: 'Comprehensive Architecture',
    question: 'AWS IAM Enterprise Architecture: Explain the 4 Core Entities, JSON Policy Grammar, the 6-Step Policy Evaluation Algorithm, and Temporary STS Token Generation.',
    answerHtml: `<strong>Model Answer & Master Blueprint:</strong><br>
    <strong>1. Foundational Doctrines:</strong>
    AWS Identity and Access Management (IAM) governs authentication and authorization under the <em>Principle of Least Privilege (PoLP)</em> and <em>Zero Trust Architecture</em>.<br><br>
    <strong>2. The Four Core IAM Entities:</strong>
    <ul>
      <li><strong>IAM Users:</strong> Persistent identity entities with long-term credentials (passwords, access keys).</li>
      <li><strong>IAM User Groups:</strong> Collections of users sharing job role privileges (Developers, Ops). Cannot be identified as a Principal.</li>
      <li><strong>IAM Roles:</strong> Temporary identities assumed by human engineers, EC2 instances, or Lambda functions. No static credentials; issues short-lived temporary tokens via AWS STS.</li>
      <li><strong>IAM Policies:</strong> JSON permission documents defining fine-grained Allow/Deny controls. Divided into Identity-based and Resource-based policies.</li>
    </ul>
    <strong>3. JSON Policy Grammar:</strong><br>
    Composed of <code>Version</code> ("2012-10-17"), <code>Statement</code> array, <code>Effect</code> (Allow/Deny), <code>Principal</code> (resource policies), <code>Action</code> (e.g. <code>s3:GetObject</code>), <code>Resource</code> (ARN), and <code>Condition</code> (MFA check, source IP CIDR).<br><br>
    <strong>4. 6-Step Evaluation Algorithm (The Absolute Authority of Explicit Deny):</strong><br>
    Step 1: Default Implicit Deny &rarr; Step 2: <strong>Explicit Deny Check</strong> (If ANY statement contains <code>"Effect": "Deny"</code> matching the request, the evaluation halts immediately and access is REJECTED. Explicit Deny overrides all allows!) &rarr; Step 3: Service Control Policies (SCPs) check &rarr; Step 4: Resource-based policy check &rarr; Step 5: IAM Permissions Boundary & Identity Policy check &rarr; Step 6: If at least one Explicit Allow exists and zero Explicit Denies exist, access is ALLOWED; otherwise it defaults to DENY.<br><br>
    <strong>5. AWS STS Temporary Credentials:</strong><br>
    Executing <code>AssumeRole</code> returns temporary credentials valid for 15 minutes to 12 hours: <code>AccessKeyId</code> (prefix <code>ASIA...</code>), <code>SecretAccessKey</code>, and signed <code>SessionToken</code>.`,
    tip: 'Score breakdown: 2M IAM philosophy & PoLP; 2M 4 Core Entities; 2M JSON grammar & policy code example; 3M 6-Step decision algorithm with Explicit Deny rule; 1M AWS STS temporary credential structure.',
    googleQuery: 'AWS IAM Policy Evaluation Logic Flowchart Diagram',
    markCat: '10m',
    unitKey: 'unit5'
  },
  {
    unit: 'Unit 3: Architecture',
    marks: '10 Marks',
    type: 'Comprehensive Architecture',
    question: 'Cloud Deployment Models & Enterprise Migration: Compare Public, Private, Hybrid (Cloud Bursting & Direct Connect), Community Clouds, Multi-Cloud Strategy, and detail the Gartner 6 R\'s Migration Framework.',
    answerHtml: `<strong>Model Answer & Master Blueprint:</strong><br>
    <strong>1. The Four Primary Cloud Deployment Models:</strong>
    <ul>
      <li><strong>Public Cloud (AWS, Azure, GCP):</strong> Owned by third-party CSP, multi-tenant, 100% OpEx (pay-per-use), virtually infinite elastic scale. Ideal for startups and digital products.</li>
      <li><strong>Private Cloud:</strong> Dedicated to a single enterprise (OpenStack, VMware). High data privacy, custom hardware compliance, heavy upfront CapEx. Ideal for Defense and Central Banks.</li>
      <li><strong>Hybrid Cloud:</strong> Orchestrated binding of private and public clouds via dedicated fiber lines (AWS Direct Connect / Azure ExpressRoute) and IPsec VPNs. Enables <em>Cloud Bursting</em> (steady-state on private, excess surge bursts to public).</li>
      <li><strong>Community Cloud:</strong> Shared infrastructure among organizations with shared mission or regulatory compliance (e.g. Interpol, European police, shared genomics research).</li>
    </ul>
    <strong>2. Multi-Cloud Strategy Drivers:</strong><br>
    Utilizing 2+ public cloud providers to prevent vendor lock-in, satisfy national data sovereignty laws (GDPR, India DPDP Act), and ensure extreme disaster resiliency against single-provider global control plane outages.<br><br>
    <strong>3. Gartner 6 R's Cloud Migration Framework:</strong><br>
    <ol>
      <li><strong>Rehost ("Lift and Shift"):</strong> Move VMs directly to EC2 without code changes. Fastest, lowest initial risk.</li>
      <li><strong>Replatform ("Lift, Tinker and Shift"):</strong> Optimize components (e.g. migrate self-hosted DB to AWS RDS managed database) without changing core code.</li>
      <li><strong>Refactor / Re-architect:</strong> Rewrite monolith into cloud-native microservices, containers (Kubernetes), and serverless functions (AWS Lambda).</li>
      <li><strong>Repurchase ("Drop and Shop"):</strong> Discard custom software in favor of SaaS solutions (e.g. Salesforce, Microsoft 365).</li>
      <li><strong>Retain:</strong> Keep applications on-premise due to hardware dependencies or recent capital investments.</li>
      <li><strong>Retire:</strong> Identify and decommission obsolete or redundant applications, saving 10–20% IT budget.</li>
    </ol>`,
    tip: 'Score breakdown: 3M Definitions & characteristics of 4 models; 2M Hybrid Cloud Bursting & Direct Connect; 2M Multi-Cloud drivers & data residency; 2M Gartner 6 R\'s Migration framework; 1M 10-parameter comparative matrix.',
    googleQuery: 'Cloud Deployment Models Public Private Hybrid Community Diagram',
    markCat: '10m',
    unitKey: 'unit3'
  },
  {
    unit: 'Unit 3: Architecture',
    marks: '10 Marks',
    type: 'Comprehensive Architecture',
    question: 'Enterprise Multi-Server 3-Tier Web Architecture: Detail Layer Anatomy, Layer 4 (NLB) vs Layer 7 (ALB) Load Balancing, calculate Serial vs Parallel Availability SLA, and compare Disaster Recovery RTO vs RPO.',
    answerHtml: `<strong>Model Answer & Master Blueprint:</strong><br>
    <strong>1. 3-Tier VPC Architecture:</strong>
    <ul>
      <li><strong>Tier 1: Presentation (Public Subnet):</strong> Internet Gateway, Application Load Balancer terminating SSL/TLS 1.3, Nginx reverse proxy serving cached frontend assets.</li>
      <li><strong>Tier 2: Application (Private Subnet):</strong> Zero public IPs; outbound updates via NAT Gateway. Runs stateless microservice APIs inside an Auto Scaling Group with Redis memory caching.</li>
      <li><strong>Tier 3: Database (Isolated Subnet):</strong> Zero internet route; accepts TCP port 5432 strictly from Tier 2. Multi-AZ Master R/W database with standby replica in AZ-2 and Read-Replicas in AZ-3.</li>
    </ul>
    <strong>2. Layer 4 vs Layer 7 Load Balancing:</strong><br>
    Network Load Balancer (NLB - Layer 4) routes by TCP/UDP port at wire speed (millions RPS, static IP, sub-millisecond latency). Application Load Balancer (ALB - Layer 7) performs deep packet inspection (path routing <code>/api</code> vs <code>/static</code>, host headers, cookie sticky sessions).<br><br>
    <strong>3. High Availability Mathematics & SLA Formulas:</strong><br>
    Fundamental formula: <code>A = MTBF / (MTBF + MTTR) × 100%</code>.<br>
    <ul>
      <li><strong>Serial Components:</strong> Total availability is the product of individual components: <code>A_total = A1 × A2 × A3</code> (99% × 99% = 98.01%).</li>
      <li><strong>Parallel (Redundant) Components:</strong> Components fail only if all fail simultaneously: <code>A_total = 1 - (1 - A1)(1 - A2)</code>. Two 99% servers in parallel deliver <strong>99.99% (Four Nines)</strong>!</li>
    </ul>
    <strong>4. Disaster Recovery Strategies (RTO vs RPO):</strong><br>
    Backup & Restore (RTO: Days, RPO: 24 hrs, Lowest cost) &rarr; Pilot Light (RTO: Hours, RPO: Minutes, Core DB replicating) &rarr; Warm Standby (RTO: Minutes, RPO: Seconds, Scaled-down live fleet) &rarr; Multi-Region Active-Active (RTO: Zero, RPO: Zero, Highest cost).`,
    tip: 'Score breakdown: 3M 3-Tier VPC architecture & subnets diagram; 3M Layer 4 vs Layer 7 load balancing; 2M High availability formulas (Serial vs Parallel) and SLA downtime table; 2M Disaster recovery strategies (RTO vs RPO).',
    googleQuery: 'Three Tier Cloud Web Architecture AWS Diagram',
    markCat: '10m',
    unitKey: 'unit3'
  },
  {
    unit: 'Unit 4: Virtualization',
    marks: '10 Marks',
    type: 'Comprehensive Architecture',
    question: 'Cloud Storage Architectures: Compare Block Storage, Object Storage, and File Storage on 8 parameters. Explain the mathematics of 11-Nines S3 Durability, Erasure Coding, and analyze distributed consistency via the CAP Theorem.',
    answerHtml: `<strong>Model Answer & Master Blueprint:</strong><br>
    <strong>1. Tri-Storage Paradigms:</strong>
    <ol>
      <li><strong>Block Storage (AWS EBS, Azure Disk):</strong> Raw addressable sectors mounted over iSCSI/NVMe-oF. Ultra-low sub-millisecond latency, high IOPS, in-place byte updates. Ideal for OS boot drives and transactional relational databases (MySQL, Oracle).</li>
      <li><strong>Object Storage (AWS S3, GCP Cloud Storage):</strong> Flat namespace (buckets), HTTP REST APIs (GET, PUT, DELETE, HEAD), immutable payloads with custom metadata and unique Keys. Petabyte to exabyte scale. Ideal for static websites, media streaming, data lakes, and backups.</li>
      <li><strong>File Storage (AWS EFS, Azure Files):</strong> Hierarchical folder-and-file directory tree adhering to POSIX standards. Mounted simultaneously across thousands of compute nodes over NFSv4/SMB with distributed file locking.</li>
    </ol>
    <strong>2. The Mathematics of 11-Nines (99.999999999%) S3 Durability:</strong><br>
    Statistically, storing 10,000,000 objects in AWS S3 expects to lose a single object once every 10,000 years! Annual probability of losing an object is <code>10^-11</code>.<br>
    <em>Implementation:</em> Replicated across at least 3 geographically separated Availability Zones (AZs) and encoded using Reed-Solomon Erasure Coding ($k$ data fragments + $m$ parity fragments). Even if an entire datacenter facility is destroyed, objects are reconstructed in milliseconds via automated self-healing daemons.<br><br>
    <strong>3. Distributed Consistency & CAP Theorem:</strong><br>
    Eric Brewer proves distributed systems can guarantee at most 2 of 3: Consistency (C), Availability (A), Partition Tolerance (P). Network packet drops (P) are unavoidable in physical networks, forcing a choice between CP or AP. AWS S3 provides Strong Read-After-Write Consistency for all PUT, LIST, and DELETE calls.<br><br>
    <strong>4. S3 Storage Lifecycle Automation Tiers:</strong><br>
    S3 Standard &rarr; S3 Standard-IA (Infrequent Access, 50% storage savings) &rarr; S3 Glacier Flexible Retrieval &rarr; S3 Glacier Deep Archive ($0.00099/GB/mo, replaces magnetic tape).`,
    tip: 'Score breakdown: 3M Architectural mechanisms of Block, Object, and File storage; 2M 8-Parameter comparison table; 3M 11-Nines durability mathematics and Erasure Coding; 2M CAP Theorem trade-offs and S3 lifecycle automation.',
    googleQuery: 'Block vs File vs Object Storage Cloud Diagram',
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
  if (currentRouletteFilter === 'unit45') return ALL_QUESTIONS_POOL.filter(q => q.unitKey === 'unit4' || q.unitKey === 'unit5' || q.isU45);
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


// Initialize on Load
window.addEventListener('DOMContentLoaded', () => {
  initPowerModes();
  updateFlashcardUI();
  renderQuiz();
  // By default, open the first topic in each unit for immediate readability
  document.querySelectorAll('.main-topic-card:first-of-type').forEach(card => {
    const h = card.querySelector('.main-topic-header');
    const b = card.querySelector('.main-topic-body');
    if (h) h.classList.add('open');
    if (b) b.classList.add('open');
    const subH = card.querySelector('.sub-topic-header:first-of-type');
    const subD = card.querySelector('.sub-topic-detail:first-of-type');
    if (subH) subH.classList.add('open');
    if (subD) subD.classList.add('open');
  });
});
"""

JS_CODE = _RAW_JS_CODE.replace('__U45_ITEMS_PLACEHOLDER__', U45_JS_DATA)

