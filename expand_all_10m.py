# -*- coding: utf-8 -*-
"""
Updates parts_power_modes.py and parts_js.py to include all 8 master 10-mark questions
with extensive, rich content, model answers, blueprints, and diagrams.
"""
import re

EXTRA_10M_IMP_CARDS = """
    <!-- IMP 15: Virtualization in Depth (10 Marks) -->
    <div class="imp-card tier-1" data-tier="tier1" data-marks="10m">
      <div class="imp-header">
        <div class="imp-title">15. Comprehensive Virtualization Architecture & Intel VT-x Hardware Assist</div>
        <div class="imp-tags">
          <span class="badge badge-priority">Unit 4 · 10 Marks</span>
          <span class="badge" style="background-color: var(--danger-bg); color: var(--danger); font-weight: 700;">98% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"Explain the architecture of virtualization in cloud computing. Compare Full Virtualization, Paravirtualization, and Hardware-Assisted Virtualization with neat diagrams. Explain Popek-Goldberg theorem and Intel VT-x VMX Root/Non-Root modes."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>Popek-Goldberg Theorem:</strong> An architecture is strictly virtualizable iff all sensitive instructions are a subset of privileged instructions ($Sensitive \\subseteq Privileged$). x86 had 17 sensitive unprivileged instructions (the x86 virtualization hole).</li>
          <li><strong>3 CPU Virtualization Models:</strong> 1) Full Virtualization (Binary translation of sensitive instructions), 2) Paravirtualization (Guest OS modified with Hypercalls), 3) Hardware-Assisted (Silicon traps via Intel VT-x / AMD-V).</li>
          <li><strong>Intel VT-x VMX Modes:</strong> VMX Root Mode (Hypervisor full control) and VMX Non-Root Mode (Guest OS). Traps trigger hardware <strong>VM-Exit</strong>; hypervisor resumes VM with <strong>VM-Entry</strong> via <code>VMRESUME</code>. Extended Page Tables (EPT) handle hardware memory virtualization.</li>
          <li><strong>Three Virtualization Domains:</strong> Compute (vCPUs/RAM overcommit), Storage (LVM, SAN pools, Ceph), and Network Virtualization (vSwitches, VXLAN 24-bit overlay tunnels).</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <a href="https://www.google.com/search?tbm=isch&q=Compute+Storage+Network+Virtualization+Hardware+Assisted+Intel+VT+Diagram" target="_blank" class="btn btn-sm">🔍 View Diagrams on Google</a>
        <button class="btn btn-sm btn-primary" onclick="switchTab('qbank'); filterQBank('10m', null);">📝 View 10M Model Answer</button>
      </div>
    </div>

    <!-- IMP 16: AWS IAM Enterprise Security Architecture (10 Marks) -->
    <div class="imp-card tier-1" data-tier="tier1" data-marks="10m">
      <div class="imp-header">
        <div class="imp-title">16. AWS IAM Enterprise Architecture & 6-Step Policy Evaluation Algorithm</div>
        <div class="imp-tags">
          <span class="badge badge-priority">Unit 5 · 10 Marks</span>
          <span class="badge" style="background-color: var(--danger-bg); color: var(--danger); font-weight: 700;">99% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"Discuss AWS IAM Enterprise Security Architecture. Detail the 4 core entities, JSON policy grammar, the 6-step policy evaluation algorithm, and explain why Explicit Deny is absolute."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>Core Entities:</strong> Users (long-term human credentials), User Groups (batch permission sets), Roles (temporary identities assumed by EC2/Lambda with STS tokens), Policies (JSON permission documents).</li>
          <li><strong>JSON Grammar:</strong> <code>Version</code> ("2012-10-17"), <code>Statement</code>, <code>Effect</code> (Allow/Deny), <code>Principal</code>, <code>Action</code>, <code>Resource</code> (ARN), and <code>Condition</code> (MFA, Source IP CIDR).</li>
          <li><strong>6-Step Evaluation Engine:</strong> 1) Default Implicit Deny &rarr; 2) <strong>Explicit Deny Check</strong> (If any policy statement denies, evaluate halts immediately and returns DENY) &rarr; 3) SCP Check &rarr; 4) Resource-based Policy Check &rarr; 5) IAM Permissions Boundary & Identity Policy Check &rarr; 6) Final Allow/Deny.</li>
          <li><strong>AWS STS Token Generation:</strong> <code>AssumeRole</code> issues temporary credentials (<code>AccessKeyId</code> starting with <code>ASIA</code>, <code>SecretAccessKey</code>, <code>SessionToken</code>) with 1-hour auto-expiration.</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <a href="https://www.google.com/search?tbm=isch&q=AWS+IAM+Policy+Evaluation+Logic+Flowchart+Diagram" target="_blank" class="btn btn-sm">🔍 View Diagrams on Google</a>
        <button class="btn btn-sm btn-primary" onclick="switchTab('qbank'); filterQBank('10m', null);">📝 View 10M Model Answer</button>
      </div>
    </div>

    <!-- IMP 17: Enterprise Multi-Server 3-Tier Web Architecture (10 Marks) -->
    <div class="imp-card tier-2" data-tier="tier2" data-marks="10m">
      <div class="imp-header">
        <div class="imp-title">17. Enterprise Multi-Server 3-Tier Web Architecture & High Availability Math</div>
        <div class="imp-tags">
          <span class="badge badge-accent">Unit 3 · 10 Marks</span>
          <span class="badge" style="background-color: var(--warning-bg); color: var(--warning); font-weight: 700;">95% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"Design a highly available 3-Tier Web Architecture on Cloud. Contrast Layer 4 (NLB) vs Layer 7 (ALB) Load Balancing, calculate Serial vs Parallel Availability SLA, and discuss Disaster Recovery strategies (RTO/RPO)."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>3 VPC Tiers:</strong> Tier 1: Web Presentation (Public subnet, Internet Gateway, ALB terminating SSL, Nginx). Tier 2: Application Logic (Private subnet, NAT Gateway, stateless microservices in Auto Scaling Group, Redis cache). Tier 3: Database Persistence (Isolated subnet, Multi-AZ Primary R/W Master with Read-Replicas).</li>
          <li><strong>Layer 4 vs Layer 7 Load Balancing:</strong> NLB (L4) routes by TCP/UDP port at wire speed (millions RPS, static IP). ALB (L7) performs deep HTTP packet inspection (path routing <code>/api</code> vs <code>/static</code>, host headers, cookie sticky sessions).</li>
          <li><strong>High Availability Mathematics:</strong> Serial components multiply availabilities: $A_{\\text{system}} = A_1 \\times A_2$ (99% &times; 99% = 98.01%). Parallel redundant components: $A_{\\text{system}} = 1 - (1 - A_1)(1 - A_2)$ (Two 99% servers in parallel = 99.99% 'Four Nines'!).</li>
          <li><strong>Disaster Recovery RTO & RPO:</strong> Backup & Restore (RTO: Days, Lowest cost) &rarr; Pilot Light (RTO: Hours, Core DB replicating) &rarr; Warm Standby (RTO: Minutes, Scaled-down fleet) &rarr; Multi-Region Active-Active (RTO: Zero, Highest cost).</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <a href="https://www.google.com/search?tbm=isch&q=Three+Tier+Cloud+Web+Architecture+AWS+Diagram" target="_blank" class="btn btn-sm">🔍 View Diagrams on Google</a>
        <button class="btn btn-sm btn-primary" onclick="switchTab('qbank'); filterQBank('10m', null);">📝 View 10M Model Answer</button>
      </div>
    </div>

    <!-- IMP 18: Cloud Storage Architectures & CAP Theorem (10 Marks) -->
    <div class="imp-card tier-1" data-tier="tier1" data-marks="10m">
      <div class="imp-header">
        <div class="imp-title">18. Cloud Storage Architectures: Block vs Object vs File & 11-Nines Durability Math</div>
        <div class="imp-tags">
          <span class="badge badge-priority">Unit 4 · 10 Marks</span>
          <span class="badge" style="background-color: var(--danger-bg); color: var(--danger); font-weight: 700;">92% Probability</span>
        </div>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.6rem;">
        <strong>Question Format:</strong> <em>"Compare Block, Object, and File Storage on 8 parameters. Explain the mathematics of 11-Nines S3 durability, Erasure Coding, and analyze distributed consistency via the CAP Theorem."</em>
      </p>
      <div class="def-box" style="margin: 0.5rem 0; font-size: 0.88rem;">
        <strong>4-Point Answer Blueprint:</strong>
        <ul style="margin: 0.35rem 0 0.35rem 1.2rem; font-size: 0.85rem;">
          <li><strong>Tri-Storage Paradigms:</strong> Block (AWS EBS): Raw sectors, iSCSI/NVMe-oF, ultra-low latency, in-place byte writes (OS boot/DBs). Object (AWS S3): Flat namespace, HTTP REST (GET/PUT), immutable payloads, petabyte scale (Data lakes/media). File (AWS EFS): POSIX directory tree, NFSv4, concurrent multi-instance read/write.</li>
          <li><strong>11-Nines (99.999999999%) Durability Math:</strong> Storing 10,000,000 objects in S3 loses statistically 1 object every 10,000 years! Annual loss probability is $10^{-11}$. Achieved via multi-AZ replication across 3+ independent geographical failure zones and Reed-Solomon Erasure Coding.</li>
          <li><strong>CAP Theorem:</strong> Distributed data systems can guarantee at most 2 of 3: Consistency (C), Availability (A), Partition Tolerance (P). Network partitions (P) are inevitable in physical cables; systems must choose CP (HBase) or AP (Cassandra). S3 delivers Strong Read-After-Write Consistency.</li>
          <li><strong>S3 Storage Lifecycle Tiers:</strong> S3 Standard &rarr; S3 Standard-IA (Infrequent Access) &rarr; Glacier Flexible Retrieval &rarr; Glacier Deep Archive ($0.00099/GB/mo for 10-year tape replacement).</li>
        </ul>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem;">
        <a href="https://www.google.com/search?tbm=isch&q=Block+vs+File+vs+Object+Storage+Cloud+Diagram" target="_blank" class="btn btn-sm">🔍 View Diagrams on Google</a>
        <button class="btn btn-sm btn-primary" onclick="switchTab('qbank'); filterQBank('10m', null);">📝 View 10M Model Answer</button>
      </div>
    </div>
"""

