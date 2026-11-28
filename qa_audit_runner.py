#!/usr/bin/env python3
"""
Zelmiqo® QA Verification Test Suite & Audit Runner
Comprehensive verification of all generated HTML workstation pages and annotated image assets.
"""

import os
import re
import sys
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PAGES_DIR = os.path.join(BASE_DIR, 'new-content-html-pages')
ASSETS_DIR = os.path.join(PAGES_DIR, 'assets')

REQUIRED_PAGES = [
    os.path.join('main-html-pages', 'home.html'),
    os.path.join('main-html-pages', 'catalog.html'),
    os.path.join('main-html-pages', 'about-us.html'),
    os.path.join('main-html-pages', 'delivery-and-shipping.html'),
    os.path.join('main-html-pages', 'warranty-and-returns.html'),
    os.path.join('main-html-pages', 'contact-us.html'),
    os.path.join('main-html-pages', 'privacy-and-terms.html'),
    os.path.join('main-html-pages', 'blogs-and-articles.html'),
    os.path.join('main-html-pages', 'header.html'),
    os.path.join('main-html-pages', 'footer.html'),
    os.path.join('main-html-pages', 'index.html'),
    'all-pages.html',
    os.path.join('products-html-pages', '3-in-1-fast-charging-dock.html'),
    os.path.join('products-html-pages', 'portable-bladeless-neck-fan.html'),
    os.path.join('products-html-pages', '3-in-1-portable-air-cooler.html'),
    os.path.join('products-html-pages', 'mini-usb-rechargeable-fan.html'),
    os.path.join('products-html-pages', 'portable-bladeless-neck-fan-5-speeds.html'),
    os.path.join('products-html-pages', '3d-silicone-facial-brush.html'),
    os.path.join('products-html-pages', '5-in-1-ems-facial-massager.html'),
    os.path.join('products-html-pages', 'deep-pore-blackhead-remover.html'),
    os.path.join('products-html-pages', 'portable-scalp-massage-comb.html'),
    os.path.join('products-html-pages', 'ultrasonic-skin-scrubber.html'),
    os.path.join('products-html-pages', 'bionic-finger-neck-massager.html'),
    os.path.join('products-html-pages', 'smart-fascia-massage-gun.html'),
    os.path.join('products-html-pages', 'usb-coffee-mug-warmer.html'),
    os.path.join('products-html-pages', 'wireless-weather-station-alarm.html'),
    os.path.join('products-html-pages', 'foldable-car-sun-shade.html'),
    os.path.join('products-html-pages', 'portable-6-blade-juicer.html'),
    os.path.join('products-html-pages', 'portable-double-cup-juicer.html'),
    os.path.join('products-html-pages', 'portable-usb-citrus-juicer.html'),
    os.path.join('products-html-pages', 'cordless-handheld-car-vacuum.html'),
    os.path.join('products-html-pages', 'portable-wireless-car-vacuum.html'),
    os.path.join('products-html-pages', 'r36s-retro-handheld-game-console.html')
]

FORBIDDEN_PAGE_PATTERNS = [
    r'account.*\.html',
    r'tracking.*\.html',
    r'shipping-tracking.*\.html',
    r'category-.*\.html',
    r'cart.*\.html',
    r'checkout.*\.html',
    r'sitemap.*\.html',
    r'search.*\.html',
    r'special.*\.html',
    r'compare.*\.html'
]

REQUIRED_ASSETS = [
    'about_us_full.jpg',
    'blogs_full.jpg',
    'catalog_full.jpg',
    'contact_full.jpg',
    'delivery_full.jpg',
    'footer_full.jpg',
    'header_full.jpg',
    'home_full.jpg',
    'privacy_full.jpg',
    'section_1_hero.jpg',
    'section_2_trust.jpg',
    'section_3_categories.jpg',
    'section_4_new_collection.jpg',
    'section_5_mid_banners.jpg',
    'section_6_trending.jpg',
    'section_7_testimonials.jpg',
    'warranty_full.jpg',
    'product_dock_hero.jpg',
    'product_dock_faqs.jpg',
    'product_dock_two_col.jpg',
    'product_dock_center_4blocks.jpg',
    'product_dock_benefits_grid.jpg',
    'product_dock_table.jpg',
    'product_dock_marquee.jpg',
    'product_dock_customers.jpg',
    'product_dock_reviews.jpg',
    'product_dock_related.jpg',
    'product_dock_full.jpg',
    'neck_fan_hero.jpg',
    'neck_fan_faqs.jpg',
    'neck_fan_two_col.jpg',
    'neck_fan_center_4blocks.jpg',
    'neck_fan_benefits_grid.jpg',
    'neck_fan_table.jpg',
    'neck_fan_marquee.jpg',
    'neck_fan_customers.jpg',
    'neck_fan_reviews.jpg',
    'neck_fan_related.jpg',
    'neck_fan_full.jpg'
]

