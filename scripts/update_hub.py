# -*- coding: utf-8 -*-
import os
import re

hub_path = "new-content-html-pages/index.html"
with open(hub_path, "r", encoding="utf-8") as f:
    html = f.read()

# Update stats
html = re.sub(
    r'<span class="stat-value">10 Pages</span>',
    '<span class="stat-value">30 Workstations</span>',
    html
)
html = re.sub(
    r'<span class="stat-sub">✓ 100% Complete & Verified</span>',
    '<span class="stat-sub">✓ 10 Store Pages + 20 Flagship Products</span>',
    html
)

products_data = [
    # Climate & Cooling
    {
        "file": "product-3-in-1-portable-air-cooler.html",
        "icon": "❄️",
        "badge": "Climate & Cooling • 11 Sections",
        "title_en": "3-in-1 Portable Air Cooler Fan with Humidifier & LED Light",
        "title_ar": "مكيف ومبرد هواء صيفي متنقل 3 في 1 مع مرطب رذاذ وإضاءة ليلية",
        "desc": "Arctic evaporative cooling mist for desk and bedside. Combats dry AC air and summer heat waves across Saudi Arabia.",
        "url": "https://zelmiqo.com/products/3-in-1-portable-air-cooler-fan",
        "price": "SAR 119.00 (SAR 29.75 x 4 Tabby/Tamara)"
    },
    {
        "file": "product-mini-usb-rechargeable-fan.html",
        "icon": "💨",
        "badge": "Climate & Cooling • 11 Sections",
        "title_en": "Mini USB Rechargeable Handheld & Desktop Fan with 3 Speeds",
        "title_ar": "مروحة الجيب اليدوية والمكتبية القابلة للشحن مع قاعدة وحامل جوال",
        "desc": "Pocket-sized personal arctic breeze with built-in phone stand. Essential for outdoor commutes, campus walks, and Umrah pilgrimage.",
        "url": "https://zelmiqo.com/products/mini-usb-rechargeable-handheld-desktop-fan",
        "price": "SAR 49.00 (SAR 12.25 x 4 Tabby/Tamara)"
    },
    {
        "file": "product-portable-bladeless-neck-fan-5-speeds.html",
        "icon": "🌬️",
        "badge": "Climate & Cooling • 11 Sections",
        "title_en": "Portable Bladeless Neck Fan with 5 Turbo Speeds & LED Display",
        "title_ar": "مروحة الرقبة التوربينية بدون شفرات بـ 5 سرعات وشاشة ذكية",
        "desc": "Hands-free surround personal airflow with ultra-quiet brushless twin turbines. Keeps your neck and face sweat-free in 45°C+ summer heat.",
        "url": "https://zelmiqo.com/products/portable-bladeless-neck-fan-5-speeds",
        "price": "SAR 95.00 (SAR 23.75 x 4 Tabby/Tamara)"
    },
    # Beauty & Skincare
    {
        "file": "product-3d-silicone-facial-brush.html",
        "icon": "✨",
        "badge": "Beauty Tech • 11 Sections",
        "title_en": "3D Double-Sided Silicone Facial Cleansing Brush",
        "title_ar": "فرشاة تنظيف الوجه السيليكونية ثلاثية الأبعاد 3D للمسام والمساج",
        "desc": "Dual-sided food-grade silicone and ultra-fine microfibers for deep pore purification and gentle facial massage.",
        "url": "https://zelmiqo.com/products/3d-silicone-facial-brush",
        "price": "SAR 45.00 (SAR 11.25 x 4 Tabby/Tamara)"
    },
    {
        "file": "product-5-in-1-ems-facial-massager.html",
        "icon": "💆‍♀️",
        "badge": "Beauty Tech • 11 Sections",
        "title_en": "5-in-1 EMS Skin Tightening Massager with LED Light Therapy",
        "title_ar": "جهاز شد ونحت الوجه 5 في 1 مع نبضات EMS وعلاج ضوئي LED",
        "desc": "Clinic-grade facelift at home with microcurrent EMS, 42°C thermal infusion, and tri-color phototherapy for sculpted jawline and collagen renewal.",
        "url": "https://zelmiqo.com/products/5-in-1-ems-facial-massager-led-light-therapy",
        "price": "SAR 135.00 (SAR 33.75 x 4 Tabby/Tamara)"
    },
    {
        "file": "product-deep-pore-blackhead-remover.html",
        "icon": "💎",
        "badge": "Beauty Tech • 11 Sections",
        "title_en": "PorePure Vacuum Blackhead Remover with LED Screen & 5 Levels",
        "title_ar": "جهاز شفط وتنظيف الرؤوس السوداء والمسام مع شاشة LED ذكية",
        "desc": "Dermatologist-safe calibrated pore vacuum extraction with 5 suction tiers, 4 beauty probes, and crystal HD display.",
        "url": "https://zelmiqo.com/products/deep-pore-blackhead-remover-vacuum",
        "price": "SAR 99.00 (SAR 24.75 x 4 Tabby/Tamara)"
    },
    {
        "file": "product-portable-scalp-massage-comb.html",
        "icon": "💆‍♂️",
        "badge": "Hair Wellness • 11 Sections",
        "title_en": "Portable Scalp Massage Comb with Liquid Hair Oil Applicator",
        "title_ar": "مشط مساج فروة الرأس المتنقل مع موزع زيوت وسيروم الشعر الدقيق",
        "desc": "Delivers rosemary oils and hair growth serums directly to follicles via rolling ball teeth and gentle micro-vibrations with zero messy hands.",
        "url": "https://zelmiqo.com/products/portable-scalp-massage-liquid-comb",
        "price": "SAR 135.00 (SAR 33.75 x 4 Tabby/Tamara)"
    },
    {
        "file": "product-ultrasonic-skin-scrubber.html",
        "icon": "🌊",
        "badge": "Beauty Tech • 11 Sections",
        "title_en": "DermaSonic Ultrasonic Skin Scrubber & Deep Pore Spatula",
        "title_ar": "جهاز تقشير وتنظيف البشرة بالموجات فوق الصوتية والأيونات والنبضات",
        "desc": "24,000Hz ultrasonic wave peeling spatula with Ion+ pore extraction, Ion- nutrient infusion, and EMS lifting for radiant glass skin.",
        "url": "https://zelmiqo.com/products/ultrasonic-skin-scrubber-deep-pore-care",
        "price": "SAR 169.00 (SAR 42.25 x 4 Tabby/Tamara)"
    },
    # Wellness & Smart Tech
    {
        "file": "product-bionic-finger-neck-massager.html",
        "icon": "🖐️",
        "badge": "Wellness Tech • 11 Sections",
        "title_en": "Bionic Finger Shiatsu Neck & Shoulder Kneading Massager with Heat",
        "title_ar": "جهاز مساج وتدليك الرقبة والأكتاف الحيوي 4D مع تدفئة حرارية",
        "desc": "Authentic human-touch 4D thumb kneading with 42°C infrared heat to melt away desk stiffness and neck tension in 15 minutes.",
        "url": "https://zelmiqo.com/products/bionic-finger-neck-shoulder-massager",
        "price": "SAR 149.00 (SAR 37.25 x 4 Tabby/Tamara)"
    },
    {
        "file": "product-smart-fascia-massage-gun.html",
        "icon": "⚡️",
        "badge": "Recovery Tech • 11 Sections",
        "title_en": "ProPercuss 9-Speed Deep Tissue Fascia Massage Gun with LCD Touch",
        "title_ar": "مسدس تدليك العضلات العميق الاحترافي بـ 9 سرعات وشاشة لمس ذكية",
        "desc": "Pro-athlete 3,200 RPM percussive recovery gun with 9 digital speed tiers, LCD touchscreen, and 4 therapy heads for muscle soreness.",
        "url": "https://zelmiqo.com/products/smart-fascia-deep-tissue-massage-gun",
        "price": "SAR 139.00 (SAR 34.75 x 4 Tabby/Tamara)"
    },
    {
        "file": "product-usb-coffee-mug-warmer.html",
        "icon": "☕️",
        "badge": "Smart Living • 11 Sections",
        "title_en": "ThermoDesk Smart Heated Beverage Coaster & Mug Warmer",
        "title_ar": "قاعدة تسخين الأكواب والمشروبات الذكية للمكتب مع 3 درجات حرارة",
        "desc": "Smart constant temperature heating plate with 3 custom warmth levels (55/65/75°C), tempered glass, and 8-hour auto-shutoff safety.",
        "url": "https://zelmiqo.com/products/thermodesk-smart-heated-beverage-coaster",
        "price": "SAR 184.00 (SAR 46.00 x 4 Tabby/Tamara)"
    },
    {
        "file": "product-wireless-weather-station-alarm.html",
        "icon": "🌈",
        "badge": "Smart Living • 11 Sections",
        "title_en": "MeteoTouch Wireless Color Touchscreen Weather Station & Dual Alarm",
        "title_ar": "محطة الأرصاد الجوية المنزلية الذكية اللاسلكية بشاشة لمس ملونة ومنبه",
        "desc": "High-precision meteorological home console with 60m remote outdoor transmitter, barometer trend forecasting, and dual alarm clock.",
        "url": "https://zelmiqo.com/products/wireless-touchscreen-weather-station-clock",
        "price": "SAR 149.00 (SAR 37.25 x 4 Tabby/Tamara)"
    },
    {
        "file": "product-foldable-car-sun-shade.html",
        "icon": "🚗",
        "badge": "Automotive Tech • 11 Sections",
        "title_en": "TitaniumShield Foldable Car Windshield Sun Shade Umbrella (UPF 50+)",
        "title_ar": "مظلة الزجاج الأمامي العازلة للحرارة وأشعة الشمس للسيارات",
        "desc": "Pops open in 3 seconds to block 99% UV rays and drop cabin heat by up to 30°C. Protects dashboard and leather from 50°C summer sun.",
        "url": "https://zelmiqo.com/products/foldable-car-windshield-sun-shade-umbrella",
        "price": "SAR 115.00 (SAR 28.75 x 4 Tabby/Tamara)"
    },
    # Kitchen & Auto
    {
        "file": "product-portable-6-blade-juicer.html",
        "icon": "🌪️",
        "badge": "Kitchen Tech • 11 Sections",
        "title_en": "NutriBlend 6-Blade Portable USB Smoothie Maker & Fruit Juicer",
        "title_ar": "خلاط العصائر والسموذي المحمول بـ 6 شفرات فولاذية وشحن USB",
        "desc": "High-torque 22,000 RPM ice-crushing portable blender with food-grade Tritan cup and 4,000mAh battery for 15 fresh smoothies.",
        "url": "https://zelmiqo.com/products/nutriblend-portable-6-blade-juicer",
        "price": "SAR 149.00 (SAR 37.25 x 4 Tabby/Tamara)"
    },
    {
        "file": "product-portable-double-cup-juicer.html",
        "icon": "🥤",
        "badge": "Kitchen Tech • 11 Sections",
        "title_en": "DuoCup Portable Double-Cup Blender & Travel Smoothie Maker",
        "title_ar": "خلاط العصائر المحمول بنظام الكوبين المزدوجين DuoCup والشحن السريع",
        "desc": "Blend one, take both. Comes with two detachable sports Tritan bottles and individual sip lids for couples and active lifestyles.",
        "url": "https://zelmiqo.com/products/portable-double-cup-juicer-blender",
        "price": "SAR 172.00 (SAR 43.00 x 4 Tabby/Tamara)"
    },
    {
        "file": "product-portable-usb-citrus-juicer.html",
        "icon": "🍊",
        "badge": "Kitchen Tech • 11 Sections",
        "title_en": "FreshPress Wireless Automatic Citrus Juicer & Orange Extractor",
        "title_ar": "عصارة الحمضيات والبرتقال الكهربائية اللاسلكية الأوتوماتيكية بضغطة زر",
        "desc": "Hands-free motorized 360° slow-masticating orange and pomegranate squeezer. 100% pure fresh juice with zero manual hand strain.",
        "url": "https://zelmiqo.com/products/wireless-automatic-citrus-juicer-press",
        "price": "SAR 109.00 (SAR 27.25 x 4 Tabby/Tamara)"
    },
    {
        "file": "product-cordless-handheld-car-vacuum.html",
        "icon": "🧹",
        "badge": "Automotive Care • 11 Sections",
        "title_en": "TurboClean Pro Cordless Handheld Car Vacuum Cleaner (9,000Pa)",
        "title_ar": "مكنسة السيارة اللاسلكية المحمولة بقوة شفط 9000 باسكال وفلتر HEPA",
        "desc": "Cyclone 9,000Pa suction easily picks up desert sand, biscuit crumbs, and pet hair. Includes washable HEPA filter and detailing crevice tools.",
        "url": "https://zelmiqo.com/products/cordless-handheld-car-vacuum-cleaner",
        "price": "SAR 159.00 (SAR 39.75 x 4 Tabby/Tamara)"
    },
    {
        "file": "product-portable-wireless-car-vacuum.html",
        "icon": "🚀",
        "badge": "Automotive Care • 11 Sections",
        "title_en": "ProVac 2-in-1 Wireless Car Vacuum Cleaner & Air Duster Blower",
        "title_ar": "مكنسة ومنفاخ هواء السيارة اللاسلكي 2 في 1 بمحرك براشلس توربيني",
        "desc": "Dual-function 75,000 RPM brushless turbine vacuums debris and blasts high-speed air to detail AC vents and clean keyboards.",
        "url": "https://zelmiqo.com/products/portable-wireless-car-vacuum-air-duster",
        "price": "SAR 179.00 (SAR 44.75 x 4 Tabby/Tamara)"
    }
]

