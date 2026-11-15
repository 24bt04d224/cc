# -*- coding: utf-8 -*-
with open('d:/Downloads/cc/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('File size:', len(html))
assert 'main-topic-card' in html, 'Missing main-topic-card'
assert 'main-topic-header' in html, 'Missing main-topic-header'
assert 'sub-topic-card' in html, 'Missing sub-topic-card'
assert 'sub-topic-header' in html, 'Missing sub-topic-header'
assert 'sub-topic-detail' in html, 'Missing sub-topic-detail'
assert 'toggleMainTopic' in html, 'Missing toggleMainTopic JS'
assert 'toggleSubTopic' in html, 'Missing toggleSubTopic JS'
assert 'expandAllInUnit' in html, 'Missing expandAllInUnit JS'
assert 'jumpToTopic' in html, 'Missing jumpToTopic JS'

assert 'mobile-menu-btn' in html, 'Missing mobile-menu-btn'
assert 'mobile-bottom-nav' in html, 'Missing mobile-bottom-nav'
assert 'sidebar-backdrop' in html, 'Missing sidebar-backdrop'
assert 'toggleMobileNav' in html, 'Missing toggleMobileNav JS'
assert 'closeMobileNav' in html, 'Missing closeMobileNav JS'
assert 'viewport-fit=cover' in html, 'Missing viewport-fit=cover'

print('Main topic cards count:', html.count('class="main-topic-card"'))
print('Sub topic cards count:', html.count('class="sub-topic-card"'))
print('All dropdown & mobile responsive assertions successfully passed!')