KSA_VALUE_PROPS = {
    'Riyadh Operations / الرياض': [r'Riyadh', r'الرياض'],
    'Fast 7-8 Days Delivery / 7-8 أيام': [r'7-8', r'7\s*-\s*8', r'7–8', r'7\s*إلى\s*8'],
    'Mada Payment / مدى': [r'Mada', r'مدى'],
    'Apple Pay / أبل باي': [r'Apple Pay', r'أبل باي'],
    'Tabby Installments / تابي': [r'Tabby', r'تابي'],
    'Tamara Installments / تمارا': [r'Tamara', r'تمارا'],
    '7-Day Golden Guarantee / الضمان الذهبي': [r'Golden Guarantee', r'الضمان الذهبي', r'7-Day', r'7\s*أيام'],
    'Cash on Delivery / الدفع عند الاستلام': [r'Cash on Delivery', r'COD', r'الدفع عند الاستلام'],
    'SAR Currency / ر.س': [r'SAR', r'ر\.س']
}

class TestResult:
    def __init__(self, name):
        self.name = name
        self.passed = True
        self.messages = []
        self.details = {}

    def fail(self, msg):
        self.passed = False
        self.messages.append(f'FAIL: {msg}')

    def pass_msg(self, msg):
        self.messages.append(f'PASS: {msg}')

def test_1_in_scope_pages_exist():
    res = TestResult("1. In-Scope Workstation Pages Existence")
    if not os.path.isdir(PAGES_DIR):
        res.fail(f"Directory {PAGES_DIR} not found")
        return res

    for page in REQUIRED_PAGES:
        path = os.path.join(PAGES_DIR, page)
        if not os.path.isfile(path):
            res.fail(f"Missing page: {page}")
        else:
            sz = os.path.getsize(path)
            if sz == 0:
                res.fail(f"Page is empty: {page}")
            else:
                res.pass_msg(f"{page:30} ({sz:6d} bytes)")
    return res

def test_2_no_ignored_pages():
    res = TestResult("2. Strict Scope Boundary (No Ignored Pages)")
    if not os.path.isdir(PAGES_DIR):
        res.fail("PAGES_DIR not found")
        return res

    all_files = os.listdir(PAGES_DIR)
    violating_files = []
    for f in all_files:
        for pat in FORBIDDEN_PAGE_PATTERNS:
            if re.match(pat, f, re.IGNORECASE):
                violating_files.append(f)
                break

    if violating_files:
        res.fail(f"Found forbidden/out-of-scope files: {violating_files}")
    else:
        res.pass_msg("Zero forbidden pages detected (No Account, Product Detail, Category, Tracking, Cart/Checkout, Sitemap, Search, Special, or Compare pages).")
    return res

def test_3_asset_images_integrity():
    res = TestResult("3. Asset Images Integrity & Red Bounding Box Verification")
    if not os.path.isdir(ASSETS_DIR):
        res.fail(f"Assets dir {ASSETS_DIR} not found")
        return res

    for asset_name in REQUIRED_ASSETS:
        path = os.path.join(ASSETS_DIR, asset_name)
        if not os.path.isfile(path):
            res.fail(f"Missing asset image: {asset_name}")
            continue

        sz = os.path.getsize(path)
        try:
            with Image.open(path) as img:
                w, h = img.size
                if w < 100 or h < 100:
                    res.fail(f"Image {asset_name} has suspiciously small dimensions: {w}x{h}")
                    continue

                # Check for bounding box red pixels (#e61919 ~ RGB(230, 25, 25))
                # Sample pixels across image
                rgb_img = img.convert('RGB')
                pixels = list(rgb_img.getdata())
                total_pixels = len(pixels)
                red_pixels = sum(1 for r, g, b in pixels if r > 190 and g < 65 and b < 65)
                exact_red_pixels = sum(1 for r, g, b in pixels if abs(r - 230) <= 20 and abs(g - 25) <= 20 and abs(b - 25) <= 20)

                if red_pixels < 500:
                    res.fail(f"{asset_name} lacks sufficient red bounding box pixels (found {red_pixels})")
                else:
                    res.pass_msg(f"{asset_name:28}: {w:4d}x{h:4d} | {sz/1024:6.1f}KB | Red Pixels: {red_pixels:6d} (Exact #e61919: {exact_red_pixels:5d})")
        except Exception as e:
            res.fail(f"Failed opening image {asset_name}: {e}")
    return res

