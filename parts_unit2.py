# -*- coding: utf-8 -*-
from parts_svg import SVG_PIZZA

TAB_UNIT2_HTML = f"""
<div id="unit2" class="tab-pane">
  <div class="hero-banner">
    <div class="hero-header">
      <div class="hero-title">Unit 2: Cloud Service Models (SPI Framework)</div>
      <div class="hero-badge-group">
        <span class="badge badge-accent">15% Exam Weightage</span>
        <span class="badge">7 Contact Hours</span>
        <span class="badge badge-priority">IaaS · PaaS · SaaS Core</span>
      </div>
    </div>
    <p class="hero-desc">
      Master all 14 syllabus topics of Unit 2: The SPI Framework, "Pizza-as-a-Service" Analogy, IaaS Deep Dive (EC2 Lifecycle,
      AMI, GCE, Azure VMs), PaaS Platforms (Google App Engine 3-Layer Architecture, Elastic Beanstalk Web vs Worker Tiers),
      SaaS 4-Tier Architecture (Google Docs vs Microsoft 365), and the Master 7-Mark IaaS vs PaaS vs SaaS Comparison Table.
      Click any <strong>Main Topic Header</strong> to drop down sub-topics, then click any <strong>Sub-Topic</strong> to view full notes.
    </p>
  </div>

  <!-- Unit 2 Dropdown Controls Bar -->
  <div class="unit-controls-bar">
    <div class="unit-controls-left">
      <span style="font-weight: 700; font-size: 0.88rem; color: var(--accent);">📌 Jump to Topic:</span>
      <select class="topic-select" onchange="jumpToTopic('unit2', this)">
        <option value="">Select a Topic...</option>
        <option value="u2-t1">Topic 1: Introduction to Cloud Service Models & Pizza Analogy</option>
        <option value="u2-t2">Topic 2: Infrastructure as a Service (IaaS) Deep Dive</option>
        <option value="u2-t3">Topic 3: Amazon EC2, GCE & Azure Virtual Machines</option>
        <option value="u2-t4">Topic 4: Platform as a Service (PaaS) & Kitchen Analogy</option>
        <option value="u2-t5">Topic 5: Google App Engine vs AWS Elastic Beanstalk</option>
        <option value="u2-t6">Topic 6: Software as a Service (SaaS), Docs & M365</option>
        <option value="u2-t7">Topic 7: Master Comparison: IaaS vs PaaS vs SaaS (7 Marks)</option>
      </select>
    </div>
    <div class="unit-controls-right">
      <button class="btn btn-sm btn-primary" onclick="expandAllInUnit('unit2')">📂 Expand All</button>
      <button class="btn btn-sm" onclick="collapseAllInUnit('unit2')">📁 Collapse All</button>
    </div>
  </div>

  <!-- ==================== TOPIC 1 ==================== -->
  <div class="main-topic-card" id="u2-t1">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🍕</span>
        <span class="main-topic-title">Topic 1: Introduction to Cloud Service Models & "Pizza-as-a-Service"</span>
        <span class="badge badge-accent">SPI Framework</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>2 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 1.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.1 What are Cloud Service Models? The SPI Taxonomy</span>
          </div>
          <span class="sub-topic-badge">SPI Model</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Cloud Service Models:</strong> Describe the standardized ways cloud computing resources and capabilities are delivered to consumers. They define the technical boundary of responsibilities between the cloud provider and the customer, governing who manages hardware, operating systems, execution runtimes, and application logic.
          </div>
          <div class="grid-3" style="margin-top: 0.75rem;">
            <div class="subcard" style="border-top: 3px solid #38bdf8;">
              <h4 style="color: #38bdf8;">1. IaaS (Infrastructure)</h4>
              <p>Rent raw virtual computing resources (servers, disks, networks). You manage the OS, middleware, and application code.</p>
            </div>
            <div class="subcard" style="border-top: 3px solid #10b981;">
              <h4 style="color: #10b981;">2. PaaS (Platform)</h4>
              <p>Use a fully configured application execution and deployment runtime. You write the code; the provider handles servers and OS.</p>
            </div>
            <div class="subcard" style="border-top: 3px solid #a855f7;">
              <h4 style="color: #a855f7;">3. SaaS (Software)</h4>
              <p>Access turnkey, finished software over a browser or mobile app. The provider handles 100% of the underlying stack.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 1.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.2 The "Pizza-as-a-Service" Analogy (From Lecture Slides)</span>
          </div>
          <span class="sub-topic-badge">Analogy Diagram</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="diagram-container">
            {SVG_PIZZA}
            <div class="diagram-caption">Figure 2.1: Pizza-as-a-Service Analogy mapping Traditional On-Premises, IaaS, PaaS, and SaaS.</div>
          </div>
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Service Model</th><th>Pizza Equivalent</th><th>Analogy Explanation</th></tr></thead>
              <tbody>
                <tr><td><strong>Traditional On-Premises</strong></td><td><strong>Made at Home</strong></td><td>You buy all ingredients, make dough, use your own oven, gas, dining table, and clean up dishes.</td></tr>
                <tr><td><strong>IaaS (Infrastructure as a Service)</strong></td><td><strong>Take and Bake</strong></td><td>Vendor prepares the raw pizza (dough, sauce, cheese); you take it home, bake in your own oven, and provide dining table.</td></tr>
                <tr><td><strong>PaaS (Platform as a Service)</strong></td><td><strong>Pizza Delivered</strong></td><td>Vendor cooks pizza in their oven and delivers it hot to your door; you supply the dining table and soda drinks.</td></tr>
                <tr><td><strong>SaaS (Software as a Service)</strong></td><td><strong>Dine at Restaurant</strong></td><td>You walk into a restaurant; vendor provides dining table, kitchen, oven, drinks, and waiter service. You just enjoy!</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 2 ==================== -->
  <div class="main-topic-card" id="u2-t2">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🖥️</span>
        <span class="main-topic-title">Topic 2: Infrastructure as a Service (IaaS) Deep Dive</span>
        <span class="badge badge-accent">IaaS Architecture</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>3 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 2.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>2.1 IaaS Definition, Characteristics & Traditional Infrastructure Comparison</span>
          </div>
          <span class="sub-topic-badge">Definition</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Exam-Ready Definition:</strong> Infrastructure as a Service (IaaS) is a cloud computing service model in which a cloud service provider delivers virtualized computing resources (virtual servers, CPUs, memory, block and object storage, and virtual networks) over the Internet on an elastic, pay-as-you-go basis.
          </div>
          <h4>Core Characteristics</h4>
          <ul>
            <li><strong>Virtualized Raw Resources:</strong> Compute is presented as Virtual Machines (VMs) or raw physical bare-metal instances.</li>
            <li><strong>Complete OS Control:</strong> Consumers have administrative root access to choose, install, patch, and manage the guest operating system.</li>
            <li><strong>Dynamic Rapid Provisioning:</strong> Spin up hundreds of servers programmatically via APIs in seconds.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 2.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>2.2 The 5 Core Components of IaaS & Working Process</span>
          </div>
          <span class="sub-topic-badge">5 Components</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="grid-2">
            <div class="subcard">
              <h4>1. Compute</h4>
              <p>Virtual Machines, vCPUs, physical hypervisors, and RAM capacity allocated on demand.</p>
            </div>
            <div class="subcard">
              <h4>2. Storage</h4>
              <p>Block Storage (EBS boot disks), Object Storage (S3 blobs), and File Storage (EFS network shares).</p>
            </div>
            <div class="subcard">
              <h4>3. Networking</h4>
              <p>Software-defined Virtual Private Clouds (VPCs), subnets, routing tables, and Elastic IP addresses.</p>
            </div>
            <div class="subcard">
              <h4>4. Security & Access</h4>
              <p>Stateful Security Groups (virtual firewalls), Network ACLs, and IAM access credentials.</p>
            </div>
          </div>
          <h4>How IaaS Works (User Request Flow)</h4>
          <p>User logs into Cloud Console &rarr; Selects compute sizing (e.g. 4 vCPUs, 16 GB RAM) &rarr; Cloud hypervisor provisions virtual machine from physical hardware pool &rarr; User attaches virtual disk and connects via SSH/RDP &rarr; User installs runtime and software.</p>
        </div>
      </div>

      <!-- Sub-topic 2.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>2.3 Who Manages What in IaaS? (Shared Responsibility)</span>
          </div>
          <span class="sub-topic-badge">Responsibility</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Cloud Provider Manages (Under the Hypervisor)</th><th>Cloud Customer Manages (Above the Hypervisor)</th></tr></thead>
              <tbody>
                <tr><td>Physical datacenters, building security, CCTV</td><td>Guest Operating System installation, patching, updates</td></tr>
                <tr><td>Physical server hardware (CPU, RAM, motherboards)</td><td>Application source code and business logic</td></tr>
                <tr><td>Physical network cabling, routers, fiber lines</td><td>Application data, databases, and customer records</td></tr>
                <tr><td>Physical storage arrays, SAN controllers</td><td>User accounts, credentials, and IAM permissions</td></tr>
                <tr><td>Power backup generators, HVAC chiller cooling</td><td>Security group firewall rules and OS-level firewalls</td></tr>
                <tr><td>Type 1 Hypervisor software (KVM, ESXi)</td><td>Antivirus, middleware, and application runtime</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 3 ==================== -->
  <div class="main-topic-card" id="u2-t3">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">☁️</span>
        <span class="main-topic-title">Topic 3: Amazon EC2, GCE & Azure Virtual Machines</span>
        <span class="badge badge-priority">High-Yield (7 Marks)</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>3 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 3.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>3.1 Amazon EC2 Deep Dive: Instance Concept, Lifecycle & 10-Step Launch Workflow</span>
          </div>
          <span class="sub-topic-badge">Amazon EC2</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Amazon EC2 (Elastic Compute Cloud):</strong> A foundational AWS web service that provides secure, resizable compute capacity in the cloud, allowing users to rent virtual computers (EC2 instances) without purchasing physical hardware.
          </div>
          <h4>EC2 Instance Lifecycle States (From Lecture Slides)</h4>
          <div class="table-wrapper">
            <table>
              <thead><tr><th>State</th><th>Operational Meaning & Billing Impact</th></tr></thead>
              <tbody>
                <tr><td><strong>Pending</strong></td><td>Instance is being provisioned by AWS hypervisor; resources are being allocated. (No billing yet)</td></tr>
                <tr><td><strong>Running</strong></td><td>Instance is active, OS has booted, and applications are executing. (Billed per second)</td></tr>
                <tr><td><strong>Stopping</strong></td><td>Instance is preparing to shut down; flushing memory buffers to EBS disk.</td></tr>
                <tr><td><strong>Stopped</strong></td><td>Instance is powered down. (Zero compute charges; only EBS storage charges apply). Can be restarted!</td></tr>
                <tr><td><strong>Shutting-Down</strong></td><td>Instance is in the process of permanent decommissioning.</td></tr>
                <tr><td><strong>Terminated</strong></td><td>Instance is permanently deleted; root EBS volume is released. Cannot be restarted!</td></tr>
              </tbody>
            </table>
          </div>
          <h4>10-Step EC2 Launch Workflow (From Lecture Slides)</h4>
          <p>1. Open AWS Management Console &rarr; 2. Navigate to EC2 Dashboard &rarr; 3. Click <strong>Launch Instance</strong> &rarr; 4. Choose an <strong>AMI</strong> (e.g. Ubuntu 22.04 LTS) &rarr; 5. Select <strong>Instance Type</strong> (e.g. <code>t3.micro</code>) &rarr; 6. Configure Network & VPC Subnet &rarr; 7. Configure EBS Storage Size (e.g. 30 GB) &rarr; 8. Configure Security Group Firewall Rules (Allow Port 22 SSH, Port 80 HTTP) &rarr; 9. Select or Create SSH Key Pair &rarr; 10. Click Launch Instance!</p>
          <div class="def-box" style="border-left-color: var(--accent);">
            <strong>What is an AMI (Amazon Machine Image)?</strong> A pre-packaged master image template containing the operating system, initial application software, and configuration files required to launch a new virtual server instance.
          </div>
        </div>
      </div>

      <!-- Sub-topic 3.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>3.2 Google Compute Engine (GCE) & Azure Virtual Machines</span>
          </div>
          <span class="sub-topic-badge">GCE & Azure</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="grid-2">
            <div class="subcard">
              <h4>Google Compute Engine (GCE)</h4>
              <p>Google Cloud's IaaS compute offering. Allows users to launch scalable Linux and Windows VMs on Google's global fiber backbone. Features custom machine types (choose custom vCPU and RAM combinations) and Persistent Disks.</p>
            </div>
            <div class="subcard">
              <h4>Microsoft Azure Virtual Machines</h4>
              <p>Microsoft's IaaS compute platform providing virtualized computing on Azure datacenters. Provides deep integration with Microsoft enterprise stacks (Windows Server, SQL Server, Active Directory) and Linux distributions.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 3.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>3.3 Comparison of IaaS Providers: AWS EC2 vs Azure VMs vs Google GCE</span>
          </div>
          <span class="sub-topic-badge">Provider Matrix</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Feature Dimension</th>
                  <th>AWS (Amazon)</th>
                  <th>Microsoft Azure</th>
                  <th>Google Cloud (GCP)</th>
                </tr>
              </thead>
              <tbody>
                <tr><td><strong>Virtual Compute Unit</strong></td><td>EC2 Instance</td><td>Azure Virtual Machine</td><td>Compute Engine (GCE VM)</td></tr>
                <tr><td><strong>VM Template</strong></td><td>Amazon Machine Image (AMI)</td><td>Azure VM Image</td><td>Compute Engine Disk Image</td></tr>
                <tr><td><strong>Virtual Network</strong></td><td>Virtual Private Cloud (VPC)</td><td>Virtual Network (VNet)</td><td>Virtual Private Cloud (VPC)</td></tr>
                <tr><td><strong>Block Storage</strong></td><td>Elastic Block Store (EBS)</td><td>Azure Managed Disks</td><td>Persistent Disk (PD)</td></tr>
                <tr><td><strong>Object Storage</strong></td><td>Amazon S3</td><td>Azure Blob Storage</td><td>Google Cloud Storage</td></tr>
                <tr><td><strong>Managed Relational DB</strong></td><td>Amazon RDS</td><td>Azure SQL Database</td><td>Cloud SQL</td></tr>
                <tr><td><strong>Identity Management</strong></td><td>AWS IAM</td><td>Microsoft Entra ID</td><td>Cloud IAM</td></tr>
                <tr><td><strong>Network Firewall</strong></td><td>Security Groups & NACLs</td><td>Network Security Groups (NSGs)</td><td>VPC Firewall Rules</td></tr>
                <tr><td><strong>Monitoring Tool</strong></td><td>Amazon CloudWatch</td><td>Azure Monitor</td><td>Google Cloud Monitoring</td></tr>
                <tr><td><strong>Auto-Scaling Service</strong></td><td>Auto Scaling Groups (ASG)</td><td>VM Scale Sets (VMSS)</td><td>Managed Instance Groups (MIG)</td></tr>
                <tr><td><strong>Command Line CLI</strong></td><td><code>aws</code> CLI</td><td><code>az</code> CLI</td><td><code>gcloud</code> CLI</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 4 ==================== -->
  <div class="main-topic-card" id="u2-t4">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🍳</span>
        <span class="main-topic-title">Topic 4: Platform as a Service (PaaS) & The Kitchen Analogy</span>
        <span class="badge badge-accent">PaaS Concept</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>2 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 4.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>4.1 PaaS Definition, Characteristics & Fully Equipped Kitchen Analogy</span>
          </div>
          <span class="sub-topic-badge">Definition</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Platform as a Service (PaaS):</strong> A cloud service model providing a pre-configured development, runtime, execution, and deployment environment over the Internet. The provider manages the underlying servers, operating system, and middleware, allowing software developers to focus 100% of their effort on writing code and building applications.
          </div>
          <h4>The Fully Equipped Kitchen Analogy (From Lecture Slides)</h4>
          <ul>
            <li><strong>Traditional Approach:</strong> If you want to cook food, you must first construct a kitchen room, install gas pipelines, buy a cooking stove, purchase a refrigerator, utensils, and connect water pipes.</li>
            <li><strong>PaaS Approach:</strong> You walk into a <strong>modern, fully equipped commercial kitchen</strong> where stoves, gas, water, and pans are already set up and operating. You simply bring your personal recipe and ingredients to cook! Developers simply bring their application code!</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 4.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>4.2 The 7 Components of PaaS & Responsibility Division</span>
          </div>
          <span class="sub-topic-badge">Components</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p>1. <strong>Development Tools:</strong> SDKs, CLI tools, IDE plugins | 2. <strong>Middleware:</strong> API gateways, message queues | 3. <strong>Operating Systems:</strong> Managed Linux/Windows kernels | 4. <strong>Database Services:</strong> Embedded relational and NoSQL engines | 5. <strong>Runtime Environment:</strong> JVM, Python interpreter, Node.js engine | 6. <strong>Infrastructure Layer:</strong> Scalable VMs managed by provider | 7. <strong>Analytics & Monitoring:</strong> Application performance monitoring (APM).</p>
          <div class="table-wrapper" style="margin-top: 0.75rem;">
            <table>
              <thead><tr><th>Provider Manages in PaaS</th><th>Developer Manages in PaaS</th></tr></thead>
              <tbody>
                <tr><td>Physical servers, storage arrays, network switches</td><td>Application source code and business logic</td></tr>
                <tr><td>Operating System installation and kernel patches</td><td>Application configuration files and API endpoints</td></tr>
                <tr><td>Execution runtime updates (e.g. Node 18 &rarr; 20)</td><td>Application data schema and user accounts</td></tr>
                <tr><td>Automated scaling, load balancing, failover</td><td>User experience, UI layouts, and frontend assets</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 5 ==================== -->
  <div class="main-topic-card" id="u2-t5">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">⚡</span>
        <span class="main-topic-title">Topic 5: Google App Engine vs AWS Elastic Beanstalk</span>
        <span class="badge badge-priority">High-Yield (7 Marks)</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>3 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 5.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>5.1 Google App Engine (GAE): Concept & 3-Layer Architecture</span>
          </div>
          <span class="sub-topic-badge">Google App Engine</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Google App Engine (GAE):</strong> Google Cloud's premier PaaS platform that allows developers to build and host scalable web applications and mobile backends on Google's managed infrastructure with zero server administration.
          </div>
          <h4>The 3-Layer Architecture of Google App Engine</h4>
          <ul>
            <li><strong>1. Application Layer:</strong> Contains developer-written business logic, web controllers, REST APIs, and application-specific settings (<code>app.yaml</code>).</li>
            <li><strong>2. Platform Layer:</strong> Managed execution environment providing programming language runtimes (Python, Java, Go, Node.js), version branching, traffic splitting, and automated scaling.</li>
            <li><strong>3. Infrastructure Layer:</strong> Google's physical datacenter machinery, global network routing, Bigtable storage, and load balancers.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 5.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>5.2 AWS Elastic Beanstalk: Runtimes, Components & Web vs Worker Tiers</span>
          </div>
          <span class="sub-topic-badge">Elastic Beanstalk</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>AWS Elastic Beanstalk:</strong> A managed PaaS orchestration service from Amazon Web Services that simplifies deploying, monitoring, and scaling web applications developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker.
          </div>
          <h4>Two Elastic Beanstalk Environment Tiers (From Lecture Slides)</h4>
          <div class="grid-2">
            <div class="subcard">
              <h4>1. Web Server Environment</h4>
              <p>Designed for applications that process front-facing public HTTP/HTTPS requests from end users (e.g. web portals, RESTful APIs, e-commerce storefronts). Deploys an Application Load Balancer and Auto-Scaling EC2 web nodes.</p>
            </div>
            <div class="subcard">
              <h4>2. Worker Environment</h4>
              <p>Designed for background, asynchronous, compute-intensive processing (e.g. video rendering, generating PDF invoices, nightly database rollups). Pulls background tasks from an <strong>Amazon SQS (Simple Queue Service)</strong> message queue.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 5.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>5.3 Comparison: Google App Engine vs AWS Elastic Beanstalk</span>
          </div>
          <span class="sub-topic-badge">Comparison</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Feature</th><th>Google App Engine (GAE)</th><th>AWS Elastic Beanstalk</th></tr></thead>
              <tbody>
                <tr><td><strong>Provider</strong></td><td>Google Cloud Platform (GCP)</td><td>Amazon Web Services (AWS)</td></tr>
                <tr><td><strong>Service Model</strong></td><td>PaaS (Pure serverless platform)</td><td>PaaS (Managed orchestration over IaaS)</td></tr>
                <tr><td><strong>Underlying Control</strong></td><td>Abstracted; zero direct VM access</td><td>Complete; developer can SSH into underlying EC2 instances</td></tr>
                <tr><td><strong>Scale to Zero</strong></td><td>Yes (Standard environment scales to 0 instances)</td><td>No (Minimum 1 EC2 instance running in normal setup)</td></tr>
                <tr><td><strong>Monitoring Tool</strong></td><td>Google Cloud Monitoring</td><td>Amazon CloudWatch</td></tr>
                <tr><td><strong>Supported Environments</strong></td><td>Python, Java, Node.js, Go, PHP, Ruby</td><td>Java, .NET, Node.js, PHP, Python, Ruby, Go, Docker</td></tr>
                <tr><td><strong>Other PaaS Examples</strong></td><td colspan="2">Heroku (simple git push deployments), Microsoft Azure App Service</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 6 ==================== -->
  <div class="main-topic-card" id="u2-t6">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">📱</span>
        <span class="main-topic-title">Topic 6: Software as a Service (SaaS), Google Docs & Microsoft 365</span>
        <span class="badge badge-accent">SaaS Architecture</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>3 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 6.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>6.1 SaaS Definition, 8 Core Characteristics & Pros/Cons</span>
          </div>
          <span class="sub-topic-badge">Definition</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Software as a Service (SaaS):</strong> A cloud service model where fully functional application software is hosted centrally by a provider and made available to users over the Internet, typically accessed via a web browser or mobile app on a subscription basis without local installation.
          </div>
          <h4>8 Core Characteristics (From Lecture Slides)</h4>
          <p>1. Internet-based browser access | 2. Centralized cloud hosting | 3. Subscription billing (monthly/annual) | 4. Automatic provider-managed software updates | 5. Multi-tenancy infrastructure | 6. Instant on-demand scalability | 7. Multi-device accessibility (PC, phone, tablet) | 8. Centralized cloud data storage.</p>
        </div>
      </div>

      <!-- Sub-topic 6.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>6.2 The 4-Layer SaaS Architecture Stack (From Lecture Slides)</span>
          </div>
          <span class="sub-topic-badge">4 Layers</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Layer</th><th>Layer Name</th><th>Architectural Components</th></tr></thead>
              <tbody>
                <tr><td><strong>Layer 1</strong></td><td><strong>Client Layer</strong></td><td>Web browsers (Chrome, Edge), iOS/Android mobile apps, desktop thin-clients.</td></tr>
                <tr><td><strong>Layer 2</strong></td><td><strong>Application Layer</strong></td><td>SaaS software application, business logic, microservices, REST APIs, authentication tokens.</td></tr>
                <tr><td><strong>Layer 3</strong></td><td><strong>Data Layer</strong></td><td>Relational/NoSQL databases, file storage buckets, tenant metadata, search indexes.</td></tr>
                <tr><td><strong>Layer 4</strong></td><td><strong>Infrastructure Layer</strong></td><td>Virtual machines, container clusters (Kubernetes), physical servers, datacenter networks.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Sub-topic 6.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>6.3 Google Docs vs Microsoft 365 Comparison</span>
          </div>
          <span class="sub-topic-badge">Product Comparison</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Dimension</th><th>Google Docs (Google Workspace)</th><th>Microsoft 365 (Office 365)</th></tr></thead>
              <tbody>
                <tr><td><strong>Provider</strong></td><td>Google</td><td>Microsoft</td></tr>
                <tr><td><strong>Primary Nature</strong></td><td>Cloud-native online document editor</td><td>Comprehensive enterprise productivity suite</td></tr>
                <tr><td><strong>Document Tool</strong></td><td>Google Docs</td><td>Microsoft Word (Web + Desktop)</td></tr>
                <tr><td><strong>Spreadsheet Tool</strong></td><td>Google Sheets</td><td>Microsoft Excel</td></tr>
                <tr><td><strong>Presentation Tool</strong></td><td>Google Slides</td><td>Microsoft PowerPoint</td></tr>
                <tr><td><strong>Storage Backend</strong></td><td>Google Drive</td><td>OneDrive / SharePoint</td></tr>
                <tr><td><strong>Collaboration Example</strong></td><td colspan="2">Five students simultaneously editing one academic report in real-time without emailing file copies.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 7 ==================== -->
  <div class="main-topic-card" id="u2-t7">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">📊</span>
        <span class="main-topic-title">Topic 7: Master Comparison: IaaS vs PaaS vs SaaS (7 Marks)</span>
        <span class="badge badge-priority">Most Important 7-Mark Question</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>2 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 7.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>7.1 Comprehensive Comparison Matrix (IaaS vs PaaS vs SaaS)</span>
          </div>
          <span class="sub-topic-badge">Comparison Matrix</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Parameter</th>
                  <th>IaaS (Infrastructure as a Service)</th>
                  <th>PaaS (Platform as a Service)</th>
                  <th>SaaS (Software as a Service)</th>
                </tr>
              </thead>
              <tbody>
                <tr><td><strong>What It Provides</strong></td><td>Virtual hardware (Compute, Storage, Network)</td><td>Complete application execution platform</td><td>Finished, ready-to-use software applications</td></tr>
                <tr><td><strong>Customer Control</strong></td><td>Highest control (OS, middleware, apps)</td><td>Moderate control (Application code & data)</td><td>Lowest control (Only personal data & settings)</td></tr>
                <tr><td><strong>Target Audience</strong></td><td>Cloud Architects, SysAdmins, DevOps</td><td>Software Developers, Programmers</td><td>Business End-Users, Consumers</td></tr>
                <tr><td><strong>Technical Complexity</strong></td><td>High (Requires server & OS admin skills)</td><td>Medium (Focus on coding & DB queries)</td><td>Low (Simple browser point-and-click)</td></tr>
                <tr><td><strong>Infrastructure Managed By</strong></td><td>Provider</td><td>Provider</td><td>Provider</td></tr>
                <tr><td><strong>OS & Runtime Managed By</strong></td><td>Customer</td><td>Provider</td><td>Provider</td></tr>
                <tr><td><strong>Application Managed By</strong></td><td>Customer</td><td>Customer</td><td>Provider</td></tr>
                <tr><td><strong>Primary Examples</strong></td><td>AWS EC2, Google GCE, Azure VMs</td><td>Google App Engine, Elastic Beanstalk, Heroku</td><td>Google Docs, Microsoft 365, Salesforce, Zoom</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Sub-topic 7.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>7.2 Selection Guide: When Should You Use Which Service Model?</span>
          </div>
          <span class="sub-topic-badge">Decision Guide</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Organizational Requirement</th><th>Optimal Cloud Service Model</th></tr></thead>
              <tbody>
                <tr><td>Complete control over OS, custom kernel modules, and network routing</td><td><strong>IaaS (e.g. AWS EC2)</strong></td></tr>
                <tr><td>Rapid custom web application development without server management duties</td><td><strong>PaaS (e.g. Google App Engine)</strong></td></tr>
                <tr><td>Ready-made corporate office productivity, email, and video conferencing</td><td><strong>SaaS (e.g. Microsoft 365)</strong></td></tr>
                <tr><td>Hosting legacy commercial software requiring specific OS dependencies</td><td><strong>IaaS (e.g. Azure Virtual Machines)</strong></td></tr>
                <tr><td>Agile software sprint teams deploying web apps using continuous integration</td><td><strong>PaaS (e.g. AWS Elastic Beanstalk)</strong></td></tr>
                <tr><td>Student collaborative document writing and team spreadsheets</td><td><strong>SaaS (e.g. Google Docs)</strong></td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

</div>
"""
