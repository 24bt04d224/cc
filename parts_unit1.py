# -*- coding: utf-8 -*-

TAB_UNIT1_HTML = """
<div id="unit1" class="tab-pane">
  <div class="hero-banner">
    <div class="hero-header">
      <div class="hero-title">Unit 1: Introduction to Cloud Computing</div>
      <div class="hero-badge-group">
        <span class="badge badge-accent">15% Exam Weightage</span>
        <span class="badge">9 Contact Hours</span>
        <span class="badge badge-priority">Foundations & Infrastructure</span>
      </div>
    </div>
    <p class="hero-desc">
      Master all 18 syllabus topics plus lecture slide additions: NIST Characteristics, 12 Benefits, 10 Challenges,
      Cloud vs Traditional Computing, Infrastructure Management, 10 Provider Selection Criteria, Fog Computing,
      and Computing vs Storage vs Resource Virtualization. Click any <strong>Main Topic Header</strong> to drop down sub-topics,
      then click any <strong>Sub-Topic</strong> to view complete exam-ready notes, analogies, and tables.
    </p>
  </div>

  <!-- Unit 1 Dropdown Controls Bar -->
  <div class="unit-controls-bar">
    <div class="unit-controls-left">
      <span style="font-weight: 700; font-size: 0.88rem; color: var(--accent);">📌 Jump to Topic:</span>
      <select class="topic-select" onchange="jumpToTopic('unit1', this)">
        <option value="">Select a Topic...</option>
        <option value="u1-t1">Topic 1: Definition, Characteristics & Working</option>
        <option value="u1-t2">Topic 2: 12 Benefits & 10 Challenges of Cloud</option>
        <option value="u1-t3">Topic 3: Cloud vs Traditional Computing & 9 Layers</option>
        <option value="u1-t4">Topic 4: Cloud Infrastructure Management & Operations</option>
        <option value="u1-t5">Topic 5: Provider Selection Criteria & Fog Computing</option>
        <option value="u1-t6">Topic 6: Virtualization, VMs, Hypervisors & Types</option>
      </select>
    </div>
    <div class="unit-controls-right">
      <button class="btn btn-sm btn-primary" onclick="expandAllInUnit('unit1')">📂 Expand All</button>
      <button class="btn btn-sm" onclick="collapseAllInUnit('unit1')">📁 Collapse All</button>
    </div>
  </div>

  <!-- ==================== TOPIC 1 ==================== -->
  <div class="main-topic-card" id="u1-t1">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">📖</span>
        <span class="main-topic-title">Topic 1: Definition, Characteristics & Working of Cloud Computing</span>
        <span class="badge badge-accent">Foundations (5 Marks)</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>3 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 1.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.1 What is Cloud Computing? Definition & Google Drive Real-World Example</span>
          </div>
          <span class="sub-topic-badge">Definition</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Exam-Ready Definition:</strong> Cloud Computing is the on-demand delivery of computing services (including servers, storage, databases, networking, software, analytics, and artificial intelligence) over the Internet ("the cloud"), providing flexible, affordable, effective, and efficient resources for the development, execution, and scaling of applications without requiring users to purchase and maintain physical infrastructure.
          </div>
          <h4>Real-Life Example: Google Drive</h4>
          <ul>
            <li><strong>Without Cloud Computing:</strong> You must purchase physical hard drives or USB flash drives, store files locally, and if the laptop crashes or is stolen, access to those files is permanently lost.</li>
            <li><strong>With Cloud Computing:</strong> You upload files to Google Drive; files reside securely on redundant Google cloud infrastructure; you can access and collaborate on them from any smartphone or laptop worldwide without maintaining a single physical storage drive.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 1.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.2 The 5 Essential Characteristics of Cloud Computing (NIST SP 800-145)</span>
          </div>
          <span class="sub-topic-badge">5 Marks</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="grid-2">
            <div class="subcard">
              <h4>1. On-Demand Self-Service</h4>
              <p>A consumer can unilaterally provision computing capabilities, such as server time and network storage, as needed automatically without requiring human interaction with each service provider.</p>
            </div>
            <div class="subcard">
              <h4>2. Broad Network Access</h4>
              <p>Capabilities are available over the network and accessed through standard mechanisms that promote use by heterogeneous thin or thick client platforms (e.g., mobile phones, tablets, laptops, and workstations).</p>
            </div>
            <div class="subcard">
              <h4>3. Resource Pooling</h4>
              <p>The provider's computing resources are pooled to serve multiple consumers using a multi-tenant model, with different physical and virtual resources dynamically assigned and reassigned according to consumer demand.</p>
            </div>
            <div class="subcard">
              <h4>4. Rapid Elasticity</h4>
              <p>Capabilities can be elastically provisioned and released, in some cases automatically, to scale rapidly outward and inward commensurate with demand. To the consumer, available resources often appear infinite.</p>
            </div>
            <div class="subcard" style="grid-column: 1 / -1;">
              <h4>5. Measured Service (Pay-as-You-Go)</h4>
              <p>Cloud systems automatically control and optimize resource use by leveraging a metering capability at some level of abstraction appropriate to the type of service (e.g., storage, processing, bandwidth, active user accounts).</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 1.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.3 How Cloud Computing Works (Step-by-Step Flow)</span>
          </div>
          <span class="sub-topic-badge">Workflow</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <ol style="margin-left: 1.25rem; line-height: 1.7;">
            <li><strong>Client Connection:</strong> User establishes an Internet connection via browser, app, or CLI.</li>
            <li><strong>Service Request:</strong> User initiates a request (e.g., login, file save, database query).</li>
            <li><strong>Routing & Load Balancing:</strong> Cloud network gateways authenticate credentials and route traffic.</li>
            <li><strong>Virtualized Processing:</strong> Hypervisors and container clusters execute business logic.</li>
            <li><strong>Persistence:</strong> Data is read or written to distributed storage arrays across multiple AZs.</li>
            <li><strong>Response Delivery:</strong> Result is encrypted and transmitted back to the client device.</li>
          </ol>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 2 ==================== -->
  <div class="main-topic-card" id="u1-t2">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">⚖️</span>
        <span class="main-topic-title">Topic 2: The 12 Key Benefits & 10 Major Challenges of Cloud Computing</span>
        <span class="badge badge-priority">High-Yield (7 Marks)</span>
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
            <span>2.1 The 12 Benefits of Cloud Computing (From Lecture Slides)</span>
          </div>
          <span class="sub-topic-badge">12 Benefits</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="grid-2">
            <div class="subcard"><strong>1. Cost Efficiency:</strong> Eliminates upfront CapEx; pay only for resources consumed on a utility basis.</div>
            <div class="subcard"><strong>2. Scalability:</strong> Effortlessly scale compute power up or out to handle growing user workloads.</div>
            <div class="subcard"><strong>3. High Availability:</strong> Redundant multi-AZ datacenters ensure 24x7 operations with automated failover.</div>
            <div class="subcard"><strong>4. Ubiquitous Accessibility:</strong> Access applications from anywhere across smartphones, tablets, and PCs.</div>
            <div class="subcard"><strong>5. Backup & Disaster Recovery:</strong> Automated snapshots and cross-region replication prevent permanent data loss.</div>
            <div class="subcard"><strong>6. Enterprise Security:</strong> End-to-end encryption, IAM access controls, MFA, and automated threat detection.</div>
            <div class="subcard"><strong>7. Architectural Flexibility:</strong> Freedom to choose OS, programming languages, runtimes, and databases.</div>
            <div class="subcard"><strong>8. Real-Time Collaboration:</strong> Simultaneous multi-user editing (Google Docs, Microsoft 365, Slack).</div>
            <div class="subcard"><strong>9. Automatic Updates:</strong> Provider handles zero-downtime security patching and software updates.</div>
            <div class="subcard"><strong>10. Superior Performance:</strong> High-speed NVMe SSDs, low-latency backbones, and smart load balancing.</div>
            <div class="subcard"><strong>11. Global Reach:</strong> Deploy applications in dozens of international regions within minutes.</div>
            <div class="subcard"><strong>12. Environmental Sustainability:</strong> High server utilization reduces power waste and carbon footprint.</div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 2.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>2.2 The 10 Major Challenges of Cloud Computing (From Lecture Slides)</span>
          </div>
          <span class="sub-topic-badge">10 Challenges</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <ol style="margin-left: 1.25rem; line-height: 1.6;">
            <li><strong>Security & Privacy:</strong> Threat of data leakage, malware, and unauthorized access in shared multi-tenant hosts.</li>
            <li><strong>Internet Dependency:</strong> Cloud access is strictly gated by stable, high-speed Internet connectivity.</li>
            <li><strong>Downtime & Service Outages:</strong> Hyperscaler outages (e.g. AWS us-east-1 disruptions) can temporarily halt business operations.</li>
            <li><strong>Vendor Lock-in:</strong> Incompatible proprietary APIs, databases, and high data egress fees make switching providers painful.</li>
            <li><strong>Data Loss & Recovery Risks:</strong> Inadequate snapshot schedules or misconfigured retention policies can risk accidental loss.</li>
            <li><strong>Compliance & Legal Jurisdiction:</strong> Strict compliance laws (GDPR, HIPAA, RBI localization) restrict off-shore data storage.</li>
            <li><strong>Cost Management & Bill Shock:</strong> Unmonitored zombie VMs, unattached disks, and high egress traffic cause soaring bills.</li>
            <li><strong>Performance Jitter:</strong> Network latency and noisy neighbors sharing the same physical CPU/storage degrade responsiveness.</li>
            <li><strong>Limited Infrastructure Control:</strong> Users have zero control over bare-metal hardware, hypervisor versions, or physical switches.</li>
            <li><strong>Migration & Technical Skill Gaps:</strong> Refactoring monolithic legacy apps to cloud-native microservices requires rare skills.</li>
          </ol>
        </div>
      </div>

      <!-- Sub-topic 2.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>2.3 Benefits vs Challenges Direct Comparison Table</span>
          </div>
          <span class="sub-topic-badge">Comparison</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Core Benefit</th><th>Corresponding Challenge</th></tr></thead>
              <tbody>
                <tr><td>Cost efficiency (OpEx)</td><td>Uncontrolled usage and cost overruns (Bill shock)</td></tr>
                <tr><td>Rapid elasticity & scalability</td><td>Complex distributed resource management & noisy neighbors</td></tr>
                <tr><td>High availability</td><td>Unexpected cloud provider datacenter outages</td></tr>
                <tr><td>Universal remote accessibility</td><td>Total dependency on external Internet connectivity</td></tr>
                <tr><td>Managed security features</td><td>Data privacy risks and shared responsibility vulnerabilities</td></tr>
                <tr><td>Architectural flexibility</td><td>Vendor lock-in through proprietary APIs and services</td></tr>
                <tr><td>Automated provider updates</td><td>Loss of control over underlying infrastructure configurations</td></tr>
                <tr><td>Global multi-region reach</td><td>Cross-border regulatory compliance and data sovereignty laws</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 3 ==================== -->
  <div class="main-topic-card" id="u1-t3">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🔄</span>
        <span class="main-topic-title">Topic 3: Cloud Computing vs Traditional Computing & The 9 Layers</span>
        <span class="badge badge-accent">Architectural Comparison</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>2 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 3.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>3.1 Traditional On-Premises Computing vs Cloud Computing (Exam Table)</span>
          </div>
          <span class="sub-topic-badge">7 Marks</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Parameter</th>
                  <th>Traditional On-Premises Computing</th>
                  <th>Cloud Computing</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Infrastructure</strong></td>
                  <td>Physical servers, SAN storage, hardware switches</td>
                  <td>Virtual machines, containers, cloud storage, software-defined networks</td>
                </tr>
                <tr>
                  <td><strong>Ownership</strong></td>
                  <td>Organization owns 100% of physical equipment</td>
                  <td>Cloud Service Provider owns and maintains physical infrastructure</td>
                </tr>
                <tr>
                  <td><strong>Initial Cost</strong></td>
                  <td>Very High (Heavy Capital Expenditure - CapEx)</td>
                  <td>Zero to Low (Operational Expenditure - OpEx pay-as-you-go)</td>
                </tr>
                <tr>
                  <td><strong>Hardware Maintenance</strong></td>
                  <td>Organization's in-house IT team handles hardware repairs</td>
                  <td>Handled 100% transparently by the cloud service provider</td>
                </tr>
                <tr>
                  <td><strong>Scalability</strong></td>
                  <td>Rigid and slow; requires purchasing and installing new hardware</td>
                  <td>Instantaneous and elastic; add or remove nodes in seconds</td>
                </tr>
                <tr>
                  <td><strong>Accessibility</strong></td>
                  <td>Often restricted to office LAN or complex internal VPN</td>
                  <td>Universally accessible over the public Internet from any authorized device</td>
                </tr>
                <tr>
                  <td><strong>Deployment Time</strong></td>
                  <td>Weeks to months (procurement, shipping, racking, cabling)</td>
                  <td>Minutes (automated provisioning via Web Console or API)</td>
                </tr>
                <tr>
                  <td><strong>Resource Utilization</strong></td>
                  <td>Often poor (~15% server capacity utilized; idle waste)</td>
                  <td>High efficiency through dynamic multi-tenant resource pooling</td>
                </tr>
                <tr>
                  <td><strong>Disaster Recovery</strong></td>
                  <td>Expensive; requires maintaining an entire secondary datacenter</td>
                  <td>Built-in; automated snapshot replication across global regions</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p><strong>Example Scenario:</strong> A college needing 10 servers under Traditional IT must purchase 10 physical machines, build a server room, arrange air conditioning and UPS batteries, and hire hardware technicians. Under Cloud Computing, the college rents 10 virtual machines from AWS/Azure in 5 minutes and pays only while classes run.</p>
        </div>
      </div>

      <!-- Sub-topic 3.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>3.2 The 9 Layers of Cloud Computing & Ownership Stack</span>
          </div>
          <span class="sub-topic-badge">9 Layers</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Layer</th>
                  <th>Layer Name</th>
                  <th>Core Functionality</th>
                  <th>Managed By (Traditional vs IaaS vs PaaS vs SaaS)</th>
                </tr>
              </thead>
              <tbody>
                <tr><td>Layer 9</td><td><strong>Applications</strong></td><td>Software programs and business logic</td><td>User (Trad, IaaS, PaaS) | Provider (SaaS)</td></tr>
                <tr><td>Layer 8</td><td><strong>Data</strong></td><td>User datasets, databases, records</td><td>User (Trad, IaaS, PaaS, SaaS controls access)</td></tr>
                <tr><td>Layer 7</td><td><strong>Runtime</strong></td><td>Execution engine (Java JVM, Node.js, Python)</td><td>User (Trad, IaaS) | Provider (PaaS, SaaS)</td></tr>
                <tr><td>Layer 6</td><td><strong>Middleware</strong></td><td>Message queues, API connectors, web servers</td><td>User (Trad, IaaS) | Provider (PaaS, SaaS)</td></tr>
                <tr><td>Layer 5</td><td><strong>Operating System</strong></td><td>Manages software & hardware (Linux/Windows)</td><td>User (Trad, IaaS) | Provider (PaaS, SaaS)</td></tr>
                <tr><td>Layer 4</td><td><strong>Virtualization</strong></td><td>Hypervisors (KVM, ESXi) slicing hardware</td><td>User (Trad) | Provider (IaaS, PaaS, SaaS)</td></tr>
                <tr><td>Layer 3</td><td><strong>Servers</strong></td><td>Physical CPU, RAM, motherboards</td><td>User (Trad) | Provider (IaaS, PaaS, SaaS)</td></tr>
                <tr><td>Layer 2</td><td><strong>Storage</strong></td><td>Hard disks, NVMe arrays, SAN/NAS</td><td>User (Trad) | Provider (IaaS, PaaS, SaaS)</td></tr>
                <tr><td>Layer 1</td><td><strong>Networking</strong></td><td>Physical switches, fiber cables, routers</td><td>User (Trad) | Provider (IaaS, PaaS, SaaS)</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 4 ==================== -->
  <div class="main-topic-card" id="u1-t4">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🛠️</span>
        <span class="main-topic-title">Topic 4: Cloud Infrastructure Management & Operations</span>
        <span class="badge">Operations</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>4 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 4.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>4.1 Cloud Infrastructure Definition & Principal / College Campus Analogy</span>
          </div>
          <span class="sub-topic-badge">Analogy</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Cloud Infrastructure Management:</strong> The structured operational process of monitoring, controlling, maintaining, securing, and optimizing all cloud resources (compute, storage, network, identity, and billing) to ensure continuous high availability, security, and cost efficiency.
          </div>
          <h4>The College Principal Campus Analogy (From Lecture Slides)</h4>
          <p>Imagine you are the <strong>Principal of a university college campus</strong>:</p>
          <ul>
            <li>You must oversee and manage classrooms, electricity generators, water supply, security staff, campus Wi-Fi, teaching faculty, and maintenance schedules.</li>
            <li>Similarly, a <strong>Cloud Administrator</strong> oversees and manages Virtual Machines, storage buckets, virtual private networks, firewall security groups, user access privileges, and automated data backups.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 4.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>4.2 Resource Provisioning: Manual vs Automatic (Restaurant Analogy)</span>
          </div>
          <span class="sub-topic-badge">Provisioning</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Resource Provisioning:</strong> The allocation and deployment of cloud resources (VMs, storage, networking) according to user demands and application requirements.
          </div>
          <ul>
            <li><strong>Manual Provisioning:</strong> An administrator logs into the cloud console (e.g. AWS Management Console) and manually clicks through to create an EC2 virtual machine and configure disk storage.</li>
            <li><strong>Automatic Provisioning:</strong> Cloud systems monitor workload metrics (e.g. CPU > 80%) and automatically spawn additional virtual instances using <strong>Auto Scaling</strong> without human intervention.</li>
          </ul>
          <p><strong>The Restaurant Working Analogy:</strong> When a restaurant experiences a sudden rush of customers during dinner time, the manager opens up additional dining tables, calls in reserve waiters, and powers on backup cooking stoves. Once the rush ends, extra tables are closed. This is exactly how cloud Auto Scaling operates!</p>
        </div>
      </div>

      <!-- Sub-topic 4.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>4.3 Cloud Infrastructure Monitoring & The Amazon CloudWatch 95% CPU Case</span>
          </div>
          <span class="sub-topic-badge">Monitoring</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p><strong>Infrastructure Monitoring</strong> continuously checks the operational health, availability, and performance telemetry of cloud resources:</p>
          <ul>
            <li><strong>Key Metrics Monitored:</strong> CPU Utilization (%), RAM Usage, Disk Read/Write IOPS, Network In/Out Bandwidth, HTTP Response Latency, and Error Rates.</li>
            <li><strong>AWS Monitoring Tool:</strong> <strong>Amazon CloudWatch</strong> collects telemetry metrics, tracks log events, and triggers automated alarm actions.</li>
          </ul>
          <div class="def-box" style="border-left-color: var(--danger);">
            <strong>Real-World Monitoring Flow (Lecture Slides Case):</strong><br>
            Suppose an e-commerce database instance experiences a CPU utilization surge to <strong>95%</strong>:
            <ol style="margin-left: 1rem; margin-top: 0.5rem;">
              <li>CloudWatch detects CPU crossing the 85% threshold rule.</li>
              <li>An automated CloudWatch Alarm triggers an Amazon SNS notification to the SRE team.</li>
              <li>Concurrently, an Auto-Scaling policy triggers the provisioning of a read-replica database to relieve query pressure, preventing server crash.</li>
            </ol>
          </div>
        </div>
      </div>

      <!-- Sub-topic 4.4 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>4.4 Security, Backup vs Disaster Recovery & Administrator Responsibilities</span>
          </div>
          <span class="sub-topic-badge">Security & DR</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <h4>Backup vs Disaster Recovery (DR)</h4>
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Dimension</th><th>Data Backup</th><th>Disaster Recovery (DR)</th></tr></thead>
              <tbody>
                <tr><td><strong>Primary Objective</strong></td><td>Creating redundant copies of data files</td><td>Restoring complete system operation after a catastrophe</td></tr>
                <tr><td><strong>Focus Area</strong></td><td>Data preservation and integrity</td><td>Business continuity and uptime resumption</td></tr>
                <tr><td><strong>Typical Example</strong></td><td>Scheduled nightly snapshot of database to S3</td><td>Failing over complete web and app tiers to another region</td></tr>
              </tbody>
            </table>
          </div>
          <h4>8 Core Responsibilities of a Cloud Administrator (From Lecture Slides)</h4>
          <p>1. Provision and launch Virtual Machines | 2. Configure Virtual Networks & Subnets | 3. Manage Storage Volumes & Buckets | 4. Continuously Monitor Performance & Health | 5. Manage IAM Security & Firewalls | 6. Implement Automated Data Backups | 7. Optimize Costs & Eliminate Idle Resources | 8. Troubleshoot & Remediate Outages.</p>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 5 ==================== -->
  <div class="main-topic-card" id="u1-t5">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🌐</span>
        <span class="main-topic-title">Topic 5: Selection of Cloud Service Provider & Fog Computing</span>
        <span class="badge badge-accent">Lecture Additions (5 Marks)</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>2 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 5.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>5.1 Ten Criteria for Selecting a Cloud Service Provider (CSP)</span>
          </div>
          <span class="sub-topic-badge">10 Criteria</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="exam-tip">
            <strong>Formula from Lecture Slides:</strong><br>
            $$\\text{{Sustenance}} = \\text{{Technology Strength}} + \\text{{Business Skills}}$$
          </div>
          <ol style="margin-left: 1.25rem; line-height: 1.6;">
            <li><strong>Certifications & Standards Compliance:</strong> Must comply with ISO 27001, Open Cloud Consortium (OCC), IEEE, and SNIA standards.</li>
            <li><strong>Financial Health & Stability:</strong> Provider must possess sufficient funding, strong profitability, and long-term operating viability.</li>
            <li><strong>Business & Technology Strength:</strong> Must demonstrate deep architectural expertise and agility to adapt to customer requirements.</li>
            <li><strong>Compliance Audits:</strong> Willingness to undergo third-party independent audits for transparent governance.</li>
            <li><strong>Service Level Agreements (SLAs):</strong> Binding legal contracts defining uptime percentages (e.g. 99.99%) and financial penalty credits.</li>
            <li><strong>Reporting & Activity Tracking:</strong> Automated performance reporting dashboards and immutable audit trail logs.</li>
            <li><strong>Costing & Billing Transparency:</strong> Granular, itemized pay-as-you-go billing with real-time budget threshold alerts.</li>
            <li><strong>Maintenance, Monitoring & Upgrade:</strong> Painless software upgrades and affordable long-term operational maintenance.</li>
            <li><strong>Technical Support:</strong> Tiered 24x7 support with guaranteed response times and dedicated technical account managers.</li>
            <li><strong>Security Architecture:</strong> Robust defense-in-depth, hardware security modules (HSMs), data encryption, and physical security.</li>
          </ol>
        </div>
      </div>

      <!-- Sub-topic 5.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>5.2 Fog Computing — Concept, IoT Node Architecture & Applications</span>
          </div>
          <span class="sub-topic-badge">Fog Computing</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Fog Computing:</strong> A decentralized computing paradigm that extends cloud computing and storage to the edge of an enterprise's network, performing data processing, filtering, and analysis on intermediate "Fog Nodes" located physically closer to IoT devices rather than transmitting all raw telemetry to a distant centralized cloud.
          </div>
          <h4>How Fog Computing Works</h4>
          <p>IoT Sensors &rarr; Local Fog Nodes (Gateways / Local Edge Servers) &rarr; Real-Time Analysis & Immediate Actuation &rarr; Filtered Summarized Records sent to Central Cloud for Big Data Archival.</p>
          <h4>Primary Industrial Applications (From Lecture Slides)</h4>
          <ul>
            <li><strong>Manufacturing Factory Lines:</strong> Real-time robotic arm monitoring to prevent machine collision without waiting for cloud round-trip latency.</li>
            <li><strong>Oil & Gas Pipelines:</strong> Local acoustic sensor fault analysis to detect sudden pipeline pressure drops and trigger emergency shutoff valves.</li>
            <li><strong>On-Flight In-Flight Avionics:</strong> Real-time engine telemetry analysis while aircraft is in flight with limited satellite bandwidth.</li>
            <li><strong>Smart Traffic & Autonomous Vehicles:</strong> Immediate collision avoidance decisions executed at local traffic intersection fog nodes.</li>
          </ul>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 6 ==================== -->
  <div class="main-topic-card" id="u1-t6">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🧱</span>
        <span class="main-topic-title">Topic 6: Virtualization Foundations: VMs, Hypervisors & Resource Slicing</span>
        <span class="badge badge-priority">High-Yield (7/10 Marks)</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>4 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 6.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>6.1 Virtualization Concept, Need & The Apartment Building Analogy</span>
          </div>
          <span class="sub-topic-badge">Foundations</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Virtualization:</strong> The foundational technology of cloud computing that creates virtual (software-based) representations of physical computing resources (servers, storage, network interfaces, operating systems), allowing a single physical server to operate as multiple independent virtual computers.
          </div>
          <h4>The Apartment Building Analogy (From Lecture Slides)</h4>
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Real-World Concept</th><th>Virtualization Concept</th></tr></thead>
              <tbody>
                <tr><td>One Large Apartment Building</td><td>One Physical Bare-Metal Server</td></tr>
                <tr><td>Independent Apartment Units</td><td>Independent Virtual Machines (VMs)</td></tr>
                <tr><td>Different Families living inside</td><td>Different Guest Operating Systems & Users</td></tr>
                <tr><td>Building Shared Water & Power Pipes</td><td>Shared Physical CPU, RAM, and Disk</td></tr>
                <tr><td>Locked Apartment Front Doors</td><td>Logical Isolation enforced by Hypervisor</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Sub-topic 6.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>6.2 Virtual Machines (VMs), 5 Components & Server Slicing Example</span>
          </div>
          <span class="sub-topic-badge">VM Structure</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p>A <strong>Virtual Machine (VM)</strong> is a software emulation of a physical computer containing:</p>
          <ul>
            <li><strong>vCPU:</strong> Virtual CPU cores scheduled onto physical cores.</li>
            <li><strong>Virtual Memory:</strong> Virtual RAM address space allocated from physical RAM.</li>
            <li><strong>Virtual Disk:</strong> An image file (e.g. <code>.vmdk</code>, <code>.qcow2</code>) representing physical hard drive storage.</li>
            <li><strong>Virtual NIC:</strong> Emulated network card with unique MAC address and virtual IP.</li>
            <li><strong>Guest OS:</strong> Full operating system (Ubuntu, Windows Server) running inside the VM.</li>
          </ul>
          <h4>Server Slicing Example (From Lecture Slides)</h4>
          <p>Consider a physical server with <strong>16 CPU Cores</strong> and <strong>64 GB RAM</strong>:</p>
          <ul>
            <li><strong>VM 1 (Web Server):</strong> Allocated 4 Cores + 16 GB RAM (Linux OS)</li>
            <li><strong>VM 2 (Database Server):</strong> Allocated 6 Cores + 24 GB RAM (Linux OS)</li>
            <li><strong>VM 3 (Application Server):</strong> Allocated 4 Cores + 16 GB RAM (Windows Server OS)</li>
            <li><strong>VM 4 (Testing Environment):</strong> Allocated 2 Cores + 8 GB RAM (Linux OS)</li>
          </ul>
          <p><em>Result: 100% of physical capacity is utilized without resource wastage!</em></p>
        </div>
      </div>

      <!-- Sub-topic 6.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>6.3 Hypervisors — Role & Type 1 (Bare-Metal) vs Type 2 (Hosted) Comparison</span>
          </div>
          <span class="sub-topic-badge">Type 1 vs 2</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Hypervisor (Virtual Machine Monitor / VMM):</strong> A software or firmware layer that creates, runs, isolates, and manages Virtual Machines, mediating all VM access to physical hardware.
          </div>
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Feature</th><th>Type 1 Hypervisor (Bare-Metal)</th><th>Type 2 Hypervisor (Hosted)</th></tr></thead>
              <tbody>
                <tr><td><strong>Installation</strong></td><td>Installed directly on physical bare-metal hardware</td><td>Runs as an application on top of an existing Host OS</td></tr>
                <tr><td><strong>Host OS Overhead</strong></td><td>None (Zero host OS overhead)</td><td>High overhead caused by intermediate host OS</td></tr>
                <tr><td><strong>Performance</strong></td><td>Near-native, ultra-high performance</td><td>Lower performance due to translation layers</td></tr>
                <tr><td><strong>Isolation & Security</strong></td><td>Hardware-enforced, maximum isolation</td><td>Depends on security integrity of the host OS</td></tr>
                <tr><td><strong>Primary Usage</strong></td><td>Cloud datacenters, enterprise server consolidation</td><td>Software development, local testing, education</td></tr>
                <tr><td><strong>Real Examples</strong></td><td>VMware ESXi, Microsoft Hyper-V, KVM, Xen</td><td>Oracle VirtualBox, VMware Workstation, Fusion</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Sub-topic 6.4 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>6.4 Computing Virtualization vs Storage Virtualization vs Resource Virtualization</span>
          </div>
          <span class="sub-topic-badge">Comparison</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Dimension</th>
                  <th>Computing Virtualization</th>
                  <th>Storage Virtualization</th>
                  <th>Resource Virtualization</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Core Meaning</strong></td>
                  <td>Creates virtual computers (VMs) from physical servers</td>
                  <td>Combines multiple physical hard drives into a single logical storage pool</td>
                  <td>Abstracts all hardware resources (CPU, RAM, network, storage) into virtual pools</td>
                </tr>
                <tr>
                  <td><strong>Primary Focus</strong></td>
                  <td>CPU processing cycles and RAM allocation</td>
                  <td>Disk capacity, block allocation, and SAN/NAS management</td>
                  <td>Holistic abstraction across compute, memory, I/O, and network bandwidth</td>
                </tr>
                <tr>
                  <td><strong>Mechanism</strong></td>
                  <td>Hypervisors scheduling vCPUs and memory pages</td>
                  <td>Logical Volume Managers (LVM), RAID, and SAN storage controllers</td>
                  <td>Software-Defined Everything (SDDC), hyper-converged infrastructure (HCI)</td>
                </tr>
                <tr>
                  <td><strong>Primary Benefit</strong></td>
                  <td>Run multiple OSs simultaneously on one server</td>
                  <td>Centralized storage administration and zero disk waste</td>
                  <td>Dynamic, automated resource allocation matching cloud demand</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

</div>
"""