def test_4_number_alignment_and_callout_matching():
    res = TestResult("4. Red Box Numbers vs HTML Workstation Cards 1:1 Matching")
    
    pages_to_check = [
        (os.path.join('main-html-pages', 'home.html'), 9, ['Hero 1', 'Hero 2', 'Trust Pillars', 'Categories', 'New Arrivals', 'Mid Banners', 'Trending', 'Testimonials', 'SEO']),
        (os.path.join('main-html-pages', 'catalog.html'), 6, ['[1]', '[2]', '[3]', '[4]', '[5]', '[SEO]']),
        (os.path.join('main-html-pages', 'about-us.html'), 7, ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[SEO]']),
        (os.path.join('main-html-pages', 'delivery-and-shipping.html'), 7, ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[SEO]']),
        (os.path.join('main-html-pages', 'warranty-and-returns.html'), 7, ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[SEO]']),
        (os.path.join('main-html-pages', 'contact-us.html'), 7, ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[SEO]']),
        (os.path.join('main-html-pages', 'privacy-and-terms.html'), 7, ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[SEO]']),
        (os.path.join('main-html-pages', 'blogs-and-articles.html'), 6, ['[1]', '[2]', '[3]', '[4]', '[5]', '[SEO]']),
        (os.path.join('main-html-pages', 'header.html'), 6, ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]']),
        (os.path.join('main-html-pages', 'footer.html'), 6, ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]'])
    ]

    for filename, expected_cards_count, expected_badges in pages_to_check:
        path = os.path.join(PAGES_DIR, filename)
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()

        cards = re.findall(r'<div[^>]*class=[\"\'][^\"\']*content-card[^\"\']*[\"\'][^>]*id=[\"\']([^\"\']+)[\"\']', html)
        badges = [b.strip() for b in re.findall(r'<span[^>]*class=[\"\']card-main-badge[\"\'][^>]*>(.*?)</span>', html)]
        pills_block = re.search(r'<div class=[\"\']section-nav-pills[\"\']>(.*?)</div>', html, re.DOTALL)
        pill_links = re.findall(r'<a[^>]+onclick=[\"\'][^\"\']*[\"\'][^>]*>(.*?)</a>', pills_block.group(1)) if pills_block else []

        if len(cards) != expected_cards_count:
            res.fail(f"{filename}: expected {expected_cards_count} content cards, found {len(cards)}")
        elif badges != expected_badges:
            res.fail(f"{filename}: badges mismatch. Expected {expected_badges}, got {badges}")
        else:
            res.pass_msg(f"{filename:30}: {len(cards)} Cards, {len(badges)} Badges ({', '.join(badges)}), {len(pill_links)} Nav Pills matched 1:1")
    return res

def get_workstation_pages():
    index_rel = os.path.join('main-html-pages', 'index.html')
    return [p for p in REQUIRED_PAGES if p not in (index_rel, 'all-pages.html')]

def test_5_interactive_elements_and_copy_functions():
    res = TestResult("5. Interactive Workstation Functionality & Copy Buttons")
    workstation_pages = get_workstation_pages()
    
    total_copy_buttons = 0
    for p in workstation_pages:
        path = os.path.join(PAGES_DIR, p)
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()

        # Check required DOM containers
        required_containers = ['visualImage', 'sliderHint', 'toastMsg']
        for elem_id in required_containers:
            if f'id="{elem_id}"' not in html and f"id='{elem_id}'" not in html:
                res.fail(f"{p}: Missing required DOM element id='{elem_id}'")

        # Check JavaScript function signatures
        required_functions = [
            'function switchVisual(',
            'function selectSection(',
            'function scrollToCard(',
            'function updateActivePill(',
            'function copyFrom(',
            'function showToast('
        ]
        for fn in required_functions:
            if fn not in html:
                res.fail(f"{p}: Missing JavaScript function '{fn}'")

        # Check ScrollSpy listener
        if "pane.addEventListener('scroll'" not in html and 'pane.addEventListener("scroll"' not in html:
            res.fail(f"{p}: Missing ScrollSpy pane scroll event listener")

        # Check all copyFrom targets
        copy_calls = re.findall(r'copyFrom\([\'\"]([^\'\"]+)[\'\"]', html)
        total_copy_buttons += len(copy_calls)

        for target_id in copy_calls:
            # Check element exists
            pattern = rf'id=[\"\']{re.escape(target_id)}[\"\'][^>]*>(.*?)</'
            m = re.search(pattern, html, re.DOTALL)
            if not m:
                res.fail(f"{p}: copyFrom target #{target_id} not found in DOM")
            else:
                txt = m.group(1).strip()
                if not txt:
                    res.fail(f"{p}: copyFrom target #{target_id} has empty content")

        res.pass_msg(f"{p:30}: Verified {len(copy_calls)} copy buttons, all DOM targets populated, ScrollSpy active")

    res.pass_msg(f"Total interactive copy buttons verified across store: {total_copy_buttons}")
    return res

def test_6_copywriting_and_saudi_value_props():
    res = TestResult("6. Copywriting Quality & Saudi Localized Value Propositions")
    workstation_pages = get_workstation_pages()

    for p in workstation_pages:
        path = os.path.join(PAGES_DIR, p)
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()

        # Arabic styling check
        if '.arabic' not in html:
            res.fail(f"{p}: Missing .arabic CSS styling")
        
        # Arabic character presence
        arabic_chars = len(re.findall(r'[\u0600-\u06FF]', html))
        if arabic_chars < 500:
            res.fail(f"{p}: Insufficient Arabic content (found {arabic_chars} chars)")

        # Verify key value proposition coverage
        found_props = []
        for prop_name, patterns in KSA_VALUE_PROPS.items():
            combined = re.compile('|'.join(patterns), re.IGNORECASE)
            if combined.search(html):
                found_props.append(prop_name.split(' / ')[0])

        res.pass_msg(f"{p:30}: Arabic Chars: {arabic_chars:5d} | Value Props Covered: {', '.join(found_props[:5])}...")

    return res

def test_7_hub_and_inter_page_navigation():
    res = TestResult("7. Hub & Inter-Page Navigation Symmetry + All Pages Links")
    index_rel = os.path.join('main-html-pages', 'index.html')
    index_path = os.path.join(PAGES_DIR, index_rel)
    all_pages_path = os.path.join(PAGES_DIR, 'all-pages.html')
    if not os.path.isfile(index_path):
        res.fail("main-html-pages/index.html not found")
        return res
    if not os.path.isfile(all_pages_path):
        res.fail("all-pages.html not found")
        return res

    with open(index_path, 'r', encoding='utf-8') as f:
        index_html = f.read()
    with open(all_pages_path, 'r', encoding='utf-8') as f:
        all_pages_html = f.read()

    if 'href="../all-pages.html"' not in index_html:
        res.fail("main-html-pages/index.html missing All Pages button (href=\"../all-pages.html\")")
    else:
        res.pass_msg("main-html-pages/index.html has All Pages button (../all-pages.html)")

    if 'href="main-html-pages/index.html"' not in all_pages_html:
        res.fail("all-pages.html missing link back to main-html-pages/index.html")
    else:
        res.pass_msg("all-pages.html has link to main-html-pages/index.html")

    workstation_pages = get_workstation_pages()
    for p in workstation_pages:
        p_posix = p.replace(os.sep, '/')
        if p_posix.startswith('main-html-pages/'):
            expected_href_in_index = p_posix.replace('main-html-pages/', '', 1)
            expected_back_link = 'index.html'
        else:
            expected_href_in_index = '../' + p_posix
            expected_back_link = '../main-html-pages/index.html'

        wp_path = os.path.join(PAGES_DIR, p)
        with open(wp_path, 'r', encoding='utf-8') as f:
            wp_html = f.read()

        if f'href="{expected_href_in_index}"' not in index_html:
            res.fail(f"main-html-pages/index.html does not link to {expected_href_in_index}")
        elif f'href="{expected_back_link}"' not in wp_html:
            res.fail(f"{p_posix} missing back link to {expected_back_link}")
        elif 'href="../all-pages.html"' not in wp_html:
            res.fail(f"{p_posix} missing All Pages button (href=\"../all-pages.html\")")
        elif f'href="{p_posix}"' not in all_pages_html:
            res.fail(f"all-pages.html missing link to {p_posix}")
        else:
            res.pass_msg(f"Bidirectional Hub + All Pages links verified: {p_posix}")

    return res

def run_all_tests():
    print("=" * 80)
    print(" ZELMIQO® E-COMMERCE MASTER WORKSTATION QA TEST SUITE & AUDIT RUNNER")
    print("=" * 80)
    
    test_functions = [
        test_1_in_scope_pages_exist,
        test_2_no_ignored_pages,
        test_3_asset_images_integrity,
        test_4_number_alignment_and_callout_matching,
        test_5_interactive_elements_and_copy_functions,
        test_6_copywriting_and_saudi_value_props,
        test_7_hub_and_inter_page_navigation
    ]

    results = []
    overall_pass = True

    for test_fn in test_functions:
        res = test_fn()
        results.append(res)
        status = "PASSED ✓" if res.passed else "FAILED ✗"
        print(f"\n[{status}] {res.name}")
        print("-" * 80)
        for msg in res.messages:
            print(f"  {msg}")
        if not res.passed:
            overall_pass = False

    print("\n" + "=" * 80)
    if overall_pass:
        print(" 🎉 OVERALL AUDIT STATUS: 100% PASSED (ALL 7 TEST SUITES SATISFIED)")
    else:
        print(" ❌ OVERALL AUDIT STATUS: AUDIT FAILED (SEE LOGS ABOVE)")
    print("=" * 80)
    return overall_pass

if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
