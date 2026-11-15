# -*- coding: utf-8 -*-

JS_CODE = """
// State Management
let currentTheme = localStorage.getItem('cc_theme') || 'dark';
document.documentElement.setAttribute('data-theme', currentTheme);

// Tab Navigation
function switchTab(tabId) {
  document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
  
  const targetTab = document.getElementById(tabId);
  const targetNav = document.getElementById('nav-' + tabId);
  
  if (targetTab) targetTab.classList.add('active');
  if (targetNav) targetNav.classList.add('active');
  
  window.scrollTo({ top: 0, behavior: 'smooth' });
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
    if (markFilter === 'all' || item.getAttribute('data-marks') === markFilter) {
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
window.addEventListener('DOMContentLoaded', () => {
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