# Generate HTML cards for all products
cards_html = ""
for p in products_data:
    cards_html += f"""
      <!-- {p['file']} -->
      <div class="page-card" style="border: 1px solid var(--border);">
        <div class="card-banner" style="background: #1e293b;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 18px;">{p['icon']}</span>
            <h3 style="color: #fff; font-size: 15px;">{p['title_en']}</h3>
          </div>
          <span class="card-badge" style="background: var(--gold); color: var(--primary);">{p['badge']}</span>
        </div>
        <div class="card-content">
          <div style="font-size: 13px; font-weight: 700; color: var(--gold); margin-bottom: 8px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; direction: rtl;">
            {p['title_ar']}
          </div>
          <div class="card-desc">
            {p['desc']}
          </div>
          <div class="card-meta">
            <strong>Target URL:</strong> {p['url']}<br>
            <strong>Pricing:</strong> {p['price']}<br>
            <strong>Delivery:</strong> Fast 7–8 Days Across Saudi Arabia
          </div>
          <a href="{p['file']}" class="open-btn">Open Product Workstation →</a>
        </div>
      </div>
"""

# Replace in index.html right after pilot 12
marker = '<!-- 12. Portable Bladeless Neck Fan with Smart Digital LED Display -->'
pos = html.find(marker)
if pos != -1:
    end_of_pilot2 = html.find('</div>\n    </div>', pos) + 6
    html = html[:end_of_pilot2] + "\n\n" + cards_html + html[end_of_pilot2:]
    with open(hub_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html updated successfully with all 20 product workstations!")
else:
    print("Could not find marker in index.html!")
