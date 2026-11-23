# -*- coding: utf-8 -*-
import os
import re

with open("new-content-html-pages/product-3-in-1-fast-charging-dock.html", "r", encoding="utf-8") as f:
    template_html = f.read()

def generate_product_page(badge_text, updates, old_boxes, out_filename):
    html = template_html
    # Update badge
    html = re.sub(
        r'<span class="badge">[^<]+</span>',
        f'<span class="badge">Pilot Template • {badge_text}</span>',
        html
    )
    # Update old content boxes if provided
    for old_b, new_b in old_boxes.items():
        html = html.replace(old_b, new_b)
    # Update preview IDs
    for pid, pval in updates.items():
        pat = rf'(<div class=[\"\']content-preview[^\"]*[\"\'] id=[\"\']{pid}[\"\']>)([\s\S]*?)(</div>)'
        if re.search(pat, html):
            html = re.sub(pat, rf'\g<1>{pval}\g<3>', html)
        else:
            print(f"Warning: id {pid} not found in template for {out_filename}")
            
    out_path = os.path.join("new-content-html-pages", out_filename)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {out_path} ({len(html)} bytes)")

# -------------------------------------------------------------
# 1. 5-in-1 EMS Facial Massager (PRD-04)
# -------------------------------------------------------------
p_ems = {
    "hero-title-en": "5-in-1 EMS Skin Tightening Massager with LED Light Therapy",
    "hero-title-ar": "جهاز شد ونحت الوجه 5 في 1 مع نبضات EMS وعلاج ضوئي LED",
    "hero-subtitle-en": "Clinic-Grade Facelift & Firming at Home<br>Microcurrent lifting, 42°C thermal infusion & tri-color LED phototherapy for contoured V-line and collagen renewal. Fast 7–8 days delivery across Saudi Arabia.",
    "hero-subtitle-ar": "شد وتحديد ملامح الوجه بجودة العيادات من منزلك<br>مساج نبضات EMS الدقيقة وتدفئة حرارية 42° مع إضاءة LED ثلاثية لتجديد الكولاجين، مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "hero-callout-en": "5-in-1 Facial Rejuvenation & V-Line Sculptor",
    "hero-callout-ar": "جهاز تجديد ونحت الوجه 5 في 1 المتكامل",
    "hero-bullets-en": "• ⚡️ Microcurrent EMS Face Sculpting\n• 🔴 Red, Blue & Orange LED Therapy\n• 🌡️ 42°C Warm Serum Infusion\n• 🔋 USB Rechargeable & Ergonomic Grip",
    "hero-bullets-ar": "• ⚡️ نبضات EMS لشد ونحت ملامح الوجه\n• 🔴 علاج ضوئي LED أحمر، أزرق وبرتقالي\n• 🌡️ تدفئة لطيفة 42° لامتصاص عميق للسيروم\n• 🔋 شحن USB وتصميم مريح لليد",
    
    "faq-head-en": "CLINICAL SKIN REJUVENATION AT HOME<br>Sculpted Contours & Youthful Glow<br>Target sagging skin, fine lines, and dull texture with 5 clinically proven spa therapies in one sleek handheld device. Fast 7–8 days delivery across Saudi Arabia.",
    "faq-head-ar": "عناية متقدمة بالبشرة بجودة المراكز المتخصصة<br>ملامح منحوتة ونضارة شبابية تدوم<br>تخلصي من ترهل البشرة والخطوط الدقيقة وبهتان الوجه مع 5 تقنيات علاجية مثبتة في جهاز واحد أنيق. توصيل سريع وموثوق خلال 7–8 أيام لكافة مناطق المملكة.",
    "faq-1-en": "How does EMS microcurrent technology lift and firm the facial muscles?<br>Gentle bio-electric microcurrents painlessly stimulate underlying facial muscles and trigger ATP cellular renewal, promoting a visibly sculpted jawline and firmer skin.",
    "faq-1-ar": "كيف تعمل نبضات EMS الدقيقة على شد عضلات البشرة؟<br>ترسل النبضات الدقيقة إشارات حيوية آمنة وغير مؤلمة لتحفيز عضلات الوجه وإنتاج الكولاجين الطبيعي، مما يرفع خط الفك ويمنحك شداً ملحوظاً.",
    "faq-2-en": "What are the benefits of the tri-color LED light therapy modes?<br>Red Light (630nm) stimulates collagen to smooth fine lines; Blue Light (470nm) calms active blemishes and purifies pores; Orange Light (590nm) restores radiant glow and evens skin tone.",
    "faq-2-ar": "ما هي فوائد ألوان العلاج الضوئي LED الثلاثية للبشرة؟<br>الضوء الأحمر يحفز الكولاجين وينعم الخطوط، والضوء الأزرق يهدئ الشوائب ويعقم المسام، والضوء البرتقالي يمنح البشرة إشراقة نضرة ويوحد لونها.",
    "faq-3-en": "Should I apply face oil, gel, or serum before using the device?<br>Yes, always apply an aloe vera gel, hydrating serum, or facial moisturizer. Moisture ensures optimal microcurrent conductivity and allows the 42°C warm thermal plate to infuse active nutrients deep into skin.",
    "faq-3-ar": "هل يجب استخدام سيروم أو جل مرطب قبل تشغيل الجهاز؟<br>نعم بالتأكيد، يُفضل دائماً وضع جل الصبار أو السيروم المرطب المفضل لديك، حيث يضمن التوصيل المثالي لنبضات EMS والتدفئة الحرارية لامتصاص عميق ومريح.",
    "faq-4-en": "Is the device safe for daily skincare routines in dry Saudi climates?<br>Completely safe. It features smart timer auto-shutoff and calibrated heat levels designed for delicate skin exposed to dry desert air and indoor AC environments.",
    "faq-4-ar": "هل الجهاز آمن للاستخدام اليومي في مناخ المملكة الجاف؟<br>آمن تماماً ومعتمد، حيث يحتوي على مؤقت إيقاف تلقائي ذكي ودرجات حرارة مضبوطة تحمي حاجز البشرة الطبيعي من الجفاف وبرودة أجهزة التكييف.",

    "twocol-head-en": "DAILY BEAUTY ESSENTIAL • SALON RESULTS AT HOME<br>Effortless 10-Minute Daily Face Sculpting Routine<br>Achieve a contoured jawline, refined skin texture, and long-lasting radiance from the comfort of home. Fast 7–8 days delivery across Saudi Arabia.",
    "twocol-head-ar": "روتين الجمال اليومي • نتائج العيادات براحة منزلك<br>10 دقائق يومياً لنحت الوجه وتجديد شباب البشرة<br>احصلي على خط فك محدد وبشرة مشدودة وأكثر نضارة دون الحاجة لجلسات باهظة، مع توصيل سريع وموثوق خلال 7–8 أيام لكافة مدن المملكة.",
    "twocol-cards-en": "Card 1: 🚚 Fast 7–8 Days Delivery\nCard 2: 🛡️ 14-Day Golden Guarantee\nCard 3: 💳 Secure Mada & Apple Pay",
    "twocol-cards-ar": "البطاقة 1: 🚚 توصيل سريع خلال 7–8 أيام\nالبطاقة 2: 🛡️ الضمان الذهبي 14 يوماً\nالبطاقة 3: 💳 دفع آمن بمدى وأبل باي",

    "center-head-en": "5 ADVANCED CLINICAL TECHNOLOGIES IN ONE DEVICE<br>Lift, Tighten & Infuse with Precision Care<br>Ergonomic curved treatment head adapts seamlessly to cheeks, jawline, forehead, and neck contours.",
    "center-head-ar": "5 تقنيات تجميلية متطورة في جهاز واحد مدمج<br>شد، ونحت، وتغلغل عميق للسيروم بعناية فائقة<br>رأس تدليك منحني بانسيابية ليتطابق بدقة مع زوايا الخدين، خط الفك، الجبين، ومنطقة الرقبة.",
    "center-b1-en": "Microcurrent EMS Lifting<br>Reactivates facial muscle tone for a defined, lifted V-line silhouette.",
    "center-b1-ar": "شد نبضات EMS الدقيقة<br>ينشط عضلات الوجه المرتخية لنحت خط الفك واستعادة مظهر الشباب.",
    "center-b2-en": "Tri-Color LED Phototherapy<br>Red for collagen, blue for clearing pores, and orange for bright radiance.",
    "center-b2-ar": "علاج ضوئي ثلاثي الألوان<br>أحمر لتحفيز الكولاجين، أزرق لتنقية المسام، وبرتقالي لإشراقة ونضارة الوجه.",
    "center-b3-en": "42°C Thermal Infusion<br>Gentle therapeutic heat opens pores to boost skincare product absorption by 300%.",
    "center-b3-ar": "تدفئة حرارية 42° مريحة<br>تفتح المسام بلطف لتسريع امتصاص السيروم والزيوت المغذية بنسبة تصل إلى 300%.",
    "center-b4-en": "Sonic Micro-Vibrations<br>Relieves facial muscle tension and drains puffiness around eyes and cheeks.",
    "center-b4-ar": "مساج اهتزازي لطيف<br>يخفف توتر ملامح الوجه ويقلل انتفاخات الصباح حول العينين والوجنتين.",

    "grid-head-en": "VISIBLE RESULTS YOU WILL NOTICE IN WEEKS<br>Transformative Benefits for Every Skin Type<br>Incorporate this soothing treatment into your morning prep or nighttime winding down.",
    "grid-head-ar": "نتائج ملموسة تلاحظينها خلال أسابيع قليلة<br>فوائد حقيقية تناسب كافة أنواع البشرة<br>أضيفي هذا التدليك المنعش إلى روتينك الصباحي أو قبل النوم لراحة ونضارة لا مثيل لها.",
    "grid-b1-en": "Sculpted Jawline & V-Shape<br>Firms sagging skin along the neck and chin for a youthful profile.",
    "grid-b1-ar": "تحديد ونحت خط الفك<br>يشد ترهلات الذقن وأسفل الرقبة لمظهر V-Shape ممشوق وأكثر جاذبية.",
    "grid-b2-en": "Deeper Serum Absorption<br>Maximizes the benefits of expensive anti-aging creams and hydrating ampoules.",
    "grid-b2-ar": "امتصاص أعمق لمرطباتك<br>يضاعف فعالية سيرومات النضارة وكريمات الترطيب الغالية لتغذي خلايا البشرة.",
    "grid-b3-en": "Reduces Morning Puffiness<br>Lymphatic drainage action banishes sleep puffiness and dark under-eye circles.",
    "grid-b3-ar": "إزالة انتفاخات الصباح<br>ينشط الدورة الدموية اللمفاوية لتقليل التورم والإرهاق حول محيط العينين.",
    "grid-b4-en": "Smooth Fine Lines<br>Consistent collagen stimulation smooths smile lines and forehead furrows.",
    "grid-b4-ar": "تنعيم الخطوط التعبيرية<br>يحفز إنتاج الإيلاستين الطبيعي ليقلل ظهور تجاعيد الجبين وحول الفم.",

    "table-head-en": "WHY CHOOSE ZELMIQO LUMINALIFT<br>Premium Quality Engineered for Daily Beauty<br>Compare our multi-wave technology and safe temperature calibration against generic wands.",
    "table-head-ar": "لماذا تختارين جهاز زيلميكو لومي ليفت؟<br>جودة وتقنيات معتمدة تضمن سلامة بشرتك<br>قارني بين تقنياتنا المتعددة وحمايتنا الذكية للبشرة مقابل الأجهزة التقليدية في السوق.",
    "table-rows-en": "Row 1: ⚡️ 5-in-1 Multi-Technology | Zelmiqo (✓ EMS, 3x LED, Heat & Vibration) | Generic Wands (✕ Single vibration only)\nRow 2: 🌡️ Safe 42°C Thermal Control | Zelmiqo (✓ Built-in temperature sensor) | Generic Wands (✕ Overheats or no warming)\nRow 3: 🔴 Triple Phototherapy | Zelmiqo (✓ Pure 630nm/470nm/590nm LEDs) | Generic Wands (✕ Weak aesthetic colored bulbs)\nRow 4: 🔋 Rechargeable Battery Life | Zelmiqo (✓ Up to 15 sessions per charge) | Generic Wands (✕ Needs disposable batteries)\nRow 5: 🚚 Fast KSA Delivery | Zelmiqo (✓ Fast 7–8 days across Saudi Arabia) | Generic Wands (✕ Weeks of unverified transit)",
    "table-rows-ar": "الصف 1: ⚡️ 5 تقنيات في جهاز واحد | جهاز زيلميكو (✓ نبضات EMS، 3 ألوان LED، تدفئة واهتزاز) | الأجهزة العادية (✕ اهتزاز سطحي بسيط فقط)\nالصف 2: 🌡️ تحكم حراري آمن 42° | جهاز زيلميكو (✓ حساس ذكي يمنع ارتفاع الحرارة) | الأجهزة العادية (✕ حرارة غير مستقرة أو بدون تدفئة)\nالصف 3: 🔴 علاج ضوئي ثلاثي نقي | جهاز زيلميكو (✓ أطوال موجية علاجية دقيقة للبشرة) | الأجهزة العادية (✕ لمبات ملونة بدون أي تأثير علاجي)\nالصف 4: 🔋 بطارية تدوم طويلاً | جهاز زيلميكو (✓ حتى 15 جلسة متتالية بالشحنة الواحدة) | الأجهزة العادية (✕ بطاريات عادية تفرغ بسرعة)\nالصف 5: 🚚 شحن سريع لكافة المدن | جهاز زيلميكو (✓ توصيل خلال 7–8 أيام لكافة مدن المملكة) | الأجهزة العادية (✕ شحن بطيء لأسابيع دون ضمان)",

    "marquee-text-en": "🚚 Fast 7–8 Days Delivery Across Saudi Arabia • 🛡️ 14-Day Golden Guarantee • 💳 Split in 4 with Tabby & Tamara • 🔒 100% Secure Mada & Apple Pay Checkout",
    "marquee-text-ar": "🚚 توصيل سريع خلال 7–8 أيام لكافة مدن المملكة • 🛡️ الضمان الذهبي 14 يوماً • 💳 قسّم فاتورتك مع تابي وتمارا • 🔒 دفع آمن 100% عبر مدى وأبل باي",
    "cust-head-en": "OUR HAPPY CUSTOMERS<br>Real Skincare Transformations Across Saudi Arabia<br>Read verified reviews from clients who rejuvenated their daily self-care rituals.",
    "cust-head-ar": "تجارب عميلاتنا المعتمدة<br>نتائج حقيقية وتألق يومي لسيدات في مختلف مدن المملكة<br>آراء موثقة لعميلات استعدن نضارة وشد بشرتهن مع جهاز زيلميكو المتطور.",
    "rev-stats-en": "⭐️⭐️⭐️⭐️⭐️ 4.9 out of 5 Stars (Based on 142 Verified Purchases across Saudi Arabia)<br>96% would recommend to a friend • Fast 7–8 days delivery to Riyadh, Jeddah, Dammam & all Saudi cities.",
    "rev-stats-ar": "⭐️⭐️⭐️⭐️⭐️ 4.9 من 5 نجوم (استناداً إلى 142 تقييم موثق لعملاء داخل المملكة العربية السعودية)<br>96% يوصون بالجهاز لصديقاتهم • توصيل سريع وموثوق خلال 7–8 أيام للرياض، جدة، الدمام وكافة المدن.",
    "rel-head-en": "COMPLETE YOUR BEAUTY RITUAL<br>You May Also Like<br>Smart skincare accessories designed to elevate your everyday glow—delivered in 7–8 days across Saudi Arabia.",
    "rel-head-ar": "أكملي روتين جمالك المتألق<br>منتجات مختارة قد تنال إعجابك<br>أجهزة وتقنيات ذكية للعناية بالبشرة صُممت لتمنحك إشراقة دائمة — مع توصيل خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-title-en": "5-in-1 EMS Skin Tightening Massager with LED Light Therapy | Zelmiqo® KSA",
    "seo-title-ar": "جهاز شد ونحت الوجه 5 في 1 مع مساج EMS وعلاج ضوئي LED | زيلميكو السعودية",
    "seo-desc-en": "Clinic-grade facelift at home with 5-in-1 EMS microcurrent, 42°C heat, and tri-color LED phototherapy. Fast 7–8 days delivery across Saudi Arabia with Tabby and Tamara.",
    "seo-desc-ar": "شد ونحت فوري للوجه بتقنيات العيادات المتطورة مع نبضات EMS وعلاج ضوئي ثلاثي. توصيل سريع خلال 7–8 أيام لكافة مدن المملكة مع تقسيط تابي وتمارا وضمان 14 يوماً.",
    "seo-keywords-en": "5 in 1 ems facial massager saudi arabia, microcurrent face lift device ksa, led light therapy wand, skin rejuvenation tool 7-8 days delivery, tabby tamara beauty devices",
    "seo-keywords-ar": "جهاز شد الوجه ems السعودية, جهاز مساج الوجه الضوئي, علاج ضوئي ليد للبشرة, جهاز تحديد الفك, تقسيط تابي وتمارا, متجر زيلميكو توصيل 7-8 ايام"
}

