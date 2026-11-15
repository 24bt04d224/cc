# -*- coding: utf-8 -*-
from parts_svg import SVG_CIA_TRIAD, SVG_IAM_EVAL

TAB_UNIT5_HTML = f"""
<div id="unit5" class="tab-pane">
  <div class="hero-banner" style="border-color: rgba(239, 68, 68, 0.4);">
    <div class="hero-header">
      <div class="hero-title">Unit 5: Security, Privacy & Cloud Management</div>
      <div class="hero-badge-group">
        <span class="badge badge-priority">25% Exam Weightage</span>
        <span class="badge">10 Contact Hours</span>
        <span class="badge badge-accent">Deep Technical Unit</span>
      </div>
    </div>
    <p class="hero-desc">
      Explore all 8 core security and cloud management topics in interactive dropdowns.
      Click any <strong>Main Head</strong> to reveal sub-topics, then click on a <strong>Sub-Topic</strong> to view complete technical explanations, AWS IAM policy JSON, and real-world incident case studies.
    </p>
  </div>

  <!-- Unit 5 Dropdown Controls Bar -->
  <div class="unit-controls-bar">
    <div class="unit-controls-left">
      <span style="font-weight: 700; font-size: 0.88rem; color: var(--accent);">📌 Jump to Topic:</span>
      <select class="topic-select" onchange="jumpToTopic('unit5', this)">
        <option value="">Select a Topic...</option>
        <option value="u5-t1">Topic 1: Cloud Security Issues & 4 Pillars</option>
        <option value="u5-t2">Topic 2: Data Security & CIA Triad</option>
        <option value="u5-t3">Topic 3: Cloud Privacy, Governance & Compliance</option>
        <option value="u5-t4">Topic 4: Authentication vs Authorization</option>
        <option value="u5-t5">Topic 5: AWS IAM Deep Dive (Prof. Amin Shaikh)</option>
        <option value="u5-t6">Topic 6: Virtual Machine Security</option>
        <option value="u5-t7">Topic 7: Cloud Resource Management (Scalability vs Elasticity)</option>
        <option value="u5-t8">Topic 8: Real-World Cloud Security Incidents</option>
      </select>
    </div>
    <div class="unit-controls-right">
      <button class="btn btn-sm btn-primary" onclick="expandAllInUnit('unit5')">📂 Expand All</button>
      <button class="btn btn-sm" onclick="collapseAllInUnit('unit5')">📁 Collapse All</button>
    </div>
  </div>

  <!-- ==================== TOPIC 1 ==================== -->
  <div class="main-topic-card" id="u5-t1">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🛡️</span>
        <span class="main-topic-title">Topic 1: Cloud Security Issues & The 4 Pillars</span>
        <span class="badge badge-priority">Fundamental</span>
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
            <span>1.1 What is Cloud Security & The 4 Key Pillars</span>
          </div>
          <span class="sub-topic-badge">Pillars</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">Exam Definition: Cloud Security</div>
            <strong>Cloud Security</strong> is a broad set of policies, technologies, applications, and controls utilized to protect virtualized IP, data, applications, services, and the associated cloud infrastructure from cyber threats.
          </div>
          <h5 style="margin-top: 1rem; color: var(--text-primary);">The 4 Key Pillars of Cloud Security (From Lecture Slides):</h5>
          <div class="grid-2" style="margin-top: 0.75rem;">
            <div class="subcard">
              <h4>1. Infrastructure Security</h4>
              <p>Hardening physical datacenter facilities, host hardware, hypervisor kernels, and host operating systems.</p>
            </div>
            <div class="subcard">
              <h4>2. Data Security</h4>
              <p>Protecting data across its lifecycle using cryptographic encryption, access control policies, and Data Loss Prevention (DLP).</p>
            </div>
            <div class="subcard">
              <h4>3. Network Security</h4>
              <p>Isolating communication channels via Virtual Private Clouds (VPCs), subnets, firewalls, and encrypted VPN connections.</p>
            </div>
            <div class="subcard">
              <h4>4. Application Security</h4>
              <p>Securing cloud-native software using secure code pipelines, SAST/DAST testing, and Web Application Firewalls (WAF).</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 1.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.2 Major Cloud Security Issues & 4 Risk Categories</span>
          </div>
          <span class="sub-topic-badge">Risks</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p>Your PPT categorizes cloud security risks into four major domains:</p>
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Risk Category</th><th>Description & Manifestation</th></tr></thead>
              <tbody>
                <tr><td><strong>Infrastructure & Architecture Flaws</strong></td><td>Insecure default configurations, open database ports, vulnerable hypervisors.</td></tr>
                <tr><td><strong>IAM Risks</strong></td><td>Weak authentication, lack of MFA, excessive privileges granted to users or service accounts.</td></tr>
                <tr><td><strong>Operational & Strategic Risks</strong></td><td>Inadequate logging/monitoring, absence of incident response plans, poor patch hygiene.</td></tr>
                <tr><td><strong>Compliance, Supply Chain & Legal</strong></td><td>Violations of data residency laws (GDPR), compromised third-party dependencies.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Sub-topic 1.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.3 Top 10 Best Practices for Cloud Data Security</span>
          </div>
          <span class="sub-topic-badge">Checklist</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <ol style="margin-left: 1.25rem; line-height: 1.7;">
            <li>Enforce mandatory Multi-Factor Authentication (MFA) across all console and CLI accounts.</li>
            <li>Adhere strictly to the Principle of Least Privilege in IAM permissions.</li>
            <li>Enable default encryption for all storage buckets, volumes, and databases.</li>
            <li>Block public access to cloud storage buckets (e.g. S3 Block Public Access).</li>
            <li>Isolate workloads using virtual private clouds (VPCs) and fine-grained security groups.</li>
            <li>Centralize and protect audit trails using AWS CloudTrail or Azure Activity Log.</li>
            <li>Automate regular operating system patching and container vulnerability scanning.</li>
            <li>Never hardcode static API credentials in code; use assumable IAM roles with temporary STS tokens.</li>
            <li>Enforce IMDSv2 on all EC2 instances to mitigate Server-Side Request Forgery (SSRF) attacks.</li>
            <li>Conduct continuous automated configuration compliance audits using tools like AWS Config.</li>
          </ol>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 2 ==================== -->
  <div class="main-topic-card" id="u5-t2">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🔐</span>
        <span class="main-topic-title">Topic 2: Data Security, CIA Triad & Encryption States</span>
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
            <span>2.1 The CIA Triad in Cloud Computing</span>
          </div>
          <span class="sub-topic-badge">Core Security</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="diagram-container">
            {SVG_CIA_TRIAD}
            <div class="diagram-caption">Figure 5.1: The CIA Triad (Confidentiality, Integrity, Availability) in Cloud Security.</div>
          </div>
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Pillar</th><th>Objective</th><th>Threats</th><th>Cloud Defenses</th></tr></thead>
              <tbody>
                <tr><td><strong>Confidentiality</strong></td><td>Only authorized entities can access data</td><td>Data leaks, snooping, credential theft</td><td>AES-256 encryption, strict IAM, MFA</td></tr>
                <tr><td><strong>Integrity</strong></td><td>Data remains accurate, intact & untampered</td><td>SQL injection, man-in-the-middle, bit rot</td><td>SHA-256 hashing, digital signatures, TLS</td></tr>
                <tr><td><strong>Availability</strong></td><td>Systems are reliably accessible when needed</td><td>DDoS attacks, server outages, hardware failure</td><td>Load balancers, auto-scaling, multi-region failover</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Sub-topic 2.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>2.2 Multi-Tenancy & Data Isolation Risks</span>
          </div>
          <span class="sub-topic-badge">Multi-Tenancy</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">What is Multi-Tenancy?</div>
            <strong>Multi-Tenancy</strong> is an architectural model where multiple customers (tenants) share the same underlying physical cloud infrastructure, while their applications and data remain logically isolated.
          </div>
          <h5 style="margin-top: 1rem; color: var(--text-primary);">Security Challenges & Defenses:</h5>
          <ul>
            <li><strong>Cross-Tenant Data Leakage:</strong> Prevented by hypervisor memory isolation and per-tenant database encryption keys.</li>
            <li><strong>Noisy Neighbor Syndrome:</strong> Addressed via CPU/RAM quota limits enforced by hypervisors and cgroups.</li>
            <li><strong>Side-Channel Attacks:</strong> CPU microarchitectural mitigations (Spectre/Meltdown patches).</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 2.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>2.3 The 3 States of Data Encryption</span>
          </div>
          <span class="sub-topic-badge">Encryption</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="grid-3">
            <div class="subcard">
              <h4>1. Encryption at Rest</h4>
              <p>Protects static data saved on storage media (disks, databases, S3 buckets, archives). Encrypted via AES-256 with KMS keys.</p>
            </div>
            <div class="subcard">
              <h4>2. Encryption in Transit</h4>
              <p>Protects data traveling over public or private networks between client and server. Secured via TLS 1.3, HTTPS, and IPsec VPN.</p>
            </div>
            <div class="subcard">
              <h4>3. Encryption in Use</h4>
              <p>Protects active data in CPU cache and RAM during active processing using hardware <strong>Confidential Computing</strong> (Intel SGX, AMD SEV).</p>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 3 ==================== -->
  <div class="main-topic-card" id="u5-t3">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">⚖️</span>
        <span class="main-topic-title">Topic 3: Cloud Privacy, Governance & Compliance Standards</span>
        <span class="badge">Regulations</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>4 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 3.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>3.1 Cloud Privacy & Shared Responsibility for Privacy</span>
          </div>
          <span class="sub-topic-badge">Privacy</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">What is Cloud Privacy?</div>
            <strong>Cloud Privacy</strong> focuses on rights and controls governing how personal data (Personally Identifiable Information - PII) is collected, stored, processed, and shared in cloud environments.
          </div>
          <p><strong>Shared Responsibility for Privacy:</strong> Cloud providers ensure datacenter physical security and compliance certifications; customers are responsible for data classification, consent management, access restrictions, and privacy policies.</p>
        </div>
      </div>

      <!-- Sub-topic 3.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>3.2 Cloud Governance Framework</span>
          </div>
          <span class="sub-topic-badge">Governance</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p>The structured framework of rules, roles, and policies to control cloud adoption:</p>
          <div class="grid-3" style="margin-top: 0.75rem;">
            <div class="subcard"><h4>1. Policies</h4><p>Rules governing allowable cloud resource creation.</p></div>
            <div class="subcard"><h4>2. Cost Control</h4><p>Enforcing budget limits and tagging discipline.</p></div>
            <div class="subcard"><h4>3. Risk & Audit</h4><p>Monitoring configuration drift and policy violations.</p></div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 3.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>3.3 Key Regulatory Standards (ISO, GDPR, HIPAA, PCI DSS, SOC 2)</span>
          </div>
          <span class="sub-topic-badge">Standards</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Standard / Law</th><th>Scope & Purpose</th></tr></thead>
              <tbody>
                <tr><td><strong>ISO/IEC 27001</strong></td><td>Information Security Management System (ISMS) framework.</td></tr>
                <tr><td><strong>ISO/IEC 27017</strong></td><td>Code of practice for information security controls in cloud computing.</td></tr>
                <tr><td><strong>ISO/IEC 27018</strong></td><td>Protection of Personally Identifiable Information (PII) in public cloud services.</td></tr>
                <tr><td><strong>GDPR</strong></td><td>European privacy law mandating consent, data minimization, and 72-hour breach notices.</td></tr>
                <tr><td><strong>HIPAA</strong></td><td>United States law protecting electronic Protected Health Information (ePHI).</td></tr>
                <tr><td><strong>PCI DSS</strong></td><td>Global payment card industry security standard for credit card transactions.</td></tr>
                <tr><td><strong>SOC 2</strong></td><td>Audits vendors across 5 Trust Services Criteria (Security, Availability, Privacy...).</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Sub-topic 3.4 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>3.4 Data Residency vs Data Sovereignty & Cloud Audit</span>
          </div>
          <span class="sub-topic-badge">Residency</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="grid-2">
            <div class="subcard">
              <h4>Data Residency</h4>
              <p>The geographic location where data is physically stored (e.g. choosing an AWS datacenter region in Mumbai).</p>
            </div>
            <div class="subcard">
              <h4>Data Sovereignty</h4>
              <p>The legal doctrine that data is subject to the local laws and subpoena authority of the nation where it physically sits.</p>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 4 ==================== -->
  <div class="main-topic-card" id="u5-t4">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🔑</span>
        <span class="main-topic-title">Topic 4: Authentication vs Authorization</span>
        <span class="badge badge-accent">Core IAM</span>
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
            <span>4.1 Authentication ("Who are you?") Methods</span>
          </div>
          <span class="sub-topic-badge">AuthN</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Authentication (AuthN)</strong> verifies claimed identity before access is allowed ("Who are you?").
          </div>
          <ul>
            <li><strong>Password / PIN:</strong> Knowledge factor (something you know).</li>
            <li><strong>MFA / OTP Tokens:</strong> Possession factor (something you have).</li>
            <li><strong>Biometrics:</strong> Inherence factor (something you are — FaceID, Fingerprint).</li>
            <li><strong>Single Sign-On (SSO):</strong> Log in once to authenticate across multiple integrated applications.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 4.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>4.2 Authorization ("What can you do?") & Comparison Matrix</span>
          </div>
          <span class="sub-topic-badge">AuthZ</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Authorization (AuthZ)</strong> determines the specific resources and operations an authenticated identity is permitted to perform ("What are you allowed to do?").
          </div>
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Dimension</th><th>Authentication</th><th>Authorization</th></tr></thead>
              <tbody>
                <tr><td><strong>Main Question</strong></td><td><strong>"Who are you?"</strong></td><td><strong>"What are you allowed to do?"</strong></td></tr>
                <tr><td><strong>Execution</strong></td><td>Happens <strong>first</strong></td><td>Evaluated <strong>after</strong> authentication succeeds</td></tr>
                <tr><td><strong>Methods</strong></td><td>Passwords, OTP, MFA, Biometrics</td><td>IAM Policies, Roles, ACLs, Scopes</td></tr>
                <tr><td><strong>Result</strong></td><td>Login succeeds or fails</td><td>Action permitted or denied</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 5 ==================== -->
  <div class="main-topic-card" id="u5-t5">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🏛️</span>
        <span class="main-topic-title">Topic 5: AWS Identity & Access Management (IAM) Deep Dive</span>
        <span class="badge badge-priority">High-Yield (10 Marks)</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>5 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 5.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>5.1 Core Concepts: Users, Groups, Roles & Policies (Prof. Amin Shaikh Notes)</span>
          </div>
          <span class="sub-topic-badge">IAM Entities</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p>From the official lecture slides by <strong>Prof. Amin Shaikh (CSE Dept, GSFC University)</strong>:</p>
          <div class="grid-2" style="margin-top: 1rem;">
            <div class="subcard">
              <h4>1. IAM Users</h4>
              <p>Individual persons or service accounts with long-term credentials (password for console, access key ID + secret key for CLI).</p>
            </div>
            <div class="subcard">
              <h4>2. IAM Groups</h4>
              <p>Collections of users (e.g. <code>Developers</code>, <code>Admins</code>). Policies attached to the group apply automatically to all members.</p>
            </div>
            <div class="subcard">
              <h4>3. IAM Roles</h4>
              <p>Identities with permissions designed to be <strong>assumed</strong> temporarily by EC2 instances, Lambda functions, or federated users (provides temporary STS credentials).</p>
            </div>
            <div class="subcard">
              <h4>4. IAM Policies</h4>
              <p>Declarative JSON documents formally defining permissions (Allow or Deny) on specific resources.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 5.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>5.2 Anatomy of an IAM JSON Policy & ARN Format</span>
          </div>
          <span class="sub-topic-badge">JSON & ARN</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <pre><code>{{
  "Version": "2012-10-17",
  "Statement": [
    {{
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::my-gsfc-bucket/*",
      "Condition": {{
        "IpAddress": {{ "aws:SourceIp": "192.168.1.0/24" }}
      }}
    }}
  ]
}}</code></pre>
          <div class="def-box" style="margin-top: 1rem;">
            <div class="def-title">Amazon Resource Name (ARN) Anatomy:</div>
            <code>arn:partition:service:region:account-id:resource</code><br>
            <strong>Example:</strong> <code>arn:aws:ec2:ap-south-1:123456789012:instance/i-0123456789abcdef0</code>
          </div>
        </div>
      </div>

      <!-- Sub-topic 5.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>5.3 5 Types of IAM Policies</span>
          </div>
          <span class="sub-topic-badge">Policy Types</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <ol style="margin-left: 1.25rem; line-height: 1.7;">
            <li><strong>Identity-Based Policies:</strong> Attached directly to Users, Groups, or Roles.</li>
            <li><strong>Resource-Based Policies:</strong> Attached to AWS resources (e.g. S3 Bucket Policy) for cross-account access.</li>
            <li><strong>Permissions Boundaries:</strong> Managed policies that set the maximum permissions an identity can receive.</li>
            <li><strong>Service Control Policies (SCPs):</strong> Organization-level guardrails applied across AWS member accounts.</li>
            <li><strong>Session Policies:</strong> Temporary policies passed when assuming a role via AWS STS.</li>
          </ol>
        </div>
      </div>

      <!-- Sub-topic 5.4 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>5.4 Cardinal Rule of IAM Evaluation: Explicit Deny Overrides Allow!</span>
          </div>
          <span class="sub-topic-badge">Cardinal Rule</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="diagram-container">
            {SVG_IAM_EVAL}
            <div class="diagram-caption">Figure 5.2: AWS IAM Policy Evaluation Logic Flow.</div>
          </div>
          <div class="alert-box">
            <div class="alert-title">Exam Rule to Remember:</div>
            All requests start as <strong>Implicitly Denied</strong>. An <strong>Explicit Deny</strong> immediately and unconditionally trumps all Allow statements!
          </div>
        </div>
      </div>

      <!-- Sub-topic 5.5 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>5.5 Principle of Least Privilege & Best Practices</span>
          </div>
          <span class="sub-topic-badge">Best Practices</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p><strong>Principle of Least Privilege:</strong> Grant users, roles, and applications only the absolute minimum set of permissions necessary to complete their required tasks.</p>
          <ul>
            <li>Lock away the AWS Root user access keys.</li>
            <li>Enforce MFA on all accounts.</li>
            <li>Use IAM Roles instead of hardcoding static credentials.</li>
            <li>Audit unused credentials with IAM Access Analyzer.</li>
          </ul>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 6 ==================== -->
  <div class="main-topic-card" id="u5-t6">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">💻</span>
        <span class="main-topic-title">Topic 6: Virtual Machine Security & Hypervisor Hardening</span>
        <span class="badge">VM Security</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>2 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 6.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>6.1 Major VM Security Threats (VM Escape, Hypervisor Bugs)</span>
          </div>
          <span class="sub-topic-badge">Threats</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <ul>
            <li><strong>VM Escape:</strong> A catastrophic exploit where malware inside a guest VM escapes virtual boundaries to execute code on the host hypervisor.</li>
            <li><strong>Side-Channel Attacks:</strong> Exploiting CPU cache timing (Spectre/Meltdown) to read neighbor VM memory.</li>
            <li><strong>Unpatched Guest OS:</strong> Leaving guest systems vulnerable to network exploits.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 6.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>6.2 Shared Responsibility Model for VM Security</span>
          </div>
          <span class="sub-topic-badge">Responsibilities</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Cloud Provider Duty</th><th>Cloud Customer Duty</th></tr></thead>
              <tbody>
                <tr><td>Physical datacenter security</td><td>Guest operating system updates & patching</td></tr>
                <tr><td>Server hardware integrity</td><td>Virtual firewall / Security Group rules</td></tr>
                <tr><td>Hypervisor hardening & patching</td><td>Application security & data encryption</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 7 ==================== -->
  <div class="main-topic-card" id="u5-t7">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">📈</span>
        <span class="main-topic-title">Topic 7: Cloud Resource Management — Scalability vs Elasticity</span>
        <span class="badge badge-priority">High-Yield (7 Marks)</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>3 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 7.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>7.1 Scalability: Vertical (Scale Up), Horizontal (Scale Out), Diagonal</span>
          </div>
          <span class="sub-topic-badge">Scalability</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="grid-3">
            <div class="subcard">
              <h4>Vertical (Scale Up)</h4>
              <p>Adding more CPU cores or RAM to an existing machine (e.g. 4GB &rarr; 16GB RAM). Limited by physical hardware boundaries; requires reboot downtime.</p>
            </div>
            <div class="subcard">
              <h4>Horizontal (Scale Out)</h4>
              <p>Adding more server nodes/instances to the computing pool behind a load balancer (e.g. 2 &rarr; 6 instances). High fault tolerance.</p>
            </div>
            <div class="subcard">
              <h4>Diagonal Scaling</h4>
              <p>Combines vertical and horizontal: scale up individual instances first, then scale out horizontally as traffic expands.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 7.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>7.2 Elasticity: Definition & Dynamic Real-Time Adaptation</span>
          </div>
          <span class="sub-topic-badge">Elasticity</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">What is Elasticity?</div>
            <strong>Elasticity</strong> is the ability of cloud computing resources to automatically scale up/out during demand spikes and scale down/in when demand subsides, optimizing costs dynamically.
          </div>
          <p><strong>Example:</strong> An online shopping portal runs on 2 servers during regular hours, automatically scales to 10 servers during Black Friday sales, and contracts back to 2 servers afterward.</p>
        </div>
      </div>

      <!-- Sub-topic 7.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>7.3 Scalability vs Elasticity Comparison Matrix (7 Marks)</span>
          </div>
          <span class="sub-topic-badge">7 Marks</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Dimension</th><th>Scalability</th><th>Elasticity</th></tr></thead>
              <tbody>
                <tr><td><strong>Definition</strong></td><td>Ability to handle growing workloads by expanding capacity</td><td>Ability to dynamically grow and shrink matching real-time demand</td></tr>
                <tr><td><strong>Direction</strong></td><td>Unidirectional (Scale Up or Out)</td><td>Bidirectional (Scale Out and Scale In)</td></tr>
                <tr><td><strong>Automation</strong></td><td>Often manual or planned capacity expansion</td><td>Fully automated in real time via metric triggers</td></tr>
                <tr><td><strong>Focus</strong></td><td>Meeting peak demand without crashing</td><td>Minimizing cloud cost by avoiding idle resources</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 8 ==================== -->
  <div class="main-topic-card" id="u5-t8">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🚨</span>
        <span class="main-topic-title">Topic 8: Real-World Cloud Security Incidents (7 Case Studies)</span>
        <span class="badge badge-priority">High-Yield (10 Marks)</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>7 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 8.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>8.1 Capital One Data Breach (2019) — AWS SSRF & WAF Flaw</span>
          </div>
          <span class="sub-topic-badge">AWS</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p><strong>Provider:</strong> AWS | <strong>Impact:</strong> 106 Million customer records exfiltrated.</p>
          <p><strong>Vulnerability:</strong> A misconfigured Web Application Firewall (ModSecurity WAF) hosted on EC2 was vulnerable to Server-Side Request Forgery (SSRF).</p>
          <p><strong>Exploit:</strong> Attacker queried the EC2 Instance Metadata Service (IMDSv1) at <code>169.254.169.254</code> to extract temporary IAM credentials, using them to download credit card applications from S3.</p>
          <p><strong>Lesson:</strong> Migrate to IMDSv2, enforce strict IAM least-privilege, and audit WAF rules.</p>
        </div>
      </div>

      <!-- Sub-topic 8.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>8.2 AWS Misconfigured Storage Incidents (Public S3 Buckets)</span>
          </div>
          <span class="sub-topic-badge">AWS</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p><strong>Vulnerability:</strong> System administrators inadvertently configured S3 bucket ACLs to <code>AllUsers</code> (Public Read).</p>
          <p><strong>Impact:</strong> Automated scrapers harvested millions of sensitive military and medical records.</p>
          <p><strong>Lesson:</strong> Enable S3 "Block Public Access" at the root account level by default.</p>
        </div>
      </div>

      <!-- Sub-topic 8.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>8.3 AWS Customer Credential Attacks (Hardcoded Keys on GitHub)</span>
          </div>
          <span class="sub-topic-badge">AWS</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p><strong>Vulnerability:</strong> Developers accidentally committed root/IAM access keys into public code repositories.</p>
          <p><strong>Impact:</strong> Botnets seized accounts to launch GPU compute clusters for cryptocurrency mining.</p>
          <p><strong>Lesson:</strong> Never hardcode static credentials; use IAM Roles with temporary credentials and secret scanners.</p>
        </div>
      </div>

      <!-- Sub-topic 8.4 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>8.4 Storm-0558 Token Forgery Incident (2023) — Microsoft Cloud</span>
          </div>
          <span class="sub-topic-badge">Azure</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p><strong>Provider:</strong> Microsoft Azure / Microsoft Cloud | <strong>Impact:</strong> ~25 government and enterprise email accounts compromised.</p>
          <p><strong>Vulnerability:</strong> Threat actors acquired an inactive Microsoft consumer signing key (MSA key) leaked via crash dump, exploiting key-validation flaws to forge OpenID tokens.</p>
          <p><strong>Lesson:</strong> Cryptographic signing keys must be strictly isolated and key validation must not cross trust boundaries.</p>
        </div>
      </div>

      <!-- Sub-topic 8.5 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>8.5 Midnight Blizzard Targeted Activity (2024) — Microsoft Password Spray</span>
          </div>
          <span class="sub-topic-badge">Azure</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p><strong>Vulnerability:</strong> Password spray attack compromised a legacy, non-production test tenant account that lacked MFA.</p>
          <p><strong>Impact:</strong> Exploited test OAuth application permissions to view internal corporate emails.</p>
          <p><strong>Lesson:</strong> Enforce mandatory MFA across all legacy/test accounts and eliminate dormant OAuth apps.</p>
        </div>
      </div>

      <!-- Sub-topic 8.6 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>8.6 Google Cloud Customer Configuration Exposures</span>
          </div>
          <span class="sub-topic-badge">GCP</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p><strong>Vulnerability:</strong> Misconfigured GCP Cloud Storage bucket IAM bindings with <code>allUsers</code> roles exposed corporate datasets.</p>
          <p><strong>Lesson:</strong> Security follows the Shared Responsibility Model — customer configuration is 100% the customer's duty.</p>
        </div>
      </div>

      <!-- Sub-topic 8.7 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>8.7 Cloud Supply Chain & Identity Compromises</span>
          </div>
          <span class="sub-topic-badge">Supply Chain</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p><strong>Vulnerability:</strong> Poisoned third-party packages and compromised CI/CD pipeline tokens inject backdoors into production builds.</p>
          <p><strong>Lesson:</strong> Enforce Software Bill of Materials (SBOM), pin dependencies, and cryptographically sign container images.</p>
        </div>
      </div>

    </div>
  </div>

</div>
"""