JS_10M_QUESTIONS = r'''
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
'''

def update_files():
    # 1. Update parts_power_modes.py
    modes_file = "d:/Downloads/cc/parts_power_modes.py"
    with open(modes_file, "r", encoding="utf-8") as f:
        modes_content = f.read()

    target_needle = '<!-- IMP 14: Fog Computing vs Cloud Computing -->'
    # Find the end of card 14
    end_of_14_idx = modes_content.find('</div>\n    </div>\n\n  </div>\n</div>\n"""', modes_content.find(target_needle))
    if end_of_14_idx != -1:
        new_modes_content = modes_content[:end_of_14_idx+11] + "\n" + EXTRA_10M_IMP_CARDS + modes_content[end_of_14_idx+11:]
        with open(modes_file, "w", encoding="utf-8") as f:
            f.write(new_modes_content)
        print("Updated parts_power_modes.py with extra 10M IMP cards!")
    else:
        print("Could not find insertion point in parts_power_modes.py")

    # 2. Update parts_js.py
    js_file = "d:/Downloads/cc/parts_js.py"
    with open(js_file, "r", encoding="utf-8") as f:
        js_content = f.read()

    js_target_start = js_content.find("// 10-Mark Comprehensive")
    js_target_end = js_content.find("// Current Roulette State")

    if js_target_start != -1 and js_target_end != -1:
        new_js = js_content[:js_target_start] + JS_10M_QUESTIONS.strip() + "\n];\n\n" + js_content[js_target_end:]
        with open(js_file, "w", encoding="utf-8") as f:
            f.write(new_js)
        print("Updated parts_js.py with all 8 master 10-mark questions!")
    else:
        print("Could not find target range in parts_js.py")

if __name__ == "__main__":
    update_files()