# -------------------------------------------------------------
# 2. Deep Pore Blackhead Remover (PRD-07)
# -------------------------------------------------------------
p_blackhead = {
    "hero-title-en": "PorePure Vacuum Blackhead Remover with LED Screen & 5 Levels",
    "hero-title-ar": "جهاز شفط وتنظيف الرؤوس السوداء والمسام مع شاشة LED ذكية",
    "hero-subtitle-en": "Dermatologist-Safe Pore Vacuum Extraction<br>Painless powerful suction clears stubborn blackheads, excess sebum, and trapped dirt effortlessly. Fast 7–8 days delivery across Saudi Arabia.",
    "hero-subtitle-ar": "تنظيف عميق للمسام وشفط آمن للرؤوس السوداء<br>قوة شفط فعالة ولطيفة تزيل الدهون المتراكمة والأوساخ وتمنح بشرتك نقاءً فورياً، مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "hero-callout-en": "Pore Vacuum Cleanser with 5 Suction Tiers",
    "hero-callout-ar": "جهاز تنظيف المسام بخمس مستويات شفط ذكية",
    "hero-bullets-en": "• 🌪️ 65kPa Safe Vacuum Extraction\n• 💡 Smart HD LED Power Display\n• 🎚️ 5 Adjustable Suction Levels\n• 💎 4 Interchangeable Beauty Probes",
    "hero-bullets-ar": "• 🌪️ قوة شفط دقيقة وآمنة حتى 65 كيلو باسكال\n• 💡 شاشة LED رقمية لعرض المستوى والبطارية\n• 🎚️ 5 مستويات تناسب البشرة الحساسة والدهنية\n• 💎 4 رؤوس مختلفة تناسب زوايا الأنف والوجه",
    
    "faq-head-en": "DEEP CLEANSING PORE PURIFICATION<br>Clear, Blemish-Free Skin Without Pinching<br>Say goodbye to painful metal extractors and red marks with dermatologically calibrated vacuum suction. Fast 7–8 days delivery across Saudi Arabia.",
    "faq-head-ar": "نقاء فوري وتنظيف عميق للمسام<br>بشرة صافية خالية من الشوائب بدون ضغط مؤلم<br>ودعي ملاقط إزالة الرؤوس السوداء المؤلمة وعلامات الاحمرار مع جهاز الشفط الذكي المصمم لحماية البشرة. توصيل سريع وموثوق خلال 7–8 أيام لكافة مناطق المملكة.",
    "faq-1-en": "How do I prep my skin before using the pore vacuum?<br>Take a warm shower or apply a warm towel for 3–5 minutes to gently open your pores, allowing trapped sebum and blackheads to slide out smoothly without resistance.",
    "faq-1-ar": "كيف أجهز بشرتي قبل استخدام جهاز شفط المسام؟<br>اغسلي وجهك بالماء الدافئ أو ضعي فوطة دافئة لمدة 3 إلى 5 دقائق لفتح المسام برفق، مما يساعد على خروج الدهون والرؤوس السوداء بسهولة وانسيابية.",
    "faq-2-en": "Will the suction leave red marks or bruises on my skin?<br>No, as long as you keep the device gliding smoothly across the skin. Never hold the probe in one single spot for more than 2 seconds.",
    "faq-2-ar": "هل يسبب الشفط احمراراً أو كدمات على الوجه؟<br>لا، بشرط تحريك الجهاز باستمرار بنعومة وعدم تثبيته على نفس النقطة لأكثر من ثانيتين، والبدء بالمستوى الأول لاختبار حساسية البشرة.",
    "faq-3-en": "Which probe should I use for my nose and T-Zone?<br>Use the small round probe for delicate nostril contours and tight crevices, and the medium or oval probe for cheeks, forehead, and larger T-Zone areas.",
    "faq-3-ar": "ما هو الرأس الأنسب لتنظيف زوايا الأنف ومنطقة T-Zone؟<br>الرأس الدائري الصغير مثالي لانحناءات الأنف والزوايا الدقيقة، بينما الرأس البيضاوي والمتوسط مناسب لمنطقة الجبين، الوجنتين والذقن.",
    "faq-4-en": "How often should I use the blackhead vacuum?<br>For oily or combination skin, 1–2 times weekly is ideal. For dry or sensitive skin, once every 10–14 days is recommended to maintain clean, breathing pores.",
    "faq-4-ar": "كم مرة أسبوعياً يُنصح باستخدام الجهاز؟<br>للبشرة الدهنية والمختلطة يُنصح باستخدامه مرة إلى مرتين أسبوعياً، وللبشرة الجافة أو الحساسة مرة واحدة كل 10 إلى 14 يوماً للحفاظ على نضارة المسام.",

    "twocol-head-en": "EFFORTLESS PORE EXTRACTION • NO PAIN, NO BLEMISHES<br>Restore Smooth, Silky Facial Texture in Minutes<br>Target clogged pores, excess oil, and impurities without irritation. Fast 7–8 days delivery across Saudi Arabia.",
    "twocol-head-ar": "تنظيف مسام احترافي • بدون ألم وبدون علامات<br>استعيدي ملمس بشرتك المخملي والناعم في دقائق<br>تخلصي من انسداد المسام والدهون الزائدة المزعجة بنعومة تامة، مع توصيل سريع وموثوق خلال 7–8 أيام لكافة مدن المملكة.",
    "twocol-cards-en": "Card 1: 🚚 Fast 7–8 Days Delivery\nCard 2: 🛡️ 14-Day Golden Guarantee\nCard 3: 💳 Secure Mada & Apple Pay",
    "twocol-cards-ar": "البطاقة 1: 🚚 توصيل سريع خلال 7–8 أيام\nالبطاقة 2: 🛡️ الضمان الذهبي 14 يوماً\nالبطاقة 3: 💳 دفع آمن بمدى وأبل باي",

    "center-head-en": "PRECISION VACUUM PURIFICATION<br>Cleanse Pores Gently Without Squeezing<br>Engineered with constant air pressure technology to protect delicate skin capillaries while extracting deep debris.",
    "center-head-ar": "تقنية شفط دقيقة لتنقية المسام<br>تنظيف آمن يحمي البشرة من الضغط المزعج<br>صُمم بنظام ضغط هواء مستقر يحافظ على الشعيرات الدموية الرقيقة ويزيل الأوساخ العميقة بكفاءة.",
    "center-b1-en": "5 Power Suction Levels<br>Customized intensity from gentle sensitive care to stubborn pore clearing.",
    "center-b1-ar": "5 مستويات شفط متدرجة<br>قوة قابلة للتعديل تناسب البشرة الرقيقة وتتعامل مع الرؤوس السوداء العنيدة.",
    "center-b2-en": "4 Ergonomic Probe Heads<br>Interchangeable shapes target corners of the nose, cheeks, and forehead.",
    "center-b2-ar": "4 رؤوس تبديل مختلفة<br>أشكال هندسية مخصصة للوصول لأدق زوايا الأنف والجبهة والخدين بسهولة.",
    "center-b3-en": "Crystal Clear LED Screen<br>Instantly displays selected power level and remaining battery percentage.",
    "center-b3-ar": "شاشة LED رقمية واضحة<br>توضح مستوى الشفط المختار ونسبة البطارية المتبقية بلمحة سريعة.",
    "center-b4-en": "USB Rechargeable Freedom<br>Long-lasting lithium battery delivers over 120 minutes of continuous runtime.",
    "center-b4-ar": "شحن USB ببطارية قوية<br>بطارية ليثيوم متطورة تدوم لأكثر من ساعتين من الاستخدام المتواصل دون انقطاع.",

    "grid-head-en": "EVERYDAY BENEFITS YOU WILL FEEL IMMEDIATELY<br>Smooth, Clear Skin After Every Session<br>Experience clearer pores that absorb moisturizers and makeup flawlessly.",
    "grid-head-ar": "مزايا يومية تشعرين بفرقها فورياً<br>بشرة ناعمة ونقية بعد كل جلسة استخدام<br>مسام نظيفة تتنفس بحرية وتستقبل المكياج والسيروم بسلاسة ومظهر ناعم.",
    "grid-b1-en": "Clear Clogged Pores<br>Extracts oxidized black sebum and debris for a refined complexion.",
    "grid-b1-ar": "تفريغ المسام المسدودة<br>يزيل الدهون المؤكسدة والأوساخ المتراكمة ليمنحك وجهاً نضراً وخالياً من النمش.",
    "grid-b2-en": "Minimizes Visible Pore Size<br>Clean pores naturally contract, creating a tighter, smoother appearance.",
    "grid-b2-ar": "تضييق مظهر المسام الواسعة<br>المسام النظيفة تنقبض طبيعياً ليصبح مظهر الوجه متجانساً وخالياً من الفتحات الواسعة.",
    "grid-b3-en": "Flawless Makeup Application<br>Eliminates bumpy texture on the nose and chin for silky smooth foundation.",
    "grid-b3-ar": "توزيع مكياج انسيابي ومثالي<br>يزيل التكتلات والبروزات حول الأنف والذقن لثبات فاخر لكريم الأساس وبدون بهتان.",
    "grid-b4-en": "Safe for Delicate Skin<br>Smooth probe edges glide comfortably without scratching or scarring.",
    "grid-b4-ar": "آمن وناعم على البشرة<br>حواف الرؤوس ملساء مصقولة بعناية لتنزلق دون خدش أو ترك آثار مزعجة.",

    "table-head-en": "WHY CHOOSE ZELMIQO POREPURE<br>Safe, Consistent Suction That Protects Your Skin<br>Compare our calibrated air pressure system and digital monitoring with uncalibrated alternatives.",
    "table-head-ar": "لماذا يفضل عملاؤنا جهاز زيلميكو بوربيور؟<br>شفط متوازن وآمن يحمي حاجز بشرتك<br>قارني بين نظام الضغط الثابت والشاشة الرقمية المعتمدة لدينا مقابل الأجهزة المقلدة.",
    "table-rows-en": "Row 1: 🌪️ Safe Calibrated Suction | Zelmiqo (✓ Stable 65kPa max pressure) | Generic Vacuums (✕ Erratic suction bruises skin)\nRow 2: 💡 Smart HD Display | Zelmiqo (✓ Exact suction tier & battery indicator) | Generic Vacuums (✕ Blind buttons, no feedback)\nRow 3: 💎 Medical-Grade Probes | Zelmiqo (✓ 4 smooth skin-friendly nozzles) | Generic Vacuums (✕ Rough, scratchy plastic heads)\nRow 4: 🔋 USB Quick Charge | Zelmiqo (✓ Modern Type-C rechargeable) | Generic Vacuums (✕ Outdated ports, weak battery)\nRow 5: 🚚 Fast KSA Delivery | Zelmiqo (✓ Fast 7–8 days across Saudi Arabia) | Generic Vacuums (✕ Slow overseas transit with no guarantee)",
    "table-rows-ar": "الصف 1: 🌪️ شفط آمن ومتوازن | جهاز زيلميكو (✓ ضغط ثابت 65 كيلو باسكال يحمي البشرة) | الأجهزة المقلدة (✕ شفط عشوائي يسبب كدمات واحمرار)\nالصف 2: 💡 شاشة رقمية تفاعلية | جهاز زيلميكو (✓ توضح مستوى القوة وحالة البطارية بدقة) | الأجهزة المقلدة (✕ أزرار عمياء بدون أي شاشة عرض)\nالصف 3: 💎 رؤوس طبية آمنة | جهاز زيلميكو (✓ 4 رؤوس ناعمة مصممة بعناية فائقة) | الأجهزة المقلدة (✕ بلاستيك خشن قد يخدش سطح الجلد)\nالصف 4: 🔋 شحن USB سريع | جهاز زيلميكو (✓ منفذ تايب سي حديث وبطارية تدوم طويلاً) | الأجهزة المقلدة (✕ منافذ قديمة وبطارية تفرغ فوراً)\nالصف 5: 🚚 شحن سريع لكافة المدن | جهاز زيلميكو (✓ توصيل خلال 7–8 أيام لكافة مدن المملكة) | الأجهزة المقلدة (✕ انتظار أسابيع طويلة دون أي ضمان)",

    "marquee-text-en": "🚚 Fast 7–8 Days Delivery Across Saudi Arabia • 🛡️ 14-Day Golden Guarantee • 💳 Split in 4 with Tabby & Tamara • 🔒 100% Secure Mada & Apple Pay Checkout",
    "marquee-text-ar": "🚚 توصيل سريع خلال 7–8 أيام لكافة مدن المملكة • 🛡️ الضمان الذهبي 14 يوماً • 💳 قسّم فاتورتك مع تابي وتمارا • 🔒 دفع آمن 100% عبر مدى وأبل باي",
    "cust-head-en": "OUR HAPPY CUSTOMERS<br>Real Pore Cleansing Results Across Saudi Arabia<br>Read verified reviews from clients who transformed their T-Zone clarity.",
    "cust-head-ar": "تجارب عميلاتنا المعتمدة<br>نتائج حقيقية ونقاء ملحوظ للمسام في مدن المملكة<br>قصص موثقة لعملاء تخلصوا من الرؤوس السوداء المزعجة وحصلوا على بشرة نقية.",
    "rev-stats-en": "⭐️⭐️⭐️⭐️⭐️ 4.8 out of 5 Stars (Based on 116 Verified Purchases across Saudi Arabia)<br>95% would recommend to a friend • Fast 7–8 days delivery to Riyadh, Jeddah, Dammam & all Saudi cities.",
    "rev-stats-ar": "⭐️⭐️⭐️⭐️⭐️ 4.8 من 5 نجوم (استناداً إلى 116 تقييم موثق لعملاء داخل المملكة العربية السعودية)<br>95% يوصون بالجهاز لأصدقائهم • توصيل سريع وموثوق خلال 7–8 أيام للرياض، جدة، الدمام وكافة المدن.",
    "rel-head-en": "COMPLETE YOUR PORE PURIFYING ROUTINE<br>You May Also Like<br>Smart beauty tech essentials designed to keep your skin fresh—delivered in 7–8 days across Saudi Arabia.",
    "rel-head-ar": "أكملي مجموعة العناية بمسام بشرتك<br>منتجات مختارة قد تنال إعجابك<br>أجهزة وتقنيات تجميلية ذكية متوافقة ومثالية لنقاء بشرتك — مع توصيل خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-title-en": "PorePure Vacuum Blackhead Remover with LED Screen & 5 Levels | Zelmiqo® KSA",
    "seo-title-ar": "جهاز شفط وتنظيف الرؤوس السوداء والمسام مع شاشة LED ذكية | زيلميكو السعودية",
    "seo-desc-en": "Dermatologist-safe vacuum blackhead remover with 5 power levels and 4 beauty probes. Painlessly extracts deep sebum and dead skin. Fast 7–8 days delivery across Saudi Arabia.",
    "seo-desc-ar": "جهاز شفط وتنظيف الرؤوس السوداء والدهون المتراكمة مع 5 مستويات شفط وشاشة LED تفاعلية. توصيل سريع خلال 7–8 أيام لكافة مدن المملكة مع تقسيط تابي وتمارا.",
    "seo-keywords-en": "pore vacuum blackhead remover saudi arabia, facial pore cleaner ksa, electric blackhead suction tool, pore purifier 7-8 days delivery, tabby tamara skincare devices",
    "seo-keywords-ar": "جهاز شفط الرؤوس السوداء السعودية, تنظيف مسام الوجه, جهاز ازالة دهون الانف, شفط الدهون بالفاكيوم, تقسيط تابي وتمارا, متجر زيلميكو توصيل 7-8 ايام"
}

