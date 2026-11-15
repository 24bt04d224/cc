# -*- coding: utf-8 -*-
from parts_svg import SVG_HYPERVISOR, SVG_VM_VS_CONTAINER, SVG_OPENSTACK, SVG_SDN

TAB_UNIT4_HTML = f"""
<div id="unit4" class="tab-pane">
  <div class="hero-banner" style="border-color: rgba(239, 68, 68, 0.4);">
    <div class="hero-header">
      <div class="hero-title">Unit 4: Virtualization Technologies & Cloud Tools</div>
      <div class="hero-badge-group">
        <span class="badge badge-priority">25% Exam Weightage</span>
        <span class="badge">10 Contact Hours</span>
        <span class="badge badge-accent">Highest Scoring Unit</span>
      </div>
    </div>
    <p class="hero-desc">
      Explore all 9 major topics of Unit 4 in structured hierarchical dropdowns.
      Click on any <strong>Main Head</strong> to reveal sub-topics, then click on a <strong>Sub-Topic</strong> to view full detailed descriptions, diagrams, and exam tips.
    </p>
  </div>

  <!-- Unit 4 Dropdown Controls Bar -->
  <div class="unit-controls-bar">
    <div class="unit-controls-left">
      <span style="font-weight: 700; font-size: 0.88rem; color: var(--accent);">📌 Jump to Topic:</span>
      <select class="topic-select" onchange="jumpToTopic('unit4', this)">
        <option value="">Select a Topic...</option>
        <option value="u4-t1">Topic 1: Hypervisors & Reference Model</option>
        <option value="u4-t2">Topic 2: Virtual Machines (VMs)</option>
        <option value="u4-t3">Topic 3: Containers and Docker</option>
        <option value="u4-t4">Topic 4: Kubernetes (K8s)</option>
        <option value="u4-t5">Topic 5: Cloud Management Platforms (CMPs)</option>
        <option value="u4-t6">Topic 6: OpenStack Architecture & 9 Services</option>
        <option value="u4-t7">Topic 7: Apache CloudStack</option>
        <option value="u4-t8">Topic 8: Cloud Storage (Block, Object, File)</option>
        <option value="u4-t9">Topic 9: Cloud Networking (SDN, VPN, LB, CDN)</option>
      </select>
    </div>
    <div class="unit-controls-right">
      <button class="btn btn-sm btn-primary" onclick="expandAllInUnit('unit4')">📂 Expand All</button>
      <button class="btn btn-sm" onclick="collapseAllInUnit('unit4')">📁 Collapse All</button>
    </div>
  </div>

  <!-- ==================== TOPIC 1 ==================== -->
  <div class="main-topic-card" id="u4-t1">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🖥️</span>
        <span class="main-topic-title">Topic 1: Hypervisors — Concepts, Types & Reference Model</span>
        <span class="badge badge-priority">Very High Priority</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>5 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 1.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.1 What is a Hypervisor? & Key Responsibilities</span>
          </div>
          <span class="sub-topic-badge">Definition</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">Exam-Ready Definition: Hypervisor / Virtual Machine Monitor (VMM)</div>
            A <strong>Hypervisor</strong>, also known as a <strong>Virtual Machine Monitor (VMM)</strong>, is a specialized software layer, firmware, or hardware that allows multiple operating systems to run concurrently on a single physical host machine by abstracting physical CPU, memory, storage, and I/O resources.
          </div>
          <h5 style="margin-top: 1rem; color: var(--text-primary);">Main Responsibilities of a Hypervisor (Table from Slides):</h5>
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Responsibility</th><th>Detailed Explanation</th></tr></thead>
              <tbody>
                <tr><td><strong>VM Creation</strong></td><td>Instantiates, boots, and configures new virtual machine instances.</td></tr>
                <tr><td><strong>CPU Allocation</strong></td><td>Schedules and divides physical CPU cores into virtual cores (vCPUs).</td></tr>
                <tr><td><strong>Memory Allocation</strong></td><td>Dynamically partitions physical RAM pages among competing guest VMs.</td></tr>
                <tr><td><strong>Storage Management</strong></td><td>Allocates virtual disks (vDisks) from physical hard drives or SAN.</td></tr>
                <tr><td><strong>Network Management</strong></td><td>Provisions virtual switches (vSwitch) and virtual NICs for guest communication.</td></tr>
                <tr><td><strong>Isolation Enforcement</strong></td><td>Strictly isolates VM memory spaces so one VM cannot peek into another.</td></tr>
                <tr><td><strong>VM Execution Control</strong></td><td>Monitors instruction flow, state changes, pausing, snapshots, and migration.</td></tr>
              </tbody>
            </table>
          </div>
          <div class="tip-box">
            <strong>Exam Summary:</strong> Hypervisor = <em>Executive Manager of Virtual Machines</em>.
          </div>
        </div>
      </div>

      <!-- Sub-topic 1.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.2 Type 1 Hypervisor (Bare-Metal) — Architecture, Examples, Pros & Cons</span>
          </div>
          <span class="sub-topic-badge">Architecture</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">Definition: Type 1 Hypervisor</div>
            A <strong>Type 1 Hypervisor</strong> runs directly on the host's physical bare-metal hardware without an intermediate host operating system. It possesses direct hardware control.
          </div>
          <p><strong>Architecture Stack:</strong> Physical Hardware &rarr; Type 1 Hypervisor &rarr; Guest Virtual Machines (OS + Apps).</p>
          <div class="diagram-container">
            {SVG_HYPERVISOR}
            <div class="diagram-caption">Figure 4.1: Type 1 (Bare-Metal) vs Type 2 (Hosted) Hypervisor Architecture.</div>
          </div>
          <div class="grid-2">
            <div>
              <h5 style="color: var(--success);">Advantages:</h5>
              <ul>
                <li><strong>Maximum Performance:</strong> Direct hardware execution without host OS overhead.</li>
                <li><strong>Robust Security & Isolation:</strong> Smaller attack surface; no underlying host OS to hack.</li>
                <li><strong>High Resource Efficiency:</strong> Dedicated strictly to running guest VMs.</li>
              </ul>
            </div>
            <div>
              <h5 style="color: var(--danger);">Disadvantages & Use Cases:</h5>
              <ul>
                <li><strong>Setup Complexity:</strong> Requires dedicated physical server hardware.</li>
                <li><strong>Specialized Management:</strong> Configured via remote management consoles.</li>
                <li><strong>Industry Examples:</strong> VMware ESXi, Microsoft Hyper-V, KVM, Xen.</li>
                <li><strong>Ideal For:</strong> Enterprise cloud datacenters (AWS, Azure, GCP).</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 1.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.3 Type 2 Hypervisor (Hosted) — Architecture, Examples, Pros & Cons</span>
          </div>
          <span class="sub-topic-badge">Architecture</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">Definition: Type 2 Hypervisor</div>
            A <strong>Type 2 Hypervisor</strong> runs as an application process on top of a conventional host operating system (e.g. Windows 11, macOS, Ubuntu Linux).
          </div>
          <p><strong>Architecture Stack:</strong> Physical Hardware &rarr; Host OS &rarr; Type 2 Hypervisor &rarr; Guest Virtual Machines.</p>
          <div class="grid-2">
            <div>
              <h5 style="color: var(--success);">Advantages:</h5>
              <ul>
                <li><strong>Ease of Installation:</strong> Installs like any standard desktop software (.exe / .dmg).</li>
                <li><strong>Convenient Host Integration:</strong> Easily share clipboard, folders, and USB devices.</li>
                <li><strong>Cost Effective:</strong> Runs on ordinary laptops without dedicated servers.</li>
              </ul>
            </div>
            <div>
              <h5 style="color: var(--danger);">Disadvantages & Examples:</h5>
              <ul>
                <li><strong>Performance Penalty:</strong> System calls pass through guest OS &rarr; hypervisor &rarr; host OS &rarr; hardware.</li>
                <li><strong>Single Point of Host Failure:</strong> If host OS crashes, all guest VMs crash instantly.</li>
                <li><strong>Industry Examples:</strong> Oracle VirtualBox, VMware Workstation, VMware Fusion.</li>
                <li><strong>Ideal For:</strong> Software testing, student labs, desktop experimentation.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 1.4 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.4 Difference between Type 1 and Type 2 Hypervisors (7-Mark Matrix)</span>
          </div>
          <span class="sub-topic-badge">7 Marks</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr><th>Basis</th><th>Type 1 (Bare-Metal)</th><th>Type 2 (Hosted)</th></tr>
              </thead>
              <tbody>
                <tr><td><strong>Installation</strong></td><td>Directly on bare-metal physical hardware</td><td>On top of existing host OS as an application</td></tr>
                <tr><td><strong>Host OS</strong></td><td>Not required; acts as specialized micro-kernel</td><td>Mandatory (Windows, Linux, macOS)</td></tr>
                <tr><td><strong>Performance</strong></td><td>Near-native, high throughput, ultra-low latency</td><td>Lower performance due to dual OS scheduling overhead</td></tr>
                <tr><td><strong>Security</strong></td><td>Maximum isolation; minimal attack surface</td><td>Vulnerable to flaws in the host OS</td></tr>
                <tr><td><strong>Resource Access</strong></td><td>Direct hardware device driver control</td><td>Indirect; mediated through host OS system calls</td></tr>
                <tr><td><strong>Complexity</strong></td><td>Requires dedicated enterprise server setup</td><td>Simple one-click desktop installer</td></tr>
                <tr><td><strong>Examples</strong></td><td>VMware ESXi, Hyper-V, KVM, Xen</td><td>Oracle VirtualBox, VMware Workstation</td></tr>
              </tbody>
            </table>
          </div>
          <div class="tip-box">
            <strong>Memory Trick:</strong> Type 1 = <em>Hardware First</em> | Type 2 = <em>OS First</em>.
          </div>
        </div>
      </div>

      <!-- Sub-topic 1.5 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>1.5 Hypervisor Reference Model (Dispatcher, Allocator, Interpreter)</span>
          </div>
          <span class="sub-topic-badge">PPT Pages 9-10</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p>The <strong>Hypervisor Reference Model</strong> breaks down the internal instruction-handling mechanisms of a Virtual Machine Monitor (VMM) into 3 vital internal sub-modules:</p>
          <div class="grid-3" style="margin-top: 1rem;">
            <div class="subcard" style="border-top: 3px solid #38bdf8;">
              <h4 style="color: #38bdf8;">1. Dispatcher</h4>
              <p>Acts as the central entry gate of the monitor. Intercepts incoming instructions issued by guest VMs and routes them to the appropriate handler routines (Allocator or Interpreter).</p>
            </div>
            <div class="subcard" style="border-top: 3px solid #10b981;">
              <h4 style="color: #10b981;">2. Allocator</h4>
              <p>Decides how system resources (CPU slices, memory pages, I/O bandwidth) are allocated to each requesting virtual machine without starving others.</p>
            </div>
            <div class="subcard" style="border-top: 3px solid #f59e0b;">
              <h4 style="color: #f59e0b;">3. Interpreter</h4>
              <p>Contains trap-and-emulate routines that safely execute privileged instructions (e.g. CPU control register edits) without compromising host stability.</p>
            </div>
          </div>
          <div class="tip-box" style="margin-top: 1rem;">
            <strong>Memory Formula:</strong> Dispatcher = <em>Directs</em> | Allocator = <em>Allocates</em> | Interpreter = <em>Interprets</em>.
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 2 ==================== -->
  <div class="main-topic-card" id="u4-t2">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">📦</span>
        <span class="main-topic-title">Topic 2: Virtual Machines (VMs) & Cloud Virtualization</span>
        <span class="badge badge-accent">Core Concept</span>
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
            <span>2.1 Definition & Virtual Hardware Components of a VM</span>
          </div>
          <span class="sub-topic-badge">Fundamentals</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">What is a Virtual Machine?</div>
            A <strong>Virtual Machine (VM)</strong> is a tightly isolated software container that runs its own operating system and applications just as if it were a physical computer.
          </div>
          <h5 style="margin-top: 1rem; color: var(--text-primary);">Virtual Hardware Components (Virtual Box / VM Instance):</h5>
          <ul>
            <li><strong>vCPU (Virtual CPU):</strong> Logical execution units mapped to physical processor cores.</li>
            <li><strong>vRAM (Virtual Memory):</strong> Isolated address spaces allocated from host RAM.</li>
            <li><strong>Virtual Storage (vDisk):</strong> Represented as files on host storage (e.g. .vmdk, .vdi, .qcow2).</li>
            <li><strong>vNIC (Virtual Network Interface):</strong> Virtual network adapters with dedicated MAC addresses.</li>
            <li><strong>Guest OS:</strong> The operating system installed and executed inside the virtual machine.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 2.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>2.2 System Virtual Machines vs Process Virtual Machines</span>
          </div>
          <span class="sub-topic-badge">Taxonomy</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="grid-2">
            <div class="subcard">
              <h4>A. System Virtual Machine</h4>
              <p>Provides a complete virtual system platform that supports the execution of a full operating system.</p>
              <ul style="margin-top: 0.5rem; font-size: 0.88rem;">
                <li>Allows physical resources of one host machine to be shared among multiple VMs.</li>
                <li><strong>Example:</strong> An Ubuntu Linux VM running inside VirtualBox or an AWS EC2 instance.</li>
              </ul>
            </div>
            <div class="subcard">
              <h4>B. Process Virtual Machine</h4>
              <p>Designed to execute a single application process and masks hardware differences to provide a platform-independent runtime.</p>
              <ul style="margin-top: 0.5rem; font-size: 0.88rem;">
                <li>Exists only for the duration of that single application process.</li>
                <li><strong>Example:</strong> Java Virtual Machine (JVM), .NET Common Language Runtime (CLR).</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 2.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>2.3 5 Types of Virtualization in Cloud Computing</span>
          </div>
          <span class="sub-topic-badge">Cloud Types</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Type</th><th>Meaning & Mechanism</th><th>Industry Example</th></tr></thead>
              <tbody>
                <tr><td><strong>Server Virtualization</strong></td><td>Partitioning one physical server into multiple isolated VMs.</td><td>AWS EC2, VMware vSphere</td></tr>
                <tr><td><strong>Storage Virtualization</strong></td><td>Pooling multiple physical storage arrays into a single logical pool.</td><td>Ceph, SAN Storage Pools</td></tr>
                <tr><td><strong>Network Virtualization</strong></td><td>Decoupling network devices into virtual switches, VLANs, and VXLANs.</td><td>Amazon VPC, Open vSwitch</td></tr>
                <tr><td><strong>Desktop Virtualization (VDI)</strong></td><td>Hosting desktop environments centrally on cloud servers for thin clients.</td><td>Amazon WorkSpaces, Citrix</td></tr>
                <tr><td><strong>Application Virtualization</strong></td><td>Encapsulating applications from underlying OS for isolated execution.</td><td>Docker Containers, App-V</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 3 ==================== -->
  <div class="main-topic-card" id="u4-t3">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🐳</span>
        <span class="main-topic-title">Topic 3: Containers and Docker Platform</span>
        <span class="badge badge-priority">High Priority (7 Marks)</span>
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
            <span>3.1 Containers vs Virtual Machines (Architecture & Comparison)</span>
          </div>
          <span class="sub-topic-badge">7 Marks</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">What is a Container?</div>
            A <strong>Container</strong> is a lightweight, isolated user-space environment that packages an application together with its binaries, libraries, and dependencies, running as an isolated process directly on the host operating system kernel.
          </div>
          <div class="diagram-container">
            {SVG_VM_VS_CONTAINER}
            <div class="diagram-caption">Figure 4.2: Architectural difference between Virtual Machines (Guest OS) and Containers (Shared Kernel).</div>
          </div>
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Dimension</th><th>Virtual Machine</th><th>Docker Container</th></tr></thead>
              <tbody>
                <tr><td><strong>OS Kernel</strong></td><td>Boots a full independent guest kernel per VM</td><td>Shares the host OS kernel directly</td></tr>
                <tr><td><strong>Startup Time</strong></td><td>Minutes (full hardware & OS boot sequence)</td><td>Milliseconds to seconds (process spawn)</td></tr>
                <tr><td><strong>Storage Size</strong></td><td>Gigabytes (2 GB to 20 GB)</td><td>Megabytes (10 MB to 200 MB)</td></tr>
                <tr><td><strong>Resource Overhead</strong></td><td>High RAM and CPU reservation</td><td>Extremely low; uses only active process memory</td></tr>
                <tr><td><strong>Isolation Mechanism</strong></td><td>Hardware virtualization via hypervisor rings</td><td>Linux Namespaces & Control Groups (cgroups)</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Sub-topic 3.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>3.2 Docker Architecture & 4 Core Building Blocks</span>
          </div>
          <span class="sub-topic-badge">Deep Dive</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p>Docker operates on a client-server architecture consisting of the Docker Client (CLI), Docker Daemon (<code>dockerd</code>), and Docker Registries.</p>
          <div class="grid-2" style="margin-top: 1rem;">
            <div class="subcard">
              <h4>1. Dockerfile</h4>
              <p>A declarative text file containing instructions to construct an image.</p>
              <pre><code>FROM python:3.12-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]</code></pre>
            </div>
            <div class="subcard">
              <h4>2. Docker Image</h4>
              <p>An immutable, read-only template built in stacked layers representing file modifications. Used as the blueprint for containers.</p>
              <h4 style="margin-top: 1rem;">3. Docker Container</h4>
              <p>A runnable, stateful instance of an image with a thin read-write top layer.</p>
              <h4 style="margin-top: 1rem;">4. Docker Hub</h4>
              <p>A centralized public/private registry to push, store, and pull container images.</p>
            </div>
          </div>
          <div class="tip-box" style="margin-top: 1rem;">
            <strong>Analogy:</strong> Dockerfile = <em>Recipe</em> | Docker Image = <em>Packaged Food</em> | Docker Container = <em>Served Dish</em> | Docker Hub = <em>Supermarket</em>.
          </div>
        </div>
      </div>

      <!-- Sub-topic 3.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>3.3 Essential Docker CLI Commands Cheat Sheet</span>
          </div>
          <span class="sub-topic-badge">CLI Syntax</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Command</th><th>Purpose & Action</th></tr></thead>
              <tbody>
                <tr><td><code>docker build -t myapp:1.0 .</code></td><td>Builds an image named <code>myapp</code> from Dockerfile in current directory.</td></tr>
                <tr><td><code>docker run -d -p 80:8080 myapp:1.0</code></td><td>Runs container in background (<code>-d</code>) mapping host port 80 to container 8080.</td></tr>
                <tr><td><code>docker ps</code> / <code>docker ps -a</code></td><td>Lists running containers / Lists all containers including stopped.</td></tr>
                <tr><td><code>docker stop &lt;id&gt;</code></td><td>Sends SIGTERM signal to gracefully stop a running container.</td></tr>
                <tr><td><code>docker rm &lt;id&gt;</code> / <code>docker rmi &lt;img&gt;</code></td><td>Deletes a stopped container / Deletes a local image.</td></tr>
                <tr><td><code>docker pull &lt;image&gt;</code> / <code>push</code></td><td>Downloads an image from Docker Hub / Uploads image to registry.</td></tr>
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
            <span>3.4 Docker vs Container Distinction (From Slides)</span>
          </div>
          <span class="sub-topic-badge">Exam Tip</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <strong>Key Distinction:</strong><br>
            A <strong>Container</strong> is the isolated environment / box where an application and its runtime execute.<br>
            <strong>Docker</strong> is the platform, tooling ecosystem, and runtime engine used to build, package, run, and manage that container.
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 4 ==================== -->
  <div class="main-topic-card" id="u4-t4">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">☸️</span>
        <span class="main-topic-title">Topic 4: Kubernetes (Container Orchestration)</span>
        <span class="badge badge-accent">Production Scale</span>
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
            <span>4.1 What is Kubernetes & Why is it Required?</span>
          </div>
          <span class="sub-topic-badge">Overview</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">Definition: Kubernetes (K8s)</div>
            <strong>Kubernetes</strong> is an open-source container orchestration engine that automates the deployment, scaling, load balancing, and management of containerized applications across clustered servers.
          </div>
          <p><strong>Why is K8s required?</strong> While Docker easily runs 5 containers on a laptop, an enterprise running 500 microservices across 50 servers needs automated scheduling, self-healing, rolling updates, and internal DNS discovery.</p>
          <div class="grid-3" style="margin-top: 1rem;">
            <div class="subcard">
              <h4>Auto-Scaling</h4>
              <p>Scales Pod counts dynamically up or down based on observed CPU and memory metrics (Horizontal Pod Autoscaler).</p>
            </div>
            <div class="subcard">
              <h4>Self-Healing</h4>
              <p>Restarts crashed containers, replaces failed worker nodes, and terminates unresponsive health-check endpoints.</p>
            </div>
            <div class="subcard">
              <h4>Rolling Updates</h4>
              <p>Rolls out new container releases gradually with zero application downtime and instant rollback capabilities.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 4.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>4.2 Docker vs Kubernetes Comparison</span>
          </div>
          <span class="sub-topic-badge">Comparison</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Dimension</th><th>Docker</th><th>Kubernetes</th></tr></thead>
              <tbody>
                <tr><td><strong>Primary Function</strong></td><td>Creates, builds, and runs individual containers</td><td>Orchestrates fleets of containers across clusters</td></tr>
                <tr><td><strong>Scope</strong></td><td>Single machine / host focus</td><td>Multi-node distributed cluster management</td></tr>
                <tr><td><strong>Auto-Scaling</strong></td><td>Manual intervention required</td><td>Native automated Horizontal Pod Autoscaling (HPA)</td></tr>
                <tr><td><strong>Self-Healing</strong></td><td>Limited restart policies on local daemon</td><td>Automated rescheduling, replacement, and node migration</td></tr>
              </tbody>
            </table>
          </div>
          <div class="tip-box">
            <strong>Rule of Thumb:</strong> Docker creates the containers; Kubernetes manages the army of containers.
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 5 ==================== -->
  <div class="main-topic-card" id="u4-t5">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🎛️</span>
        <span class="main-topic-title">Topic 5: Cloud Management Platforms (CMPs)</span>
        <span class="badge">Management</span>
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
            <span>5.1 Definition & What a CMP Manages</span>
          </div>
          <span class="sub-topic-badge">Concept</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">What is a CMP?</div>
            A <strong>Cloud Management Platform (CMP)</strong> is an integrated software suite that provides centralized control to provision, monitor, govern, and optimize multi-cloud and private cloud resources through a unified pane of glass.
          </div>
          <p><strong>Resources Managed by a CMP:</strong> Virtual machines, storage volumes, software-defined networks, IAM roles, application deployments, financial cost budgets, and compliance posture.</p>
        </div>
      </div>

      <!-- Sub-topic 5.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>5.2 6 Core Objectives & Functions of CMPs</span>
          </div>
          <span class="sub-topic-badge">Functions</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="grid-3">
            <div class="subcard"><h4>1. Manage</h4><p>Centralized resource inventory across heterogeneous clouds.</p></div>
            <div class="subcard"><h4>2. Monitor</h4><p>Live health telemetry, uptime tracking, and alerting.</p></div>
            <div class="subcard"><h4>3. Automate</h4><p>Template-driven Infrastructure as Code deployment.</p></div>
            <div class="subcard"><h4>4. Optimize</h4><p>Downsizing idle VMs and capacity balancing.</p></div>
            <div class="subcard"><h4>5. Secure</h4><p>Role-based access control and policy auditing.</p></div>
            <div class="subcard"><h4>6. Cost Control</h4><p>Billing breakdown, budget tracking, and chargeback.</p></div>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 6 ==================== -->
  <div class="main-topic-card" id="u4-t6">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">☁️</span>
        <span class="main-topic-title">Topic 6: OpenStack Architecture & 9 Core Components</span>
        <span class="badge badge-priority">High-Yield (10 Marks)</span>
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
            <span>6.1 OpenStack Definition & 9 Core Projects Matrix</span>
          </div>
          <span class="sub-topic-badge">Must Memorize</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">What is OpenStack?</div>
            <strong>OpenStack</strong> is an open-source cloud operating system that controls large pools of compute, storage, and networking resources throughout a datacenter, managed via a dashboard or RESTful APIs (IaaS platform).
          </div>
          <div class="diagram-container">
            {SVG_OPENSTACK}
            <div class="diagram-caption">Figure 4.3: OpenStack Service Architecture and Inter-Service Relationships.</div>
          </div>
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Project</th><th>Service Type</th><th>Key Function</th><th>AWS Equivalent</th></tr></thead>
              <tbody>
                <tr><td><strong>Nova</strong></td><td>Compute</td><td>Lifecycle management of virtual machine instances</td><td>Amazon EC2</td></tr>
                <tr><td><strong>Neutron</strong></td><td>Networking</td><td>Virtual networks, subnets, routers, floating IPs, security groups</td><td>Amazon VPC</td></tr>
                <tr><td><strong>Keystone</strong></td><td>Identity</td><td>Authentication, authorization, token service, service catalog</td><td>AWS IAM</td></tr>
                <tr><td><strong>Glance</strong></td><td>Image</td><td>Discovery, registration, and delivery of VM disk images</td><td>Amazon AMI</td></tr>
                <tr><td><strong>Cinder</strong></td><td>Block Storage</td><td>Persistent block-level storage volumes for virtual machines</td><td>Amazon EBS</td></tr>
                <tr><td><strong>Swift</strong></td><td>Object Storage</td><td>High-durability object storage for unstructured data and blobs</td><td>Amazon S3</td></tr>
                <tr><td><strong>Horizon</strong></td><td>Dashboard</td><td>Web-based graphical user interface for administration</td><td>AWS Console</td></tr>
                <tr><td><strong>Heat</strong></td><td>Orchestration</td><td>Template-driven orchestration for multi-resource cloud apps</td><td>CloudFormation</td></tr>
                <tr><td><strong>Octavia</strong></td><td>Load Balancing</td><td>Load Balancer as a Service (LBaaS) distributing traffic</td><td>AWS ELB</td></tr>
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
            <span>6.2 Step-by-Step 7-Step VM Creation Flow</span>
          </div>
          <span class="sub-topic-badge">Exam Question</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <ol style="margin-left: 1.25rem; line-height: 1.7;">
            <li><strong>Step 1 (Login & Auth):</strong> User authenticates on <strong>Horizon</strong>; credentials validated by <strong>Keystone</strong>, which returns an Auth Token.</li>
            <li><strong>Step 2 (Image Selection):</strong> User selects OS; request sent to <strong>Glance</strong> to fetch the base image location.</li>
            <li><strong>Step 3 (Compute Provisioning):</strong> Request forwarded to <strong>Nova API</strong> with hardware flavor (CPU/RAM sizing).</li>
            <li><strong>Step 4 (Network Binding):</strong> Nova contacts <strong>Neutron</strong> to allocate virtual interfaces, subnets, and security groups.</li>
            <li><strong>Step 5 (Storage Volume Attachment):</strong> If persistent storage is needed, Nova triggers <strong>Cinder</strong> to attach a block volume.</li>
            <li><strong>Step 6 (Scheduling to Node):</strong> <code>nova-scheduler</code> selects the optimal Compute Node based on available CPU/RAM.</li>
            <li><strong>Step 7 (Execution):</strong> Local hypervisor (KVM) boots the VM instance, which obtains its IP via DHCP from Neutron.</li>
          </ol>
        </div>
      </div>

      <!-- Sub-topic 6.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>6.3 OpenStack Physical Infrastructure Nodes</span>
          </div>
          <span class="sub-topic-badge">Hardware</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="grid-3">
            <div class="subcard">
              <h4>1. Controller Node</h4>
              <p>Runs control-plane management services: Keystone, Glance, Horizon, Nova API, RabbitMQ message broker, and MariaDB state database.</p>
            </div>
            <div class="subcard">
              <h4>2. Compute Node</h4>
              <p>Runs the Hypervisor (KVM), <code>nova-compute</code> daemon, and Open vSwitch networking agents to physically run guest VMs.</p>
            </div>
            <div class="subcard">
              <h4>3. Storage Node</h4>
              <p>Contains physical hard drives running Cinder volume drivers (LVM, Ceph) and Swift storage daemons to serve block and object I/O.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 6.4 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>6.4 OpenStack vs AWS Service Mapping</span>
          </div>
          <span class="sub-topic-badge">Mapping</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p>OpenStack enables enterprises to build their own private version of AWS inside their own corporate datacenters:</p>
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Function</th><th>AWS Public Cloud</th><th>OpenStack Private Cloud</th></tr></thead>
              <tbody>
                <tr><td>Virtual Compute</td><td>EC2</td><td>Nova</td></tr>
                <tr><td>Virtual Private Network</td><td>VPC</td><td>Neutron</td></tr>
                <tr><td>Identity & Access</td><td>IAM</td><td>Keystone</td></tr>
                <tr><td>Machine Image Registry</td><td>AMI</td><td>Glance</td></tr>
                <tr><td>Persistent Block Storage</td><td>EBS</td><td>Cinder</td></tr>
                <tr><td>Scalable Object Storage</td><td>S3</td><td>Swift</td></tr>
                <tr><td>Web Management Console</td><td>AWS Console</td><td>Horizon</td></tr>
                <tr><td>Infrastructure as Code</td><td>CloudFormation</td><td>Heat</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 7 ==================== -->
  <div class="main-topic-card" id="u4-t7">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🥞</span>
        <span class="main-topic-title">Topic 7: Apache CloudStack Architecture & Resource Hierarchy</span>
        <span class="badge">Turnkey IaaS</span>
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
            <span>7.1 What is Apache CloudStack & Core Components</span>
          </div>
          <span class="sub-topic-badge">Overview</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">What is Apache CloudStack?</div>
            <strong>Apache CloudStack</strong> is an open-source turnkey Infrastructure as a Service (IaaS) software platform that pools computing, network, and storage resources to build public and private clouds.
          </div>
          <h5 style="margin-top: 1rem; color: var(--text-primary);">Core Parts of CloudStack:</h5>
          <ul>
            <li><strong>CloudStack Management Server:</strong> Single coordinator orchestrating VM placement, APIs, and Web UI.</li>
            <li><strong>Database:</strong> Central MySQL database storing system state and cloud configuration.</li>
            <li><strong>Primary Storage:</strong> High-performance storage hosting running VM disk volumes (SAN, NFS).</li>
            <li><strong>Secondary Storage:</strong> Capacity storage for ISO boot images, VM templates, and snapshots.</li>
            <li><strong>System VMs:</strong> Virtual routers, console proxies, and secondary storage worker VMs.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 7.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>7.2 CloudStack 5-Tier Resource Hierarchy (Region > Zone > Pod > Cluster > Host)</span>
          </div>
          <span class="sub-topic-badge">Hierarchy</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Hierarchy Level</th><th>Entity</th><th>Physical Scope & Description</th></tr></thead>
              <tbody>
                <tr><td><strong>Level 1 (Top)</strong></td><td><strong>Region</strong></td><td>Geographic grouping of one or more adjacent Zones.</td></tr>
                <tr><td><strong>Level 2</strong></td><td><strong>Zone</strong></td><td>Corresponds to a physical datacenter facility. Contains Pods and Secondary Storage.</td></tr>
                <tr><td><strong>Level 3</strong></td><td><strong>Pod</strong></td><td>Represents a physical equipment rack sharing a Layer 2 switch and common subnet.</td></tr>
                <tr><td><strong>Level 4</strong></td><td><strong>Cluster</strong></td><td>A cluster of homogeneous physical hosts running the same hypervisor sharing Primary Storage.</td></tr>
                <tr><td><strong>Level 5 (Bottom)</strong></td><td><strong>Host</strong></td><td>A single physical computer server running a hypervisor (KVM, XenServer, VMware ESXi).</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Sub-topic 7.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>7.3 OpenStack vs Apache CloudStack Comparison</span>
          </div>
          <span class="sub-topic-badge">Comparison</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Feature</th><th>OpenStack</th><th>Apache CloudStack</th></tr></thead>
              <tbody>
                <tr><td><strong>Architecture</strong></td><td>Modular distributed microservices (Nova, Neutron, Cinder...)</td><td>Integrated monolithic Management Server</td></tr>
                <tr><td><strong>Setup Complexity</strong></td><td>High; requires configuring message queues, DBs, and daemons</td><td>Low; turnkey packaging with simple web configuration</td></tr>
                <tr><td><strong>Flexibility</strong></td><td>Extreme customization for complex telco/cloud designs</td><td>Standardized, turnkey datacenter cloud orchestration</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 8 ==================== -->
  <div class="main-topic-card" id="u4-t8">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">💾</span>
        <span class="main-topic-title">Topic 8: Cloud Storage — Block, Object, and File Storage</span>
        <span class="badge badge-priority">High-Yield (7 Marks)</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>4 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 8.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>8.1 Block Storage (EBS, Managed Disks, Persistent Disk)</span>
          </div>
          <span class="sub-topic-badge">Block</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">What is Block Storage?</div>
            <strong>Block Storage</strong> divides data into fixed-size raw blocks, each possessing a unique address. It behaves exactly like an unformatted physical hard drive attached to a computer.
          </div>
          <ul>
            <li><strong>Protocol:</strong> Low-level SAN protocols (iSCSI, Fibre Channel, NVMe-oF).</li>
            <li><strong>Performance:</strong> Lowest latency, highest IOPS, supports byte-level in-place edits.</li>
            <li><strong>Best For:</strong> Virtual machine boot volumes, transactional relational databases (Oracle, MySQL).</li>
            <li><strong>Cloud Services:</strong> Amazon EBS, Azure Managed Disks, Google Cloud Persistent Disk.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 8.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>8.2 Object Storage (S3, Blob Storage, Cloud Storage)</span>
          </div>
          <span class="sub-topic-badge">Object</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">What is Object Storage?</div>
            <strong>Object Storage</strong> stores unstructured data as standalone objects composed of <strong>Data Payload + Custom Metadata + Globally Unique Key</strong>, residing in a flat logical namespace called a <strong>Bucket</strong>.
          </div>
          <ul>
            <li><strong>Protocol:</strong> RESTful HTTP/HTTPS APIs (GET, PUT, POST, DELETE).</li>
            <li><strong>Performance:</strong> Higher latency, virtually infinite exabyte scalability, 99.999999999% durability.</li>
            <li><strong>Best For:</strong> Media files, video streams, website backups, big data lakes, machine learning training data.</li>
            <li><strong>Cloud Services:</strong> Amazon S3, Azure Blob Storage, Google Cloud Storage.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 8.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>8.3 File Storage (EFS, Azure Files, Filestore)</span>
          </div>
          <span class="sub-topic-badge">File</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">What is File Storage?</div>
            <strong>File Storage</strong> organizes data in a classic hierarchical tree of nested folders and named files, accessible concurrently across multiple systems over a local network.
          </div>
          <ul>
            <li><strong>Protocol:</strong> Network File System (NFS for Linux) and Server Message Block (SMB for Windows).</li>
            <li><strong>Performance:</strong> Supports concurrent read/write and distributed file locking.</li>
            <li><strong>Best For:</strong> Shared corporate departmental drives, CMS media repositories (WordPress), web server clusters.</li>
            <li><strong>Cloud Services:</strong> Amazon EFS / FSx, Azure Files, Google Cloud Filestore.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 8.4 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>8.4 3-Way Storage Comparison Matrix (7 Marks)</span>
          </div>
          <span class="sub-topic-badge">7 Marks</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Dimension</th><th>Block Storage</th><th>Object Storage</th><th>File Storage</th></tr></thead>
              <tbody>
                <tr><td><strong>Basic Unit</strong></td><td>Addressable fixed block</td><td>Object (Data + Metadata + Key)</td><td>Files inside nested folders</td></tr>
                <tr><td><strong>Structure</strong></td><td>Raw disk volume</td><td>Flat bucket namespace</td><td>Hierarchical directory tree</td></tr>
                <tr><td><strong>Access</strong></td><td>Block I/O (iSCSI, SAN)</td><td>REST APIs (HTTP GET/PUT)</td><td>NFS / SMB file paths</td></tr>
                <tr><td><strong>Performance</strong></td><td>Ultra-low latency, high IOPS</td><td>High throughput, higher latency</td><td>Moderate latency; concurrent locking</td></tr>
                <tr><td><strong>AWS Service</strong></td><td>Amazon EBS</td><td>Amazon S3</td><td>Amazon EFS</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== TOPIC 9 ==================== -->
  <div class="main-topic-card" id="u4-t9">
    <div class="main-topic-header" onclick="toggleMainTopic(this)">
      <div class="main-topic-title-area">
        <span style="font-size: 1.25rem;">🌐</span>
        <span class="main-topic-title">Topic 9: Cloud Networking — SDN, VPN, Load Balancing & CDN</span>
        <span class="badge badge-priority">High-Yield (7/10 Marks)</span>
      </div>
      <div class="main-topic-toggle-btn">
        <span>5 Sub-topics</span>
        <span class="main-topic-arrow">▼</span>
      </div>
    </div>
    <div class="main-topic-body">
      
      <!-- Sub-topic 9.1 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>9.1 Software-Defined Networking (SDN) & 3-Layer Architecture</span>
          </div>
          <span class="sub-topic-badge">Architecture</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="def-box">
            <div class="def-title">What is SDN?</div>
            <strong>Software-Defined Networking (SDN)</strong> is an architectural approach that separates the network control plane (decision-making brain) from the underlying data forwarding plane (physical packet movers).
          </div>
          <div class="diagram-container">
            {SVG_SDN}
            <div class="diagram-caption">Figure 4.4: Software-Defined Networking (SDN) 3-Layer Architecture.</div>
          </div>
          <div class="grid-3" style="margin-top: 1rem;">
            <div class="subcard">
              <h4>1. Application Layer</h4>
              <p>Programs expressing network needs (firewalls, routing topology, QoS) communicating downward via Northbound APIs.</p>
            </div>
            <div class="subcard">
              <h4>2. Control Layer</h4>
              <p>The centralized SDN Controller calculating global routing tables and installing flow rules on switches.</p>
            </div>
            <div class="subcard">
              <h4>3. Infrastructure Layer</h4>
              <p>Physical/virtual packet-forwarding switches (OpenFlow, Open vSwitch) executing packet delivery.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 9.2 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>9.2 Virtual Private Network (VPN) — Remote Access vs Site-to-Site</span>
          </div>
          <span class="sub-topic-badge">Security Tunnel</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p>A <strong>VPN</strong> establishes an encrypted, secure virtual tunnel across an untrusted public network (like the Internet).</p>
          <div class="grid-2" style="margin-top: 1rem;">
            <div class="subcard">
              <h4>A. Remote Access VPN</h4>
              <p>Connects an individual user laptop to an enterprise corporate cloud network (e.g. employee working from home accessing private AWS VPC).</p>
            </div>
            <div class="subcard">
              <h4>B. Site-to-Site VPN</h4>
              <p>Interconnects two complete static enterprise networks securely (e.g. connecting an on-premises datacenter router to an AWS Virtual Private Gateway).</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 9.3 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>9.3 Load Balancing — Layer 4 NLB vs Layer 7 ALB & 5 Core Algorithms</span>
          </div>
          <span class="sub-topic-badge">Algorithms</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p>Distributes incoming network traffic across multiple healthy backend servers.</p>
          <div class="grid-2" style="margin-top: 0.75rem;">
            <div>
              <h5 style="color: #38bdf8;">Network Load Balancer (NLB) — Layer 4</h5>
              <p style="font-size: 0.85rem;">Operates at Transport Layer (TCP/UDP). Routes based on IP and port with ultra-high throughput (millions of requests/sec).</p>
            </div>
            <div>
              <h5 style="color: #10b981;">Application Load Balancer (ALB) — Layer 7</h5>
              <p style="font-size: 0.85rem;">Operates at Application Layer (HTTP/HTTPS). Inspects URL paths (<code>/api</code> vs <code>/images</code>) and headers for microservice routing.</p>
            </div>
          </div>
          <h5 style="margin-top: 1rem; color: var(--text-primary);">5 Load Balancing Algorithms:</h5>
          <ul>
            <li><strong>Round Robin:</strong> Sequential, circular distribution (Server 1 &rarr; Server 2 &rarr; Server 3 &rarr; Server 1).</li>
            <li><strong>Weighted Round Robin:</strong> Allocates proportionally more requests to higher-capacity servers.</li>
            <li><strong>Least Connections:</strong> Directs traffic to the server currently handling the fewest active client connections.</li>
            <li><strong>IP Hash:</strong> Computes a hash of the client's IP to deterministically bind a client to the same server.</li>
            <li><strong>Least Response Time:</strong> Directs requests to the backend server with the lowest response latency.</li>
          </ul>
        </div>
      </div>

      <!-- Sub-topic 9.4 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>9.4 Content Delivery Network (CDN) — Edge Caching & Cache Hit vs Miss</span>
          </div>
          <span class="sub-topic-badge">Edge Caching</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <p>A distributed network of geographically dispersed edge servers that caches copies of static assets closer to end users.</p>
          <div class="grid-2" style="margin-top: 0.75rem;">
            <div class="subcard">
              <h4>Cache Hit</h4>
              <p>The edge POP already has the requested file cached &rarr; returns it instantly to the user without contacting origin.</p>
            </div>
            <div class="subcard">
              <h4>Cache Miss</h4>
              <p>Edge server lacks the asset &rarr; fetches from origin server, caches a copy locally, and returns asset to user.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-topic 9.5 -->
      <div class="sub-topic-card">
        <div class="sub-topic-header" onclick="toggleSubTopic(this)">
          <div class="sub-topic-title-area">
            <span class="sub-topic-icon">▶</span>
            <span>9.5 SDN vs VPN vs Load Balancing vs CDN Comparison Matrix</span>
          </div>
          <span class="sub-topic-badge">7 Marks</span>
          <span class="sub-topic-arrow">▼</span>
        </div>
        <div class="sub-topic-detail">
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Dimension</th><th>SDN</th><th>VPN</th><th>Load Balancing</th><th>CDN</th></tr></thead>
              <tbody>
                <tr><td><strong>Purpose</strong></td><td>Programmable network management</td><td>Encrypted communication tunnel</td><td>Even traffic distribution</td><td>Low-latency content delivery</td></tr>
                <tr><td><strong>Focus</strong></td><td>Control vs data plane decoupling</td><td>Security & remote access</td><td>High availability & throughput</td><td>Caches static assets at edges</td></tr>
                <tr><td><strong>Cloud Example</strong></td><td>OpenStack Neutron / AWS VPC</td><td>AWS Site-to-Site VPN</td><td>AWS ALB / NLB</td><td>Amazon CloudFront / Cloudflare</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>

</div>
"""
