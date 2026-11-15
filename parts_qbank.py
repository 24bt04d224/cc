# -*- coding: utf-8 -*-

TAB_QBANK_HTML = """
<div id="qbank" class="tab-pane">
  <div class="hero-banner">
    <div class="hero-header">
      <div class="hero-title">University Exam Question Bank & Model Answers</div>
      <div class="hero-badge-group">
        <span class="badge badge-accent">GSFC University BTCS701F</span>
        <span class="badge badge-priority">Units 1 to 5 Complete</span>
        <span class="badge">Model Answers Included</span>
      </div>
    </div>
    <p class="hero-desc">
      Curated repository of standard university examination questions divided by marks weightage (2 Marks, 5 Marks, 7 Marks, and 10 Marks).
      Every question includes a complete, exam-ready model answer with diagrams, comparison tables, formulas, and real-world case studies.
    </p>
  </div>

  <div style="display: flex; gap: 0.5rem; margin-bottom: 1.5rem; flex-wrap: wrap;">
    <button class="btn btn-primary" onclick="filterQBank('all', this)">All Questions</button>
    <button class="btn" onclick="filterQBank('2m', this)">2 Marks (Definitions)</button>
    <button class="btn" onclick="filterQBank('5m', this)">5 Marks (Concepts)</button>
    <button class="btn" onclick="filterQBank('7m', this)">7 Marks (Differences & Architecture)</button>
    <button class="btn" onclick="filterQBank('10m', this)">10 Marks (Comprehensive Essays)</button>
    <button class="btn" onclick="toggleAllAccordions()">Expand / Collapse All</button>
  </div>

  <div id="qbankList">
    <!-- ==================== 2 MARKS QUESTIONS ==================== -->
    <div class="accordion-item" data-marks="2m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[2 Marks]</strong> Define Cloud Computing according to NIST.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <p><strong>Cloud Computing (NIST SP 800-145):</strong> A model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g. networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction.</p>
      </div>
    </div>

    <div class="accordion-item" data-marks="2m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[2 Marks]</strong> What is Resource Pooling in Cloud Computing?</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <p><strong>Resource Pooling:</strong> The provider's physical and virtual computing resources (CPU, RAM, storage, network bandwidth) are pooled together to serve multiple consumers in a multi-tenant model, dynamically assigned and reassigned according to consumer demand without the consumer needing to know the exact physical location of the hardware.</p>
      </div>
    </div>

    <div class="accordion-item" data-marks="2m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[2 Marks]</strong> Define Hypervisor and state its two main categories.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <p>A <strong>Hypervisor</strong> (or <strong>Virtual Machine Monitor / VMM</strong>) is a software or firmware layer that creates, runs, isolates, and manages Virtual Machines on physical host hardware.</p>
        <ul>
          <li><strong>Type 1 (Bare-Metal):</strong> Runs directly on hardware (e.g. VMware ESXi, Hyper-V, KVM).</li>
          <li><strong>Type 2 (Hosted):</strong> Runs on top of an existing host OS (e.g. Oracle VirtualBox, VMware Workstation).</li>
        </ul>
      </div>
    </div>

    <div class="accordion-item" data-marks="2m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[2 Marks]</strong> What is an EC2 Instance and an AMI in AWS?</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <ul>
          <li><strong>EC2 Instance:</strong> A resizable virtual server running on AWS infrastructure equipped with virtual CPU, memory, network interfaces, and storage.</li>
          <li><strong>Amazon Machine Image (AMI):</strong> A pre-packaged master template containing an operating system (e.g. Ubuntu, Windows Server), application server software, and initial configuration needed to launch an EC2 instance.</li>
        </ul>
      </div>
    </div>

    <div class="accordion-item" data-marks="2m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[2 Marks]</strong> Define Cloud Bursting in a Hybrid Cloud model.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <p><strong>Cloud Bursting:</strong> A hybrid cloud deployment configuration where an application runs normally on private cloud or on-premises infrastructure, but during sudden demand surges that exceed internal compute limits, it dynamically "bursts" excess workloads into a public cloud (like AWS) to maintain availability without crashing.</p>
      </div>
    </div>

    <div class="accordion-item" data-marks="2m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[2 Marks]</strong> What is the CIA Triad in Cloud Data Security?</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <p>The <strong>CIA Triad</strong> is a fundamental security benchmark consisting of:</p>
        <ul>
          <li><strong>Confidentiality:</strong> Preventing unauthorized access to sensitive data (via AES-256 encryption and IAM).</li>
          <li><strong>Integrity:</strong> Protecting data from unauthorized modification, tampering, or deletion (via SHA-256 hashing and digital signatures).</li>
          <li><strong>Availability:</strong> Ensuring authorized users have uninterrupted access to cloud resources (via multi-AZ redundancy and load balancing).</li>
        </ul>
      </div>
    </div>

    <div class="accordion-item" data-marks="2m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[2 Marks]</strong> What is the Cardinal Rule of AWS IAM Policy Evaluation?</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <p><strong>Rule: An Explicit Deny always overrides any Explicit Allow!</strong></p>
        <p>By default, all requests are denied implicitly. If an action is granted by an Allow statement but matches even ONE applicable policy containing an <code>"Effect": "Deny"</code>, access is unconditionally refused.</p>
      </div>
    </div>

    <!-- ==================== 5 MARKS QUESTIONS ==================== -->
    <div class="accordion-item" data-marks="5m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[5 Marks]</strong> Explain the 10 Evaluation Criteria for Selecting a Cloud Service Provider (CSP).</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <p>According to lecture slides, CSP selection is governed by the principle: <code>Sustenance = Technology Strength + Business Skills</code>.</p>
        <ol>
          <li><strong>Certifications & Standards:</strong> Adherence to ISO 27001, SOC 2, Open Cloud Consortium (OCC), and IEEE standards.</li>
          <li><strong>Financial Health:</strong> Long-term fiscal stability and capitalization of the provider.</li>
          <li><strong>Business & Technology Strength:</strong> Technical capability and agility to satisfy enterprise requirements.</li>
          <li><strong>Compliance Audits:</strong> Independent third-party audit validation.</li>
          <li><strong>Service Level Agreements (SLAs):</strong> Contractual availability guarantees (e.g. 99.99%) and financial credit terms.</li>
          <li><strong>Reporting & Tracking:</strong> Real-time operational monitoring and immutable audit logging.</li>
          <li><strong>Transparent Costing & Billing:</strong> Granular pay-as-you-go billing with real-time budget alarms.</li>
          <li><strong>Maintenance & Upgrades:</strong> Low-friction software upgrades and painless data migrations.</li>
          <li><strong>Technical Support:</strong> Tiered 24x7 support with guaranteed response times.</li>
          <li><strong>Security Architecture:</strong> Defense-in-depth, data encryption at rest and in transit, and physical datacenter controls.</li>
        </ol>
      </div>
    </div>

    <div class="accordion-item" data-marks="5m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[5 Marks]</strong> Explain Fog Computing and its industrial IoT applications.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <p><strong>Fog Computing:</strong> A decentralized computing paradigm that extends cloud computing and storage to the edge of the network. Intermediate "Fog Nodes" (gateways, routers, local edge servers) perform real-time data filtering, processing, and analysis close to IoT devices instead of transmitting raw telemetry to a distant cloud.</p>
        <p><strong>Key Industrial Applications:</strong></p>
        <ul>
          <li><strong>Manufacturing Factory Lines:</strong> Real-time robotic arm monitoring to prevent machine collision without network round-trip latency.</li>
          <li><strong>Oil & Gas Pipelines:</strong> Local acoustic sensor analysis to detect sudden pressure drops and trigger emergency shutoff valves.</li>
          <li><strong>On-Flight Avionics:</strong> Real-time engine telemetry analysis while aircraft is in flight with limited satellite bandwidth.</li>
          <li><strong>Smart Traffic & Autonomous Vehicles:</strong> Sub-second collision avoidance decisions executed at local traffic intersection nodes.</li>
        </ul>
      </div>
    </div>

    <div class="accordion-item" data-marks="5m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[5 Marks]</strong> Explain the Hypervisor Reference Model (Dispatcher, Allocator, Interpreter).</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <p>The Hypervisor Reference Model (from lecture slides 9–10) decomposes a Virtual Machine Monitor into three core internal modules:</p>
        <ol>
          <li><strong>Dispatcher:</strong> Serves as the primary entry point of the VMM. It traps all instructions issued by guest virtual machines, inspects their privilege level, and reroutes non-privileged calls or passes privileged instructions to the Allocator or Interpreter.</li>
          <li><strong>Allocator:</strong> Decides and administers physical resource distribution. Whenever a VM requests additional RAM, vCPU cycles, or storage blocks, the Allocator applies scheduling algorithms to allocate system hardware safely without resource starvation.</li>
          <li><strong>Interpreter:</strong> Contains specific trap routines that simulate privileged machine instructions executed by the guest OS (such as modifying hardware control registers or page tables), executing them in a protected context without compromising the host.</li>
        </ol>
      </div>
    </div>

    <div class="accordion-item" data-marks="5m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[5 Marks]</strong> Differentiate High Availability (HA) and Fault Tolerance (FT) with the Availability Formula.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <ul>
          <li><strong>High Availability (HA):</strong> Ensures a cloud system remains operational with minimal perceptible downtime through automated failover clusters, load balancers, and multi-AZ setups.</li>
          <li><strong>Fault Tolerance (FT):</strong> Ensures zero downtime and zero data loss during component failures through 100% hot hardware mirroring.</li>
        </ul>
        <p><strong>Mathematical Availability Formula:</strong></p>
        $$\\text{{Availability (\\%)}} = \\frac{{\\text{{Uptime}}}}{{\\text{{Uptime}} + \\text{{Downtime}}}} \\times 100$$
        <p><em>Example:</em> 999 hours uptime with 1 hour downtime = $\\frac{{999}}{{1000}} \\times 100 = 99.9\\%$ (Three Nines).</p>
      </div>
    </div>

    <div class="accordion-item" data-marks="5m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[5 Marks]</strong> Compare Google App Engine and AWS Elastic Beanstalk (Web vs Worker Tiers).</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <ul>
          <li><strong>Google App Engine (GAE):</strong> Pure serverless PaaS with 3 layers (Application, Platform, Infrastructure). Automatically scales down to zero instances; provides zero direct server access.</li>
          <li><strong>AWS Elastic Beanstalk:</strong> Managed orchestration PaaS that deploys underlying EC2 instances while retaining root access for developers. Offers two environment tiers:
            <ul>
              <li><strong>Web Server Environment:</strong> Provisions an Application Load Balancer and Auto-Scaling EC2 web nodes to handle HTTP/HTTPS user requests.</li>
              <li><strong>Worker Environment:</strong> Processes compute-heavy background tasks by pulling jobs from an <strong>Amazon SQS</strong> queue.</li>
            </ul>
          </li>
        </ul>
      </div>
    </div>

    <!-- ==================== 7 MARKS QUESTIONS ==================== -->
    <div class="accordion-item" data-marks="7m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[7 Marks]</strong> Compare all four Cloud Deployment Models (Public, Private, Hybrid, Community).</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <div class="table-wrapper">
          <table>
            <thead>
              <tr><th>Parameter</th><th>Public Cloud</th><th>Private Cloud</th><th>Hybrid Cloud</th><th>Community Cloud</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Ownership</strong></td><td>Third-party provider</td><td>Single organization</td><td>Mixed (Org + Provider)</td><td>Community consortium</td></tr>
              <tr><td><strong>Cost Model</strong></td><td>Pure OpEx (Pay-as-you-go)</td><td>Heavy CapEx (Hardware purchase)</td><td>Medium to High</td><td>Shared among members</td></tr>
              <tr><td><strong>Control</strong></td><td>Low (Provider-managed)</td><td>Very High (Complete control)</td><td>High on private portion</td><td>Medium to High</td></tr>
              <tr><td><strong>Security</strong></td><td>Standard; multi-tenant</td><td>Maximum; dedicated boundary</td><td>High; sensitive on-prem</td><td>High; industry-tailored</td></tr>
              <tr><td><strong>Scalability</strong></td><td>Virtually near-infinite</td><td>Hardware-bounded</td><td>Very high (Cloud Bursting)</td><td>Moderate</td></tr>
              <tr><td><strong>Management</strong></td><td>Managed by provider</td><td>In-house IT administration</td><td>Shared responsibility</td><td>Shared governance</td></tr>
              <tr><td><strong>Examples</strong></td><td>AWS, Azure, GCP</td><td>OpenStack, UIDAI, SBI</td><td>On-prem OpenStack + AWS</td><td>MeghRaj, Banking Cloud</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="accordion-item" data-marks="7m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[7 Marks]</strong> Compare IaaS, PaaS, and SaaS across full forms, control, audience, and the Pizza Analogy.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <div class="table-wrapper">
          <table>
            <thead>
              <tr><th>Parameter</th><th>IaaS</th><th>PaaS</th><th>SaaS</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Full Form</strong></td><td>Infrastructure as a Service</td><td>Platform as a Service</td><td>Software as a Service</td></tr>
              <tr><td><strong>What It Provides</strong></td><td>Raw virtual compute, storage, networks</td><td>Application execution & dev runtime</td><td>Finished, turnkey software apps</td></tr>
              <tr><td><strong>Customer Control</strong></td><td>Highest (OS, middleware, apps, data)</td><td>Medium (Application code & data)</td><td>Lowest (Personal data & settings)</td></tr>
              <tr><td><strong>Target Audience</strong></td><td>DevOps, SysAdmins, Cloud Architects</td><td>Software Developers, Programmers</td><td>End Users, Business Consumers</td></tr>
              <tr><td><strong>Pizza Analogy</strong></td><td><strong>Take and Bake:</strong> Vendor provides dough; you bake it in your oven</td><td><strong>Pizza Delivered:</strong> Cooked pizza delivered hot; you provide table</td><td><strong>Dining Out:</strong> Restaurant provides table, oven, and waiter service</td></tr>
              <tr><td><strong>Examples</strong></td><td>AWS EC2, Google GCE, Azure VMs</td><td>Google App Engine, Elastic Beanstalk</td><td>Google Docs, Microsoft 365, Zoom</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="accordion-item" data-marks="7m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[7 Marks]</strong> Compare Virtual Machines (VMs) and Docker Containers across 7 parameters.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <div class="table-wrapper">
          <table>
            <thead><tr><th>Parameter</th><th>Virtual Machine (VM)</th><th>Docker Container</th></tr></thead>
            <tbody>
              <tr><td><strong>1. Virtualization Level</strong></td><td>Hardware abstraction (Hypervisor)</td><td>Operating System abstraction (Engine)</td></tr>
              <tr><td><strong>2. Operating System</strong></td><td>Includes full independent Guest OS</td><td>Shares the host OS kernel</td></tr>
              <tr><td><strong>3. Startup Time</strong></td><td>Minutes (boots full OS kernel)</td><td>Milliseconds to seconds (process spawn)</td></tr>
              <tr><td><strong>4. Storage Footprint</strong></td><td>Heavy (Gigabytes: 2–20 GB)</td><td>Lightweight (Megabytes: 10–200 MB)</td></tr>
              <tr><td><strong>5. Resource Efficiency</strong></td><td>Lower density; high RAM overhead</td><td>High density; thousands per host</td></tr>
              <tr><td><strong>6. Isolation Level</strong></td><td>Hardware-enforced isolation via CPU rings</td><td>Process isolation (cgroups, namespaces)</td></tr>
              <tr><td><strong>7. Portability</strong></td><td>Complex image migration across hypervisors</td><td>Supreme; runs anywhere Docker engine runs</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="accordion-item" data-marks="7m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[7 Marks]</strong> Compare Block, Object, and File Storage with features, use cases, and AWS examples.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <ol>
          <li><strong>Block Storage (e.g. AWS EBS):</strong>
            <ul>
              <li><strong>Mechanism:</strong> Data split into fixed addressable blocks mounted over SAN/iSCSI.</li>
              <li><strong>Features:</strong> Ultra-low latency, high IOPS, support for in-place byte updates.</li>
              <li><strong>Use Cases:</strong> Virtual machine boot drives, relational transactional databases (MySQL, Oracle).</li>
            </ul>
          </li>
          <li><strong>Object Storage (e.g. AWS S3):</strong>
            <ul>
              <li><strong>Mechanism:</strong> Data stored as flat objects (Payload + Metadata + Unique Key) in buckets over HTTP/REST APIs.</li>
              <li><strong>Features:</strong> 99.999999999% (11 9s) durability, massive exabyte scale, cheap archiving tiers.</li>
              <li><strong>Use Cases:</strong> Video streaming, static website hosting, backup and disaster recovery.</li>
            </ul>
          </li>
          <li><strong>File Storage (e.g. AWS EFS):</strong>
            <ul>
              <li><strong>Mechanism:</strong> Classic hierarchical tree of directories and files mounted via NFSv4/SMB.</li>
              <li><strong>Features:</strong> Concurrent multi-server read/write with distributed file locking.</li>
              <li><strong>Use Cases:</strong> Shared corporate folders, CMS document roots (WordPress), shared dev repositories.</li>
            </ul>
          </li>
        </ol>
      </div>
    </div>

    <div class="accordion-item" data-marks="7m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[7 Marks]</strong> Compare AWS, Microsoft Azure, and Google Cloud Platform (GCP) across services and strengths.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <div class="table-wrapper">
          <table>
            <thead><tr><th>Capability</th><th>Amazon Web Services (AWS)</th><th>Microsoft Azure</th><th>Google Cloud (GCP)</th></tr></thead>
            <tbody>
              <tr><td><strong>Virtual Compute</strong></td><td>Amazon EC2</td><td>Azure Virtual Machines</td><td>Compute Engine (GCE)</td></tr>
              <tr><td><strong>Object Storage</strong></td><td>Amazon S3</td><td>Azure Blob Storage</td><td>Google Cloud Storage</td></tr>
              <tr><td><strong>Block Storage</strong></td><td>Amazon EBS</td><td>Azure Managed Disks</td><td>Persistent Disk (PD)</td></tr>
              <tr><td><strong>Serverless Functions</strong></td><td>AWS Lambda</td><td>Azure Functions</td><td>Cloud Functions</td></tr>
              <tr><td><strong>Managed Kubernetes</strong></td><td>Amazon EKS</td><td>Azure AKS</td><td>Google GKE (Native author)</td></tr>
              <tr><td><strong>Data Warehouse</strong></td><td>Amazon Redshift</td><td>Azure Synapse Analytics</td><td>Google BigQuery (Petabyte SQL)</td></tr>
              <tr><td><strong>Identity & Access</strong></td><td>AWS IAM</td><td>Microsoft Entra ID</td><td>Cloud IAM</td></tr>
              <tr><td><strong>Core Superpower</strong></td><td>Largest market share & service breadth</td><td>Windows, Active Directory & Hybrid</td><td>Big Data analytics & AI/ML</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="accordion-item" data-marks="7m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[7 Marks]</strong> Explain Multi-Server 3-Tier Web Architecture and Layer 4 vs Layer 7 Load Balancing.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <p>A Multi-Server 3-Tier Architecture decouples an application into three independent layers:</p>
        <ul>
          <li><strong>Tier 1: Web Tier (Presentation):</strong> Reverse proxy and web servers (Nginx/Apache) behind a Load Balancer terminating SSL and serving static assets.</li>
          <li><strong>Tier 2: Application Tier (Business Logic):</strong> Auto-scaling worker cluster processing business logic and REST APIs, paired with an in-memory Redis cache.</li>
          <li><strong>Tier 3: Database Tier (Persistence):</strong> Primary Master database (Writes) replicating asynchronously to Read-Replicas (Reads) across multiple AZs.</li>
        </ul>
        <p><strong>Layer 4 vs Layer 7 Load Balancing:</strong></p>
        <ul>
          <li><strong>Layer 4 (Transport / NLB):</strong> Routes traffic based on IP address and TCP/UDP port without inspecting application packet content. Ultra-fast, sub-millisecond latency.</li>
          <li><strong>Layer 7 (Application / ALB):</strong> Routes traffic based on application payload (HTTP URLs, headers, hostnames, cookies). Performs smart content-based routing (e.g. <code>/api</code> &rarr; App servers, <code>/images</code> &rarr; S3).</li>
        </ul>
      </div>
    </div>

    <!-- ==================== 10 MARKS QUESTIONS ==================== -->
    <div class="accordion-item" data-marks="10m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[10 Marks]</strong> Explain Multi-Tenant Architecture. Compare Pool, Bridge, and Silo patterns and explain the Noisy Neighbor problem.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <p><strong>Multi-Tenant Architecture:</strong> A software design where a single software instance runs on shared cloud servers, serving multiple distinct customer organizations (tenants), while strictly isolating each tenant's data, custom settings, and user permissions.</p>
        <p><strong>The 3 Database Isolation Patterns:</strong></p>
        <div class="table-wrapper">
          <table>
            <thead><tr><th>Pattern</th><th>Database Instance</th><th>Schema</th><th>Isolation Level</th><th>Cost & Best Use Case</th></tr></thead>
            <tbody>
              <tr><td><strong>1. Pool Pattern</strong></td><td>100% Shared</td><td>Shared Tables (<code>tenant_id</code> column)</td><td>Logical (via Row-Level Security)</td><td>Lowest cost; high-volume B2C SaaS.</td></tr>
              <tr><td><strong>2. Bridge Pattern</strong></td><td>Shared Engine</td><td>Separate Schema per Tenant</td><td>Medium (Schema boundaries)</td><td>Moderate cost; mid-market SaaS.</td></tr>
              <tr><td><strong>3. Silo Pattern</strong></td><td>Dedicated DB per Tenant</td><td>Dedicated Schemas</td><td>Maximum (Physical DB separation)</td><td>Highest cost; Banks, Healthcare, Defense.</td></tr>
            </tbody>
          </table>
        </div>
        <p><strong>The Noisy Neighbor Problem:</strong> In a shared multi-tenant host, if one tenant executes unoptimized queries or experiences a massive traffic spike, it consumes disproportionate CPU, RAM, or connection pool sockets, starving other innocent tenants.</p>
        <p><strong>Mitigation Strategies:</strong> (1) Enforce per-tenant CPU/RAM cgroup quotas, (2) Apply token-bucket API rate limits per <code>tenant_id</code>, (3) Use partitioned database connection pools, (4) Migrate heavy "whale" tenants into dedicated Silo instances.</p>
      </div>
    </div>

    <div class="accordion-item" data-marks="10m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[10 Marks]</strong> Explain OpenStack Architecture and detail all 9 Core Components with VM creation workflow.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <p><strong>OpenStack</strong> is an open-source IaaS cloud operating system that controls pools of compute, storage, and networking resources throughout a datacenter.</p>
        <p><strong>The 9 Core Components:</strong></p>
        <ul>
          <li><strong>1. Nova (Compute):</strong> Manages the lifecycle of virtual machine instances.</li>
          <li><strong>2. Neutron (Networking):</strong> Provides virtual SDN networking, subnets, routers, floating IPs, and ports.</li>
          <li><strong>3. Keystone (Identity):</strong> Central authentication, token issuing, and service catalog endpoint discovery.</li>
          <li><strong>4. Glance (Image):</strong> Image registry storing base VM disk images and operating system templates.</li>
          <li><strong>5. Cinder (Block Storage):</strong> Manages persistent block storage volumes attached to VMs.</li>
          <li><strong>6. Swift (Object Storage):</strong> Scalable, highly durable multi-tenant object storage for unstructured files.</li>
          <li><strong>7. Horizon (Dashboard):</strong> Web-based graphical interface for administrators and self-service users.</li>
          <li><strong>8. Heat (Orchestration):</strong> Orchestrates multi-tier composite cloud applications via declarative YAML templates.</li>
          <li><strong>9. Octavia (Load Balancing):</strong> Delivers scalable Load Balancing as a Service (LBaaS).</li>
        </ul>
        <p><strong>VM Creation Workflow:</strong> Horizon &rarr; Authenticated by <strong>Keystone</strong> &rarr; Image located by <strong>Glance</strong> &rarr; <strong>Nova API</strong> scheduler chooses host node &rarr; <strong>Neutron</strong> allocates virtual NIC and IP &rarr; <strong>Cinder</strong> attaches block volume &rarr; Hypervisor (KVM) launches VM.</p>
      </div>
    </div>

    <div class="accordion-item" data-marks="10m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[10 Marks]</strong> Analyze 3 Real-World Cloud Security Incidents (Capital One, Storm-0558, S3 Leaks) with vulnerabilities and mitigations.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <p><strong>Model Answer:</strong></p>
        <p><strong>Case 1: Capital One Breach (2019) — AWS</strong></p>
        <ul>
          <li><strong>Vulnerability:</strong> Misconfigured Web Application Firewall (WAF) exploited via Server-Side Request Forgery (SSRF).</li>
          <li><strong>Exploit:</strong> Attacker queried the EC2 Instance Metadata Service (IMDSv1) at <code>169.254.169.254</code> to extract temporary IAM role credentials and exfiltrate 106M records from S3.</li>
          <li><strong>Mitigations:</strong> Enforce IMDSv2 (requires session token header), apply IAM Least Privilege on EC2 instance roles, and encrypt S3 with customer KMS keys.</li>
        </ul>
        <p><strong>Case 2: Storm-0558 Token Forgery Incident (2023) — Microsoft Azure</strong></p>
        <ul>
          <li><strong>Vulnerability:</strong> Stolen inactive consumer signing key (MSA key) leaked via corporate Windows crash dump.</li>
          <li><strong>Exploit:</strong> Verification flaw allowed the consumer key to forge enterprise authentication tokens to access Exchange Online inboxes.</li>
          <li><strong>Mitigations:</strong> Strengthen cryptographic key isolation, automate rapid key rotation, and isolate consumer/enterprise token verification.</li>
        </ul>
        <p><strong>Case 3: Publicly Exposed AWS S3 Buckets</strong></p>
        <ul>
          <li><strong>Vulnerability:</strong> Accidental assignment of public read permissions (<code>AllUsers</code>) in bucket Access Control Lists (ACLs).</li>
          <li><strong>Mitigations:</strong> Enable AWS S3 "Block Public Access" at the root account level and deploy Amazon Macie (ML scanner) for automated data exposure detection.</li>
        </ul>
      </div>
    </div>
  </div>
</div>
"""