# -------------------------------------------------------------
# 3. Portable Scalp Massage Comb (PRD-13)
# -------------------------------------------------------------
p_comb = {
    "hero-title-en": "Portable Scalp Massage Comb with Precision Liquid Hair Oil Applicator",
    "hero-title-ar": "مشط مساج فروة الرأس المتنقل مع موزع زيوت وسيروم الشعر الدقيق",
    "hero-subtitle-en": "Direct Follicle Oil Delivery with Soothing Micro-Vibration<br>Distributes rosemary oil, tonics, and hair treatments directly to roots with zero greasy hands. Fast 7–8 days delivery across Saudi Arabia.",
    "hero-subtitle-ar": "توزيع مباشر للزيوت على بصيلات الشعر مع مساج اهتزازي مريح<br>يوزع زيت الروزماري والسيروم المغذي لجذور الشعر بدقة دون تلطيخ يديك، مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "hero-callout-en": "Direct Root Oil Dispenser & Scalp Massager",
    "hero-callout-ar": "موزع زيوت دقيق ومساج لفروة الرأس والشعر",
    "hero-bullets-en": "• 💧 Rolling Ball Liquid Applicator Teeth\n• 💆‍♀️ Gentle Scalp Vibration Massage\n• 🧴 Leak-Proof Serum Reservoir Tank\n• 🧼 Washable Food-Grade Silicone Body",
    "hero-bullets-ar": "• 💧 أسنان كروية متدحرجة لتوزيع الزيوت على الجذور\n• 💆‍♀️ مساج اهتزازي خفيف ينشط تدفق الدورة الدموية\n• 🧴 خزان محكم الإغلاق ومقاوم للتسرب تماماً\n• 🧼 سيليكون طبي ناعم وسهل التنظيف والغسيل",
    
    "faq-head-en": "PRECISION SCALP CARE & HAIR FOLLICLE NOURISHMENT<br>Target Roots Directly Without Mess or Waste<br>Deliver precious hair growth tonics and nourishing oils directly to where hair grows. Fast 7–8 days delivery across Saudi Arabia.",
    "faq-head-ar": "عناية دقيقة بفروة الرأس وتغذية بصيلات الشعر<br>وصول مباشر للجذور بدون فوضى أو إهدار قطرة زيت واحدة<br>وصّلي زيوت الإنبات والسيرومات العلاجية مباشرة إلى البصيلات بعناية ومساج منعش. توصيل سريع وموثوق خلال 7–8 أيام لكافة مناطق المملكة.",
    "faq-1-en": "How do the rolling ball teeth distribute oil without clogging?<br>Each elastic comb tooth features a smooth medical-grade stainless steel rolling sphere that dispenses liquid only when pressed gently against your scalp, preventing leaks and clogging.",
    "faq-1-ar": "كيف تعمل الكرات المتدحرجة على توزيع الزيت دون انسداد؟<br>تحتوي كل سنّة على كرة ستانلس ستيل طبية متدحرجة تسمح بتدفق الزيت فقط عند ملامسة فروة الرأس والضغط اللطيف، مما يمنع التسرب والانسداد نهائياً.",
    "faq-2-en": "Can I use dense natural oils like rosemary, castor, or argan oil?<br>Yes! The applicator works smoothly with essential oils, light castor blends, rosemary water, Minoxidil solutions, and standard hair growth serums.",
    "faq-2-ar": "هل يمكن استخدامه مع الزيوت الطبيعية مثل زيت الروزماري والأرجان؟<br>نعم بالتأكيد! يتوافق المشط بامتياز مع زيت إكليل الجبل (الروزماري)، سيرومات إنبات الشعر، محلول المينوكسيديل، وخلطات الزيوت الطبيعية الخفيفة.",
    "faq-3-en": "How does vibration help stimulate natural hair density?<br>Gentle micro-vibrations relax scalp tension, increase local blood circulation around follicles, and enhance the absorption of active nutrients into the root sheath.",
    "faq-3-ar": "كيف يساعد المساج الاهتزازي على تحفيز كثافة الشعر؟<br>يعمل الاهتزاز الخفيف على استرخاء عضلات فروة الرأس وتنشيط الدورة الدموية حول البصيلات، مما يرفع امتصاص المغذيات ويحفز نمو شعر أقوى وأكثر صحة.",
    "faq-4-en": "How do I clean and wash the liquid tank after use?<br>The reservoir opens with an easy silicone cap. Simply rinse with warm water and a drop of gentle soap, then let it air dry ready for the next session.",
    "faq-4-ar": "كيف يتم تنظيف وغسيل خزان الزيوت بعد الانتهاء؟<br>يتميز الخزان بغطاء سيليكوني مرن قابل للفتح بسهولة؛ يمكنك شطفه بالماء الفاتر وقليل من الصابون اللطيف وتركه ليجف بالهواء بكل بساطة.",

    "twocol-head-en": "ROOT-FOCUSED HAIR WELLNESS • ZERO WASTE, ZERO GREASE<br>A Relaxing 5-Minute Daily Scalp Rejuvenation Therapy<br>Transform your daily hair oiling routine into a luxurious, mess-free scalp massage. Fast 7–8 days delivery across Saudi Arabia.",
    "twocol-head-ar": "عناية موجهة لجذور الشعر • بدون هدر وبدون دهون باليدين<br>جلسة مساج يومية مريحة لمدة 5 دقائق لتنشيط الفروة<br>حولي روتين تزييت الشعر التقليدي إلى جلسة استرخاء فاخرة ونظيفة تماماً، مع توصيل سريع وموثوق خلال 7–8 أيام لكافة مدن المملكة.",
    "twocol-cards-en": "Card 1: 🚚 Fast 7–8 Days Delivery\nCard 2: 🛡️ 14-Day Golden Guarantee\nCard 3: 💳 Secure Mada & Apple Pay",
    "twocol-cards-ar": "البطاقة 1: 🚚 توصيل سريع خلال 7–8 أيام\nالبطاقة 2: 🛡️ الضمان الذهبي 14 يوماً\nالبطاقة 3: 💳 دفع آمن بمدى وأبل باي",

    "center-head-en": "INNOVATIVE ROLL-ON SCALP DELIVERY SYSTEM<br>Massage, Stimulate, and Nourish in One Step<br>Designed to glide effortlessly through all hair types—curly, straight, fine, or thick—without snagging or pulling.",
    "center-head-ar": "نظام توزيع متطور مع مساج كروي متدحرج<br>تدليك، وتنشيط، وتغذية عميقة في خطوة واحدة<br>ينساب بسلاسة فائقة عبر كافة أنواع الشعر؛ الناعم، الكيرلي، والكثيف دون أي تشابك أو شد للشعر.",
    "center-b1-en": "Rolling Ball Teeth<br>Directs serum precisely onto the scalp surface, keeping hair strands clean and dry.",
    "center-b1-ar": "أسنان كروية متدحرجة<br>توجه قطرات السيروم مباشرة لفروة الرأس دون أن تبتل خصلات الشعر بالزيوت.",
    "center-b2-en": "Micro-Vibration Massage<br>Improves microcirculation around hair roots to stimulate healthy follicle growth.",
    "center-b2-ar": "مساج اهتزازي منشط<br>يعزز تدفق الدم للبصيلات ليغذي جذور الشعر ويقلل تساقط الشعر الناتج عن الإجهاد.",
    "center-b3-en": "Leak-Proof Reservoir Tank<br>Holds up to 6ml of treatment oil securely with no accidental pocket spills.",
    "center-b3-ar": "خزان محكم مانع للتسرب<br>يتسع حتى 6 مل من الزيوت والسيروم بدون أي تسريب في حقيبتك أو على الطاولة.",
    "center-b4-en": "Ergonomic Palm Fit<br>Contoured rounded grip sits comfortably in your palm for easy scalp gliding.",
    "center-b4-ar": "قبضة مريحة لراحة اليد<br>تصميم بيضاوي مدمج يستقر بانسيابية في راحة يدك لتحكم كامل ودقيق أثناء المساج.",

    "grid-head-en": "EVERYDAY BENEFITS YOU WILL NOTICE IN WEEKS<br>Fuller, Healthier Hair Starting from the Roots<br>Maximize the true potential of your favorite oils and serums with zero hassle.",
    "grid-head-ar": "مزايا يومية تلمسين فرقها خلال أسابيع<br>شعر أكثر كثافة وحيوية يبدأ من تغذية الجذور<br>استفيدي بنسبة 100% من الزيوت والسيرومات المفضلة لديك دون إهدار أو فوضى.",
    "grid-b1-en": "No Greasy Hands or Pillow Stains<br>Applies liquid directly to the scalp without drenching hair length or staining clothes.",
    "grid-b1-ar": "بدون تلطيخ اليدين أو الوسادة<br>تصل الزيوت للفروة فقط دون أن تدهن أطراف الشعر أو تترك بقعاً على الملابس والوسائد.",
    "grid-b2-en": "Saves 50% on Expensive Oils<br>Eliminates wasteful dripping, making your premium rosemary oils and tonics last twice as long.",
    "grid-b2-ar": "يوفر نصف كمية الزيوت الغالية<br>يمنع إهدار القطرات العشوائية؛ فتستمر عبوة زيت الروزماري أو السيروم لضعف المدة.",
    "grid-b3-en": "Relieves Daily Scalp Tension<br>Gentle massage eases stress, head pressure, and tightness after long work days.",
    "grid-b3-ar": "يخفف شد وضغط الرأس اليومي<br>تدليك لطيف يريح عضلات الفروة ويزيل الإجهاد وصداع التوتر بعد يوم عمل طويل.",
    "grid-b4-en": "Travel-Friendly Pocket Size<br>Compact and lightweight, perfect for keeping in your gym bag or carry-on.",
    "grid-b4-ar": "حجم جيب مدمج وسهل التنقل<br>وزن خفيف وتصميم أنيق يرافقك في حقيبة اليد أو النادي والسفر بكل راحة.",

    "table-head-en": "WHY CHOOSE ZELMIQO SCALPCARE<br>Engineered Precision for Superior Hair Health<br>Compare our stainless rolling spheres and sealed tank with messy manual oil droppers.",
    "table-head-ar": "لماذا يفضل عملاؤنا مشط زيلميكو؟<br>دقة هندسية تمنح شعرك أقصى درجات العناية<br>قارني بين الأسنان الكروية المعدنية والخزان المحكم لدينا مقابل قطارات الزيت التقليدية الفوضوية.",
    "table-rows-en": "Row 1: 💧 Direct Root Delivery | Zelmiqo (✓ Steel rolling ball teeth directly on scalp) | Traditional Dropper (✕ Drips all over hair lengths & face)\nRow 2: 💆‍♀️ Vibrating Stimulation | Zelmiqo (✓ Calibrated micro-vibrations for follicles) | Traditional Dropper (✕ Zero massage stimulation)\nRow 3: 🧴 Clean & Waste-Free | Zelmiqo (✓ Sealed reservoir, zero messy hands) | Traditional Dropper (✕ Sticky fingers, greasy pillows)\nRow 4: 🧼 Easy to Sanitize | Zelmiqo (✓ Washable medical-grade materials) | Traditional Dropper (✕ Hard to clean glass pipettes)\nRow 5: 🚚 Fast KSA Delivery | Zelmiqo (✓ Fast 7–8 days across Saudi Arabia) | Traditional Dropper (✕ Unverified transit with no local support)",
    "table-rows-ar": "الصف 1: 💧 وصول مباشر لجذور الشعر | مشط زيلميكو (✓ كرات ستانلس ستيل توزع الزيت على الفروة) | القطارة التقليدية (✕ تسيل الزيوت على الوجه والشعر)\nالصف 2: 💆‍♀️ مساج اهتزازي منشط | مشط زيلميكو (✓ ذبذبات خفيفة تنشط تدفق الدم للبصيلات) | القطارة التقليدية (✕ لا يوجد أي تدليك أو تحفيز)\nالصف 3: 🧴 عناية نظيفة وبدون إهدار | مشط زيلميكو (✓ خزان محكم ويدين نظيفتين تماماً) | القطارة التقليدية (✕ يدين لزجة وزيوت على المفارش)\nالصف 4: 🧼 سهل التنظيف والغسيل | مشط زيلميكو (✓ مواد طبية قابلة للشطف بالماء) | القطارة التقليدية (✕ أنابيب زجاجية صعبة التنظيف)\nالصف 5: 🚚 شحن سريع لكافة المدن | مشط زيلميكو (✓ توصيل خلال 7–8 أيام لكافة مدن المملكة) | القطارة التقليدية (✕ شحن بطيء لأسابيع دون ضمان ذهبي)",

    "marquee-text-en": "🚚 Fast 7–8 Days Delivery Across Saudi Arabia • 🛡️ 14-Day Golden Guarantee • 💳 Split in 4 with Tabby & Tamara • 🔒 100% Secure Mada & Apple Pay Checkout",
    "marquee-text-ar": "🚚 توصيل سريع خلال 7–8 أيام لكافة مدن المملكة • 🛡️ الضمان الذهبي 14 يوماً • 💳 قسّم فاتورتك مع تابي وتمارا • 🔒 دفع آمن 100% عبر مدى وأبل باي",
    "cust-head-en": "OUR HAPPY CUSTOMERS<br>Real Scalp & Hair Density Journeys Across Saudi Arabia<br>Read verified reviews from clients who transformed their hair wellness rituals.",
    "cust-head-ar": "تجارب عملائنا المعتمدة<br>نتائج حقيقية وكثافة شعر ملحوظة في مختلف مدن المملكة<br>قصص موثقة لعملاء وعميلات استمتعوا بروتين تزييت نظيف وسريع ونمو شعر صحي.",
    "rev-stats-en": "⭐️⭐️⭐️⭐️⭐️ 4.9 out of 5 Stars (Based on 134 Verified Purchases across Saudi Arabia)<br>97% would recommend to a friend • Fast 7–8 days delivery to Riyadh, Jeddah, Dammam & all Saudi cities.",
    "rev-stats-ar": "⭐️⭐️⭐️⭐️⭐️ 4.9 من 5 نجوم (استناداً إلى 134 تقييم موثق لعملاء داخل المملكة العربية السعودية)<br>97% يوصون بالمشط لأصدقائهم • توصيل سريع وموثوق خلال 7–8 أيام للرياض، جدة، الدمام وكافة المدن.",
    "rel-head-en": "COMPLETE YOUR HAIR CARE RITUAL<br>You May Also Like<br>Smart personal wellness essentials designed to elevate your everyday routine—delivered in 7–8 days across Saudi Arabia.",
    "rel-head-ar": "أكملي مجموعة العناية المتكاملة بشعرك<br>منتجات مختارة قد تنال إعجابك<br>أجهزة ومنتجات عناية شخصية ذكية صُممت لراحتك اليومية — مع توصيل خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-title-en": "Portable Scalp Massage Comb with Liquid Hair Oil Applicator | Zelmiqo® KSA",
    "seo-title-ar": "مشط مساج فروة الرأس المتنقل مع موزع زيوت وسيروم الشعر | زيلميكو السعودية",
    "seo-desc-en": "Distribute hair oils and growth serums directly to follicles with precision rolling teeth and gentle micro-vibrations. Fast 7–8 days delivery across Saudi Arabia with Tabby & Tamara.",
    "seo-desc-ar": "مشط مساج فروة الرأس الذكي مع أسنان كروية لتوزيع زيت الروزماري وسيروم الشعر على الجذور دون تلطيخ اليدين. توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-keywords-en": "scalp massage comb saudi arabia, liquid oil applicator comb ksa, rosemary oil scalp massager, hair growth oil dispenser, tabby tamara hair care devices",
    "seo-keywords-ar": "مشط مساج فروة الرأس السعودية, موزع زيت الشعر, مشط زيت الروزماري, مساج الشعر بالاهتزاز, تقسيط تابي وتمارا, متجر زيلميكو توصيل 7-8 ايام"
}

