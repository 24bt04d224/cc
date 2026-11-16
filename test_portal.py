# -*- coding: utf-8 -*-
with open('d:/Downloads/cc/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('File size:', len(html))

# Structural checks
assert 'main-topic-card' in html, 'Missing main-topic-card'
assert 'main-topic-header' in html, 'Missing main-topic-header'
assert 'sub-topic-card' in html, 'Missing sub-topic-card'
assert 'sub-topic-header' in html, 'Missing sub-topic-header'
assert 'sub-topic-detail' in html, 'Missing sub-topic-detail'
assert 'toggleMainTopic' in html, 'Missing toggleMainTopic JS'
assert 'toggleSubTopic' in html, 'Missing toggleSubTopic JS'
assert 'expandAllInUnit' in html, 'Missing expandAllInUnit JS'
assert 'jumpToTopic' in html, 'Missing jumpToTopic JS'

# Responsive checks
assert 'mobile-menu-btn' in html, 'Missing mobile-menu-btn'
assert 'mobile-bottom-nav' in html, 'Missing mobile-bottom-nav'
assert 'sidebar-backdrop' in html, 'Missing sidebar-backdrop'
assert 'toggleMobileNav' in html, 'Missing toggleMobileNav JS'
assert 'closeMobileNav' in html, 'Missing closeMobileNav JS'
assert 'viewport-fit=cover' in html, 'Missing viewport-fit=cover'

# Google Images Diagram references
assert 'btn-ref-google' in html, 'Missing Google Images diagram button class'
assert 'https://www.google.com/search?tbm=isch' in html, 'Missing Google Images search links'

# Section 1: Random Topics
assert 'id="random-topics"' in html, 'Missing random-topics tab pane'
assert 'id="nav-random-topics"' in html, 'Missing nav-random-topics sidebar item'
assert 'rollNextRandomTopic' in html, 'Missing rollNextRandomTopic JS function'
assert 'setRandomTopicUnit' in html, 'Missing setRandomTopicUnit JS function'
assert 'toggleTopicDetails' in html, 'Missing toggleTopicDetails JS function'
assert 'ALL_TOPICS_POOL' in html, 'Missing ALL_TOPICS_POOL JS array'

# Section 2: IMP Topics
assert 'id="imp-topics"' in html, 'Missing imp-topics tab pane'
assert 'id="nav-imp-topics"' in html, 'Missing nav-imp-topics sidebar item'
assert 'filterImpCards' in html, 'Missing filterImpCards JS function'
assert 'class="imp-card' in html, 'Missing imp-card elements'
assert 'tier-1' in html, 'Missing tier-1 styling'
assert 'data-marks="7m"' in html, 'Missing 7m mark tags'

# Section 3: Random Questions Roulette
assert 'id="random-questions"' in html, 'Missing random-questions tab pane'
assert 'id="nav-random-questions"' in html, 'Missing nav-random-questions sidebar item'
assert 'rollNextRouletteQuestion' in html, 'Missing rollNextRouletteQuestion JS function'
assert 'setRouletteFilter' in html, 'Missing setRouletteFilter JS function'
assert 'toggleRouletteAnswer' in html, 'Missing toggleRouletteAnswer JS function'
assert 'ALL_QUESTIONS_POOL' in html, 'Missing ALL_QUESTIONS_POOL JS array'
assert 'id="rqAnswerPanel"' in html, 'Missing answer panel element'

# No MAD leakage
assert 'Mobile Application Development' not in html, 'MAD found in index.html!'
assert 'Android Studio' not in html, 'Android Studio found in index.html!'
assert 'Activity Lifecycle' not in html, 'Activity Lifecycle found in index.html!'

print('Main topic cards count:', html.count('class="main-topic-card"'))
print('Sub topic cards count:', html.count('class="sub-topic-card"'))
print('IMP cards count:', html.count('class="imp-card'))
print('Google Images links count:', html.count('https://www.google.com/search?tbm=isch'))

# Units 4 & 5 Guaranteed Questions assertions (All 21 Questions)
u45_expected = [
    "What is virtualization? Compare its different types in detail.",
    "Explain the role of Hypervisor.",
    "Differentiate between Container and docker in detail.",
    "Compare the VM and containers with respect to Cloud Computing. Which one is preferred in terms of performance and convenience.",
    "Explain Openstack in detail.",
    "List and explain different services and its purpose provided by Openstack.",
    "Explain Cloudstack and compare with Openstack.",
    "What are different Cloud storage methods.",
    "Compare Block, file and object storage in detail.",
    "What is SDN? Explain its role in terms of Cloud computing.",
    "Explain the load balancer with one real example.",
    "What are different services provided by AWS with respect to storage?",
    "Explain Kubernetes and compare with Docker.",
    "Explain EKS, ECS, ECR and Fargate services of AWS.",
    "What are major data security concerns in Cloud computing?",
    "Differentiate between Authentication and Authorisation.",
    "What is the role of IAM? How does it help to improve security in Cloud Computing?",
    "Differentiate between Scalability and Elasticity.",
    "How can VMs be secured to protect the data and cloud resources?",
    "What do you mean by cloud computing governance and compliance?",
    "Differentiate between Cloud security, Cloud Governance, and Cloud Compliance"
]

for q_text in u45_expected:
    assert q_text in html, f"Missing guaranteed question in index.html: {q_text}"

print(f"All {len(u45_expected)} Units 4 & 5 Guaranteed Questions verified in index.html!")

# JavaScript Syntax Check with Node
import re, subprocess
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
assert len(scripts) > 0, "No script tag found in index.html"
for i, s in enumerate(scripts):
    tmp_js = f"_temp_check_{i}.js"
    with open(tmp_js, 'w', encoding='utf-8') as out:
        out.write(s)
    res = subprocess.run(['node', '--check', tmp_js], capture_output=True, text=True)
    import os
    if os.path.exists(tmp_js):
        os.remove(tmp_js)
    assert res.returncode == 0, f"JavaScript syntax error in script {i}:\n{res.stderr}"

print(f"All {len(scripts)} embedded JavaScript blocks passed zero-error Node.js syntax validation!")
print('All 3 Exam Power Modes, Dropdowns, Responsive & Quality assertions PASSED!')
