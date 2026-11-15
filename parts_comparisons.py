# -*- coding: utf-8 -*-

TAB_COMPARISONS_HTML = """
<div id="comparisons" class="tab-pane">
  <div class="hero-banner">
    <div class="hero-header">
      <div class="hero-title">Master Comparison Matrices</div>
      <div class="hero-badge-group">
        <span class="badge badge-priority">High-Yield 7 & 10 Marks</span>
        <span class="badge">Side-by-Side Analysis</span>
      </div>
    </div>
    <p class="hero-desc">
      University examinations frequently feature 7-mark and 10-mark difference questions.
      Below are the master comparison matrices curated directly from your lecture slides and standard university marking criteria.
    </p>
  </div>

  <!-- Comparison 1: Type 1 vs Type 2 Hypervisors -->
  <div class="topic-card">
    <div class="topic-header">
      <div class="topic-title">1. Type 1 (Bare-Metal) vs Type 2 (Hosted) Hypervisors</div>
      <span class="topic-tag">Unit 4 · 7 Marks</span>
    </div>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Comparison Parameter</th>
            <th>Type 1 Hypervisor (Bare-Metal)</th>
            <th>Type 2 Hypervisor (Hosted)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Installation Layer</strong></td>
            <td>Installed directly on physical bare-metal hardware.</td>
            <td>Installed on top of an existing host operating system as an application.</td>
          </tr>
          <tr>
            <td><strong>Host OS Dependency</strong></td>
            <td>None; acts as its own specialized operating system.</td>
            <td>Requires a fully functioning host OS (Windows, Linux, macOS).</td>
          </tr>
          <tr>
            <td><strong>Performance & Overhead</strong></td>
            <td>Near-native performance; negligible virtualization overhead.</td>
            <td>Noticeable overhead; I/O must pass through the host OS stack.</td>
          </tr>
          <tr>
            <td><strong>Hardware Access</strong></td>
            <td>Direct hardware management and direct device drivers.</td>
            <td>Mediated indirectly through host OS system calls.</td>
          </tr>
          <tr>
            <td><strong>Security & Isolation</strong></td>
            <td>Strong hardware isolation; small attack surface.</td>
            <td>Dependent on host OS security; host compromise compromises all guest VMs.</td>
          </tr>
          <tr>
            <td><strong>Setup Complexity</strong></td>
            <td>Higher; requires dedicated server hardware and specialized setup.</td>
            <td>Low; simple installer package on everyday laptops/desktops.</td>
          </tr>
          <tr>
            <td><strong>Industry Examples</strong></td>
            <td>VMware ESXi, Microsoft Hyper-V, KVM, Xen.</td>
            <td>Oracle VirtualBox, VMware Workstation, VMware Fusion, Parallels.</td>
          </tr>
          <tr>
            <td><strong>Primary Target</strong></td>
            <td>Enterprise datacenters, cloud providers, mission-critical production.</td>
            <td>Software developers, QA testers, students, local lab environments.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- Comparison 2: VMs vs Containers -->
  <div class="topic-card">
    <div class="topic-header">
      <div class="topic-title">2. Virtual Machines (VMs) vs Docker Containers</div>
      <span class="topic-tag">Unit 4 · 7 Marks</span>
    </div>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Feature</th>
            <th>Virtual Machine (VM)</th>
            <th>Container (Docker)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Virtualization Level</strong></td>
            <td>Hardware-level virtualization (hypervisor abstracts CPU/RAM/Disk).</td>
            <td>Operating-system-level virtualization (shares host OS kernel).</td>
          </tr>
          <tr>
            <td><strong>Guest Operating System</strong></td>
            <td>Each VM runs a complete, standalone Guest OS (kernel + drivers).</td>
            <td>No guest OS; containers share the host Linux/Windows kernel.</td>
          </tr>
          <tr>
            <td><strong>Startup Time</strong></td>
            <td>Minutes (must boot full BIOS, kernel, and init system).</td>
            <td>Milliseconds to seconds (starts as an isolated host process).</td>
          </tr>
          <tr>
            <td><strong>Storage Footprint</strong></td>
            <td>Gigabytes (GBs) per VM image due to full OS files.</td>
            <td>Megabytes (MBs) per container image (layered diffs).</td>
          </tr>
          <tr>
            <td><strong>Resource Utilization</strong></td>
            <td>High memory and CPU reservation overhead.</td>
            <td>Minimal overhead; lightweight process-level resource consumption.</td>
          </tr>
          <tr>
            <td><strong>Isolation Boundary</strong></td>
            <td>Hardware-level isolation enforced by hypervisor CPU rings.</td>
            <td>Process-level isolation enforced by Linux <code>cgroups</code> & <code>namespaces</code>.</td>
          </tr>
          <tr>
            <td><strong>Density per Physical Host</strong></td>
            <td>Tens of VMs per physical host server.</td>
            <td>Hundreds to thousands of containers per physical host server.</td>
          </tr>
          <tr>
            <td><strong>Portability</strong></td>
            <td>Good, but large disk exports (.ova/.vmdk) are cumbersome to move.</td>
            <td>Supreme; immutable images run identically on any Docker engine.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- Comparison 3: OpenStack vs Apache CloudStack -->
  <div class="topic-card">
    <div class="topic-header">
      <div class="topic-title">3. OpenStack vs Apache CloudStack</div>
      <span class="topic-tag">Unit 4 · 7 Marks</span>
    </div>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Dimension</th>
            <th>OpenStack</th>
            <th>Apache CloudStack</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Architecture Model</strong></td>
            <td>Modular, microservices-oriented (dozens of independent projects).</td>
            <td>Integrated turnkey platform with centralized Management Server.</td>
          </tr>
          <tr>
            <td><strong>Deployment Complexity</strong></td>
            <td>High; requires configuring message queues, DBs, and services.</td>
            <td>Low to moderate; packaged management server and wizard installer.</td>
          </tr>
          <tr>
            <td><strong>Compute Management</strong></td>
            <td>Nova (Compute service daemon).</td>
            <td>Integrated CloudStack Management Server + Hypervisor Agents.</td>
          </tr>
          <tr>
            <td><strong>Networking Engine</strong></td>
            <td>Neutron (complex virtual software-defined network topologies).</td>
            <td>Integrated Virtual Routers and standard network tiers.</td>
          </tr>
          <tr>
            <td><strong>Storage Model</strong></td>
            <td>Dedicated services: Cinder (Block) and Swift (Object).</td>
            <td>Two-tier model: Primary Storage (VM disks) & Secondary Storage (templates).</td>
          </tr>
          <tr>
            <td><strong>Resource Hierarchy</strong></td>
            <td>Regions & Availability Zones.</td>
            <td>Strict 5-level hierarchy: Region &rarr; Zone &rarr; Pod &rarr; Cluster &rarr; Host.</td>
          </tr>
          <tr>
            <td><strong>Community & Industry</strong></td>
            <td>Massive ecosystem supported by Red Hat, Canonical, Mirantis.</td>
            <td>Lean, mature, enterprise-focused Apache Software Foundation project.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- Comparison 4: Storage Comparison -->
  <div class="topic-card">
    <div class="topic-header">
      <div class="topic-title">4. Block Storage vs Object Storage vs File Storage</div>
      <span class="topic-tag">Unit 4 · 7 Marks</span>
    </div>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Characteristic</th>
            <th>Block Storage</th>
            <th>Object Storage</th>
            <th>File Storage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Data Structure</strong></td>
            <td>Fixed-size addressable blocks on raw volume.</td>
            <td>Flat objects with data, metadata, and unique ID key.</td>
            <td>Hierarchical tree of files inside nested folders.</td>
          </tr>
          <tr>
            <td><strong>Access Mechanism</strong></td>
            <td>Block I/O protocols (SAN, iSCSI, Fibre Channel).</td>
            <td>HTTP REST APIs (GET, PUT, POST, DELETE).</td>
            <td>Network File Protocols (NFS, SMB/CIFS).</td>
          </tr>
          <tr>
            <td><strong>Latency & Throughput</strong></td>
            <td>Lowest latency, highest IOPS.</td>
            <td>Higher latency; high aggregate throughput.</td>
            <td>Moderate latency; multi-user concurrent locking.</td>
          </tr>
          <tr>
            <td><strong>Scalability Limit</strong></td>
            <td>Limited to volume size bounds.</td>
            <td>Virtually limitless; exabyte-scale in flat buckets.</td>
            <td>Limited by filesystem namespace limits.</td>
          </tr>
          <tr>
            <td><strong>Modification Capability</strong></td>
            <td>Fine-grained; edit single bytes/blocks in place.</td>
            <td>Immutable; must overwrite whole object to update.</td>
            <td>File-level file system edits and append operations.</td>
          </tr>
          <tr>
            <td><strong>Ideal Workload</strong></td>
            <td>OS boot disks, transactional databases.</td>
            <td>Backups, video streaming, archives, static assets.</td>
            <td>Enterprise document sharing, content management.</td>
          </tr>
          <tr>
            <td><strong>AWS / Azure / GCP</strong></td>
            <td>AWS EBS / Azure Disks / GCP Persistent Disk</td>
            <td>AWS S3 / Azure Blob / GCP Cloud Storage</td>
            <td>AWS EFS / Azure Files / GCP Filestore</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- Comparison 5: SDN vs VPN vs Load Balancing vs CDN -->
  <div class="topic-card">
    <div class="topic-header">
      <div class="topic-title">5. SDN vs VPN vs Load Balancing vs CDN</div>
      <span class="topic-tag">Unit 4 · 7 Marks</span>
    </div>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Aspect</th>
            <th>SDN</th>
            <th>VPN</th>
            <th>Load Balancing</th>
            <th>CDN</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Primary Objective</strong></td>
            <td>Programmable, centralized network control.</td>
            <td>Encrypted, secure communications tunnel.</td>
            <td>Distribute incoming traffic across servers.</td>
            <td>Deliver cached static content with low latency.</td>
          </tr>
          <tr>
            <td><strong>Core Technology</strong></td>
            <td>Decoupled Control & Data Planes.</td>
            <td>Cryptographic tunnels (IPsec, TLS, WireGuard).</td>
            <td>Layer 4 (TCP) / Layer 7 (HTTP) proxies.</td>
            <td>Geographically distributed edge caching POPs.</td>
          </tr>
          <tr>
            <td><strong>Key Benefit</strong></td>
            <td>Agile network configuration via code.</td>
            <td>Confidentiality over untrusted public networks.</td>
            <td>Eliminates server overload and single points of failure.</td>
            <td>Drastically reduces latency and offloads origin servers.</td>
          </tr>
          <tr>
            <td><strong>Cloud Example</strong></td>
            <td>AWS VPC Virtual Router / Neutron.</td>
            <td>AWS Client VPN / Site-to-Site VPN.</td>
            <td>AWS Application Load Balancer (ALB).</td>
            <td>Amazon CloudFront / Cloudflare.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- Comparison 6: Authentication vs Authorization -->
  <div class="topic-card">
    <div class="topic-header">
      <div class="topic-title">6. Authentication vs Authorization</div>
      <span class="topic-tag">Unit 5 · 5 Marks</span>
    </div>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Comparison Parameter</th>
            <th>Authentication (AuthN)</th>
            <th>Authorization (AuthZ)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Core Question</strong></td>
            <td><strong>"Who are you?"</strong></td>
            <td><strong>"What are you permitted to do?"</strong></td>
          </tr>
          <tr>
            <td><strong>Execution Order</strong></td>
            <td>Executed <strong>first</strong> before any access is granted.</td>
            <td>Executed <strong>after</strong> authentication is successfully confirmed.</td>
          </tr>
          <tr>
            <td><strong>Verification Factors</strong></td>
            <td>Passwords, OTP, Biometrics, Certificates, MFA tokens.</td>
            <td>IAM Policies, Access Control Lists (ACLs), Roles, Scopes.</td>
          </tr>
          <tr>
            <td><strong>Outcome</strong></td>
            <td>Valid identity established or login denied.</td>
            <td>Specific requested action allowed or denied.</td>
          </tr>
          <tr>
            <td><strong>AWS Mechanism</strong></td>
            <td>AWS Console login, IAM user password, MFA.</td>
            <td>IAM JSON Policies (Effect: Allow/Deny, Actions, Resources).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- Comparison 7: Scalability vs Elasticity -->
  <div class="topic-card">
    <div class="topic-header">
      <div class="topic-title">7. Scalability vs Elasticity</div>
      <span class="topic-tag">Unit 5 · 7 Marks</span>
    </div>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Comparison Parameter</th>
            <th>Scalability</th>
            <th>Elasticity</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Fundamental Goal</strong></td>
            <td>System ability to handle larger workloads by adding resources.</td>
            <td>System ability to dynamically adapt capacity in real-time.</td>
          </tr>
          <tr>
            <td><strong>Directionality</strong></td>
            <td>Unidirectional: Scaling UP (Vertical) or OUT (Horizontal).</td>
            <td>Bidirectional: Scales OUT during peaks, scales IN during lulls.</td>
          </tr>
          <tr>
            <td><strong>Trigger Mechanism</strong></td>
            <td>Manual or planned long-term provisioning.</td>
            <td>Automated real-time metrics (CPU &gt; 70%, latency, request count).</td>
          </tr>
          <tr>
            <td><strong>Focus Area</strong></td>
            <td>System performance and maximum capacity headroom.</td>
            <td>Cost optimization and zero idle resource wastage.</td>
          </tr>
          <tr>
            <td><strong>Time Horizon</strong></td>
            <td>Long term (months to years of growth).</td>
            <td>Short term (hours, minutes, daily cyclical traffic).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""