# -------------------------------------------------------------
# 4. Ultrasonic Skin Scrubber (PRD-17)
# -------------------------------------------------------------
p_scrubber = {
    "hero-title-en": "DermaSonic Ultrasonic Skin Scrubber & Deep Pore Spatula with Ionic Care",
    "hero-title-ar": "جهاز تقشير وتنظيف البشرة بالموجات فوق الصوتية والأيونات والنبضات",
    "hero-subtitle-en": "24,000Hz Ultrasonic Peeling & Deep Nutrient Infusion<br>Gently dislodges trapped blackheads and dead skin, then deeply infuses hydrating serums. Fast 7–8 days delivery across Saudi Arabia.",
    "hero-subtitle-ar": "تقشير ناعم بـ 24,000 اهتزازة صوتية وتغلغل عميق للسيروم<br>يزيل الرؤوس السوداء والجلد الميت برفق ثم يعزز امتصاص السيروم المرطب، مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "hero-callout-en": "24kHz Ultrasonic Peeling Spatula & Ion Infuser",
    "hero-callout-ar": "ملعقة تقشير بالموجات الصوتية والأيونات",
    "hero-bullets-en": "• 🌊 24,000Hz Sonic Wave Peeling\n• ➕ Ion+ Deep Impurity Extraction\n• ➖ Ion- Deep Serum Nutrient Infusion\n• ⚡️ EMS Microcurrent Face Lifting",
    "hero-bullets-ar": "• 🌊 تقشير بموجات صوتية 24,000 اهتزازة في الثانية\n• ➕ أيونات موجبة Ion+ لإخراج الأوساخ المتراكمة\n• ➖ أيونات سالبة Ion- لامتصاص فائق للسيروم\n• ⚡️ نبضات EMS لشد البشرة وتنشيط خلايا الوجه",
    
    "faq-head-en": "CLINIC-GRADE ULTRASONIC SKIN PEELING<br>Radiant, Glass-Like Skin in Just Minutes<br>Water-atomizing sonic frequencies gently exfoliate without chemical irritation or skin tearing. Fast 7–8 days delivery across Saudi Arabia.",
    "faq-head-ar": "تقشير وتنظيف بالموجات الصوتية بجودة العيادات<br>بشرة زجاجية ونضارة نقية في دقائق معدودة<br>ترددات صوتية تفتت قطرات الماء لتزيل خلايا الجلد الميت بلطف وبدون أي مواد كيميائية حارقة. توصيل سريع وموثوق خلال 7–8 أيام لكافة مناطق المملكة.",
    "faq-1-en": "How does the ultrasonic spatula dislodge trapped blackheads?<br>Vibrating at 24,000 pulses per second, the stainless steel curved blade instantly atomizes water droplets on your skin into micro-bubbles that blast out sebum and grime painlessly.",
    "faq-1-ar": "كيف تعمل الملعقة الصوتية على إزالة الرؤوس السوداء؟<br>تهتز شفرة الستانلس ستيل 24,000 مرة في الثانية لتفتت قطرات الماء على وجهك إلى فقاعات دقيقة تنظف وتخرج الدهون والرؤوس السوداء دون أي ألم.",
    "faq-2-en": "What is the difference between Ion+ and Ion- modes?<br>Ion+ attracts negatively charged grime and oil out of deep pores (Cleaning mode); Ion- repels active serum molecules deeper into cellular dermal layers (Nutrient Infusion mode).",
    "faq-2-ar": "ما هو الفرق بين وضع الأيونات الموجبة Ion+ والسالبة Ion-؟<br>وضع الأيونات الموجبة يخرج الأوساخ والدهون العميقة من المسام، بينما وضع الأيونات السالبة يدفع مكونات السيروم المرطب لأعماق خلايا البشرة لمضاعفة الترطيب.",
    "faq-3-en": "Must my skin be wet or damp while using the peeling mode?<br>Yes, always keep your face wet with warm water, green tea mist, or rose water while using Cleaning mode. Never glide the spatula on completely dry skin.",
    "faq-3-ar": "هل يجب أن يكون الوجه مبللاً بالماء أثناء استخدام وضع التقشير؟<br>نعم بالتأكيد، يجب دائماً ترطيب الوجه بالماء الدافئ أو ماء الورد أثناء التقشير، حتى تتمكن الموجات الصوتية من تفتيت قطرات الماء وتسهيل انزلاق الشفرة بأمان.",
    "faq-4-en": "Is the stainless steel spatula safe for sensitive or acne-prone skin?<br>Yes, crafted from medical-grade 304 stainless steel, it is naturally hypoallergenic, hygienic, and much gentler on reactive skin than harsh abrasive scrubs.",
    "faq-4-ar": "هل شفرة الستانلس ستيل آمنة للبشرة الحساسة أو المعرضة لحب الشباب؟<br>نعم، الشفرة مصنوعة من الستانلس ستيل الطبي المقاوم للصدأ والمضاد للحساسية، وتعد ألطف بكثير على حاجز البشرة مقارنة بالصنفرة والمقشرات الكيميائية القاسية.",

    "twocol-head-en": "SPA-GRADE FACIAL AT HOME • WATER-POWERED CLEANSING<br>Reveal Fresh, Glowing Skin in a Simple 10-Minute Ritual<br>Cleanse, infuse nutrients, and tone your facial contours with three versatile modes. Fast 7–8 days delivery across Saudi Arabia.",
    "twocol-head-ar": "جلسة سبا منزلية متكاملة • تنظيف بقوة رذاذ الماء<br>اكشفي عن نضارة بشرتك الطبيعية بروتين سهل في 10 دقائق<br>تنظيف مسام، وتغذية سيروم عميقة، وشد لمحيط الوجه بثلاثة أوضاع ذكية، مع توصيل سريع وموثوق خلال 7–8 أيام لكافة مدن المملكة.",
    "twocol-cards-en": "Card 1: 🚚 Fast 7–8 Days Delivery\nCard 2: 🛡️ 14-Day Golden Guarantee\nCard 3: 💳 Secure Mada & Apple Pay",
    "twocol-cards-ar": "البطاقة 1: 🚚 توصيل سريع خلال 7–8 أيام\nالبطاقة 2: 🛡️ الضمان الذهبي 14 يوماً\nالبطاقة 3: 💳 دفع آمن بمدى وأبل باي",

    "center-head-en": "3 MULTI-FUNCTIONAL BEAUTY MODES<br>Deep Ultrasonic Cleanse, Nutrient Infusion & EMS Lift<br>Ergonomic stainless steel spatula curves naturally along nose bridges, forehead, and cheekbones.",
    "center-head-ar": "3 أوضاع تجميلية ذكية في جهاز واحد<br>تنظيف فائق، امتصاص مضاعف، وشد نبضات EMS<br>رأس شفرة ستانلس ستيل منحني بعناية ليتطابق مع انحناءات جسر الأنف والجبين والوجنتين.",
    "center-b1-en": "24,000Hz Ultrasonic Peeling<br>Atomizes water into microscopic mist to flush out oxidized sebum and dead cells.",
    "center-b1-ar": "تقشير صوتي 24,000 هرتز<br>يحول رذاذ الماء إلى فقاعات دقيقة تزيل الدهون المؤكسدة وخلايا الجلد الميت.",
    "center-b2-en": "Ion+ Deep Pore Extraction<br>Draws out residual cosmetic makeup and environmental pollution particles.",
    "center-b2-ar": "أيونات موجبة Ion+ لإخراج الشوائب<br>تسحب بقايا المكياج المقاوم للماء ورواسب الأتربة الدقيقة من عمق المسام.",
    "center-b3-en": "Ion- Nutrient Infusion<br>Drives vitamin C, hyaluronic acid, and peptide serums deep into the epidermis.",
    "center-b3-ar": "أيونات سالبة Ion- لامتصاص السيروم<br>تدفع جزيئات الهيالورونيك وفيتامين C لطبقات البشرة العميقة لترطيب فائق ونضارة.",
    "center-b4-en": "EMS Microcurrent Firming<br>Gently stimulates facial muscles to lift slackened skin and smooth expression lines.",
    "center-b4-ar": "شد نبضات EMS الدقيقة<br>تحفز أنسجة الوجه بلطف لشد ملامح الخدين وتنعيم الخطوط التعبيرية الرقيقة.",

    "grid-head-en": "EVERYDAY BENEFITS YOU WILL NOTICE IMMEDIATELY<br>Smooth, Velvety Glass Skin After Every Treatment<br>Experience clearer texture that glows with or without makeup.",
    "grid-head-ar": "مزايا يومية تلاحظينها من أول جلسة<br>بشرة مخملية ناعمة كالحرير بعد كل استخدام<br>تمتعي ببشرة نقية ومشرقة تتألق بصفاء طبيعي مع المكياج أو بدونه.",
    "grid-b1-en": "Glass-Like Skin Texture<br>Sweeps away rough dead skin patches, leaving skin baby-soft and touchable.",
    "grid-b1-ar": "ملمس ناعم كالبشرة الزجاجية<br>يزيل القشور والخشونة ويترك بشرتك فائقة النعومة والنقاء من أول دقيقة.",
    "grid-b2-en": "Instant Blemish & Blackhead Relief<br>Clears nose blackheads and clogged pores without redness or bruising.",
    "grid-b2-ar": "تنظيف فوري للرؤوس السوداء<br>يتخلص من دهون الأنف والمسام دون ترك أي احمرار أو علامات كدمات مزعجة.",
    "grid-b3-en": "3X More Effective Serum Use<br>Prevents costly serums from sitting on top of dead skin, maximizing every drop.",
    "grid-b3-ar": "مضاعفة فائدة سيروماتك 3 مرات<br>يمنع هدر السيروم على طبقات الجلد الميت ويضمن وصوله للبشرة الحية لتستفيدي بالكامل.",
    "grid-b4-en": "Hygienic & Easy to Sanitize<br>Wipes completely clean with an alcohol pad in seconds, preventing bacterial buildup.",
    "grid-b4-ar": "صحي وسهل التعقيم التام<br>يُمسح بمسحة كحولية في ثوانٍ ليبقى معقماً وخالياً من أي بكتيريا أو شوائب.",

    "table-head-en": "WHY CHOOSE ZELMIQO DERMASONIC<br>Medical-Grade Precision for Safe Facial Peeling<br>Compare our 24,000Hz frequency and dual ionic modes against generic scrapers.",
    "table-head-ar": "لماذا تختارين جهاز زيلميكو ديرماسونيك؟<br>دقة طبية وتقنيات صوتية معتمدة لسلامة وجهك<br>قارني بين ترددنا الصوتي 24,000 هرتز والتقنية الأيونية المزدوجة مقابل المكاشط المقلدة.",
    "table-rows-en": "Row 1: 🌊 Real 24kHz Ultrasonic Output | Zelmiqo (✓ Genuine sonic water atomization) | Generic Scrapers (✕ Fake vibration motor with zero peeling)\nRow 2: ➕ Dual Ionic Technology | Zelmiqo (✓ Dedicated Ion+ and Ion- circuits) | Generic Scrapers (✕ Passive metal strip with no ions)\nRow 3: 💎 Medical 304 Stainless Steel | Zelmiqo (✓ Hypoallergenic, smooth curved blade) | Generic Scrapers (✕ Cheap metal that rusts or scratches)\nRow 4: 🔋 USB Quick Charge Battery | Zelmiqo (✓ Long-lasting lithium battery) | Generic Scrapers (✕ Weak battery dies mid-session)\nRow 5: 🚚 Fast KSA Delivery | Zelmiqo (✓ Fast 7–8 days across Saudi Arabia) | Generic Scrapers (✕ Weeks of slow unverified shipping)",
    "table-rows-ar": "الصف 1: 🌊 تردد صوتي حقيقي 24,000 هرتز | جهاز زيلميكو (✓ تفتيت رذاذ ماء حقيقي وتقشير فعال) | المكاشط المقلدة (✕ محرك اهتزاز عادي بدون أي تقشير صوتي)\nالصف 2: ➕ تقنية أيونات مزدوجة | جهاز زيلميكو (✓ دارة أيونية متطورة Ion+ و Ion-) | المكاشط المقلدة (✕ قطعة معدن عادية بدون أي شحنات أيونية)\nالصف 3: 💎 ستانلس ستيل طبي 304 | جهاز زيلميكو (✓ شفرة مصقولة ناعمة ومضادة للحساسية) | المكاشط المقلدة (✕ معدن رديء قد يصدأ أو يخدش البشرة)\nالصف 4: 🔋 شحن USB سريع وموثوق | جهاز زيلميكو (✓ بطارية ليثيوم تدوم لعدة جلسات متتالية) | المكاشط المقلدة (✕ بطارية ضعيفة تفرغ في منتصف الجلسة)\nالصف 5: 🚚 شحن سريع لكافة المدن | جهاز زيلميكو (✓ توصيل خلال 7–8 أيام لكافة مدن المملكة) | المكاشط المقلدة (✕ شحن بطيء لأسابيع دون أي ضمان محلي)",

    "marquee-text-en": "🚚 Fast 7–8 Days Delivery Across Saudi Arabia • 🛡️ 14-Day Golden Guarantee • 💳 Split in 4 with Tabby & Tamara • 🔒 100% Secure Mada & Apple Pay Checkout",
    "marquee-text-ar": "🚚 توصيل سريع خلال 7–8 أيام لكافة مدن المملكة • 🛡️ الضمان الذهبي 14 يوماً • 💳 قسّم فاتورتك مع تابي وتمارا • 🔒 دفع آمن 100% عبر مدى وأبل باي",
    "cust-head-en": "OUR HAPPY CUSTOMERS<br>Real Ultrasonic Skin Peeling Results Across Saudi Arabia<br>Read verified reviews from clients who achieved radiant glass skin at home.",
    "cust-head-ar": "تجارب عميلاتنا المعتمدة<br>نتائج حقيقية وبشرة زجاجية نضرة لسيدات في مدن المملكة<br>قصص موثقة لعميلات تخلصن من بهتان البشرة والقشور واستمتعن بنعومة فائقة.",
    "rev-stats-en": "⭐️⭐️⭐️⭐️⭐️ 4.9 out of 5 Stars (Based on 129 Verified Purchases across Saudi Arabia)<br>96% would recommend to a friend • Fast 7–8 days delivery to Riyadh, Jeddah, Dammam & all Saudi cities.",
    "rev-stats-ar": "⭐️⭐️⭐️⭐️⭐️ 4.9 من 5 نجوم (استناداً إلى 129 تقييم موثق لعملاء داخل المملكة العربية السعودية)<br>96% يوصون بالجهاز لصديقاتهم • توصيل سريع وموثوق خلال 7–8 أيام للرياض، جدة، الدمام وكافة المدن.",
    "rel-head-en": "COMPLETE YOUR RADIANT SKIN RITUAL<br>You May Also Like<br>Smart skincare devices designed to elevate your everyday glow—delivered in 7–8 days across Saudi Arabia.",
    "rel-head-ar": "أكملي مجموعة العناية المتكاملة بجمالك<br>منتجات مختارة قد تنال إعجابك<br>أجهزة تجميل ذكية متوافقة ومثالية لتعزيز نضارة وجهك — مع توصيل خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-title-en": "DermaSonic Ultrasonic Skin Scrubber & Deep Pore Spatula | Zelmiqo® KSA",
    "seo-title-ar": "جهاز تقشير وتنظيف البشرة بالموجات فوق الصوتية والأيونات | زيلميكو السعودية",
    "seo-desc-en": "24,000Hz ultrasonic skin scrubber and pore spatula with Ion+ extraction, Ion- infusion, and EMS microcurrent lifting. Fast 7–8 days delivery across Saudi Arabia.",
    "seo-desc-ar": "جهاز تقشير البشرة بالموجات فوق الصوتية 24,000 هرتز مع تقنية الأيونات وشد نبضات EMS. تنظيف عميق ونضارة زجاجية مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-keywords-en": "ultrasonic skin scrubber saudi arabia, facial pore spatula ksa, ultrasonic blackhead extractor, ion skin peeling machine, tabby tamara skincare devices 7-8 days delivery",
    "seo-keywords-ar": "جهاز تقشير البشرة بالموجات فوق الصوتية السعودية, ملعقة تنظيف المسام, ازالة الرؤوس السوداء سونيك, تقشير البشرة المنزلي, تقسيط تابي وتمارا, متجر زيلميكو"
}

# Generate Batch 2 Pages
generate_product_page("5-in-1 EMS Skin Tightening Massager", p_ems, {}, "product-5-in-1-ems-facial-massager.html")
generate_product_page("PorePure Vacuum Blackhead Remover", p_blackhead, {}, "product-deep-pore-blackhead-remover.html")
generate_product_page("Portable Scalp Massage Comb", p_comb, {}, "product-portable-scalp-massage-comb.html")
generate_product_page("DermaSonic Ultrasonic Skin Scrubber", p_scrubber, {}, "product-ultrasonic-skin-scrubber.html")
print("Batch 2 generation finished successfully!")
