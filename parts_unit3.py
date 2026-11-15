# -*- coding: utf-8 -*-

from parts_svg import (
    SVG_DEPLOYMENT_MODELS,
    SVG_MULTI_TENANT_PATTERNS,
    SVG_THREE_TIER_ARCHITECTURE
)

TAB_UNIT3_HTML = f"""
<div id="unit3" class="tab-pane">
  <div class="hero-banner">
    <div class="hero-header">
      <div class="hero-title">Unit 3: Cloud Deployment Models & Cloud Architecture</div>
      <div class="hero-badge-group">
        <span class="badge badge-accent">20% Exam Weightage</span>
        <span class="badge">9 Contact Hours</span>
        <span class="badge badge-priority">High-Yield Syllabus Focus</span>
      </div>
    </div>
    <p class="hero-desc">
      Master all 28 topics of Unit 3: The 4 Cloud Deployment Models, Multi-Cloud Strategy, 5 Core Cloud Sub-Architectures,
      Multi-Tenant Isolation Models (Pool vs Bridge vs Silo), Multi-Server 3-Tier Scalability, Distributed Systems,
      and the AWS vs Azure vs GCP Master Comparison. Click on any <strong>Main Topic Header</strong> to drop down sub-topics,
      then click any <strong>Sub-Topic</strong> to view complete exam-ready notes, architectures, and formulas.
    </p>
  </div>

  <!-- Unit 3 Dropdown Controls Bar -->
  <div class="unit-controls-bar">
    <div class="unit-controls-left">
      <span style="font-weight: 700; font-size: 0.88rem; color: var(--accent);">📌 Jump to Topic:</span>
      <select class="topic-select" onchange="jumpToTopic('unit3', this)">
        <option value="">Select a Topic...</option>
        <option value="u3-t1">Topic 1: Cloud Deployment Models & Comparative Analysis</option>
        <option value="u3-t2">Topic 2: Cloud Architecture — Layers & Data Centres</option>
        <option value="u3-t3">Topic 3: The 5 Core Cloud Sub-Architectures</option>
        <option value="u3-t4">Topic 4: Principles, Scalability, Elasticity & High Availability</option>
        <option value="u3-t5">Topic 5: Structural Models: Multi-Tenant Architecture</option>
        <option value="u3-t6">Topic 6: Structural Models: Multi-Server & Distributed Architecture</option>
        <option value="u3-t7">Topic 7: Major Cloud Providers (AWS vs Azure vs GCP)</option>
      </select>
    </div>
    <div class="unit-controls-right">
      <button class="btn btn-sm btn-primary" onclick="expandAllInUnit('unit3')">📂 Expand All</button>
      <button class="btn btn-sm" onclick="collapseAllInUnit('unit3')">📁 Collapse All</button>
    </div>
  </div>

  <!-- ==================== TOPIC 1 ==================== -->
  <div class="main-topic-card" id="u3-t1">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🌐</span>
        <span class="main-topic-title">Topic 1: Cloud Deployment Models & Comparative Analysis</span>
        <span class="badge badge-priority">Very High Priority (7 Marks)</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>9 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">

      <!-- Diagram -->
      <div class="diagram-container">
        {SVG_DEPLOYMENT_MODELS}
        <div class="diagram-caption">Figure 3.1: Cloud Deployment Models & Hybrid Cloud Bursting Architecture</div>
      </div>
      
      <!-- Sub-topic 1.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.1 What is a Cloud Deployment Model? Purpose & Factors Determined</span>
          </div>
          <span class="sub-topic-badge">Definition</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Cloud Deployment Model:</strong> Defines where cloud infrastructure is hosted, who owns and operates it, who can access it, and how cloud resources are managed. In simple terms: <em>It tells us where the cloud is located, who manages it, and who can use it.</em>
          </div>
          <h4>What does a Deployment Model Determine?</h4>
          <ul>
            <li><strong>Ownership:</strong> Third-party provider, private enterprise, community consortium, or mixed.</li>
            <li><strong>Accessibility:</strong> Public Internet vs. internal corporate Intranet vs. dedicated VPN / Direct Connect.</li>
            <li><strong>Infrastructure Location:</strong> On-premises corporate datacenter vs. off-premises cloud hyperscaler facility.</li>
            <li><strong>Security Responsibility:</strong> Customer-managed vs. provider-managed under the Shared Responsibility Model.</li>
            <li><strong>Cost Structure:</strong> Pure Operational Expenditure (OpEx pay-as-you-go) vs. Capital Expenditure (CapEx server purchase).</li>
            <li><strong>Scalability & Elasticity:</strong> Hardware-bounded scaling vs. near-infinite cloud auto-scaling.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 1.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.2 Cloud Development vs Cloud Deployment (Exam Critical Table)</span>
          </div>
          <span class="sub-topic-badge">Comparison</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Parameter</th>
                  <th>Cloud Development</th>
                  <th>Cloud Deployment</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Meaning</strong></td>
                  <td>Designing, coding, and testing applications specifically built for the cloud</td>
                  <td>Making the developed application operational and available to end users</td>
                </tr>
                <tr>
                  <td><strong>Main Objective</strong></td>
                  <td>Build and prepare the application software</td>
                  <td>Deliver, run, and scale the application in production</td>
                </tr>
                <tr>
                  <td><strong>Focus</strong></td>
                  <td>Coding, unit testing, debugging, and cloud API integration</td>
                  <td>Infrastructure provisioning, containerization, network routing, and release</td>
                </tr>
                <tr>
                  <td><strong>Activities</strong></td>
                  <td>Writing source code, data modeling, mock API testing</td>
                  <td>Configuration management, CI/CD pipeline release, health monitoring</td>
                </tr>
                <tr>
                  <td><strong>Environment</strong></td>
                  <td>Development & Staging environments</td>
                  <td>Production environment (live traffic)</td>
                </tr>
                <tr>
                  <td><strong>Primary Users</strong></td>
                  <td>Software engineers, developers, and QA testers</td>
                  <td>End users, customers, and DevOps site-reliability engineers (SRE)</td>
                </tr>
                <tr>
                  <td><strong>Primary Tools</strong></td>
                  <td>IDEs (VS Code), Cloud SDKs (boto3), Git, Unit Test frameworks</td>
                  <td>CI/CD (GitHub Actions), Docker, Kubernetes, Terraform, CloudFormation</td>
                </tr>
                <tr>
                  <td><strong>Example</strong></td>
                  <td>Developing a Python web application using AWS Boto3 SDK</td>
                  <td>Deploying the application onto an AWS EC2 Auto-Scaling Group behind an ALB</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="exam-tip">
            <strong>💡 Memory Trick:</strong> Development = <em>How do we build the application?</em> | Deployment = <em>How do we make it available and running for users?</em>
          </div>
        </div>
      </div>

      <!-- Sub-topic 1.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.3 Public Cloud — Characteristics, Architecture, Pros/Cons & Global Examples</span>
          </div>
          <span class="sub-topic-badge">Public Cloud</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Public Cloud:</strong> A computing model where infrastructure and computing resources are owned, operated, and maintained by a third-party cloud service provider and delivered to multiple organizations (tenants) over the public Internet on a pay-as-you-go basis.
          </div>
          <h4>Core Characteristics</h4>
          <ul>
            <li><strong>Third-Party Owned:</strong> Providers like Amazon, Microsoft, and Google own the physical servers, switches, and cooling facilities.</li>
            <li><strong>Multi-Tenancy:</strong> Multiple unrelated customers share the same physical hardware pools through logical hypervisor isolation.</li>
            <li><strong>Pay-As-You-Go (Utility Pricing):</strong> Billed strictly for compute seconds, gigabytes stored, and data transferred.</li>
            <li><strong>Near-Infinite Elasticity:</strong> Instantly scale from 1 server to 10,000 servers without ordering hardware.</li>
          </ul>
          <h4>Advantages & Limitations</h4>
          <div class="grid-2">
            <div class="subcard">
              <h4 style="color: var(--success);">Advantages (Pros)</h4>
              <ul>
                <li><strong>Zero CapEx:</strong> No server hardware purchases or datacenter leasing costs.</li>
                <li><strong>High Availability:</strong> Global footprint across multiple Regions and Availability Zones.</li>
                <li><strong>Rapid Deployment:</strong> Provision complex multi-tier clusters in minutes via web console or CLI.</li>
                <li><strong>Zero Maintenance Duty:</strong> Hardware lifecycle, power cooling, and physical security handled by provider.</li>
              </ul>
            </div>
            <div class="subcard">
              <h4 style="color: var(--danger);">Limitations (Cons)</h4>
              <ul>
                <li><strong>Loss of Physical Control:</strong> Zero access to bare-metal hardware or physical storage drives.</li>
                <li><strong>Multi-Tenant Jitter:</strong> Risk of "noisy neighbors" degrading shared resource throughput.</li>
                <li><strong>Regulatory Barriers:</strong> Strict data sovereignty laws may prohibit storing customer records off-premises.</li>
                <li><strong>Uncontrolled Cost Risk:</strong> Idle VMs and unmonitored egress traffic can cause bill shock.</li>
              </ul>
            </div>
          </div>
          <h4>Real-World Case Studies (From Lecture Slides)</h4>
          <ul>
            <li><strong>Netflix:</strong> Migrated 100% of its streaming services, video encoding pipelines, and recommendation engine onto AWS public cloud infrastructure.</li>
            <li><strong>Spotify:</strong> Leverages Google Cloud Platform (GCP) for data storage, audio streaming, and personalized recommendation analytics.</li>
            <li><strong>The New York Times:</strong> Processed and digitized its historical archives (millions of scanned newspaper pages) using GCP compute instances in just a few days.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 1.4 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.4 Private Cloud — On-Premises vs Hosted, Architecture & Indian Examples</span>
          </div>
          <span class="sub-topic-badge">Private Cloud</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Private Cloud:</strong> Cloud infrastructure provisioned for exclusive use by a single organization comprising multiple consumers (e.g. business units). It may be owned, managed, and operated by the organization, a third party, or some combination of them, and it may exist on or off premises.
          </div>
          <h4>Two Deployment Types of Private Cloud</h4>
          <ul>
            <li><strong>1. On-Premises Private Cloud:</strong> Hosted inside the organization's own physical datacenter. Complete internal control, managed by corporate IT staff. Highest security and upfront CapEx.</li>
            <li><strong>2. Third-Party Hosted (Dedicated) Private Cloud:</strong> Hosted in an external provider's facility (e.g., Equinix, Rackspace, AWS Dedicated Hosts), but the physical servers and network are physically or logically dedicated exclusively to that single enterprise.</li>
          </ul>
          <h4>Key Architecture Components</h4>
          <p>Physical Servers &rarr; Bare-Metal Hypervisors (KVM, ESXi) &rarr; Virtualized VM & Container Pools &rarr; Private SAN/NAS Storage &rarr; Software-Defined Networking (SDN) &rarr; Corporate Identity Management (LDAP/Active Directory) &rarr; Cloud Management Platform (OpenStack / CloudStack).</p>
          <h4>Indian Real-World Examples (From Lecture Slides)</h4>
          <ul>
            <li><strong>UIDAI (Aadhaar):</strong> Runs dedicated private cloud infrastructure to store and verify biometric and demographic records of 1.4+ billion Indian residents with zero external data sharing.</li>
            <li><strong>Public & Private Banks (e.g. Indian Bank, SBI):</strong> Utilize on-premises private clouds for core banking solutions (CBS) to comply with Reserve Bank of India (RBI) data localization mandates.</li>
            <li><strong>Telecom Giants (Tata Communications, Reliance Jio, Airtel):</strong> Maintain massive internal private clouds to manage core cellular switching, 5G packet cores, and billing infrastructure.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 1.5 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.5 Hybrid Cloud — Architecture, Working, Benefits & Cloud Bursting</span>
          </div>
          <span class="sub-topic-badge">Hybrid Cloud</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Hybrid Cloud:</strong> An infrastructure composition of two or more distinct cloud environments (commonly a Private Cloud and a Public Cloud) that remain unique entities but are bound together by standardized technology enabling data and application portability.
          </div>
          <h4>Working Architecture & Banking Example</h4>
          <p>Consider an enterprise banking platform:</p>
          <ul>
            <li><strong>Sensitive Workloads (Private Cloud):</strong> Core account ledgers, customer credit histories, and sensitive transactions remain secured on the private on-premises datacenter.</li>
            <li><strong>Customer-Facing Workloads (Public Cloud):</strong> Mobile banking front-ends, promotional campaign micro-sites, and statement PDF generators run on AWS/Azure public cloud for elastic scale.</li>
            <li><strong>Secure Interconnect:</strong> Bound together via encrypted IPsec VPN tunnels or dedicated private fiber connections (AWS Direct Connect / Azure ExpressRoute).</li>
          </ul>
          <div class="def-box" style="border-left-color: var(--warning);">
            <strong>⚡ Cloud Bursting:</strong> A dynamic application deployment model where an application runs normally in a private cloud or datacenter, but during sudden demand surges that exceed internal compute limits, it automatically "bursts" excess workloads into a public cloud to prevent crashes.
          </div>
        </div>
      </div>

      <!-- Sub-topic 1.6 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.6 Community Cloud — Shared Sectoral Infrastructure & 4 Core Applications</span>
          </div>
          <span class="sub-topic-badge">Community Cloud</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Community Cloud:</strong> A cloud infrastructure shared exclusively by multiple organizations that have common requirements, shared missions, uniform security concerns, or industry-specific regulatory compliance mandates.
          </div>
          <h4>4 Primary Applications (From Lecture Slides)</h4>
          <ul>
            <li><strong>1. Hospitals & Medical Centers:</strong> Regional hospitals share a specialized medical cloud to securely exchange patient electronic health records (EHR) while complying with healthcare privacy standards (e.g. HIPAA).</li>
            <li><strong>2. Universities & Research Laboratories:</strong> Academic institutions connect supercomputers and research datasets, pooling compute cycles for joint genomics, physics, and climate simulation research.</li>
            <li><strong>3. Government Agencies:</strong> Local municipal and state government departments share a dedicated government cloud (e.g., MeghRaj in India, AWS GovCloud) sharing security tooling and disaster recovery costs.</li>
            <li><strong>4. Banks & Credit Unions:</strong> Regional financial institutions collaborate on a shared banking community cloud for inter-bank transaction settlement, fraud intelligence sharing, and RBI compliance.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 1.7 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.7 Multi-Cloud Strategy — Definition, Rationale, Pros & Cons</span>
          </div>
          <span class="sub-topic-badge">Multi-Cloud</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Multi-Cloud:</strong> The operational strategy of using cloud computing services from two or more independent cloud service providers (e.g. AWS + Microsoft Azure + Google Cloud) simultaneously for distinct enterprise workloads.
          </div>
          <h4>Why Enterprises Adopt Multi-Cloud (Workload Distribution)</h4>
          <ul>
            <li><strong>AWS:</strong> Best-in-class raw compute (EC2) and massive global footprint for international web apps.</li>
            <li><strong>Microsoft Azure:</strong> Seamless enterprise Active Directory (Entra ID), Office 365, and Windows Server integration.</li>
            <li><strong>Google Cloud (GCP):</strong> Industry-leading big data processing (BigQuery) and advanced machine learning (Vertex AI).</li>
            <li><strong>Specialized Provider:</strong> Cold archive storage or disaster recovery backup target.</li>
          </ul>
          <h4>Advantages vs. Operational Challenges</h4>
          <ul>
            <li><strong>Key Advantages:</strong> Eliminates single-vendor lock-in, increases negotiation leverage, provides superior disaster recovery (if one hyperscaler suffers an outage, the other remains live), and leverages specialized best-of-breed features.</li>
            <li><strong>Operational Challenges:</strong> High management complexity, disparate security configurations across consoles, high egress data transfer fees between providers, and necessity for multi-cloud tooling (Terraform, Kubernetes).</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 1.8 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.8 Hybrid Cloud vs Multi-Cloud (Crucial 7-Mark Comparison)</span>
          </div>
          <span class="sub-topic-badge">Exam Distinction</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Feature</th>
                  <th>Hybrid Cloud</th>
                  <th>Multi-Cloud</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Main Concept</strong></td>
                  <td>Combining different <em>types of environments</em> (Private + Public)</td>
                  <td>Using multiple <em>cloud service providers</em> (e.g. AWS + Azure + GCP)</td>
                </tr>
                <tr>
                  <td><strong>Typical Setup</strong></td>
                  <td>On-premises private datacenter bound to a public cloud</td>
                  <td>Services deployed across two or more public cloud vendors</td>
                </tr>
                <tr>
                  <td><strong>Primary Goal</strong></td>
                  <td>Flexibility, legacy integration, and cloud bursting</td>
                  <td>Vendor diversification, best-of-breed tools, and eliminating lock-in</td>
                </tr>
                <tr>
                  <td><strong>Vendor Lock-in</strong></td>
                  <td>Moderately reduced</td>
                  <td>Strongly reduced</td>
                </tr>
                <tr>
                  <td><strong>Integration Focus</strong></td>
                  <td>Tightly bound private-to-public network pipe (Direct Connect / VPN)</td>
                  <td>Independent workloads or abstracted container orchestration (Kubernetes)</td>
                </tr>
                <tr>
                  <td><strong>Example</strong></td>
                  <td>On-premises OpenStack datacenter + AWS EC2</td>
                  <td>AWS for Compute + Azure for Active Directory + GCP for BigQuery</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="exam-tip">
            <strong>⚠️ Crucial Lecture PPT Point:</strong> <em>Hybrid Cloud and Multi-Cloud are NOT mutually exclusive!</em> An enterprise can operate a <strong>Hybrid Multi-Cloud</strong> simultaneously—for example, connecting its private datacenter to AWS while also running enterprise analytics on Microsoft Azure.
          </div>
        </div>
      </div>

      <!-- Sub-topic 1.9 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.9 Master 5-Way Comparison Matrix of Deployment Models (7 Marks)</span>
          </div>
          <span class="sub-topic-badge">Master Matrix</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Parameter</th>
                  <th>Public Cloud</th>
                  <th>Private Cloud</th>
                  <th>Hybrid Cloud</th>
                  <th>Community Cloud</th>
                  <th>Multi-Cloud</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Ownership</strong></td>
                  <td>3rd-Party Provider</td>
                  <td>Single Organization</td>
                  <td>Mixed (Org + Provider)</td>
                  <td>Community Group</td>
                  <td>Multiple Providers</td>
                </tr>
                <tr>
                  <td><strong>Cost Model</strong></td>
                  <td>Lowest (Pure OpEx)</td>
                  <td>Highest (Heavy CapEx)</td>
                  <td>Medium to High</td>
                  <td>Shared across members</td>
                  <td>Variable / Complex</td>
                </tr>
                <tr>
                  <td><strong>Infrastructure Control</strong></td>
                  <td>Low / Provider-managed</td>
                  <td>Very High (Complete)</td>
                  <td>High (on private portion)</td>
                  <td>Medium to High</td>
                  <td>High (Distributed)</td>
                </tr>
                <tr>
                  <td><strong>Security & Privacy</strong></td>
                  <td>Standard (Multi-tenant)</td>
                  <td>Very High (Isolated)</td>
                  <td>Very High (Split data)</td>
                  <td>High (Industry-specific)</td>
                  <td>High (Multi-boundary)</td>
                </tr>
                <tr>
                  <td><strong>Scalability</strong></td>
                  <td>Near-Infinite</td>
                  <td>Hardware-bounded</td>
                  <td>Very High (Bursting)</td>
                  <td>Moderate</td>
                  <td>Near-Infinite</td>
                </tr>
                <tr>
                  <td><strong>Management</strong></td>
                  <td>Managed by Provider</td>
                  <td>Managed by In-House IT</td>
                  <td>Shared responsibility</td>
                  <td>Shared governance</td>
                  <td>Complex multi-tool</td>
                </tr>
                <tr>
                  <td><strong>Vendor Lock-in</strong></td>
                  <td>High</td>
                  <td>Low</td>
                  <td>Medium</td>
                  <td>Low to Medium</td>
                  <td>Lowest (Diversified)</td>
                </tr>
                <tr>
                  <td><strong>Best Suited For</strong></td>
                  <td>Startups, Web Apps</td>
                  <td>Banks, UIDAI, Defense</td>
                  <td>Enterprises with legacy</td>
                  <td>Hospitals, Univs, Gov</td>
                  <td>Global Enterprises</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 2 ==================== -->
  <div class="main-topic-card" id="u3-t2">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🏛️</span>
        <span class="main-topic-title">Topic 2: Cloud Architecture — Layers, Data Centres & Infrastructure</span>
        <span class="badge">Architecture Focus</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>5 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 2.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>2.1 Cloud Architecture Definition & 3 Main Parts</span>
          </div>
          <span class="sub-topic-badge">Overview</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Cloud Architecture:</strong> The blueprint and structural design of components and sub-systems (hardware, virtualized resources, software capabilities, network routing, and security policies) required to deliver cloud computing services to users.
          </div>
          <h4>The 3 Broad Structural Parts of Cloud Architecture</h4>
          <ul>
            <li><strong>1. Front End:</strong> The client-side interfaces, applications, browsers, and mobile devices through which users interact with cloud services.</li>
            <li><strong>2. Back End:</strong> The provider-side infrastructure, datacenter hardware, hypervisors, storage clusters, databases, security systems, and management engines.</li>
            <li><strong>3. Cloud Network / Internet:</strong> The high-speed networking fabric (IP routing, DNS, CDN, VPN) connecting front-end users to back-end cloud resources.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 2.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>2.2 Front-End vs Back-End Architecture & Functions</span>
          </div>
          <span class="sub-topic-badge">Front vs Back</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Component</th>
                  <th>Front-End Architecture</th>
                  <th>Back-End Architecture</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Ownership & Location</strong></td>
                  <td>Client device (Desktop, Laptop, Smartphone, Tablet)</td>
                  <td>Cloud Service Provider Datacenter facilities</td>
                </tr>
                <tr>
                  <td><strong>Interfaces</strong></td>
                  <td>Web browsers (Chrome, Edge), Mobile apps, Command-Line (CLI), REST SDKs</td>
                  <td>Server racks, virtualization layers, storage arrays, database engines</td>
                </tr>
                <tr>
                  <td><strong>Primary Role</strong></td>
                  <td>Input capture, presentation, session rendering, user authentication prompt</td>
                  <td>Data processing, storage durability, security enforcement, resource scheduling</td>
                </tr>
                <tr>
                  <td><strong>Core Functions</strong></td>
                  <td>Displaying UI dashboards, sending HTTP/HTTPS API requests</td>
                  <td>Authentication verification, transaction execution, data persistence, auto-scaling</td>
                </tr>
                <tr>
                  <td><strong>Examples</strong></td>
                  <td>AWS Management Console, Google Drive Web UI, Netflix mobile app</td>
                  <td>AWS EC2 hypervisor pools, Amazon S3 storage servers, DynamoDB clusters</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Sub-topic 2.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>2.3 Physical Infrastructure & Data Centres</span>
          </div>
          <span class="sub-topic-badge">Datacenters</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Data Centre:</strong> A physical, high-security facility housing computer servers, storage systems, networking switches, redundant power generators, and climate cooling equipment used to operate cloud computing services.
          </div>
          <h4>Core Physical Infrastructure Sub-Systems</h4>
          <ul>
            <li><strong>Compute Racks:</strong> Standardized 19-inch server racks populated with multi-core x86 and ARM blade servers.</li>
            <li><strong>Storage Infrastructure:</strong> SAN (Storage Area Network), NAS arrays, and petabyte-scale hard drive / NVMe SSD storage chassis.</li>
            <li><strong>Power Redundancy:</strong> Dual utility grid feeds, Uninterruptible Power Supplies (UPS battery banks), and diesel backup generators.</li>
            <li><strong>Cooling & Climate Systems:</strong> HVAC chillers, hot/cold aisle containment, and liquid cooling for high-density AI accelerators.</li>
            <li><strong>Physical Security:</strong> Biometric mantrap doors, 24/7 CCTV surveillance, and perimeter fencing.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 2.4 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>2.4 Geographic Distribution: Regions vs Availability Zones</span>
          </div>
          <span class="sub-topic-badge">Regions & AZs</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="grid-2">
            <div class="subcard">
              <h4>Geographic Region</h4>
              <p>A separate physical geographic area around the world (e.g. <code>ap-south-1</code> in Mumbai, <code>us-east-1</code> in N. Virginia). Each Region is completely isolated from other regions to achieve fault tolerance and satisfy national data sovereignty regulations.</p>
            </div>
            <div class="subcard">
              <h4>Availability Zone (AZ)</h4>
              <p>One or more discrete physical datacenters located within a Region, each with independent power, cooling, and networking. AZs are connected via ultra-low-latency private fiber. Designing apps across multi-AZs ensures zero downtime even if a lightning strike or flood takes down an entire datacenter.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 2.5 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>2.5 Virtualization Layer & Hypervisors in Cloud Architecture</span>
          </div>
          <span class="sub-topic-badge">Virtualization</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p>The <strong>Virtualization Layer</strong> acts as the fundamental abstraction bridge between physical hardware and cloud services:</p>
          <ul>
            <li><strong>Server Consolidation:</strong> Converts single physical machines into multiple isolated Virtual Machines (VMs) running different operating systems simultaneously (e.g., VM 1 Web Server, VM 2 Database Server).</li>
            <li><strong>Type 1 Hypervisors:</strong> Bare-metal hypervisors (KVM, VMware ESXi) drive cloud hyperscaler infrastructure for raw bare-metal efficiency.</li>
            <li><strong>Resource Pooling:</strong> Dynamically slices and overcommits CPU, RAM, and network bandwidth according to tenant demand.</li>
          </ul>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 3 ==================== -->
  <div class="main-topic-card" id="u3-t3">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">⚙️</span>
        <span class="main-topic-title">Topic 3: The 5 Core Cloud Sub-Architectures</span>
        <span class="badge badge-accent">5 Core Pillars</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>5 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 3.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>3.1 Compute Architecture (VMs, Containers, Serverless & Bare-Metal)</span>
          </div>
          <span class="sub-topic-badge">Compute</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Compute Layer:</strong> Provides CPU processing, memory execution, and application compute engines dynamically allocated to meet variable workload requests.
          </div>
          <h4>The 4 Major Cloud Compute Models</h4>
          <ul>
            <li><strong>Virtual Machines (IaaS):</strong> Full guest OS virtualization (e.g. AWS EC2, Azure VMs, Google Compute Engine). Long-running, stateful, full OS control.</li>
            <li><strong>Containers (CaaS):</strong> OS-level lightweight isolation sharing the host kernel (e.g. Docker, AWS ECS/EKS, Azure AKS, Google GKE). Fast spin-up, portable.</li>
            <li><strong>Serverless Computing (FaaS):</strong> Event-driven, stateless functions executed on-demand with zero server management and micro-billing per millisecond (e.g. AWS Lambda, Azure Functions, Google Cloud Functions).</li>
            <li><strong>Dedicated Bare-Metal Instances:</strong> Physical non-virtualized servers provisioned for extreme workloads (SAP HANA) or nested virtualization.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 3.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>3.2 Storage Architecture (Block, Object, File & Replication)</span>
          </div>
          <span class="sub-topic-badge">Storage</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Storage Architecture:</strong> Provides scalable, network-accessible data storage characterized by high durability, automatic multi-AZ replication, access control, and tiered encryption.
          </div>
          <ul>
            <li><strong>Block Storage:</strong> Raw addressable block volumes mounted over SAN/iSCSI for VM boot disks and low-latency databases (e.g. AWS EBS, Azure Managed Disks, GCP Persistent Disk).</li>
            <li><strong>Object Storage:</strong> Flat unstructured data store accessible via HTTP/REST APIs storing file bytes, custom metadata, and unique keys. Infinite scale for images, backups, media (e.g. AWS S3, Azure Blob, Google Cloud Storage).</li>
            <li><strong>File Storage:</strong> Shared hierarchical file system mounted concurrently across multiple servers via NFS/SMB (e.g. AWS EFS, Azure Files, GCP Filestore).</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 3.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>3.3 Network Architecture (VPCs, Subnets, Routers, Firewalls & Gateways)</span>
          </div>
          <span class="sub-topic-badge">Network</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p>Enables secure, high-throughput communication between cloud components, clients, and datacenters:</p>
          <ul>
            <li><strong>Virtual Private Cloud (VPC):</strong> Logically isolated virtual network dedicated to a tenant account.</li>
            <li><strong>Subnets:</strong> IP address ranges partitioned into Public Subnets (Internet-accessible) and Private Subnets (isolated databases).</li>
            <li><strong>Internet & NAT Gateways:</strong> Route inbound web traffic and allow private instances to download security updates without exposing them to public inbound attacks.</li>
            <li><strong>Virtual Firewalls:</strong> Security Groups (stateful instance-level firewalls) and Network ACLs (stateless subnet-level boundary guards).</li>
            <li><strong>Virtual Private Network (VPN) & Direct Connect:</strong> Encrypted tunnels linking corporate offices directly into cloud VPCs.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 3.4 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>3.4 Security Architecture & Identity and Access Management (IAM)</span>
          </div>
          <span class="sub-topic-badge">Security & IAM</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Security Architecture:</strong> Design of protective controls, authentication barriers, data encryption mechanisms, and audit trails to protect cloud assets.
          </div>
          <h4>Core Security Controls</h4>
          <ul>
            <li><strong>IAM:</strong> Controls <em>Authentication</em> (Who are you?) and <em>Authorization</em> (What resources can you touch?) via Users, Groups, Roles, and JSON Policies.</li>
            <li><strong>Data Encryption:</strong> Encryption-at-Rest (AES-256 via KMS) and Encryption-in-Transit (TLS 1.3 cryptographic tunnels).</li>
            <li><strong>Multi-Factor Authentication (MFA):</strong> Prevents credential stuffing breaches.</li>
            <li><strong>Principle of Least Privilege:</strong> Granting zero trust and minimal permissions required for specific operational tasks.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 3.5 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>3.5 Management Architecture (Provisioning, Billing, Monitoring & Capacity)</span>
          </div>
          <span class="sub-topic-badge">Management</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p>Controls, monitors, and orchestrates the entire cloud lifecycle:</p>
          <ul>
            <li><strong>Resource Provisioning:</strong> Infrastructure-as-Code (IaC) engines (AWS CloudFormation, Terraform).</li>
            <li><strong>Monitoring & Telemetry:</strong> Real-time metrics collection, CPU alarms, and automated alerts (AWS CloudWatch, Azure Monitor).</li>
            <li><strong>Billing & FinOps:</strong> Pay-as-you-go metered chargeback, cost allocation tags, and budget thresholds.</li>
            <li><strong>Capacity Planning:</strong> Predictive analytics to automatically reserve compute reservations before seasonal spikes.</li>
          </ul>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 4 ==================== -->
  <div class="main-topic-card" id="u3-t4">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">📈</span>
        <span class="main-topic-title">Topic 4: Principles, Scalability, Elasticity & High Availability</span>
        <span class="badge badge-priority">High-Yield Exam Focus</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>6 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 4.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>4.1 Scalability — Vertical (Scale Up), Horizontal (Scale Out) & Diagonal Scaling</span>
          </div>
          <span class="sub-topic-badge">Scalability</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Scalability:</strong> The planned capability of a system to handle growing workloads by provisioning additional hardware or compute resources without degrading application performance.
          </div>
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Feature</th>
                  <th>Vertical Scaling (Scale Up)</th>
                  <th>Horizontal Scaling (Scale Out)</th>
                  <th>Diagonal Scaling</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Meaning</strong></td>
                  <td>Increasing CPU, RAM, or Disk of an <em>existing single machine</em></td>
                  <td>Adding <em>more independent server nodes</em> into the cluster</td>
                  <td>Combining both vertical upgrades and horizontal node additions</td>
                </tr>
                <tr>
                  <td><strong>Common Term</strong></td>
                  <td>Scale Up / Scale Down</td>
                  <td>Scale Out / Scale In</td>
                  <td>Hybrid / Combined Scaling</td>
                </tr>
                <tr>
                  <td><strong>Example</strong></td>
                  <td>Upgrading a VM from 4 GB RAM & 2 vCPUs to 16 GB RAM & 8 vCPUs</td>
                  <td>Scaling a web tier from 2 EC2 instances to 10 EC2 instances behind an ALB</td>
                  <td>First upgrade instances to 16 GB, then spawn additional instances</td>
                </tr>
                <tr>
                  <td><strong>Hardware Limit</strong></td>
                  <td>Bounded by physical server socket/motherboard capacity</td>
                  <td>Near-infinite (distributed cloud architecture)</td>
                  <td>High flexibility and high capacity ceiling</td>
                </tr>
                <tr>
                  <td><strong>Downtime Risk</strong></td>
                  <td>Often requires server reboot or downtime</td>
                  <td>Zero-downtime (new nodes spin up seamlessly)</td>
                  <td>Minimal downtime when managed properly</td>
                </tr>
                <tr>
                  <td><strong>Architecture</strong></td>
                  <td>Simpler; no distributed state changes</td>
                  <td>Requires Load Balancers and stateless web tiers</td>
                  <td>Requires advanced auto-scaling policies</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Sub-topic 4.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>4.2 Elasticity — Definition, Working & Auto-Scaling</span>
          </div>
          <span class="sub-topic-badge">Elasticity</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Elasticity:</strong> The degree to which a cloud system is able to adapt to workload changes by provisioning and de-provisioning resources in an automated manner, such that at each point in time the available resources match the current demand as closely as possible.
          </div>
          <h4>Real-World E-Commerce Example (From Lecture Slides)</h4>
          <ul>
            <li><strong>Normal Morning Traffic:</strong> Web tier operates on <strong>2 servers</strong> to handle typical checkout volume.</li>
            <li><strong>Flash Sale Peak Surge (12:00 PM):</strong> Traffic surges 500%. Cloud elasticity auto-scales instances dynamically from <strong>2 servers &rarr; 10 servers</strong> without dropped requests.</li>
            <li><strong>Post-Sale Cooldown (3:00 PM):</strong> Traffic normalizes. Elasticity automatically de-provisions the 8 extra instances, scaling back down to <strong>2 servers</strong> to prevent idle cloud billing waste.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 4.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>4.3 Scalability vs Elasticity (Exam Critical Comparison)</span>
          </div>
          <span class="sub-topic-badge">Exam Comparison</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Feature</th>
                  <th>Scalability</th>
                  <th>Elasticity</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Meaning</strong></td>
                  <td>Ability to handle increasing workload by adding resources</td>
                  <td>Ability to dynamically grow AND shrink resources to match live demand</td>
                </tr>
                <tr>
                  <td><strong>Primary Focus</strong></td>
                  <td>Handling maximum capacity ceiling</td>
                  <td>Optimizing operational cost and matching dynamic demand swings</td>
                </tr>
                <tr>
                  <td><strong>Directionality</strong></td>
                  <td>Mainly unidirectional (Expanding capacity)</td>
                  <td>Bidirectional (Scaling Out during peaks, Scaling In during lulls)</td>
                </tr>
                <tr>
                  <td><strong>Operation Nature</strong></td>
                  <td>Often manual, planned, or architectural</td>
                  <td>Fully automated and real-time (driven by metric threshold alarms)</td>
                </tr>
                <tr>
                  <td><strong>Time Horizon</strong></td>
                  <td>Long-term business or user base growth</td>
                  <td>Short-term, hour-by-hour dynamic fluctuations</td>
                </tr>
                <tr>
                  <td><strong>Example</strong></td>
                  <td>Migrating from 2 servers to 10 servers for yearly growth</td>
                  <td>2 servers &rarr; 10 servers (Black Friday) &rarr; 2 servers (Saturday morning)</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="exam-tip">
            <strong>💡 Memory Trick:</strong> Scalability = <em>Can the system grow?</em> | Elasticity = <em>Can the system automatically grow AND shrink?</em>
          </div>
        </div>
      </div>

      <!-- Sub-topic 4.4 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>4.4 Load Balancing — Request Distribution Workflow & Health Checks</span>
          </div>
          <span class="sub-topic-badge">Load Balancing</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Load Balancer:</strong> A reverse-proxy network device or managed service that acts as a single point of entry to accept incoming application traffic and intelligently distribute requests across a pool of healthy backend servers.
          </div>
          <h4>Step-by-Step Request Distribution Workflow</h4>
          <ol>
            <li><strong>Client Request:</strong> User browser initiates an HTTPS request to <code>example.com</code>.</li>
            <li><strong>Load Balancer Ingestion:</strong> The public Load Balancer terminates the TLS handshake and ingests the request.</li>
            <li><strong>Health Check Evaluation:</strong> Checks its dynamic registry to filter out servers marked unhealthy.</li>
            <li><strong>Algorithm Execution:</strong> Applies configured routing algorithm (Round Robin, Least Connections, IP Hash) to select an optimal server.</li>
            <li><strong>Forwarding & Processing:</strong> Forwards request to private IP of selected worker; worker generates response.</li>
            <li><strong>Return Response:</strong> Load balancer delivers response back to client transparently.</li>
          </ol>
        </div>
      </div>

      <!-- Sub-topic 4.5 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>4.5 High Availability vs Fault Tolerance & Availability Calculation Formula</span>
          </div>
          <span class="sub-topic-badge">HA vs FT</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="grid-2">
            <div class="subcard">
              <h4>High Availability (HA)</h4>
              <p>Ensures the system remains accessible and operational for a specified percentage of time (e.g. 99.9% or 99.99%) with minimal perceptible downtime. Leverages automated failover clusters, load balancers, and multi-AZ deployments.</p>
            </div>
            <div class="subcard">
              <h4>Fault Tolerance (FT)</h4>
              <p>The aggressive capability of a system to continue functioning with <strong>zero downtime and zero data loss</strong> even when one or more underlying physical components fail completely. Relies on 100% hot duplicate hardware mirroring.</p>
            </div>
          </div>
          <h4>High Availability Mathematical Formula (From Lecture Slides)</h4>
          <div class="def-box">
            $$\\text{{Availability (\\%)}} = \\frac{{\\text{{Uptime}}}}{{\\text{{Uptime}} + \\text{{Downtime}}}} \\times 100$$
          </div>
          <p><strong>Example Problem:</strong> If a cloud portal operates for 999 hours in a month and experiences 1 hour of total unexpected downtime:</p>
          $$\\text{{Availability}} = \\frac{{999}}{{999 + 1}} \\times 100 = \\frac{{999}}{{1000}} \\times 100 = 99.9\\% \\quad (\\text{{Three Nines}})$$
        </div>
      </div>

      <!-- Sub-topic 4.6 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>4.6 8 Golden Principles of Cloud Architecture</span>
          </div>
          <span class="sub-topic-badge">8 Principles</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>No.</th>
                  <th>Principle</th>
                  <th>Architectural Meaning & Exam Explanation</th>
                </tr>
              </thead>
              <tbody>
                <tr><td>1</td><td><strong>Scalability</strong></td><td>Architecture must accommodate sustained long-term workload growth.</td></tr>
                <tr><td>2</td><td><strong>Elasticity</strong></td><td>Compute and storage capacity must grow and shrink dynamically with demand.</td></tr>
                <tr><td>3</td><td><strong>High Availability</strong></td><td>Services must maintain operational uptime across datacenter disruptions.</td></tr>
                <tr><td>4</td><td><strong>Fault Tolerance</strong></td><td>Components must tolerate hardware failures without halting overall service.</td></tr>
                <tr><td>5</td><td><strong>Security</strong></td><td>Zero-Trust defense-in-depth across data, network, compute, and IAM.</td></tr>
                <tr><td>6</td><td><strong>Automation</strong></td><td>Deployment, health healing, patching, and scaling should eliminate manual human steps.</td></tr>
                <tr><td>7</td><td><strong>Resource Optimization</strong></td><td>Rightsizing instances, using spot instances, and auto-deleting idle volumes.</td></tr>
                <tr><td>8</td><td><strong>Continuous Monitoring</strong></td><td>Centralized metric ingestion, log tracing, and automated anomaly alarms.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 5 ==================== -->
  <div class="main-topic-card" id="u3-t5">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">👥</span>
        <span class="main-topic-title">Topic 5: Structural Models: Multi-Tenant Architecture</span>
        <span class="badge badge-priority">Very High Priority (10 Marks)</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>5 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">

      <!-- Diagram -->
      <div class="diagram-container">
        {SVG_MULTI_TENANT_PATTERNS}
        <div class="diagram-caption">Figure 3.2: Multi-Tenant Database Isolation Patterns (Pool vs Bridge vs Silo)</div>
      </div>
      
      <!-- Sub-topic 5.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>5.1 Multi-Tenant Architecture Definition, Tenant Concept & SaaS Real-World Examples</span>
          </div>
          <span class="sub-topic-badge">Definition</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Multi-Tenant Architecture:</strong> A software architecture where a single instance of an application runs on shared physical/virtual servers, serving multiple distinct customer organizations (tenants), while strictly isolating each tenant's data, custom configurations, and user access.
          </div>
          <h4>What is a Tenant?</h4>
          <p>A <strong>Tenant</strong> is an isolated customer organization, business entity, or university subscriber that accesses the shared cloud application. For instance, in a university ERP software, University A, University B, and University C share the exact same backend codebase, but University A can never view or modify records belonging to University B.</p>
          <h4>Prominent Multi-Tenant SaaS Examples (From Lecture Slides)</h4>
          <ul>
            <li><strong>Salesforce:</strong> Pioneers of multi-tenancy CRM; thousands of enterprises share the same database cluster with logical security isolation.</li>
            <li><strong>Shopify:</strong> Millions of distinct online merchants operate independent storefronts powered by shared cloud infrastructure.</li>
            <li><strong>Slack:</strong> Independent corporate workgroups collaborate inside their isolated communication spaces hosted on shared AWS clusters.</li>
            <li><strong>HubSpot, Workday & Zoom:</strong> Enterprise marketing, human resource, and video conferencing systems built entirely on multi-tenant foundations.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 5.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>5.2 Single-Tenant vs Multi-Tenant Architecture (Comparison Matrix)</span>
          </div>
          <span class="sub-topic-badge">Tenancy Comparison</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Feature</th>
                  <th>Single-Tenant Architecture</th>
                  <th>Multi-Tenant Architecture</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Infrastructure</strong></td>
                  <td>Dedicated physical or virtual servers per customer</td>
                  <td>Shared compute, database, storage, and networking</td>
                </tr>
                <tr>
                  <td><strong>Cost per Customer</strong></td>
                  <td>Much higher (CapEx & dedicated hosting per client)</td>
                  <td>Significantly lower (Economy of scale & shared pooling)</td>
                </tr>
                <tr>
                  <td><strong>Security Isolation</strong></td>
                  <td>Highest physical isolation (Independent perimeter)</td>
                  <td>Logical isolation (Requires strict application/DB filters)</td>
                </tr>
                <tr>
                  <td><strong>Scalability & Elasticity</strong></td>
                  <td>Low; requires scaling separate servers for each client</td>
                  <td>Exceptional; cluster automatically scales to serve all tenants</td>
                </tr>
                <tr>
                  <td><strong>Maintenance & Upgrades</strong></td>
                  <td>Complex; patching must be repeated on each customer's stack</td>
                  <td>Centralized; a single software release updates 100% of tenants</td>
                </tr>
                <tr>
                  <td><strong>Tenant Customization</strong></td>
                  <td>Total freedom to modify database schema and server OS</td>
                  <td>Limited to tenant-specific configuration toggles</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Sub-topic 5.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>5.3 The 3 Database Isolation Patterns: Pool, Bridge & Silo</span>
          </div>
          <span class="sub-topic-badge">Isolation Patterns</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="grid-3">
            <div class="subcard">
              <h4>1. Pool Pattern (Shared DB / Shared Table)</h4>
              <p>All tenants share the exact same database tables. Every row includes a mandatory <code>tenant_id</code> partition key. Isolation is enforced through application SQL filters or database <strong>Row-Level Security (RLS)</strong>.</p>
              <p style="font-size: 0.85rem; color: var(--accent);"><strong>Pros:</strong> Lowest cost, simplest management.<br><strong>Cons:</strong> Highest risk of cross-tenant data leak if SQL filter is missed.</p>
            </div>
            <div class="subcard">
              <h4>2. Bridge Pattern (Shared DB / Separate Schema)</h4>
              <p>All tenants reside in the same physical database engine instance, but each tenant receives their own dedicated database <strong>Schema</strong> (e.g. <code>schema_tenant_a</code>, <code>schema_tenant_b</code>).</p>
              <p style="font-size: 0.85rem; color: var(--success);"><strong>Pros:</strong> Balanced cost and logical schema isolation.<br><strong>Cons:</strong> Migrations must run across hundreds of schemas.</p>
            </div>
            <div class="subcard">
              <h4>3. Silo Pattern (Database-per-Tenant)</h4>
              <p>Each tenant gets a completely dedicated database instance. Zero shared tables, zero shared schemas. Dedicated connection credentials and isolated disk storage.</p>
              <p style="font-size: 0.85rem; color: var(--purple);"><strong>Pros:</strong> Maximum isolation, compliance, zero cross-tenant leak.<br><strong>Cons:</strong> Highest cost, idle DB resource waste.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 5.4 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>5.4 Comparison of Pool vs Bridge vs Silo Patterns (7 Marks)</span>
          </div>
          <span class="sub-topic-badge">Pattern Comparison</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Feature</th>
                  <th>Pool Pattern</th>
                  <th>Bridge Pattern</th>
                  <th>Silo Pattern</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Database Instance</strong></td>
                  <td>100% Shared</td>
                  <td>Shared Engine Instance</td>
                  <td>Separate, Dedicated DB Instance</td>
                </tr>
                <tr>
                  <td><strong>Schema</strong></td>
                  <td>Shared Schema & Tables</td>
                  <td>Separate Schema per Tenant</td>
                  <td>Dedicated Schemas on Dedicated DBs</td>
                </tr>
                <tr>
                  <td><strong>Data Isolation</strong></td>
                  <td>Logical (via <code>tenant_id</code> & RLS)</td>
                  <td>Medium (Schema-level boundaries)</td>
                  <td>Maximum (Physical/Instance level)</td>
                </tr>
                <tr>
                  <td><strong>Hosting Cost</strong></td>
                  <td>Lowest cost per tenant</td>
                  <td>Moderate</td>
                  <td>Highest cost per tenant</td>
                </tr>
                <tr>
                  <td><strong>Backup / Restore</strong></td>
                  <td>Complex to restore single tenant</td>
                  <td>Moderate</td>
                  <td>Easiest (Snapshot single tenant DB)</td>
                </tr>
                <tr>
                  <td><strong>Best Suited For</strong></td>
                  <td>High-volume, low-cost B2C/B2B SaaS</td>
                  <td>Mid-market SaaS with customizations</td>
                  <td>Banks, Healthcare, Defense enterprises</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Sub-topic 5.5 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>5.5 Multi-Tenant Security & The Noisy Neighbor Problem</span>
          </div>
          <span class="sub-topic-badge">Challenges & Fixes</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box" style="border-left-color: var(--danger);">
            <strong>The Noisy Neighbor Problem:</strong> In a shared multi-tenant environment, if one tenant experiences a sudden massive traffic surge or runs unoptimized database queries, it consumes disproportionate CPU, RAM, disk I/O, or connection pool bandwidth, severely degrading performance for all other innocent tenants on the same server.
          </div>
          <h4>Effective Mitigation Strategies</h4>
          <ul>
            <li><strong>Tenant Resource Quotas:</strong> Enforce strict CPU/memory limits per tenant using Linux cgroups or container constraints.</li>
            <li><strong>API Rate Limiting & Throttling:</strong> Enforce token-bucket rate limits per <code>tenant_id</code> (e.g. max 500 requests/minute).</li>
            <li><strong>Dedicated Connection Pooling:</strong> Avoid a single global database pool; allocate partitioned pools to prevent exhaustion.</li>
            <li><strong>Tiered Silo Migration:</strong> Automatically migrate high-volume enterprise "whale" tenants into dedicated Silo instances.</li>
            <li><strong>Tenant-Specific Encryption Keys:</strong> Protect sensitive tenant rows using distinct AWS KMS encryption keys.</li>
          </ul>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 6 ==================== -->
  <div class="main-topic-card" id="u3-t6">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🔀</span>
        <span class="main-topic-title">Topic 6: Structural Models: Multi-Server & Distributed Architecture</span>
        <span class="badge badge-accent">Structural Models</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>7 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">

      <!-- Diagram -->
      <div class="diagram-container">
        {SVG_THREE_TIER_ARCHITECTURE}
        <div class="diagram-caption">Figure 3.3: Multi-Server 3-Tier Enterprise Web Architecture</div>
      </div>
      
      <!-- Sub-topic 6.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>6.1 Multi-Server Architecture Definition, Objectives & Single vs Multi-Server</span>
          </div>
          <span class="sub-topic-badge">Multi-Server</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Multi-Server Architecture:</strong> A system design where an application is decoupled and deployed across two or more interconnected physical or virtual servers, partitioning responsibilities (web presentation, application business logic, caching, database persistence) so each layer can scale and fail independently.
          </div>
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Feature</th>
                  <th>Single-Server Architecture</th>
                  <th>Multi-Server Architecture</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Core Setup</strong></td>
                  <td>1 machine runs Web, App, and Database</td>
                  <td>Workload split across dedicated server tiers</td>
                </tr>
                <tr>
                  <td><strong>Scalability</strong></td>
                  <td>Vertical scaling only (hardware limits)</td>
                  <td>Horizontal scaling (Add instances dynamically)</td>
                </tr>
                <tr>
                  <td><strong>Reliability</strong></td>
                  <td>Zero; single point of failure crashes all</td>
                  <td>High; if 1 server dies, other servers handle traffic</td>
                </tr>
                <tr>
                  <td><strong>Maintenance</strong></td>
                  <td>Requires system downtime to patch or upgrade</td>
                  <td>Zero-downtime rolling deployments</td>
                </tr>
                <tr>
                  <td><strong>Cost</strong></td>
                  <td>Low setup cost; higher long-term limits</td>
                  <td>Higher base cost; superior cost per user at scale</td>
                </tr>
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
            <span>6.2 Multi-Server Components & 3-Tier Web Architecture</span>
          </div>
          <span class="sub-topic-badge">3 Tiers</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <h4>The 3 Classic Enterprise Tiers</h4>
          <ul>
            <li><strong>Tier 1: Web Presentation Tier (Load Balancer & Web Servers):</strong> Handles incoming public HTTP/HTTPS traffic, performs SSL/TLS termination, serves static CSS/JS assets, and forwards dynamic requests to the app tier. (e.g., Nginx, Apache HTTPD).</li>
            <li><strong>Tier 2: Application Tier (Business Logic & Caching):</strong> Runs core computational logic, user authentication, checkout algorithms, and API processing. Scaled horizontally via auto-scaling groups with in-memory Redis/Memcached caching.</li>
            <li><strong>Tier 3: Database Data Tier (Persistence & Storage):</strong> Stores structured data with high durability. Configured with a Primary Master (handles Writes) and Read-Only Replicas (handles Reads) across multiple AZs.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 6.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>6.3 Load Balancer Types & Layer 4 vs Layer 7 Load Balancing</span>
          </div>
          <span class="sub-topic-badge">L4 vs L7</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <h4>3 Types of Load Balancers</h4>
          <p><strong>Hardware LB</strong> (Dedicated appliance like F5 BIG-IP), <strong>Software LB</strong> (Open-source software like HAProxy/Nginx), and <strong>Cloud LB</strong> (Managed hyperscaler services like AWS ALB/NLB, Azure Load Balancer).</p>
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Feature</th>
                  <th>Layer 4 Load Balancer (Network)</th>
                  <th>Layer 7 Load Balancer (Application)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>OSI Layer</strong></td>
                  <td>Transport Layer (Layer 4)</td>
                  <td>Application Layer (Layer 7)</td>
                </tr>
                <tr>
                  <td><strong>Protocols</strong></td>
                  <td>TCP, UDP, TLS</td>
                  <td>HTTP, HTTPS, gRPC, WebSockets</td>
                </tr>
                <tr>
                  <td><strong>Routing Decision</strong></td>
                  <td>Based strictly on Source/Dest IP & Port</td>
                  <td>Based on URL path, HTTP headers, cookies, hostnames</td>
                </tr>
                <tr>
                  <td><strong>Content Inspection</strong></td>
                  <td>No (Packets forwarded without inspecting payload)</td>
                  <td>Yes (Can route <code>/api</code> to App servers, <code>/static</code> to S3)</td>
                </tr>
                <tr>
                  <td><strong>Performance & Latency</strong></td>
                  <td>Ultra-high throughput, sub-millisecond latency</td>
                  <td>Slightly higher compute overhead due to deep inspection</td>
                </tr>
                <tr>
                  <td><strong>AWS Example</strong></td>
                  <td>Network Load Balancer (NLB)</td>
                  <td>Application Load Balancer (ALB)</td>
                </tr>
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
            <span>6.4 The 6 Load Balancing Algorithms (From Lecture Slides)</span>
          </div>
          <span class="sub-topic-badge">Algorithms</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <ul>
            <li><strong>1. Round Robin:</strong> Cyclically distributes incoming requests sequentially down the server list (Request 1 &rarr; Server 1, Request 2 &rarr; Server 2, Request 3 &rarr; Server 3, Request 4 &rarr; Server 1). Best when all servers have identical hardware specs.</li>
            <li><strong>2. Weighted Round Robin:</strong> Assigns numerical weights proportional to server processing power (e.g. Server 1 weight 3, Server 2 weight 1; Server 1 receives 3x more requests).</li>
            <li><strong>3. Least Connections:</strong> Routes the incoming request to the server that currently has the lowest active open client connections. Ideal for transactions with variable processing durations.</li>
            <li><strong>4. Weighted Least Connections:</strong> Considers both current open connections and the baseline capacity/weight of each server node.</li>
            <li><strong>5. IP Hash:</strong> Hashes the client's source IP address to determine the target backend server. Ensures session stickiness (the same client consistently reaches the same server).</li>
            <li><strong>6. Response Time Based:</strong> Directs requests to servers exhibiting the fastest health-check ping and lowest response latency.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 6.5 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>6.5 Distributed System Architecture, Objectives & Distribution Transparency</span>
          </div>
          <span class="sub-topic-badge">Distributed Systems</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Distributed System:</strong> A collection of independent, autonomous computers that communicate via a computer network and coordinate their actions by passing messages, presenting themselves to end users as a single coherent unified system.
          </div>
          <h4>Centralized vs Distributed Systems</h4>
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Feature</th>
                  <th>Centralized System</th>
                  <th>Distributed System</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Processing</strong></td>
                  <td>Single central computer (Mainframe)</td>
                  <td>Multiple independent networked computers</td>
                </tr>
                <tr>
                  <td><strong>Failure Impact</strong></td>
                  <td>Single point of failure halts entire system</td>
                  <td>Failure isolated to single node; cluster continues</td>
                </tr>
                <tr>
                  <td><strong>Scalability</strong></td>
                  <td>Limited by physical mainframe chassis</td>
                  <td>Near-infinite by adding standard commodity nodes</td>
                </tr>
                <tr>
                  <td><strong>Communication</strong></td>
                  <td>Local shared memory / IPC bus</td>
                  <td>Network message passing (gRPC, REST, Kafka)</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="def-box">
            <strong>Distribution Transparency:</strong> The property of a distributed system that conceals from users and application programs the fact that processes and physical resources are distributed across multiple computers. For example, when purchasing on Amazon, the buyer has no awareness of which physical datacenter or partition processed the credit card.
          </div>
        </div>
      </div>

      <!-- Sub-topic 6.6 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>6.6 Cloud Distributed Systems: CDN Edge Caching & API Communication</span>
          </div>
          <span class="sub-topic-badge">CDN & APIs</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <h4>Content Delivery Networks (CDN) as a Distributed System</h4>
          <p>A <strong>CDN</strong> (e.g. AWS CloudFront, Cloudflare, Akamai) is a geographically distributed network of edge cache servers designed to deliver web assets at lightning speeds:</p>
          <ul>
            <li><strong>Edge Location Caching:</strong> When a user in Mumbai requests a video hosted in Virginia, the CDN caches the video at a local Point of Presence (PoP) in Mumbai.</li>
            <li><strong>Cache Hit vs Cache Miss:</strong> If cached, the asset is delivered instantly from Mumbai (Cache Hit). If missing, it fetches once from Virginia (Origin Fetch), caches it, and serves subsequent users locally.</li>
          </ul>
          <h4>APIs as Distributed Connectors</h4>
          <p>Application Programming Interfaces (REST/JSON, gRPC) serve as the standard contracts enabling decoupled distributed services to exchange records without knowing internal database schemas.</p>
        </div>
      </div>

      <!-- Sub-topic 6.7 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>6.7 Master 3-Way Architectural Comparison: Multi-Tenant vs Multi-Server vs Distributed (7 Marks)</span>
          </div>
          <span class="sub-topic-badge">Master Comparison</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Feature</th>
                  <th>Multi-Tenant Architecture</th>
                  <th>Multi-Server Architecture</th>
                  <th>Distributed System Architecture</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Main Concept</strong></td>
                  <td>Single application instance serving multiple customers</td>
                  <td>Application decoupled across multiple dedicated servers</td>
                  <td>Multiple autonomous computers presenting as one system</td>
                </tr>
                <tr>
                  <td><strong>Primary Focus</strong></td>
                  <td>Logical data isolation and cost sharing</td>
                  <td>Workload tiering and independent tier scaling</td>
                  <td>Distributed compute, consensus, and fault isolation</td>
                </tr>
                <tr>
                  <td><strong>Infrastructure</strong></td>
                  <td>Shared compute and database engines</td>
                  <td>Dedicated web, application, and database servers</td>
                  <td>Networked commodity nodes spread across regions</td>
                </tr>
                <tr>
                  <td><strong>Primary Benefit</strong></td>
                  <td>Maximum cost efficiency and zero maintenance per client</td>
                  <td>High availability, no single point of failure</td>
                  <td>Near-infinite scalability and disaster survivability</td>
                </tr>
                <tr>
                  <td><strong>Primary Challenge</strong></td>
                  <td>Cross-tenant data leakage & Noisy Neighbor problem</td>
                  <td>Server provisioning and load balancer configuration</td>
                  <td>Network latency, CAP theorem, and data consistency</td>
                </tr>
                <tr>
                  <td><strong>Real-World Example</strong></td>
                  <td>Salesforce CRM, Shopify, Slack</td>
                  <td>WordPress on Nginx + Node.js + MySQL Master/Replica</td>
                  <td>Google Search Index, Apache Cassandra, Amazon DynamoDB</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="exam-tip">
            <strong>💡 Memory Trick:</strong> Multi-Tenant = <em>Many Customers sharing 1 app</em> | Multi-Server = <em>Many Servers splitting tiers</em> | Distributed = <em>Many Computers acting as 1</em>.
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 7 ==================== -->
  <div class="main-topic-card" id="u3-t7">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">☁️</span>
        <span class="main-topic-title">Topic 7: Major Cloud Providers (AWS vs Azure vs GCP)</span>
        <span class="badge badge-priority">Very High Priority (7 Marks)</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>6 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 7.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>7.1 Amazon Web Services (AWS) — Foundation, Core Services & Ecosystem</span>
          </div>
          <span class="sub-topic-badge">AWS</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Amazon Web Services (AWS):</strong> Launched commercially in 2006 by Amazon, AWS is the world's most comprehensive and broadly adopted cloud platform, offering over 200+ fully featured services from datacenters globally.
          </div>
          <h4>Core AWS Services</h4>
          <ul>
            <li><strong>EC2 (Elastic Compute Cloud):</strong> Resizable virtual server compute capacity.</li>
            <li><strong>S3 (Simple Storage Service):</strong> Industry-standard object storage with 99.999999999% (11 9's) durability.</li>
            <li><strong>RDS (Relational Database Service):</strong> Managed MySQL, PostgreSQL, Oracle, and SQL Server with multi-AZ failover.</li>
            <li><strong>Lambda:</strong> Pioneer of event-driven serverless computing.</li>
            <li><strong>VPC (Virtual Private Cloud):</strong> Software-defined isolated virtual networks.</li>
            <li><strong>EKS & ECS:</strong> Managed Kubernetes (EKS) and native container execution (ECS).</li>
            <li><strong>Amazon Bedrock:</strong> Enterprise Generative AI foundation model hosting.</li>
            <li><strong>CloudWatch & CloudTrail:</strong> Real-time operational monitoring and governance audit logging.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 7.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>7.2 Microsoft Azure — Foundation, Enterprise Integration & Hybrid Dominance</span>
          </div>
          <span class="sub-topic-badge">Azure</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Microsoft Azure:</strong> Launched in 2010 by Microsoft, Azure is the leading enterprise-focused cloud platform, renowned for seamless Windows Server, Active Directory, SQL Server, and Microsoft 365 hybrid integration.
          </div>
          <h4>Core Azure Services</h4>
          <ul>
            <li><strong>Azure Virtual Machines:</strong> Scalable Windows and Linux virtual servers.</li>
            <li><strong>Azure Blob Storage:</strong> Massively scalable object storage for cloud-native apps.</li>
            <li><strong>Azure SQL Database:</strong> Fully managed relational database engine with automated tuning.</li>
            <li><strong>Azure Functions:</strong> Event-driven serverless code execution.</li>
            <li><strong>Azure Virtual Network (VNet):</strong> Private network interconnectivity.</li>
            <li><strong>AKS (Azure Kubernetes Service):</strong> Production managed Kubernetes cluster engine.</li>
            <li><strong>Microsoft Entra ID (formerly Azure AD):</strong> Global enterprise identity and single sign-on (SSO).</li>
            <li><strong>Azure App Service:</strong> Managed PaaS hosting for web applications and REST APIs.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 7.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>7.3 Google Cloud Platform (GCP) — Big Data, BigQuery, Vertex AI & GKE</span>
          </div>
          <span class="sub-topic-badge">Google Cloud</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Google Cloud Platform (GCP):</strong> Introduced in 2008 by Google, GCP excels in high-performance big data analytics, machine learning, artificial intelligence, and open-source container innovations (birthplace of Kubernetes).
          </div>
          <h4>Core GCP Services</h4>
          <ul>
            <li><strong>Compute Engine (GCE):</strong> High-performance virtual machines with custom machine sizing.</li>
            <li><strong>Cloud Storage:</strong> Unified object storage across standard, nearline, coldline, and archive tiers.</li>
            <li><strong>Cloud SQL & Spanner:</strong> Managed relational databases, including Cloud Spanner (globally distributed ACID DB).</li>
            <li><strong>BigQuery:</strong> Serverless, highly scalable multi-cloud data warehouse designed for petabyte-scale SQL analytics.</li>
            <li><strong>GKE (Google Kubernetes Engine):</strong> The industry's premier managed Kubernetes platform, created by the original authors of Kubernetes.</li>
            <li><strong>Vertex AI:</strong> Unified artificial intelligence platform for training and serving ML and Gemini models.</li>
            <li><strong>Cloud Run:</strong> Serverless container execution platform that automatically scales from zero to thousands of containers.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 7.4 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>7.4 Service-by-Service Mapping Table across AWS, Azure, and GCP</span>
          </div>
          <span class="sub-topic-badge">Mapping Table</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Cloud Capability</th>
                  <th>Amazon Web Services (AWS)</th>
                  <th>Microsoft Azure</th>
                  <th>Google Cloud Platform (GCP)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Virtual Machines</strong></td>
                  <td>Amazon EC2</td>
                  <td>Azure Virtual Machines</td>
                  <td>Google Compute Engine (GCE)</td>
                </tr>
                <tr>
                  <td><strong>Object Storage</strong></td>
                  <td>Amazon S3</td>
                  <td>Azure Blob Storage</td>
                  <td>Google Cloud Storage</td>
                </tr>
                <tr>
                  <td><strong>Block Storage</strong></td>
                  <td>Amazon EBS</td>
                  <td>Azure Managed Disks</td>
                  <td>GCP Persistent Disk</td>
                </tr>
                <tr>
                  <td><strong>Managed Relational DB</strong></td>
                  <td>Amazon RDS / Aurora</td>
                  <td>Azure SQL Database</td>
                  <td>Cloud SQL / Cloud Spanner</td>
                </tr>
                <tr>
                  <td><strong>Serverless Functions</strong></td>
                  <td>AWS Lambda</td>
                  <td>Azure Functions</td>
                  <td>Google Cloud Functions</td>
                </tr>
                <tr>
                  <td><strong>Managed Kubernetes</strong></td>
                  <td>Amazon EKS</td>
                  <td>Azure AKS</td>
                  <td>Google GKE</td>
                </tr>
                <tr>
                  <td><strong>Serverless Containers</strong></td>
                  <td>AWS Fargate</td>
                  <td>Azure Container Apps</td>
                  <td>Google Cloud Run</td>
                </tr>
                <tr>
                  <td><strong>Data Warehousing</strong></td>
                  <td>Amazon Redshift</td>
                  <td>Azure Synapse Analytics</td>
                  <td>Google BigQuery</td>
                </tr>
                <tr>
                  <td><strong>Identity Management</strong></td>
                  <td>AWS IAM</td>
                  <td>Microsoft Entra ID</td>
                  <td>Google Cloud IAM</td>
                </tr>
                <tr>
                  <td><strong>Monitoring & Logs</strong></td>
                  <td>Amazon CloudWatch</td>
                  <td>Azure Monitor</td>
                  <td>Google Cloud Monitoring</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Sub-topic 7.5 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>7.5 Pricing Models, Free Tiers & Main Cost Risks (From Lecture Slides)</span>
          </div>
          <span class="sub-topic-badge">Cost & Pricing</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Provider</th>
                  <th>Pricing & Discount Models</th>
                  <th>Main Cost Risks (Lecture Slides)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>AWS</strong></td>
                  <td>Pay-as-you-go, Reserved Instances (1 or 3 yr), Savings Plans (up to 72% off), Spot Instances (up to 90% off)</td>
                  <td>High cross-AZ data egress fees, NAT Gateway hourly & data charges, idle EBS unattached volumes, excessive API request calls.</td>
                </tr>
                <tr>
                  <td><strong>Microsoft Azure</strong></td>
                  <td>Pay-as-you-go, Reserved VM Instances, Azure Hybrid Benefit (reuse existing on-prem Windows/SQL licenses for massive savings)</td>
                  <td>Enterprise licensing misconfigurations, forgotten idle VMs running 24/7, costly inter-region data replication.</td>
                </tr>
                <tr>
                  <td><strong>Google Cloud</strong></td>
                  <td>Pay-as-you-go, Committed Use Discounts (CUDs), Automatic Sustained Use Discounts (auto-discount when run >25% of month), Spot VMs</td>
                  <td>Unoptimized SQL queries scanning massive petabytes in BigQuery, multi-region Cloud Storage replication, unmonitored egress bandwidth.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Sub-topic 7.6 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>7.6 Cloud Provider Selection Decision Matrix ("Which Provider Should You Choose?")</span>
          </div>
          <span class="sub-topic-badge">Decision Matrix</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Organizational / Workload Requirement</th>
                  <th>Most Recommended Provider</th>
                  <th>Core Strategic Justification</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Maximum Service Catalog & Mature Global Footprint</strong></td>
                  <td><strong>Amazon Web Services (AWS)</strong></td>
                  <td>Largest market share, most extensive managed services, and largest pool of certified cloud engineers worldwide.</td>
                </tr>
                <tr>
                  <td><strong>Heavy Windows Server, Active Directory & Office 365 Workloads</strong></td>
                  <td><strong>Microsoft Azure</strong></td>
                  <td>Native integration with Entra ID, Microsoft 365, and Azure Hybrid Benefit discounts for existing Windows licenses.</td>
                </tr>
                <tr>
                  <td><strong>Big Data Analytics, AI/ML & Petabyte SQL Warehousing</strong></td>
                  <td><strong>Google Cloud (GCP)</strong></td>
                  <td>BigQuery offers unequaled SQL query speeds on petabyte datasets; native home of Kubernetes and Vertex AI.</td>
                </tr>
                <tr>
                  <td><strong>Kubernetes & Cloud-Native Container Microservices</strong></td>
                  <td><strong>Google Cloud or AWS</strong></td>
                  <td>Google GKE provides the smoothest automated node management; AWS EKS provides deep VPC networking integration.</td>
                </tr>
                <tr>
                  <td><strong>Hybrid Datacenter with On-Premises Hyper-V / Windows</strong></td>
                  <td><strong>Microsoft Azure</strong></td>
                  <td>Azure Arc and Azure Stack deliver the industry's most unified hybrid control plane.</td>
                </tr>
                <tr>
                  <td><strong>Strict Government & Defense Compliance</strong></td>
                  <td><strong>All Three (AWS, Azure, GCP)</strong></td>
                  <td>Subject to isolated sovereign clouds (AWS GovCloud, Azure Government, Google Cloud for Government).</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="exam-tip">
            <strong>⚠️ Final University Exam Conclusion:</strong> <em>There is NO single universal "best" cloud provider!</em> The optimal architectural selection always depends on workload requirements, existing software licenses, security compliance, network latency, and organizational IT skillsets.
          </div>
        </div>
      </div>

    </div>
  </div>

</div>
"""
