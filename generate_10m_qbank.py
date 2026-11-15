# -*- coding: utf-8 -*-
"""
Generates rich, extensive university-grade 10-mark questions and model answers
for the Cloud Computing Exam Portal (GSFC University BTCS701F).
"""

Q10M_HTML = """
    <!-- ==================== 10 MARKS COMPREHENSIVE MASTER QUESTIONS ==================== -->

    <!-- 10M QUESTION 1: VIRTUALIZATION IN DEPTH -->
    <div class="accordion-item" data-marks="10m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[10 Marks]</strong> 1. Comprehensive Analysis of Virtualization: Full Virtualization vs Paravirtualization vs Hardware-Assisted, Popek-Goldberg Theorem, CPU Rings & Root/Non-Root Modes, and 3 Virtualization Domains (Compute, Storage, Network).</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <div class="tip-box" style="margin-bottom: 1rem;">
          <strong>🎯 University Marking Scheme (10 Marks Blueprint):</strong>
          <ul style="margin: 0.25rem 0 0 1.2rem; font-size: 0.85rem;">
            <li><strong>2 Marks:</strong> Formal Definition of Virtualization & Popek-Goldberg Virtualization Theorem ($Sensitive \subseteq Privileged$).</li>
            <li><strong>3 Marks:</strong> Architectural comparison & diagrams of Full Virtualization, Paravirtualization, and Hardware-Assisted Virtualization.</li>
            <li><strong>2 Marks:</strong> CPU Ring Privilege structure, Intel VT-x / AMD-V VMX Root & Non-Root execution, VM-Exit & VM-Entry cycles.</li>
            <li><strong>2 Marks:</strong> Detailed breakdown of Compute, Storage, and Network Virtualization techniques in cloud datacenters.</li>
            <li><strong>1 Mark:</strong> 8-Parameter comparison table (VMs vs Docker Containers vs Bare-Metal).</li>
          </ul>
        </div>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">1. Formal Definition & Foundation of Virtualization</h4>
        <p>
          <strong>Virtualization</strong> is the foundational enabling technology of Cloud Computing. It is a software abstraction layer that decouples physical hardware (CPU, physical RAM, storage controllers, network interface cards) from the operating systems and user applications running on top. It creates logical, isolated execution environments called <strong>Virtual Machines (VMs)</strong>, governed by a specialized supervisory kernel termed the <strong>Hypervisor</strong> or <strong>Virtual Machine Monitor (VMM)</strong>.
        </p>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">2. Popek-Goldberg Virtualization Theorem (1974)</h4>
        <p>
          Formulated by Gerald Popek and Robert Goldberg, this theorem establishes the formal mathematical criteria for a computer processor architecture to support efficient, direct-execution virtualization:
        </p>
        <ul>
          <li><strong>Privileged Instructions:</strong> Instructions that trap (generate a hardware exception) when executed in user mode (Ring 3), transferring control immediately to supervisor mode (Ring 0).</li>
          <li><strong>Sensitive Instructions:</strong> Instructions that inspect hardware configurations without trapping (behavior-sensitive) or modify hardware configurations / memory mappings (control-sensitive).</li>
          <li><strong>The Golden Theorem:</strong> <em>"A computer architecture is strictly virtualizable if and only if all sensitive instructions are a subset of privileged instructions."</em>
            $$\text{Sensitive Instructions} \subseteq \text{Privileged Instructions}$$
          </li>
          <li><strong>The Classical x86 Virtualization Hole:</strong> The original x86 architecture contained <strong>17 sensitive instructions</strong> (such as <code>POPF</code>, <code>PUSHF</code>, <code>SGDT</code>, <code>SIDT</code>, <code>SLDT</code>, <code>SMSW</code>) that were NOT privileged! When executed in unprivileged user mode, they simply failed silently or leaked physical hardware register values without trapping. This made standard x86 non-virtualizable without complex software binary rewriting until Intel VT-x hardware assist was released in 2005.</li>
        </ul>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">3. Three CPU Virtualization Techniques (Architectural Breakdown)</h4>
        <div class="table-wrapper">
          <table>
            <thead><tr><th>Technique</th><th>Guest OS Requirement</th><th>Mechanism</th><th>Performance & Latency</th><th>Primary Examples</th></tr></thead>
            <tbody>
              <tr>
                <td><strong>1. Full Virtualization (Binary Translation)</strong></td>
                <td>100% Unmodified Guest OS (Standard ISO images)</td>
                <td>Hypervisor uses dynamic Binary Translation to intercept non-faulting sensitive instructions in software, translating them into safe instruction sequences while user code runs natively.</td>
                <td>Moderate; carries 5% to 15% translation CPU overhead.</td>
                <td>VMware ESXi, original VMware Workstation, Microsoft Virtual PC.</td>
              </tr>
              <tr>
                <td><strong>2. Paravirtualization (Hypercalls)</strong></td>
                <td>Modified Guest OS Kernel required</td>
                <td>Guest OS kernel source code is modified to be hypervisor-aware. Sensitive CPU instructions are replaced at compile time with <strong>Hypercalls</strong> (software interrupts to hypervisor, similar to syscalls).</td>
                <td>Near-native hardware speed; minimal software translation overhead.</td>
                <td>Xen Project (Dom0 / DomU), KVM (virtio drivers), Amazon EC2 original PV AMI instances.</td>
              </tr>
              <tr>
                <td><strong>3. Hardware-Assisted Virtualization</strong></td>
                <td>100% Unmodified Guest OS</td>
                <td>CPU hardware silicon provides dedicated virtualization rings (Intel VT-x, AMD-V) enabling hardware-enforced traps via <strong>VM-Exit</strong> and <strong>VM-Entry</strong> cycles.</td>
                <td>Maximum bare-metal performance; near zero CPU virtualization penalty.</td>
                <td>KVM with Intel VT-x, VMware ESXi 7+, Hyper-V, AWS Nitro System.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">4. CPU Privilege Rings & Intel VT-x VMX Modes</h4>
        <p>
          Classical x86 utilizes 4 hierarchical rings: <strong>Ring 0 (Kernel/Supervisor)</strong>, <strong>Ring 1 & 2 (Device Drivers)</strong>, and <strong>Ring 3 (User Applications)</strong>. In traditional OS architecture, the OS kernel occupies Ring 0.
        </p>
        <p>
          <strong>The "Ring 0 Contention" Problem:</strong> Both the Hypervisor and the Guest OS believe they belong in Ring 0. Running the Guest OS in Ring 1 or 2 breaks device driver expectations.
        </p>
        <p>
          <strong>Intel VT-x & AMD-V Hardware Solution:</strong> Intel introduced two distinct hardware execution modes that operate orthogonally across all 4 rings:
        </p>
        <ul>
          <li><strong>VMX Root Operation:</strong> The hypervisor executes here with full, unrestricted access to physical hardware registers and memory management units. Contains full Rings 0 to 3.</li>
          <li><strong>VMX Non-Root Operation:</strong> The Guest OS and its applications execute here. When the Guest OS in Ring 0 executes any sensitive privileged instruction, the CPU triggers an automatic hardware <strong>VM-Exit</strong>, instantly pausing the guest VM and passing execution state to the hypervisor in Root Mode.</li>
          <li><strong>VM-Exit & VM-Entry Lifecycle:</strong> The hypervisor inspects the VMCS (Virtual Machine Control Structure), handles the I/O or privileged operation, and executes <code>VMRESUME</code> to perform a <strong>VM-Entry</strong>, restoring guest VM execution.</li>
          <li><strong>Memory Virtualization (EPT / NPT):</strong> Intel Extended Page Tables (EPT) and AMD Nested Page Tables (NPT) maintain two-dimensional page tables: Guest Virtual &rarr; Guest Physical &rarr; Host Physical memory, completely handled in CPU silicon.</li>
        </ul>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">5. The Three Virtualization Domains in Cloud Computing</h4>
        <ol>
          <li><strong>Compute Virtualization:</strong> Abstraction of CPU and memory. A single physical multi-core socket (e.g. 64 cores) is scheduled into hundreds of virtual CPUs (vCPUs) by the hypervisor credit or CFS scheduler. Features dynamic ballooning and RAM overcommitment.</li>
          <li><strong>Storage Virtualization:</strong> Pooling multiple physical hard disk drives and flash SSDs from Storage Area Networks (SAN) and Network Attached Storage (NAS) into elastic virtual storage pools. Supported by Logical Volume Management (LVM) and Software-Defined Storage (Ceph, OpenStack Cinder/Swift).</li>
          <li><strong>Network Virtualization:</strong> Decouples physical cables, top-of-rack switches, and routers into software abstractions. Uses Virtual Network Interface Cards (vNICs), virtual software switches (Open vSwitch), and overlay encapsulation protocols (VXLAN, NVGRE) to create isolated multi-tenant overlay networks.</li>
        </ol>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">6. Virtual Machines vs Docker Containers vs Bare-Metal Comparison</h4>
        <div class="table-wrapper">
          <table>
            <thead><tr><th>Parameter</th><th>Bare-Metal Server</th><th>Virtual Machine (Hypervisor)</th><th>Docker Container (OS-Level)</th></tr></thead>
            <tbody>
              <tr><td><strong>Virtualization Level</strong></td><td>None (Physical Hardware)</td><td>Hardware-level (CPU, RAM, NIC emulated)</td><td>OS Kernel-level (Namespaces & cgroups)</td></tr>
              <tr><td><strong>Operating System</strong></td><td>Single dedicated Host OS</td><td>Full Guest OS per VM (GBs in size)</td><td>Shares Host OS kernel (MBs in size)</td></tr>
              <tr><td><strong>Startup Boot Time</strong></td><td>Several minutes (POST & BIOS)</td><td>1 to 3 minutes (Full OS kernel boot)</td><td>Milliseconds to seconds (Process spawn)</td></tr>
              <tr><td><strong>Resource Overhead</strong></td><td>0% (Native execution)</td><td>High (Each VM reserves dedicated RAM/OS)</td><td>Minimal (Zero Guest OS RAM tax)</td></tr>
              <tr><td><strong>Security Isolation</strong></td><td>Physical hardware isolation</td><td>Strong hardware hypervisor boundaries</td><td>Process-level isolation (Shared kernel risk)</td></tr>
              <tr><td><strong>Server Density</strong></td><td>1 workload per server</td><td>10 to 30 VMs per host</td><td>200 to 500 containers per host</td></tr>
              <tr><td><strong>Portability</strong></td><td>Locked to physical hardware drivers</td><td>High (Hypervisor image formats: OVF, QCOW2)</td><td>Extreme (Runs identically across any Linux host)</td></tr>
              <tr><td><strong>Primary Use Case</strong></td><td>High-performance compute, latency-critical DBs</td><td>Multi-tenant cloud infrastructure, legacy apps</td><td>Cloud-native microservices, CI/CD pipelines</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- 10M QUESTION 2: OPENSTACK ARCHITECTURE -->
    <div class="accordion-item" data-marks="10m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[10 Marks]</strong> 2. OpenStack Cloud Operating System: Detailed Architecture, All 9 Core Components (Nova, Keystone, Neutron, Glance, Cinder, Swift, Horizon, Heat, Ceilometer), Message Queue Communication, and 12-Step VM Provisioning Workflow.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <div class="tip-box" style="margin-bottom: 1rem;">
          <strong>🎯 University Marking Scheme (10 Marks Blueprint):</strong>
          <ul style="margin: 0.25rem 0 0 1.2rem; font-size: 0.85rem;">
            <li><strong>2 Marks:</strong> Definition, OpenStack philosophy, and architectural communication bus (RabbitMQ & MariaDB/MySQL).</li>
            <li><strong>4 Marks:</strong> Comprehensive description of all 9 core services with internal daemons and responsibilities.</li>
            <li><strong>3 Marks:</strong> End-to-end 12-step VM launch sequence diagram and workflow description.</li>
            <li><strong>1 Mark:</strong> OpenStack High Availability (HA) deployment architecture (Controller vs Compute vs Storage nodes).</li>
          </ul>
        </div>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">1. OpenStack Overview & Modular Philosophy</h4>
        <p>
          <strong>OpenStack</strong> is the world's most widely deployed open-source cloud operating system. It orchestrates large pools of compute, storage, and networking resources throughout datacenters via a set of interrelated microservices. All services communicate asynchronously via the <strong>RabbitMQ AMQP Message Queue</strong> and store relational state in a shared <strong>MariaDB/MySQL</strong> cluster. External clients interact exclusively via uniform <strong>RESTful APIs</strong>.
        </p>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">2. The 9 Core OpenStack Services (Detailed Deep-Dive)</h4>
        <ol>
          <li>
            <strong>Keystone (Identity & Authentication Service):</strong>
            <ul>
              <li><strong>Responsibilities:</strong> Central security authority. Provides user authentication, token issuance (UUID and Fernet tokens), RBAC role evaluation, and a dynamic <em>Service Catalog</em> containing API endpoints for all cloud services.</li>
              <li><strong>Core Concepts:</strong> Users, Tenants/Projects, Roles, Domains, Endpoints (Public, Admin, Internal).</li>
            </ul>
          </li>
          <li>
            <strong>Nova (Compute Fabric Orchestrator):</strong>
            <ul>
              <li><strong>Responsibilities:</strong> Provisions and manages the lifecycle of virtual machine instances.</li>
              <li><strong>Internal Daemons:</strong> <code>nova-api</code> (receives REST requests), <code>nova-scheduler</code> (evaluates filter algorithms like RAMFilter, CoreFilter to pick optimal host), <code>nova-conductor</code> (database proxy isolating compute nodes), <code>nova-compute</code> (runs on hypervisor node controlling KVM via libvirt).</li>
            </ul>
          </li>
          <li>
            <strong>Neutron (Software-Defined Networking - SDN):</strong>
            <ul>
              <li><strong>Responsibilities:</strong> Delivers Networking-as-a-Service (NaaS), managing virtual networks, subnets, routers, floating IPs, security groups, and VPN/LBaaS plugins.</li>
              <li><strong>Internal Architecture:</strong> ML2 (Modular Layer 2) plugin coordinating Open vSwitch (OVS) or Linux Bridge drivers, L3 Agent (NAT/routing), and DHCP Agent.</li>
            </ul>
          </li>
          <li>
            <strong>Glance (Virtual Machine Image Registry):</strong>
            <ul>
              <li><strong>Responsibilities:</strong> Discovers, registers, stores, and retrieves virtual machine disk images and VM snapshots.</li>
              <li><strong>Supported Formats:</strong> QCOW2, RAW, VMDK, VHD, ISO, AMI. Backed by Swift, Ceph, or standard local filesystem storage.</li>
            </ul>
          </li>
          <li>
            <strong>Cinder (Persistent Block Storage Service):</strong>
            <ul>
              <li><strong>Responsibilities:</strong> Provisions persistent, raw block volumes attached to Nova compute instances over iSCSI, Fibre Channel, or Ceph RBD. Survives VM termination.</li>
              <li><strong>Internal Daemons:</strong> <code>cinder-api</code>, <code>cinder-scheduler</code>, <code>cinder-volume</code>.</li>
            </ul>
          </li>
          <li>
            <strong>Swift (Distributed Object Storage):</strong>
            <ul>
              <li><strong>Responsibilities:</strong> Exabyte-scale, highly durable multi-tenant object storage for unstructured media and backups accessed via HTTP/REST (GET, PUT, DELETE).</li>
              <li><strong>Architecture:</strong> Masterless Ring architecture dividing data into Account, Container, and Object servers with automated data auditing and replication.</li>
            </ul>
          </li>
          <li>
            <strong>Horizon (Web Graphical Dashboard):</strong>
            <ul>
              <li><strong>Responsibilities:</strong> Django-based web application providing self-service user management and administrative control over all OpenStack resources.</li>
            </ul>
          </li>
          <li>
            <strong>Heat (Orchestration Engine):</strong>
            <ul>
              <li><strong>Responsibilities:</strong> Template-driven cloud application deployment based on Heat Orchestration Templates (HOT) written in declarative YAML. Functionally equivalent to AWS CloudFormation.</li>
            </ul>
          </li>
          <li>
            <strong>Ceilometer (Telemetry, Metering & Alarming):</strong>
            <ul>
              <li><strong>Responsibilities:</strong> Collects performance metrics, resource consumption event logs, and billing meters across compute, disk, and network interfaces. Integrates with <strong>Aodh</strong> (alarm service) for automated horizontal scaling triggers.</li>
            </ul>
          </li>
        </ol>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">3. End-to-End 12-Step VM Provisioning Lifecycle (Sequence Workflow)</h4>
        <div class="def-box">
          <p><strong>Step-by-Step Execution Trace:</strong></p>
          <ol style="margin-left: 1.2rem; font-size: 0.88rem;">
            <li><strong>Step 1 (Authentication):</strong> User submits credentials via Horizon Web UI / OpenStack CLI. <strong>Keystone</strong> authenticates credentials and issues an unscoped token, then swaps for a tenant-scoped token and the service catalog.</li>
            <li><strong>Step 2 (Boot Request):</strong> User issues <code>openstack server create --image Ubuntu --flavor m1.small web-vm</code>. Horizon sends an HTTP POST request to <code>nova-api</code> with the Keystone auth token.</li>
            <li><strong>Step 3 (Token Validation):</strong> <code>nova-api</code> validates the token and project quotas with <strong>Keystone</strong>.</li>
            <li><strong>Step 4 (Database Update):</strong> <code>nova-api</code> writes initial VM instance state (BUILDING) into the MariaDB database via <code>nova-conductor</code>.</li>
            <li><strong>Step 5 (Scheduler Dispatch):</strong> <code>nova-api</code> publishes a message to the RabbitMQ <code>scheduler</code> exchange requesting host placement.</li>
            <li><strong>Step 6 (Filtering & Weighting):</strong> <code>nova-scheduler</code> runs filtering algorithms (RAMFilter, AvailabilityZoneFilter, DiskFilter) followed by weighting algorithms to select the optimal physical compute host (e.g. <code>compute-node-04</code>).</li>
            <li><strong>Step 7 (RPC to Compute):</strong> <code>nova-scheduler</code> sends an AMQP message through RabbitMQ to the target host's <code>nova-compute</code> daemon.</li>
            <li><strong>Step 8 (Network Allocation):</strong> <code>nova-compute</code> contacts <strong>Neutron</strong> via REST API to allocate a virtual network port, IP address, and security group firewall rules.</li>
            <li><strong>Step 9 (Image Fetching):</strong> <code>nova-compute</code> contacts <strong>Glance</strong> using image ID to stream the base QCOW2 operating system image to the local compute node cache.</li>
            <li><strong>Step 10 (Volume Attachment):</strong> If persistent storage was requested, <code>nova-compute</code> invokes <strong>Cinder</strong> to map and attach the block volume over iSCSI.</li>
            <li><strong>Step 11 (Hypervisor Spawning):</strong> <code>nova-compute</code> generates a libvirt XML domain definition and instructs the hypervisor (KVM) to instantiate and boot the VM.</li>
            <li><strong>Step 12 (Active State Notification):</strong> <code>nova-compute</code> confirms successful boot, updates instance status to <strong>ACTIVE</strong> in MariaDB, and notifies Ceilometer to begin telemetry tracking.</li>
          </ol>
        </div>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">4. OpenStack High Availability (HA) Production Architecture</h4>
        <p>
          Production OpenStack datacenters segregate machines into three functional physical tiers:
        </p>
        <ul>
          <li><strong>Controller Nodes (3 Nodes Minimum Cluster):</strong> Runs all API daemons, Keystone, Horizon, RabbitMQ (mirrored queues), and MariaDB Galera multi-master cluster managed by Pacemaker/Corosync with HAProxy for VIP load balancing.</li>
          <li><strong>Compute Nodes (Horizontally Scalable):</strong> Dedicated bare-metal servers executing <code>nova-compute</code>, Open vSwitch, and KVM hypervisors. Zero administrative database credentials.</li>
          <li><strong>Storage Nodes:</strong> Dedicated servers hosting Ceph OSDs, Cinder volume drivers, or Swift object storage rings.</li>
        </ul>
      </div>
    </div>

    <!-- 10M QUESTION 3: MULTI-TENANT ARCHITECTURE -->
    <div class="accordion-item" data-marks="10m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[10 Marks]</strong> 3. Multi-Tenant Cloud Architecture: Comprehensive Analysis of Silo, Bridge, and Pool Isolation Models, Row-Level Security (RLS) Implementation, Noisy Neighbor Problem, and Mitigation Algorithms.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <div class="tip-box" style="margin-bottom: 1rem;">
          <strong>🎯 University Marking Scheme (10 Marks Blueprint):</strong>
          <ul style="margin: 0.25rem 0 0 1.2rem; font-size: 0.85rem;">
            <li><strong>2 Marks:</strong> Definition of Multi-Tenancy, economic business rationale, and comparison with Multi-Instance architecture.</li>
            <li><strong>3 Marks:</strong> Detailed explanation and diagrams of Silo, Bridge, and Pool data isolation patterns.</li>
            <li><strong>2 Marks:</strong> Concrete Row-Level Security (RLS) SQL implementation and tenant context injection.</li>
            <li><strong>2 Marks:</strong> Noisy Neighbor problem causes and engineering mitigation algorithms (Token Bucket, Cgroups, Tenant Tiering).</li>
            <li><strong>1 Mark:</strong> 7-parameter comparison table across isolation models.</li>
          </ul>
        </div>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">1. Multi-Tenancy Definition & Economic Foundations</h4>
        <p>
          <strong>Multi-Tenant Architecture</strong> is a software architecture where a single physical or logical instance of an application runs on cloud infrastructure to serve multiple independent customer organizations, called <strong>tenants</strong>. Each tenant has a customized, isolated virtual partition with its own user accounts, access permissions, branding, and sensitive data.
        </p>
        <p>
          <strong>Economic Driver:</strong> In traditional single-tenant hosting, serving 1,000 customers requires running 1,000 distinct VM clusters, OS licenses, and database instances. Multi-tenancy aggregates workloads onto shared infrastructure, reducing Cost of Goods Sold (COGS) by 70% to 90% and simplifying software upgrades to a single centralized deployment.
        </p>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">2. The Three Database Isolation Patterns</h4>
        
        <h5 style="color: var(--text-primary); margin-top: 0.75rem;">A. Silo Pattern (Dedicated Database per Tenant)</h5>
        <ul>
          <li><strong>Architecture:</strong> Every tenant receives a completely independent, physically or logically isolated database instance (e.g. separate AWS RDS instances).</li>
          <li><strong>Advantages:</strong> Maximum data isolation, zero risk of cross-tenant data leakage, customized database configurations per tenant, zero cross-tenant blast radius, simplified tenant-specific point-in-time backups.</li>
          <li><strong>Disadvantages:</strong> Highest operational cost, extreme management overhead (running database migrations across thousands of instances), severe resource underutilization during off-peak hours.</li>
          <li><strong>Target Domain:</strong> Commercial banking, defense systems, HIPAA healthcare systems.</li>
        </ul>

        <h5 style="color: var(--text-primary); margin-top: 0.75rem;">B. Bridge Pattern (Shared Engine, Dedicated Schemas)</h5>
        <ul>
          <li><strong>Architecture:</strong> All tenants share a single database server engine, but each tenant's data resides in its own isolated database schema (e.g. PostgreSQL <code>schema_tenant123</code>).</li>
          <li><strong>Advantages:</strong> Balances cost and isolation. Physical compute/RAM costs are shared, but logical database security boundaries are maintained by database engine permissions.</li>
          <li><strong>Disadvantages:</strong> Schema migration complexity; connection pool exhaustion if hundreds of schemas are active concurrently; shared server failure impacts all tenants.</li>
          <li><strong>Target Domain:</strong> Enterprise B2B SaaS platforms.</li>
        </ul>

        <h5 style="color: var(--text-primary); margin-top: 0.75rem;">C. Pool Pattern (Shared Database, Shared Tables)</h5>
        <ul>
          <li><strong>Architecture:</strong> All tenants share the same database instance, the same schema, and the exact same database tables. Every record contains a mandatory <code>tenant_id</code> discriminator column.</li>
          <li><strong>Advantages:</strong> Lowest cost, maximum server utilization, instantaneous onboarding of new tenants (zero schema creation needed), single migration run updates 100% of tenants.</li>
          <li><strong>Disadvantages:</strong> Highest security risk (a missing <code>WHERE tenant_id = ?</code> clause leaks data to competitors); requires strict Row-Level Security (RLS) enforcement; susceptible to the Noisy Neighbor effect.</li>
          <li><strong>Target Domain:</strong> High-volume consumer and SMB SaaS (Shopify, Slack, Notion).</li>
        </ul>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">3. 7-Parameter Isolation Comparison Matrix</h4>
        <div class="table-wrapper">
          <table>
            <thead><tr><th>Evaluation Metric</th><th>Silo Pattern</th><th>Bridge Pattern</th><th>Pool Pattern</th></tr></thead>
            <tbody>
              <tr><td><strong>Infrastructure Cost</strong></td><td>Highest ($$$$)</td><td>Moderate ($$)</td><td>Lowest ($)</td></tr>
              <tr><td><strong>Data Isolation Security</strong></td><td>Maximum (Physical DB barrier)</td><td>High (Schema-level barrier)</td><td>Logical (Application/RLS enforced)</td></tr>
              <tr><td><strong>Tenant Onboarding Time</strong></td><td>Minutes to hours (DB provisioning)</td><td>Seconds to minutes (Schema setup)</td><td>Milliseconds (Single SQL INSERT)</td></tr>
              <tr><td><strong>Database Migration Complexity</strong></td><td>Very High (Iterate over N databases)</td><td>High (Iterate over N schemas)</td><td>Minimal (Single schema update)</td></tr>
              <tr><td><strong>Blast Radius on Failure</strong></td><td>Isolated to 1 tenant</td><td>All tenants on that DB engine</td><td>All tenants in that shared cluster</td></tr>
              <tr><td><strong>Noisy Neighbor Vulnerability</strong></td><td>Zero (Dedicated compute & RAM)</td><td>Moderate (Shared IOPS/CPU)</td><td>Severe (Shared table locks & memory)</td></tr>
              <tr><td><strong>Regulatory Compliance</strong></td><td>Meets strict PCI-DSS / HIPAA rules</td><td>Meets moderate compliance rules</td><td>Requires complex audit controls</td></tr>
            </tbody>
          </table>
        </div>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">4. Row-Level Security (RLS) SQL Implementation</h4>
        <p>
          To prevent catastrophic cross-tenant data leaks in the Pool model, modern cloud applications utilize database-native <strong>Row-Level Security (RLS)</strong>:
        </p>
        <pre style="background: var(--bg-primary); padding: 0.85rem; border-radius: 6px; font-family: var(--font-mono); font-size: 0.82rem; overflow-x: auto; color: var(--accent); border: 1px solid var(--border-color);">
-- 1. Enable RLS on multi-tenant table
ALTER TABLE customer_orders ENABLE ROW LEVEL SECURITY;

-- 2. Create security policy checking current session tenant variable
CREATE POLICY tenant_isolation_policy ON customer_orders
  FOR ALL
  USING (tenant_id = current_setting('app.current_tenant_id')::UUID);

-- 3. Application sets tenant context upon checkout connection
SET LOCAL app.current_tenant_id = 'a56f8901-b34e-4f12-98ab-3412567890ef';
-- Any subsequent SELECT * automatically filters only rows belonging to this tenant!
SELECT * FROM customer_orders; -- Impossible to see other tenant data even without explicit WHERE!
        </pre>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">5. The Noisy Neighbor Problem & Mitigation Engineering</h4>
        <p>
          <strong>Problem:</strong> In a shared multi-tenant environment, if Tenant A runs an unindexed query scanning 10 million rows or executes a massive flash sale, it monopolizes CPU cores, RAM buffer pools, and database connection sockets, causing latency spikes and timeouts for innocent Tenant B on the same server.
        </p>
        <p><strong>Mitigation Strategies:</strong></p>
        <ul>
          <li><strong>Token-Bucket Rate Limiting:</strong> Enforce strict per-tenant API rate limits (e.g. Tenant A is capped at 500 requests/sec with burst allowance of 1,000 via Redis token-bucket).</li>
          <li><strong>Database Connection Pool Segregation:</strong> Instead of a single shared pool, assign partitioned connection pools via PgBouncer so one tenant cannot starve available database sockets.</li>
          <li><strong>Linux Cgroups Quotas:</strong> Enforce hard CPU and memory ceilings per tenant container so runaway threads are throttled by the OS scheduler.</li>
          <li><strong>Automated Tenant Tiering ("Whale Migration"):</strong> Monitor real-time consumption. When a tenant outgrows the shared pool, automated workflows seamlessly migrate their database into a dedicated Silo instance without downtime.</li>
        </ul>
      </div>
    </div>

    <!-- 10M QUESTION 4: CLOUD SECURITY THREATS & CASE STUDIES -->
    <div class="accordion-item" data-marks="10m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[10 Marks]</strong> 4. Cloud Security Threats, Vulnerabilities & Forensics: Detailed Analysis of 4 Real-World Breaches (Capital One SSRF on IMDSv1, Microsoft Storm-0558 Token Forgery, Code Spaces Root Liquidation, Uber GitHub Leak) with Layered Defense-in-Depth Architecture.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <div class="tip-box" style="margin-bottom: 1rem;">
          <strong>🎯 University Marking Scheme (10 Marks Blueprint):</strong>
          <ul style="margin: 0.25rem 0 0 1.2rem; font-size: 0.85rem;">
            <li><strong>2 Marks:</strong> Cloud attack surface, Shared Responsibility security boundaries, and OWASP Cloud Top 10 vectors.</li>
            <li><strong>4 Marks:</strong> Comprehensive technical post-mortem of Capital One (SSRF/IMDSv1) and Microsoft Storm-0558 breaches.</li>
            <li><strong>2 Marks:</strong> Forensic analysis of Code Spaces (Root account destruction) and Uber (Hardcoded API keys) incidents.</li>
            <li><strong>2 Marks:</strong> Layered Cloud Defense-in-Depth blueprint across Perimeter, Network, IAM, Data, and Logging tiers.</li>
          </ul>
        </div>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">1. The Cloud Attack Surface & Shared Responsibility</h4>
        <p>
          In cloud environments, traditional network perimeter defenses (firewalls, DMZs) are insufficient. Cloud workloads face unique vulnerabilities including metadata exfiltration, over-permissive IAM policies, container breakouts, and multi-tenant hypervisor escape. Under the <strong>Shared Responsibility Model</strong>, the cloud provider secures the underlying physical datacenters and virtualization hypervisors, but the enterprise customer is strictly responsible for identity management, access policies, operating system patching, and data encryption.
        </p>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">2. Case Study 1: Capital One SSRF Breach (2019) — AWS</h4>
        <ul>
          <li><strong>The Vulnerability:</strong> A misconfigured open-source Web Application Firewall (ModSecurity WAF) deployed on an AWS EC2 instance was vulnerable to <strong>Server-Side Request Forgery (SSRF)</strong>.</li>
          <li><strong>The Exploit Vector:</strong>
            <ol style="margin-left: 1.2rem; font-size: 0.85rem;">
              <li>The attacker sent crafted HTTP requests to the WAF, tricking it into executing internal network requests on behalf of the attacker.</li>
              <li>The WAF queried the internal AWS <strong>Instance Metadata Service v1 (IMDSv1)</strong> located at non-routable link-local IP <code>http://169.254.169.254/latest/meta-data/iam/security-credentials/</code>.</li>
              <li>IMDSv1 returned temporary AWS Security Token Service (STS) credentials assigned to the WAF's EC2 instance IAM role without requiring authentication.</li>
              <li>Due to a violation of the Principle of Least Privilege, the WAF IAM role had broad <code>s3:*</code> permissions across all S3 buckets in the AWS account.</li>
              <li>The attacker executed <code>aws s3 sync</code> and exfiltrated <strong>106 million credit card applications</strong> and 140,000 Social Security Numbers from 700 S3 buckets.</li>
            </ol>
          </li>
          <li><strong>Remediations & Architectural Lessons:</strong>
            <ul>
              <li><strong>Migrate to IMDSv2:</strong> IMDSv2 is session-oriented. It requires a <code>PUT</code> request with a <code>X-aws-ec2-metadata-token-ttl-seconds</code> header to obtain a session token before querying metadata, completely neutralizing SSRF attacks.</li>
              <li><strong>IAM Least Privilege:</strong> Instance profiles must only be granted access to the specific resources they need, never wildcard <code>s3:*</code>.</li>
              <li><strong>KMS Key Restriction:</strong> S3 buckets must be encrypted with Customer Managed Keys (CMK) containing key policies that restrict decryption exclusively to backend data pipelines.</li>
            </ul>
          </li>
        </ul>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">3. Case Study 2: Microsoft Storm-0558 Token Forgery (2023) — Azure</h4>
        <ul>
          <li><strong>The Vulnerability:</strong> An inactive Microsoft consumer account (MSA) cryptographic signing key leaked into a Windows kernel crash dump file following an internal system crash in April 2021. The dump was moved to an internet-connected debugging environment where threat actor Storm-0558 compromised it.</li>
          <li><strong>The Exploit Vector:</strong>
            <ol style="margin-left: 1.2rem; font-size: 0.85rem;">
              <li>The threat actors utilized the stolen private signing key to forge <strong>OpenID Connect (OIDC)</strong> bearer tokens.</li>
              <li>Due to a key validation issue in the Azure AD (Entra ID) token verification endpoint, the system erroneously accepted consumer-signed tokens for enterprise Microsoft Exchange Online and Outlook Web Access (OWA).</li>
              <li>The attackers accessed email inboxes of 25 major organizations, including the US State and Commerce Departments.</li>
            </ol>
          </li>
          <li><strong>Remediations & Architectural Lessons:</strong>
            <ul>
              <li>Never allow cryptographic private keys to persist in plaintext memory crash dumps.</li>
              <li>Enforce strict isolation between consumer identity verification endpoints and enterprise cloud endpoints.</li>
              <li>Enforce automated Hardware Security Module (HSM) based key rotation with zero human access.</li>
            </ul>
          </li>
        </ul>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">4. Case Study 3: Code Spaces Complete Liquidation (2014) — AWS</h4>
        <ul>
          <li><strong>The Incident:</strong> Code Spaces was a SaaS provider offering code repositories and project management. Attackers gained access to their AWS Management Console root account.</li>
          <li><strong>The Exploit:</strong> The attackers demanded an extortion ransom. When Code Spaces attempted to regain control, the attackers systematically deleted all EBS volumes, S3 buckets, database snapshots, and off-site backup replicas.</li>
          <li><strong>The Impact:</strong> 100% of customer data and backups were permanently obliterated. Code Spaces was forced into immediate corporate liquidation within 12 hours.</li>
          <li><strong>Remediation:</strong> NEVER use the AWS root account for operational tasks. Enforce physical FIDO2 hardware MFA keys on root, lock root credentials in a corporate physical vault, and maintain cross-account immutable backups in an AWS Backup Vault with WORM compliance lock.</li>
        </ul>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">5. Layered Cloud Defense-in-Depth Architecture</h4>
        <div class="table-wrapper">
          <table>
            <thead><tr><th>Defense Layer</th><th>Threats Mitigated</th><th>Production Cloud Controls</th></tr></thead>
            <tbody>
              <tr><td><strong>1. Perimeter & Edge</strong></td><td>DDoS, Layer 7 Web Exploits, Botnets</td><td>AWS CloudFront (CDN), AWS Shield Advanced (DDoS), AWS WAF rate-limiting rules.</td></tr>
              <tr><td><strong>2. Network & VPC</strong></td><td>Lateral movement, unauthorized ports</td><td>Private Subnets, Security Groups (stateful firewall), Network ACLs (stateless), VPC Flow Logs.</td></tr>
              <tr><td><strong>3. Host & Compute</strong></td><td>OS vulnerabilities, malware, SSRF</td><td>IMDSv2 enforced, CIS benchmark hardened AMIs, AWS Systems Manager (SSM) without open SSH.</td></tr>
              <tr><td><strong>4. Identity & Access (IAM)</strong></td><td>Credential theft, privilege escalation</td><td>Hardware MFA, Principle of Least Privilege (PoLP), AWS STS short-lived tokens, Permission Boundaries.</td></tr>
              <tr><td><strong>5. Data Storage</strong></td><td>Data exfiltration, unauthorized reads</td><td>AES-256 encryption at rest (AWS KMS), TLS 1.3 in transit, S3 Block Public Access, S3 Object Lock.</td></tr>
              <tr><td><strong>6. Monitoring & SIEM</strong></td><td>Delayed detection, insider threats</td><td>AWS CloudTrail (immutable audit logs), Amazon GuardDuty (ML threat detection), AWS Security Hub.</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- 10M QUESTION 5: AWS IAM ENTERPRISE ARCHITECTURE -->
    <div class="accordion-item" data-marks="10m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[10 Marks]</strong> 5. AWS IAM Enterprise Security Architecture: Identity Entities (Users, Groups, Roles), JSON Policy Grammar, 6-Step Evaluation Logic Algorithm with the Explicit Deny Rule, and Temporary STS Token Generation.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <div class="tip-box" style="margin-bottom: 1rem;">
          <strong>🎯 University Marking Scheme (10 Marks Blueprint):</strong>
          <ul style="margin: 0.25rem 0 0 1.2rem; font-size: 0.85rem;">
            <li><strong>2 Marks:</strong> IAM foundational philosophy, Principle of Least Privilege (PoLP), and Zero Trust model.</li>
            <li><strong>2 Marks:</strong> Detailed roles and differences of IAM Users, User Groups, IAM Roles, and IAM Policies.</li>
            <li><strong>2 Marks:</strong> IAM JSON policy grammar, element definitions (Effect, Action, Resource, Condition), and complete JSON code example.</li>
            <li><strong>3 Marks:</strong> Complete 6-step IAM Policy Evaluation Decision Flowchart and the absolute authority of Explicit Deny.</li>
            <li><strong>1 Mark:</strong> AWS Security Token Service (STS) AssumeRole API temporary credential issuance.</li>
          </ul>
        </div>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">1. Foundational IAM Security Principles</h4>
        <p>
          <strong>AWS Identity and Access Management (IAM)</strong> is the central control plane for security in Amazon Web Services. It governs authentication (who are you?) and authorization (what are you allowed to do?). IAM adheres to two mandatory security doctrines:
        </p>
        <ul>
          <li><strong>Principle of Least Privilege (PoLP):</strong> Users, applications, and services must be granted only the absolute minimum permissions necessary to complete their job tasks, for the shortest duration required.</li>
          <li><strong>Zero Trust Architecture:</strong> Never trust, always verify. Every API request arriving at AWS endpoints is independently authenticated and authorized, regardless of whether it originates from inside or outside the VPC.</li>
        </ul>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">2. The Four Fundamental IAM Entities</h4>
        <ol>
          <li><strong>IAM Users:</strong> Persistent identity entities representing an individual person or service with long-term credentials (password for AWS Management Console, Access Key ID & Secret Access Key for CLI/SDK). <em>Best practice: Avoid creating IAM users with static keys; prefer SSO federation.</em></li>
          <li><strong>IAM User Groups:</strong> Collections of IAM users. Permissions assigned to a group automatically apply to all member users (e.g. <code>DevelopersGroup</code>, <code>DBAdminGroup</code>). Groups cannot be nested and cannot be identified as a <code>Principal</code> in a policy.</li>
          <li><strong>IAM Roles:</strong> Temporary identities that can be assumed by anyone who needs it: human users, internal AWS services (e.g. an EC2 instance or Lambda function needing S3 access), or external federated identities via OIDC/SAML. Roles have NO long-term passwords or access keys; they issue short-lived temporary security credentials via <strong>AWS STS</strong>.</li>
          <li><strong>IAM Policies:</strong> Formal JSON documents defining fine-grained permissions. Classified into <strong>Identity-based policies</strong> (attached to Users/Groups/Roles) and <strong>Resource-based policies</strong> (attached directly to AWS resources, such as S3 Bucket Policies or KMS Key Policies).</li>
        </ol>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">3. IAM JSON Policy Grammar & Syntax</h4>
        <p>
          Every IAM policy contains a mandatory structure defined by standard policy keys:
        </p>
        <ul>
          <li><code>Version</code>: Always specify <code>"2012-10-17"</code> (the current policy language version).</li>
          <li><code>Statement</code>: An array of individual permission rules.</li>
          <li><code>Sid</code>: Optional statement identifier for human documentation.</li>
          <li><code>Effect</code>: Required. Must be either <code>"Allow"</code> or <code>"Deny"</code>.</li>
          <li><code>Principal</code>: Required in resource-based policies (indicates who is allowed/denied).</li>
          <li><code>Action</code>: Specific API calls permitted or forbidden (e.g. <code>"s3:GetObject"</code>, <code>"ec2:StartInstances"</code>).</li>
          <li><code>Resource</code>: Amazon Resource Name (ARN) identifying the target entity (e.g. <code>"arn:aws:s3:::finance-reports/*"</code>).</li>
          <li><code>Condition</code>: Contextual constraints (IP address CIDR, MFA active, current time, SSL enforced).</li>
        </ul>

        <div class="def-box">
          <p><strong>Example: Production Least-Privilege IAM Policy with Explicit Deny & MFA Constraint:</strong></p>
          <pre style="background: var(--bg-primary); padding: 0.85rem; border-radius: 6px; font-family: var(--font-mono); font-size: 0.82rem; overflow-x: auto; color: var(--accent); border: 1px solid var(--border-color);">
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ReadWithMFA",
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": [
        "arn:aws:s3:::gsfc-finance-vault",
        "arn:aws:s3:::gsfc-finance-vault/*"
      ],
      "Condition": {
        "Bool": { "aws:MultiFactorAuthPresent": "true" }
      }
    },
    {
      "Sid": "ExplicitDenyOutsideCorporateNetwork",
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "NotIpAddress": {
          "aws:SourceIp": ["103.21.144.0/24", "115.112.45.10/32"]
        }
      }
    }
  ]
}
          </pre>
        </div>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">4. The 6-Step AWS Policy Evaluation Algorithm</h4>
        <p>
          When an authenticated principal issues an API request to AWS, the IAM Evaluation Engine processes all applicable policies through a strict deterministic algorithm:
        </p>
        <ol style="margin-left: 1.2rem; font-size: 0.88rem;">
          <li><strong>Step 1 (Default Implicit Deny):</strong> Every request begins in a state of default deny. Access is denied unless an evaluation step explicitly authorizes it.</li>
          <li><strong>Step 2 (The Golden Rule — Explicit Deny Check):</strong> The engine evaluates all attached Identity-based policies, Resource-based policies, Service Control Policies (SCPs), Permissions Boundaries, and Session Policies. <strong>If ANY single policy statement contains an explicit <code>"Effect": "Deny"</code> matching the requested action and resource, the evaluation halts immediately and the request is REJECTED!</strong> Explicit Deny unconditionally overrides any number of Allows.</li>
          <li><strong>Step 3 (AWS Organizations SCP Check):</strong> If AWS Organizations is active, Service Control Policies are evaluated. If an SCP denies access or does not allow it, access is denied.</li>
          <li><strong>Step 4 (Resource-Based Policy Check):</strong> If a resource policy (e.g. S3 Bucket Policy) exists and contains an explicit Allow, the request is permitted (for same-account and cross-account requests).</li>
          <li><strong>Step 5 (IAM Permissions Boundary & Identity Policy Check):</strong> If the principal has an attached Permissions Boundary, both the boundary AND the Identity Policy must allow the action.</li>
          <li><strong>Step 6 (Final Determination):</strong> If at least one explicit Allow exists and zero explicit Denies exist, access is <strong>ALLOWED</strong>. Otherwise, it defaults back to <strong>DENY</strong>.</li>
        </ol>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">5. AWS Security Token Service (STS) & Temporary Credentials</h4>
        <p>
          When an EC2 instance, Lambda function, or federated engineer assumes an IAM Role, it calls the STS API:
        </p>
        <p><code>aws sts assume-role --role-arn arn:aws:iam::123456789012:role/DeployerRole --role-session-name ProductionSession</code></p>
        <p>
          STS returns three temporary credential components valid for a configurable duration (15 minutes to 12 hours):
        </p>
        <ul>
          <li><strong>AccessKeyId:</strong> Starting with prefix <code>ASIA...</code> (indicating temporary STS credentials, unlike long-term user keys starting with <code>AKIA...</code>).</li>
          <li><strong>SecretAccessKey:</strong> Ephemeral cryptographic secret.</li>
          <li><strong>SessionToken:</strong> Signed token string verifying credential authenticity with AWS endpoints.</li>
        </ul>
      </div>
    </div>

    <!-- 10M QUESTION 6: CLOUD DEPLOYMENT MODELS & MIGRATION -->
    <div class="accordion-item" data-marks="10m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[10 Marks]</strong> 6. Cloud Deployment Models & Enterprise Migration: Comprehensive Comparison of Public, Private, Hybrid (Cloud Bursting & Direct Connect), Community Clouds, Multi-Cloud Strategy, and the Gartner 6 R's Migration Framework.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <div class="tip-box" style="margin-bottom: 1rem;">
          <strong>🎯 University Marking Scheme (10 Marks Blueprint):</strong>
          <ul style="margin: 0.25rem 0 0 1.2rem; font-size: 0.85rem;">
            <li><strong>3 Marks:</strong> Architectural definitions, characteristics, and use cases of Public, Private, Hybrid, and Community clouds.</li>
            <li><strong>2 Marks:</strong> Hybrid Cloud Bursting mechanisms, dedicated interconnects (Direct Connect / ExpressRoute), and VPN tunnels.</li>
            <li><strong>2 Marks:</strong> Modern Multi-Cloud strategy drivers (vendor lock-in avoidance, regulatory compliance, fault tolerance).</li>
            <li><strong>2 Marks:</strong> Gartner 6 R's Cloud Migration Framework (Rehost, Replatform, Refactor, Repurchase, Retain, Retire).</li>
            <li><strong>1 Mark:</strong> 10-Parameter comparative evaluation matrix.</li>
          </ul>
        </div>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">1. The Four Primary Cloud Deployment Models</h4>
        <ol>
          <li>
            <strong>Public Cloud (e.g. AWS, Microsoft Azure, Google Cloud):</strong>
            <ul>
              <li><strong>Definition:</strong> Computing infrastructure owned and managed by a third-party cloud service provider, made available to multiple tenants over the public Internet.</li>
              <li><strong>Key Characteristics:</strong> Zero upfront CapEx, pay-as-you-go billing, infinite elastic scalability, multi-tenant resource sharing with logical virtualization isolation.</li>
              <li><strong>Ideal For:</strong> Startups, digital consumer applications, dynamic variable-workload web apps.</li>
            </ul>
          </li>
          <li>
            <strong>Private Cloud (Internal / Corporate Cloud):</strong>
            <ul>
              <li><strong>Definition:</strong> Cloud infrastructure provisioned for exclusive use by a single organization comprising multiple business units. Can be hosted on-premise (via OpenStack, VMware vSphere) or hosted by a third party.</li>
              <li><strong>Key Characteristics:</strong> Maximum data control, dedicated hardware (zero noisy neighbors), custom compliance governance, high initial Capital Expenditure (CapEx).</li>
              <li><strong>Ideal For:</strong> National defense agencies, central banks, proprietary intellectual property labs.</li>
            </ul>
          </li>
          <li>
            <strong>Hybrid Cloud (Orchestrated Integration):</strong>
            <ul>
              <li><strong>Definition:</strong> A composition of two or more distinct cloud infrastructures (private and public) bound together by standardized or proprietary technology that enables data and application portability.</li>
              <li><strong>Connectivity:</strong> Connected via high-throughput dedicated physical fiber lines (<strong>AWS Direct Connect</strong> / <strong>Azure ExpressRoute</strong>) backed up by encrypted IPsec VPN tunnels.</li>
              <li><strong>Cloud Bursting:</strong> An architectural pattern where mission-critical steady-state workloads run securely on the private cloud, but when demand exceeds 80% capacity during peak events, excess traffic dynamically "bursts" into the public cloud.</li>
            </ul>
          </li>
          <li>
            <strong>Community Cloud:</strong>
            <ul>
              <li><strong>Definition:</strong> Cloud infrastructure shared exclusively among several organizations having common missions, security requirements, regulatory compliance, or jurisdictional policies.</li>
              <li><strong>Example:</strong> Government agency clouds (US GovCloud), banking community networks (SWIFT cloud), medical research networks sharing genomic datasets.</li>
            </ul>
          </li>
        </ol>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">2. Modern Enterprise Multi-Cloud Strategy</h4>
        <p>
          A <strong>Multi-Cloud Strategy</strong> involves utilizing services from two or more distinct public cloud service providers (e.g. AWS for general computing, GCP for BigQuery/TensorFlow AI, and Azure for Microsoft 365 / Active Directory).
        </p>
        <ul>
          <li><strong>Avoiding Vendor Lock-in:</strong> By containerizing applications with Docker and Kubernetes, enterprises avoid being held hostage to proprietary vendor pricing increases.</li>
          <li><strong>Data Sovereignty & Legal Compliance:</strong> Compliance with GDPR (Europe) and India's Digital Personal Data Protection (DPDP) Act requires citizen data to remain geographically inside national borders. Multi-cloud ensures datacenters exist in required jurisdictions.</li>
          <li><strong>Disaster Resiliency:</strong> If an entire cloud provider suffers a global outage (e.g. global AWS IAM or DNS failure), DNS traffic automatically routes to Azure.</li>
        </ul>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">3. 10-Parameter Comparative Matrix</h4>
        <div class="table-wrapper">
          <table>
            <thead><tr><th>Parameter</th><th>Public Cloud</th><th>Private Cloud</th><th>Hybrid Cloud</th><th>Community Cloud</th></tr></thead>
            <tbody>
              <tr><td><strong>Infrastructure Ownership</strong></td><td>Third-Party Provider</td><td>Single Enterprise</td><td>Shared (Enterprise + Provider)</td><td>Consortium of Organizations</td></tr>
              <tr><td><strong>Infrastructure Location</strong></td><td>Provider Datacenter</td><td>On-Premise / Hosted</td><td>On-Premise & Provider</td><td>On-Premise or Provider</td></tr>
              <tr><td><strong>Financial Cost Model</strong></td><td>100% OpEx (Pay-per-use)</td><td>Heavy CapEx + Maintenance</td><td>Mixed (CapEx base + OpEx burst)</td><td>Shared Capital & OpEx</td></tr>
              <tr><td><strong>Scalability & Elasticity</strong></td><td>Virtually Infinite</td><td>Constrained by hardware</td><td>High (Burst to public cloud)</td><td>Moderate</td></tr>
              <tr><td><strong>Data Privacy & Security</strong></td><td>Logical isolation</td><td>Physical isolation</td><td>Tiered by data sensitivity</td><td>Shared vertical policies</td></tr>
              <tr><td><strong>Setup & Onboarding Time</strong></td><td>Instantaneous (Minutes)</td><td>Months (Hardware procurement)</td><td>Weeks to months</td><td>Weeks to months</td></tr>
              <tr><td><strong>Maintenance Burden</strong></td><td>Handled by CSP</td><td>Full enterprise responsibility</td><td>Shared responsibility</td><td>Shared consortium team</td></tr>
              <tr><td><strong>Network Latency</strong></td><td>Internet-dependent</td><td>Ultra-low LAN latency</td><td>Low over Direct Connect</td><td>Low over private lines</td></tr>
              <tr><td><strong>Tenant Density</strong></td><td>Multi-Tenant</td><td>Single-Tenant</td><td>Mixed</td><td>Multi-Tenant within community</td></tr>
              <tr><td><strong>Typical Enterprise</strong></td><td>Netflix, Airbnb, Startups</td><td>JPMorgan Chase, NSA</td><td>Mayo Clinic, Walmart</td><td>Interpol, European Police</td></tr>
            </tbody>
          </table>
        </div>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">4. Gartner 6 R's Cloud Migration Framework</h4>
        <ol>
          <li><strong>Rehost ("Lift and Shift"):</strong> Migrating applications from on-premise servers directly to cloud VMs (EC2) without modifying code or architecture. Fastest migration with minimal risk, but fails to exploit cloud-native elasticity.</li>
          <li><strong>Replatform ("Lift, Tinker and Shift"):</strong> Making targeted optimizations (e.g. migrating from on-premise self-hosted Oracle DB to AWS RDS managed database) without changing core application business logic.</li>
          <li><strong>Refactor / Re-architect:</strong> Completely re-architecting the monolithic application into cloud-native microservices, serverless functions (AWS Lambda), and containerized Kubernetes clusters. Delivers maximum elasticity and lowest operational costs.</li>
          <li><strong>Repurchase ("Drop and Shop"):</strong> Abandoning legacy in-house custom software in favor of a modern SaaS solution (e.g. migrating custom on-premise CRM to Salesforce, or legacy Exchange to Microsoft 365).</li>
          <li><strong>Retain:</strong> Keeping applications on-premise that have strict low-latency hardware dependencies, recent capital investments, or regulatory constraints.</li>
          <li><strong>Retire:</strong> Identifying redundant, obsolete, or underutilized applications during discovery and decommissioning them, saving 10% to 20% of enterprise IT budgets.</li>
        </ol>
      </div>
    </div>

    <!-- 10M QUESTION 7: 3-TIER ARCHITECTURE & HA -->
    <div class="accordion-item" data-marks="10m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[10 Marks]</strong> 7. Enterprise Multi-Server 3-Tier Web Architecture: Layer Anatomy, Layer 4 (NLB) vs Layer 7 (ALB) Load Balancing, High Availability Math & SLA Downtime Calculations, and Disaster Recovery Strategies (RTO vs RPO).</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <div class="tip-box" style="margin-bottom: 1rem;">
          <strong>🎯 University Marking Scheme (10 Marks Blueprint):</strong>
          <ul style="margin: 0.25rem 0 0 1.2rem; font-size: 0.85rem;">
            <li><strong>3 Marks:</strong> Detailed VPC architectural diagram & component breakdown of Presentation, Application, and Persistence tiers.</li>
            <li><strong>3 Marks:</strong> Technical comparison of Layer 4 (Transport / NLB) vs Layer 7 (Application / ALB) load balancing mechanisms.</li>
            <li><strong>2 Marks:</strong> High Availability mathematical formulas (Serial vs Parallel Availability calculations) and SLA "Nines" table.</li>
            <li><strong>2 Marks:</strong> Disaster recovery strategies (Backup & Restore, Pilot Light, Warm Standby, Multi-Region Active-Active) with RTO and RPO trade-offs.</li>
          </ul>
        </div>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">1. Multi-Server 3-Tier Architectural Anatomy</h4>
        <p>
          Enterprise web applications decouple services into three independent layers to achieve fault isolation, independent scaling, and defense-in-depth:
        </p>
        <ul>
          <li>
            <strong>Tier 1: Presentation / Web Tier (Public Subnet):</strong>
            <ul>
              <li>Directly accessible via Internet Gateway (IGW).</li>
              <li>Fronted by an Internet-facing <strong>Application Load Balancer (ALB)</strong> terminating SSL/TLS 1.3 certificates.</li>
              <li>Runs reverse proxies and static web servers (Nginx/Apache) serving cached React/HTML bundles. Zero business logic or database credentials exist in this tier.</li>
            </ul>
          </li>
          <li>
            <strong>Tier 2: Application / Logic Tier (Private Subnet):</strong>
            <ul>
              <li>Isolated from the public Internet; has no public IP addresses. Outbound internet updates occur via a <strong>NAT Gateway</strong>.</li>
              <li>Runs backend APIs (Node.js, Spring Boot, Python) inside an <strong>Auto Scaling Group (ASG)</strong> that dynamically expands and contracts based on CPU or request queue metrics.</li>
              <li>Utilizes an in-memory <strong>Redis / Memcached</strong> cluster to cache expensive database queries and session states.</li>
            </ul>
          </li>
          <li>
            <strong>Tier 3: Database / Persistence Tier (Isolated Subnet):</strong>
            <ul>
              <li>Completely locked down with zero inbound internet route. Accepts TCP traffic exclusively on port 3306/5432 originating from Tier 2 security groups.</li>
              <li>Configured in a <strong>Multi-AZ High Availability</strong> topology: Primary Master instance in AZ-1 handles synchronous writes and replicates asynchronously to Standby Master in AZ-2 and Read-Replicas in AZ-3.</li>
            </ul>
          </li>
        </ul>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">2. Layer 4 vs Layer 7 Load Balancing Deep-Dive</h4>
        <div class="table-wrapper">
          <table>
            <thead><tr><th>Capability</th><th>Layer 4 Load Balancing (Network Load Balancer - NLB)</th><th>Layer 7 Load Balancing (Application Load Balancer - ALB)</th></tr></thead>
            <tbody>
              <tr><td><strong>OSI Layer</strong></td><td>Transport Layer (TCP / UDP / TLS)</td><td>Application Layer (HTTP / HTTPS / gRPC / WebSockets)</td></tr>
              <tr><td><strong>Packet Inspection</strong></td><td>Zero payload inspection; routes based strictly on IP & Port.</td><td>Deep packet inspection; reads HTTP headers, URLs, cookies.</td></tr>
              <tr><td><strong>Routing Decisions</strong></td><td>Static source IP / Port hash.</td><td>Path routing (<code>/api/*</code> vs <code>/static/*</code>), Host routing, Query params.</td></tr>
              <tr><td><strong>Latency & Throughput</strong></td><td>Ultra-low sub-millisecond latency; millions of RPS.</td><td>Low latency (several milliseconds for header parsing).</td></tr>
              <tr><td><strong>Static IP Support</strong></td><td>Provides a dedicated Elastic Static IP per AZ.</td><td>Dynamic DNS hostname (no static public IP).</td></tr>
              <tr><td><strong>SSL/TLS Handling</strong></td><td>High-speed TLS pass-through or hardware termination.</td><td>SSL termination, SNI support, automatic ACM cert renewal.</td></tr>
              <tr><td><strong>Ideal Use Case</strong></td><td>Gaming servers, IoT telemetry, high-volume financial trades.</td><td>Modern web applications, REST APIs, microservices.</td></tr>
            </tbody>
          </table>
        </div>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">3. High Availability Mathematics & SLA Calculations</h4>
        <p>
          High Availability (HA) measures the percentage of time a system remains operational and accessible.
        </p>
        <p><strong>Fundamental Availability Formula:</strong></p>
        $$A = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} \times 100\%$$
        <p>Where <strong>MTBF</strong> = Mean Time Between Failures, and <strong>MTTR</strong> = Mean Time To Repair.</p>

        <p><strong>System Composition Calculations:</strong></p>
        <ul>
          <li><strong>Serial Components (Chain Dependency):</strong> If any component fails, the entire system fails. Overall availability is the product of individual availabilities:
            $$A_{\text{system}} = A_1 \times A_2 \times A_3$$
            <em>Example:</em> If Web Tier is 99% (0.99) and DB Tier is 99% (0.99), total availability is $0.99 \times 0.99 = 98.01\%$!
          </li>
          <li><strong>Parallel Components (Redundancy):</strong> Redundant components running in parallel fail ONLY if both fail simultaneously:
            $$A_{\text{parallel}} = 1 - (1 - A_1) \times (1 - A_2)$$
            <em>Example:</em> Two 99% redundant servers in parallel: $1 - (0.01 \times 0.01) = 1 - 0.0001 = 99.99\%$ (Four Nines)!
          </li>
        </ul>

        <div class="table-wrapper">
          <table>
            <thead><tr><th>SLA Level</th><th>Availability %</th><th>Allowed Downtime per Year</th><th>Allowed Downtime per Month</th></tr></thead>
            <tbody>
              <tr><td>Two Nines</td><td>99.0%</td><td>3 days, 15 hours, 39 minutes</td><td>7 hours, 18 minutes</td></tr>
              <tr><td>Three Nines</td><td>99.9%</td><td>8 hours, 45 minutes, 57 seconds</td><td>43 minutes, 49 seconds</td></tr>
              <tr><td>Four Nines</td><td>99.99%</td><td>52 minutes, 35 seconds</td><td>4 minutes, 23 seconds</td></tr>
              <tr><td>Five Nines</td><td>99.999%</td><td>5 minutes, 15 seconds</td><td>26 seconds</td></tr>
            </tbody>
          </table>
        </div>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">4. Disaster Recovery Strategies (RTO vs RPO Trade-offs)</h4>
        <p>
          Disaster recovery architectures are defined by two strict metrics:
        </p>
        <ul>
          <li><strong>Recovery Time Objective (RTO):</strong> The maximum acceptable duration of system downtime before service is restored.</li>
          <li><strong>Recovery Point Objective (RPO):</strong> The maximum acceptable duration of data loss measured in time (e.g. 1 hour of lost transactions).</li>
        </ul>

        <div class="table-wrapper">
          <table>
            <thead><tr><th>Strategy</th><th>RTO</th><th>RPO</th><th>Cost Factor</th><th>Mechanism</th></tr></thead>
            <tbody>
              <tr><td><strong>1. Backup & Restore</strong></td><td>Hours to days</td><td>24 hours</td><td>Lowest ($)</td><td>Nightly snapshots shipped to remote S3; rebuild on demand.</td></tr>
              <tr><td><strong>2. Pilot Light</strong></td><td>Minutes to hours</td><td>Minutes</td><td>Low ($$)</td><td>Core DB constantly replicates to secondary region; compute servers kept stopped.</td></tr>
              <tr><td><strong>3. Warm Standby</strong></td><td>Seconds to minutes</td><td>Seconds</td><td>Moderate ($$$)</td><td>Scaled-down minimal fleet running 24/7 in secondary region; auto-scales up on failover.</td></tr>
              <tr><td><strong>4. Multi-Region Active-Active</strong></td><td>Near Zero (Instant)</td><td>Zero</td><td>Highest ($$$$)</td><td>Full production capacity in 2+ regions simultaneously serving traffic via Route 53.</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- 10M QUESTION 8: CLOUD STORAGE ARCHITECTURES -->
    <div class="accordion-item" data-marks="10m">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <span><strong>[10 Marks]</strong> 8. Cloud Storage Architectures: Block Storage vs Object Storage vs File Storage, Distributed Consistency (CAP Theorem), and the Mathematics of 11-Nines (99.999999999%) S3 Durability.</span>
        <span class="accordion-icon">▼</span>
      </div>
      <div class="accordion-content">
        <div class="tip-box" style="margin-bottom: 1rem;">
          <strong>🎯 University Marking Scheme (10 Marks Blueprint):</strong>
          <ul style="margin: 0.25rem 0 0 1.2rem; font-size: 0.85rem;">
            <li><strong>3 Marks:</strong> Architectural mechanisms, protocols, and data structures of Block Storage, Object Storage, and File Storage.</li>
            <li><strong>2 Marks:</strong> 8-Parameter comparative matrix across all three storage paradigms.</li>
            <li><strong>3 Marks:</strong> Mathematical explanation of 11-Nines (99.999999999%) durability and Erasure Coding (Reed-Solomon).</li>
            <li><strong>2 Marks:</strong> Distributed Consistency, Eric Brewer's CAP Theorem, and S3 Lifecycle Automation tiers.</li>
          </ul>
        </div>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">1. The Three Primary Cloud Storage Paradigms</h4>
        <ol>
          <li>
            <strong>Block Storage (e.g. AWS Elastic Block Store - EBS, Azure Managed Disk):</strong>
            <ul>
              <li><strong>Mechanism:</strong> Data is split into fixed-size raw blocks (e.g. 4 KB or 512 bytes), each identified by a unique sector address. The storage volume acts as a raw physical disk drive mounted over high-speed protocols (iSCSI, Fibre Channel, NVMe-oF).</li>
              <li><strong>Characteristics:</strong> Ultra-low sub-millisecond latency, high Input/Output Operations Per Second (IOPS), supports in-place random byte modifications.</li>
              <li><strong>Best Use Case:</strong> OS boot drives, ACID relational databases (Oracle, PostgreSQL, MySQL).</li>
            </ul>
          </li>
          <li>
            <strong>Object Storage (e.g. AWS S3, Google Cloud Storage, Azure Blob):</strong>
            <ul>
              <li><strong>Mechanism:</strong> Data is stored as complete, self-contained, immutable binary objects in a flat namespace (buckets). Each object consists of three elements: <strong>Data Payload</strong>, <strong>Custom Metadata</strong>, and a globally unique <strong>Key</strong> (URI).</li>
              <li><strong>Access:</strong> Accessed exclusively over standard HTTP/HTTPS REST APIs using verbs: <code>GET</code>, <code>PUT</code>, <code>DELETE</code>, <code>HEAD</code>. No folders exist physically (delimiters like <code>/</code> are simulated prefix keys).</li>
              <li><strong>Characteristics:</strong> Massive petabyte/exabyte scalability, immutable (updates require complete replacement of the object), high latency compared to block storage, but virtually infinite concurrent read throughput.</li>
              <li><strong>Best Use Case:</strong> Media streaming, static website hosting, big data data lakes, long-term backups.</li>
            </ul>
          </li>
          <li>
            <strong>File Storage (e.g. AWS Elastic File System - EFS, Azure Files):</strong>
            <ul>
              <li><strong>Mechanism:</strong> Organizes data in a classic hierarchical folder-and-file directory tree adhering to POSIX filesystem standards. Mounted simultaneously across thousands of compute nodes via standard network protocols (<strong>NFSv4</strong> for Linux, <strong>SMB/CIFS</strong> for Windows).</li>
              <li><strong>Characteristics:</strong> Supports concurrent multi-server read/write access, distributed file locking, automated elasticity.</li>
              <li><strong>Best Use Case:</strong> Shared web application assets (WordPress CMS), corporate shared network drives, distributed machine learning training datasets.</li>
            </ul>
          </li>
        </ol>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">2. 8-Parameter Cloud Storage Comparison Matrix</h4>
        <div class="table-wrapper">
          <table>
            <thead><tr><th>Parameter</th><th>Block Storage (EBS)</th><th>Object Storage (S3)</th><th>File Storage (EFS)</th></tr></thead>
            <tbody>
              <tr><td><strong>Data Structure</strong></td><td>Fixed raw addressable blocks</td><td>Flat namespace with metadata</td><td>Hierarchical directory tree</td></tr>
              <tr><td><strong>Access Protocol</strong></td><td>iSCSI, Fibre Channel, NVMe-oF</td><td>HTTP / HTTPS REST APIs</td><td>NFSv4, SMB, CIFS</td></tr>
              <tr><td><strong>Latency & IOPS</strong></td><td>Ultra-low (Sub-millisecond)</td><td>Moderate (10 to 50 ms)</td><td>Low to moderate (1 to 5 ms)</td></tr>
              <tr><td><strong>Concurrent Sharing</strong></td><td>Single instance only (Multi-attach rare)</td><td>Millions of concurrent clients</td><td>Thousands of concurrent instances</td></tr>
              <tr><td><strong>Modification Method</strong></td><td>In-place byte-level modification</td><td>Whole object overwrite (Immutable)</td><td>File-level byte appending & locking</td></tr>
              <tr><td><strong>Storage Scalability</strong></td><td>Gigabytes to Terabytes per volume</td><td>Limitless (Petabytes to Exabytes)</td><td>Elastic auto-growing (Petabytes)</td></tr>
              <tr><td><strong>Cost per Gigabyte</strong></td><td>Highest ($0.08 to $0.125 / GB / mo)</td><td>Lowest ($0.023 / GB / mo)</td><td>Moderate ($0.30 / GB / mo)</td></tr>
              <tr><td><strong>Primary Cloud Services</strong></td><td>AWS EBS, Azure Disk, GCP PD</td><td>AWS S3, Azure Blob, Google GCS</td><td>AWS EFS, Azure Files, Google Filestore</td></tr>
            </tbody>
          </table>
        </div>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">3. The Mathematics of 11-Nines (99.999999999%) S3 Durability</h4>
        <p>
          AWS S3 is engineered to provide <strong>11 Nines (99.999999999%)</strong> of annual data durability.
        </p>
        <p><strong>What Does 11 Nines Mean Mathematically?</strong></p>
        <ul>
          <li>If an enterprise stores <strong>10,000,000 (10 million) objects</strong> in AWS S3, statistically you can expect to lose a single object once every <strong>10,000 years</strong>!</li>
          <li>Annual probability of losing an object is $1 - 0.99999999999 = 0.00000000001 = 10^{-11}$.</li>
        </ul>
        <p><strong>Engineering Implementation:</strong></p>
        <ul>
          <li><strong>Multi-AZ Geodistribution:</strong> S3 redundantly replicates data across at least <strong>three physically separated Availability Zones (AZs)</strong> located tens of kilometers apart within a region, each with independent power, cooling, and network backbones.</li>
          <li><strong>Erasure Coding (Reed-Solomon $k+m$):</strong> An object is partitioned into $k$ data fragments and $m$ parity fragments distributed across separate storage racks. Even if $m$ entire storage nodes or an entire datacenter completely burns down, the object is mathematically reconstructed from the remaining fragments in milliseconds with automated self-healing background daemons.</li>
        </ul>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">4. Distributed Consistency & Eric Brewer's CAP Theorem</h4>
        <p>
          Eric Brewer's <strong>CAP Theorem</strong> proves that a distributed storage system can guarantee at most two of the following three guarantees simultaneously:
        </p>
        <ul>
          <li><strong>Consistency (C):</strong> Every read receives the most recent write or an error.</li>
          <li><strong>Availability (A):</strong> Every non-failing node returns a successful response without timeout.</li>
          <li><strong>Partition Tolerance (P):</strong> The system continues operating despite arbitrary network dropped packets between nodes. Since network partitions are inevitable in physical cables, distributed cloud storage must ALWAYS select <strong>Partition Tolerance (P)</strong>, forcing a trade-off between <strong>CP</strong> (HBase, MongoDB) or <strong>AP</strong> (Cassandra, CouchDB).</li>
          <li><strong>AWS S3 Strong Consistency:</strong> In December 2020, AWS upgraded S3 to deliver <strong>Strong Read-After-Write Consistency</strong> for all PUT, LIST, and DELETE operations with zero latency penalty and zero additional cost.</li>
        </ul>

        <h4 style="color: var(--accent); margin: 1rem 0 0.4rem;">5. AWS S3 Storage Tiers & Automated Lifecycle Policies</h4>
        <ul>
          <li><strong>S3 Standard:</strong> Frequent access; high throughput; 99.99% availability.</li>
          <li><strong>S3 Standard-Infrequent Access (IA):</strong> 50% cheaper storage; retrieval fee per GB.</li>
          <li><strong>S3 Glacier Flexible Retrieval:</strong> Archive storage; retrieval in 1 minute to 5 hours.</li>
          <li><strong>S3 Glacier Deep Archive:</strong> Lowest cost ($0.00099/GB/month); retrieval in 12 to 48 hours; replaces magnetic tape vaults.</li>
        </ul>
      </div>
    </div>
"""

def update_qbank():
    qbank_file = "d:/Downloads/cc/parts_qbank.py"
    with open(qbank_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the 10 MARKS section
    marker = "<!-- ==================== 10 MARKS QUESTIONS ==================== -->"
    end_marker = "  </div>\n</div>\n\"\"\""

    if marker not in content:
        print("Could not find marker in parts_qbank.py")
        return

    # Replace from marker to end of qbankList
    idx_start = content.find(marker)
    new_content = content[:idx_start] + Q10M_HTML.strip() + "\n  </div>\n</div>\n\"\"\""

    with open(qbank_file, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("Successfully expanded parts_qbank.py with 8 comprehensive 10-mark questions!")

if __name__ == "__main__":
    update_qbank()
