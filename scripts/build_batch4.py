# -*- coding: utf-8 -*-
import os
import re

with open("new-content-html-pages/product-3-in-1-fast-charging-dock.html", "r", encoding="utf-8") as f:
    template_html = f.read()

def generate_product_page(badge_text, updates, old_boxes, out_filename):
    html = template_html
    html = re.sub(
        r'<span class="badge">[^<]+</span>',
        f'<span class="badge">Pilot Template • {badge_text}</span>',
        html
    )
    for old_b, new_b in old_boxes.items():
        html = html.replace(old_b, new_b)
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
# 1. Portable 6-Blade Juicer (PRD-10)
# -------------------------------------------------------------
p_6blade = {
    "hero-title-en": "NutriBlend 6-Blade Portable USB Smoothie Maker & Fruit Juicer Cup",
    "hero-title-ar": "خلاط العصائر والسموذي المحمول بـ 6 شفرات فولاذية وشحن USB",
    "hero-subtitle-en": "Fresh Smoothies & Ice Crushing Anywhere You Go<br>High-speed 22,000 RPM pure copper motor and 3D serrated blades blend frozen fruits in 30 seconds. Fast 7–8 days delivery across Saudi Arabia.",
    "hero-subtitle-ar": "سموذي طازج وسحق سريع للثلج أينما ذهبت<br>محرك نحاسي قوي بسرعة 22,000 دورة بالدقيقة مع 6 شفرات مسننة تخلط الفواكه والثلج في 30 ثانية، مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "hero-callout-en": "6-Blade Ice Crushing Blender & Travel Cup",
    "hero-callout-ar": "خلاط محمول 6 شفرات لسحق الثلج والفواكه",
    "hero-bullets-en": "• 🌪️ 6 Precision 304 Stainless Steel Blades\n• ⚡️ 22,000 RPM Ice-Crushing Copper Motor\n• 🍼 Food-Grade BPA-Free Tritan Bottle\n• 🔋 USB Rechargeable 4,000mAh Battery",
    "hero-bullets-ar": "• 🌪️ 6 شفرات فولاذية حادة مقاومة للصدأ 304\n• ⚡️ محرك نحاسي قوي 22,000 دورة لسحق الثلج\n• 🍼 كاس تريتان صحي خالي تماماً من مادة BPA\n• 🔋 بطارية مزدوجة 4000 مللي أمبير بشحن USB",
    
    "faq-head-en": "NUTRITIOUS SMOOTHIES ON THE GO<br>Drink Fresh Vitamins Anywhere, Anytime<br>Blend protein shakes at the gym, fresh mango juices at work, or iced refreshments in your car. Fast 7–8 days delivery across Saudi Arabia.",
    "faq-head-ar": "عصائر وسموذي طازج مليء بالفيتامينات أينما كنت<br>انتعاش فوري وصحي في أي وقت وأي مكان<br>اخلط بروتين شيك في النادي، أو عصير المانجو الطازج في الدوام، أو مشروبات الثلج المنعشة بسيارتك. توصيل سريع وموثوق خلال 7–8 أيام لكافة مناطق المملكة.",
    "faq-1-en": "Can this portable blender truly crush ice cubes and frozen berries?<br>Yes! Powered by 6 serrated 304 stainless steel blades and a 7.4V motor, it easily pulverizes small ice cubes, frozen mango chunks, and berries with liquid.",
    "faq-1-ar": "هل يمكن للخلاط سحق مكعبات الثلج والفواكه المجمدة فعلاً؟<br>نعم بالتأكيد! بفضل الشفرات الست المسننة المصنوعة من الستانلس ستيل 304 ومحرك بقوة 7.4 فولت، يفتت مكعبات الثلج وقطع الفواكه المجمدة بسلاسة تامة.",
    "faq-2-en": "How many smoothies can I blend on a single battery charge?<br>The built-in 4,000mAh dual lithium battery yields approximately 12 to 15 full blending cycles before needing a simple Type-C recharge.",
    "faq-2-ar": "كم كوب عصير يمكن تحضيره بالشحنة الواحدة للبطارية؟<br>تمنحك البطارية القوية بسعة 4000 مللي أمبير من 12 إلى 15 دورة خلط كاملة بالشحنة الواحدة، لتستمتع بعصائرك لأيام قبل الحاجة لإعادة شحنه عبر USB.",
    "faq-3-en": "Is the blending bottle safe and BPA-free for family use?<br>100% safe. The cup is molded from crystal-clear, shatter-resistant food-grade Tritan material that produces zero chemical odor or harmful BPA leeching.",
    "faq-3-ar": "هل الكوب آمن وصحي وخالٍ من مادة BPA لجميع أفراد العائلة؟<br>آمن وصحي 100%؛ الكوب مصنوع من مادة التريتان (Tritan) الغذائية المقاومة للصدمات والمعتمدة عالمياً، خالية تماماً من الروائح أو المواد الكيميائية الضارة.",
    "faq-4-en": "How easy is it to clean after blending sticky fruits or protein?<br>Extremely easy! Simply add warm water and a drop of dish soap, double-click the power button, and let it self-clean automatically in 15 seconds.",
    "faq-4-ar": "كيف يتم تنظيف الخلاط بعد تحضير العصائر الكثيفة أو البروتين؟<br>تنظيف ذاتي في 15 ثانية فقط! ضع قليلاً من الماء الدافئ وقطرة صابون، ثم اضغط زر التشغيل مرتين ليقوم الخلاط بتنظيف نفسه ذاتياً وبشكل فائق السهولة.",

    "twocol-head-en": "FRESH BLENDING ON DEMAND • COMPACT & POWERFUL<br>Enjoy Fresh, Silky Smoothies Wherever Life Takes You<br>Upgrade your daily breakfast and post-workout nutrition with one-button effortless blending. Fast 7–8 days delivery across Saudi Arabia.",
    "twocol-head-ar": "عصائر طازجة بضغطة زر • قوة وسهولة تنقل فائقة<br>استمتع بقوام سموذي مخملي ومنعش أينما كنت<br>طور روتين فطورك الصباحي ومشروبات النادي الرياضي بكل راحة ودون الحاجة لخلاطات المطبخ الكبيرة، مع توصيل سريع وموثوق خلال 7–8 أيام لكافة مدن المملكة.",
    "twocol-cards-en": "Card 1: 🚚 Fast 7–8 Days Delivery\nCard 2: 🛡️ 7-Day Golden Guarantee\nCard 3: 💳 Secure Mada & Apple Pay",
    "twocol-cards-ar": "البطاقة 1: 🚚 توصيل سريع خلال 7–8 أيام\nالبطاقة 2: 🛡️ الضمان الذهبي 7 أيام\nالبطاقة 3: 💳 دفع آمن بمدى وأبل باي",

    "center-head-en": "PRECISION 6-BLADE VORTEX EXTRACTION<br>22,000 RPM Speed with Magnetic Safety Interlock<br>Smart safety sensors prevent blades from spinning unless the cup is locked tightly into position.",
    "center-head-ar": "خلط توربيني فائق بـ 6 شفرات مسننة<br>سرعة 22,000 دورة بالدقيقة مع قفل أمان مغناطيسي<br>حساسات أمان ذكية تمنع دوران الشفرات نهائياً ما لم يكن الكوب مغلقاً ومثبتاً بإحكام على القاعدة.",
    "center-b1-en": "6 Serrated 304 Steel Blades<br>Engineered in a 3D multi-angle layout to suck ingredients down into the vortex.",
    "center-b1-ar": "6 شفرات ستانلس ستيل مسننة<br>مصممة بزوايا هندسية ثلاثية الأبعاد تسحب قطع الفواكه والثلج لقلب الإعصار لسحق متجانس.",
    "center-b2-en": "Magnetic Safety Lock<br>Induction safety switch ensures zero accidental finger injuries when cleaning.",
    "center-b2-ar": "قفل أمان كهرومغناطيسي<br>حساس أمان يوقف المحرك فور فك الكوب لحماية اليدين والأصابع أثناء الغسيل.",
    "center-b3-en": "Universal USB / Type-C Charging<br>Charge easily via wall plug, car USB socket, power bank, or laptop port.",
    "center-b3-ar": "شحن USB و تايب سي عالمي<br>شحن سهل وسريع عبر شاحن السيارة، بنك الطاقة المتنقل، أو شاحن الجوال المنزلي.",
    "center-b4-en": "Silicone Carry Strap Lid<br>Includes a spill-proof sports drinking lid with durable carrying loop.",
    "center-b4-ar": "غطاء شرب رياضي بحزام مريح<br>غطاء محكم ضد التسرب مع مقبض سيليكوني متين يسهل حمله في اليد أو تعليقه بالحقيبة.",

    "grid-head-en": "EVERYDAY BENEFITS YOU WILL NOTICE FROM DAY ONE<br>Healthier Eating Made Completely Effortless<br>Never settle for store-bought sugary processed juices again.",
    "grid-head-ar": "مزايا يومية تشعر بفارقها من أول يوم<br>أسلوب حياة صحي وطازج أصبح في غاية السهولة<br>استغنِ تماماً عن العصائر المصنعة المليئة بالسكريات والمواد الحافظة واصنع عصيرك بيدك.",
    "grid-b1-en": "Ice-Cold Summer Refreshment<br>Blend iced dates, fresh mint lemonades, and smoothies in 45°C+ summer heat.",
    "grid-b1-ar": "انتعاش ثلجي في حر الصيف<br>اصنع عصير ليمون ونعناع مثلج، أو سموذي تمر منعش يقهر حرارة الصيف الشديدة.",
    "grid-b2-en": "Smooth Lump-Free Protein Shakes<br>No more powdery lumps at the bottom of manual gym shaker cups.",
    "grid-b2-ar": "بروتين شيك ناعم وبدون تكتلات<br>ودّع تكتل بودرة البروتين المزعجة في شيكرات النادي اليدوية واستمتع بقوام كريمي فاخر.",
    "grid-b3-en": "Fits Car Cup Holders Perfectly<br>Slim bottle diameter slips effortlessly into standard vehicle drink holders.",
    "grid-b3-ar": "يناسب حامل أكواب السيارة تماماً<br>تصميم أسطواني مدروس يستقر بثبات داخل حاملات الأكواب في كافة السيارات.",
    "grid-b4-en": "Lightweight & Travel Ready<br>Compact size packs easily into backpacks, gym bags, and office totes.",
    "grid-b4-ar": "خفيف الوزن وسهل الحمل في السفر<br>حجم مدمج لا يأخذ حيزاً في حقيبة النادي أو حقيبة الدوام والسفر والرحلات.",

    "table-head-en": "WHY CHOOSE ZELMIQO NUTRIBEND<br>Real Ice-Crushing Power Engineered for Daily Life<br>Compare our 6 serrated steel blades and 4,000mAh battery with cheap 2-blade plastic toys.",
    "table-head-ar": "لماذا يفضل عملاؤنا خلاط زيلميكو؟<br>قوة سحق ثلج حقيقية صُممت للاستخدام اليومي الشاق<br>قارن بين الشفرات الست الفولاذية والبطارية المزدوجة لدينا مقابل الخلاطات البلاستيكية الضعيفة بشفرتين.",
    "table-rows-en": "Row 1: 🌪️ 6 Serrated Steel Blades | Zelmiqo (✓ 304 stainless blades crush ice & berries) | Generic Blenders (✕ 2 dull flat blades that jam on ice)\nRow 2: ⚡️ 22,000 RPM High Torque | Zelmiqo (✓ Pure copper motor blends in 30 sec) | Generic Blenders (✕ Weak motor stalls under thick ingredients)\nRow 3: 🍼 Food-Grade Tritan Cup | Zelmiqo (✓ Shatterproof & 100% BPA-free) | Generic Blenders (✕ Toxic cheap plastic that cracks and smells)\nRow 4: 🔋 4,000mAh Battery Capacity | Zelmiqo (✓ 15 blending cycles on single charge) | Generic Blenders (✕ Dies after 2-3 weak blends)\nRow 5: 🚚 Fast KSA Delivery | Zelmiqo (✓ Fast 7–8 days across Saudi Arabia) | Generic Brands (✕ Weeks of unverified slow shipping)",
    "table-rows-ar": "الصف 1: 🌪️ 6 شفرات مسننة فولاذية | خلاط زيلميكو (✓ ستانلس ستيل 304 يسحق الثلج والفواكه) | الخلاطات العادية (✕ شفرتان مسطحتان تتعطلان مع الثلج)\nالصف 2: ⚡️ سرعة 22,000 دورة بالدقيقة | خلاط زيلميكو (✓ محرك نحاسي يخلط بكفاءة في 30 ثانية) | الخلاطات العادية (✕ محرك ضعيف يتوقف عند خلط الفواكه)\nالصف 3: 🍼 كأس تريتان غذائي آمن | خلاط زيلميكو (✓ مقاوم للكسر وخالٍ من BPA بنسبة 100%) | الخلاطات العادية (✕ بلاستيك رديء يتشقق وتظهر له روائح)\nالصف 4: 🔋 بطارية ضخمة 4000 مللي أمبير | خلاط زيلميكو (✓ تكفي لتحضير 15 كوباً بالشحنة الواحدة) | الخلاطات العادية (✕ تفرغ بطاريتها بعد كوبين أو ثلاثة فقط)\nالصف 5: 🚚 شحن سريع لكافة المدن | خلاط زيلميكو (✓ توصيل خلال 7–8 أيام لكافة مدن المملكة) | الأجهزة المقلدة (✕ شحن بطيء لأسابيع دون ضمان محلي)",

    "marquee-text-en": "🚚 Fast 7–8 Days Delivery Across Saudi Arabia • 🛡️ 7-Day Golden Guarantee • 💳 Split in 4 with Tabby & Tamara • 🔒 100% Secure Mada & Apple Pay Checkout",
    "marquee-text-ar": "🚚 توصيل سريع خلال 7–8 أيام لكافة مدن المملكة • 🛡️ الضمان الذهبي 7 أيام • 💳 قسّم فاتورتك مع تابي وتمارا • 🔒 دفع آمن 100% عبر مدى وأبل باي",
    "cust-head-en": "OUR HAPPY CUSTOMERS<br>Real Smoothie & Fresh Juice Stories Across Saudi Arabia<br>Read verified reviews from gym-goers, parents, and busy commuters.",
    "cust-head-ar": "تجارب عملائنا المعتمدة<br>قصص انتعاش حقيقية لعشاق العصائر والرياضيين في مدن المملكة<br>تقييمات موثقة لعملاء استمتعوا بعصائر طازجة وسموذي بروتين يومي في النادي والدوام.",
    "rev-stats-en": "⭐️⭐️⭐️⭐️⭐️ 4.9 out of 5 Stars (Based on 176 Verified Purchases across Saudi Arabia)<br>98% would recommend to a friend • Fast 7–8 days delivery to Riyadh, Jeddah, Dammam & all Saudi cities.",
    "rev-stats-ar": "⭐️⭐️⭐️⭐️⭐️ 4.9 من 5 نجوم (استناداً إلى 176 تقييم موثق لعملاء داخل المملكة العربية السعودية)<br>98% يوصون بالخلاط لأصدقائهم • توصيل سريع وموثوق خلال 7–8 أيام للرياض، جدة، الدمام وكافة المدن.",
    "rel-head-en": "MORE HEALTH & KITCHEN ESSENTIALS TO EXPLORE<br>You May Also Like<br>Smart portable appliances designed to elevate your daily nutrition—delivered in 7–8 days across Saudi Arabia.",
    "rel-head-ar": "المزيد من أجهزة المطبخ والتغذية الصحية<br>منتجات مختارة قد تنال إعجابك<br>أجهزة ذكية محمولة صُممت لراحتك ونمط حياة صحي متكامل — مع توصيل خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-title-en": "NutriBlend 6-Blade Portable USB Smoothie Maker & Fruit Juicer | Zelmiqo® KSA",
    "seo-title-ar": "خلاط العصائر والسموذي المحمول بـ 6 شفرات وشحن USB | زيلميكو السعودية",
    "seo-desc-en": "High-speed 22,000 RPM portable 6-blade USB rechargeable smoothie maker and travel juicer bottle with Tritan BPA-free cup. Fast 7–8 days delivery across Saudi Arabia.",
    "seo-desc-ar": "خلاط سموذي وعصائر محمول بـ 6 شفرات فولاذية وبطارية 4000 مللي أمبير لسحق الثلج والفواكه في 30 ثانية. توصيل سريع خلال 7–8 أيام لكافة مدن المملكة مع تقسيط تابي وتمارا.",
    "seo-keywords-en": "portable blender saudi arabia, 6 blade usb juicer cup ksa, travel smoothie maker, ice crushing blender 7-8 days delivery, tabby tamara kitchen gadgets",
    "seo-keywords-ar": "خلاط محمول شحن السعودية, خلاط سموذي متنقل, خلاط فواكه 6 شفرات, خلاط بروتين رياضي, تقسيط تابي وتمارا, متجر زيلميكو توصيل 7-8 ايام"
}

# -------------------------------------------------------------
# 2. Portable Double-Cup Juicer (PRD-11)
# -------------------------------------------------------------
p_doublecup = {
    "hero-title-en": "DuoCup Portable Double-Cup Blender & Travel Smoothie Maker with 2 Bottles",
    "hero-title-ar": "خلاط العصائر المحمول بنظام الكوبين المزدوجين DuoCup والشحن السريع",
    "hero-subtitle-en": "Blend One, Take Both — Dual Portable Cups for Couples & Busy Days<br>Comes with two individual sports drinking bottles and grab-and-go travel lids. Fast 7–8 days delivery across Saudi Arabia.",
    "hero-subtitle-ar": "اخلط الأول وخذ الاثنين معاً — كوبان رياضيان منفصلان للأزواج وأيام العمل المزدحمة<br>يأتي مع كأسين رياضيين وأغطية شرب مانعة للتسرب مع حزام مريح، مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "hero-callout-en": "Dual-Cup Portable Blender & Travel Bottles",
    "hero-callout-ar": "خلاط محمول بنظام الكوبين المزدوجين المتنقلين",
    "hero-bullets-en": "• 🥤 2 Detachable Food-Grade Tritan Travel Bottles\n• 🌪️ 6 Stainless Steel High-Velocity Blades\n• ⚡️ 20,000 RPM Powerful Blending Motor\n• 🔋 4,000mAh Battery with Universal USB-C Charging",
    "hero-bullets-ar": "• 🥤 كوبان متنقلان من التريتان الصحي خاليان من BPA\n• 🌪️ 6 شفرات فولاذية حادة لسحق الفواكه والثلج\n• ⚡️ محرك قوي بسرعة 20,000 دورة بالدقيقة\n• 🔋 بطارية 4000 مللي أمبير مع شحن تايب سي سريع",
    
    "faq-head-en": "DOUBLE THE CAPACITY, ZERO MORNING DELAYS<br>Perfect for Couples, Workout Partners & Families<br>Blend your morning smoothie, pop on the travel lid, and immediately blend a second bottle for your partner. Fast 7–8 days delivery across Saudi Arabia.",
    "faq-head-ar": "ضعف السعة وبدون أي تأخير في الصباح<br>مثالي للأزواج، شركاء النادي، والعائلات النشيطة<br>اخلط عصيرك الصباحي، ضع غطاء الشرب الرياضي، واخلط مباشرة الكوب الثاني لشريكك بكل سلاسة. توصيل سريع وموثوق خلال 7–8 أيام لكافة مناطق المملكة.",
    "faq-1-en": "What is the advantage of having two separate cups included?<br>You can prepare two different drinks (e.g. green detox juice for you, fresh strawberry banana smoothie for your child or spouse) without washing the cup in between.",
    "faq-1-ar": "ما هي ميزة وجود كوبين منفصلين مع الخلاط؟<br>تستطيع تحضير مشروبين مختلفين (مثل عصير الديتوكس الصحي لك، وعصير الفراولة والموز المنعش لطفلك أو شريكك) دون الحاجة لغسيل الكوب بين المرتين.",
    "faq-2-en": "Do both bottles come with drinking lids for easy transport?<br>Yes! Both bottles feature individual leak-proof sipping lids and soft silicone wrist straps for convenient gym, office, or stroller carrying.",
    "faq-2-ar": "هل يأتي الكوبان بأغطية شرب منفصلة ومحكمة؟<br>نعم بالتأكيد! كلا الكوبين مزودان بغطاء رياضي مانع للتسرب مع فوهة شرب مريحة وحزام سيليكوني لسهولة الحمل في النادي أو السيارة أو العمل.",
    "faq-3-en": "Can it blend crushed ice and frozen acai packs?<br>Yes, the 6 stainless steel blades paired with the high-torque motor effortlessly process frozen mango cubes, acai puree, and iced milk drinks.",
    "faq-3-ar": "هل يخلط الثلج المجروش وخلطات الآساي المثلجة؟<br>نعم بكل كفاءة، الشفرات الست مع المحرك القوي تخلط مكعبات المانجو والآساي المثلجة ومشروبات الحليب الباردة لقوام ناعم ومتجانس.",
    "faq-4-en": "How do I switch the base from the first cup to the second?<br>Simply unscrew the motor base from the first cup, cap it with its travel lid, screw the base onto the second filled cup, and double-click to blend.",
    "faq-4-ar": "كيف يتم نقل قاعدة المحرك من الكوب الأول إلى الكوب الثاني؟<br>بكل بساطة تفك قاعدة المحرك من الكوب الأول وتغلقه بغطاء الشرب، ثم تركب القاعدة على الكوب الثاني وتضغط زر التشغيل مرتين لتبدأ الخلط فوراً.",

    "twocol-head-en": "2-IN-1 PORTABLE BLENDER • DUAL BOTTLE FREEDOM<br>Blend Delicious Fresh Drinks for Two in Under a Minute<br>Enjoy complete versatility with dual Tritan bottles engineered for modern active lifestyles. Fast 7–8 days delivery across Saudi Arabia.",
    "twocol-head-ar": "خلاط 2 في 1 متنقل • حرية الكوب المزدوج<br>اصنع مشروبات طازجة ولذيذة لشخصين في أقل من دقيقة<br>تمتع بأقصى درجات المرونة مع كوبين من التريتان الصحي صُمما ليناسبا نمط حياتك اليومي النشط، مع توصيل سريع وموثوق خلال 7–8 أيام لكافة مدن المملكة.",
    "twocol-cards-en": "Card 1: 🚚 Fast 7–8 Days Delivery\nCard 2: 🛡️ 7-Day Golden Guarantee\nCard 3: 💳 Secure Mada & Apple Pay",
    "twocol-cards-ar": "البطاقة 1: 🚚 توصيل سريع خلال 7–8 أيام\nالبطاقة 2: 🛡️ الضمان الذهبي 7 أيام\nالبطاقة 3: 💳 دفع آمن بمدى وأبل باي",

    "center-head-en": "DUAL CUP MODULAR EXTRACTION SYSTEM<br>One Motor Base Powers Two Travel Bottles<br>Equipped with leak-proof silicone gaskets and micro-switch safety interlocks for effortless on-the-go blending.",
    "center-head-ar": "نظام خلط تركيبي مزدوج الكؤوس<br>قاعدة محرك واحدة تشغل كوبين متنقلين بكفاءة<br>مزود بحلقات سيليكونية مانعة للتسرب وقفل أمان ذكي لخلط آمن وسلس في أي وقت ومكان.",
    "center-b1-en": "Two Individual 400ml Cups<br>Molded from crystal-clear, shatter-resistant food-grade Tritan material.",
    "center-b1-ar": "كوبان منفصلان بسعة 400 مل لكل كوب<br>مصنوعان من مادة التريتان الغذائية الشفافة والمقاومة للصدمات والكسر.",
    "center-b2-en": "6 Stainless Steel Blades<br>Serrated precision edges slice through fibrous fruits, nuts, and ice smoothly.",
    "center-b2-ar": "6 شفرات ستانلس ستيل حادة<br>حواف مسننة دقيقة تقطع الألياف الصلبة والمكسرات ومكعبات الثلج بنعومة وسرعة.",
    "center-b3-en": "Individual Sip-Through Lids<br>Each cup has its own spill-proof sports cap and sturdy silicone carrying lanyard.",
    "center-b3-ar": "أغطية شرب رياضية مستقلة<br>لكل كوب غطاؤه الرياضي الخاص المحكم ضد التسرب مع حزام سيليكوني متين.",
    "center-b4-en": "Dual Lithium 4,000mAh Battery<br>USB-C fast charge delivers up to 18 blending cycles on a single full charge.",
    "center-b4-ar": "بطارية ليثيوم مزدوجة 4000 مللي أمبير<br>شحن سريع عبر منفذ Type-C يكفي لتحضير حتى 18 كوب عصير بالشحنة الواحدة.",

    "grid-head-en": "EVERYDAY BENEFITS YOU WILL NOTICE IMMEDIATELY<br>Smoothies for You & Your Partner with Zero Extra Dishes<br>Save valuable morning time and enjoy complete variety every day.",
    "grid-head-ar": "مزايا يومية تشعر بقيمتها من أول استخدام<br>عصائر طازجة لك ولشريكك بدون مواعين إضافية في المطبخ<br>وفر وقتك الصباحي الثمين واستمتع بتنوع نكهاتك المفضلة كل يوم دون فوضى.",
    "grid-b1-en": "No Flavor Contamination<br>Keep sweet fruit smoothies and savory protein shakes completely separate.",
    "grid-b1-ar": "بدون اختلاط النكهات والروائح<br>احتفظ بنكهة عصير الفواكه المنعش بشكل مستقل تماماً عن مشروب البروتين الخاص بالنادي.",
    "grid-b2-en": "Gym & Office Ready at Once<br>Pack one bottle for your morning workout and send the second to work with your spouse.",
    "grid-b2-ar": "جاهز للنادي والدوام في نفس اللحظة<br>خذ كاساً لتمارين الصباح وأرسل الكاس الآخر طازجاً مع شريكك لعمله بكل راحة.",
    "grid-b3-en": "Saves 15 Minutes Every Morning<br>No need to wash the blender cup before making the second household breakfast drink.",
    "grid-b3-ar": "يوفر 15 دقيقة من وقتك الصباحي<br>لا داعي للوقوف على المغسلة لغسل الكأس بين العصير الأول والثاني أثناء الاستعجال.",
    "grid-b4-en": "Shatterproof Tritan Durability<br>Withstands accidental drops on kitchen tiles or gym rubber floors without cracking.",
    "grid-b4-ar": "متانة تريتان فائقة ومقاومة للصدمات<br>يتحمل السقوط العرضي على أرضية المطبخ أو أرضيات النادي المطاطية دون أي كسر.",

    "table-head-en": "WHY CHOOSE ZELMIQO DUOCUP<br>Complete Dual-Bottle Value with Real Blending Power<br>Compare our 2 Tritan bottles, 6 blades, and dual battery with basic single-cup blenders.",
    "table-head-ar": "لماذا يفضل عملاؤنا خلاط الكوبين من زيلميكو؟<br>قيمة مضاعفة بكوبين متكاملين وقوة خلط حقيقية<br>قارن بين الكوبين الرياضيين والبطارية المزدوجة لدينا مقابل الخلاطات الفردية المحدودة في السوق.",
    "table-rows-en": "Row 1: 🥤 2 Travel Bottles Included | Zelmiqo (✓ Two complete Tritan cups & sports lids) | Standard Blenders (✕ Single cup only, must wash constantly)\nRow 2: 🌪️ 6 Serrated 3D Blades | Zelmiqo (✓ Crushes ice & frozen fruits smoothly) | Standard Blenders (✕ 2-4 dull blades that jam on ice)\nRow 3: 🔋 4,000mAh Battery Capacity | Zelmiqo (✓ 18 blending cycles per charge) | Standard Blenders (✕ Weak 1,200mAh battery dies fast)\nRow 4: 🍼 100% BPA-Free Tritan | Zelmiqo (✓ Food-grade baby-safe material) | Standard Blenders (✕ Cheap cloudy plastic that stains)\nRow 5: 🚚 Fast KSA Delivery | Zelmiqo (✓ Fast 7–8 days across Saudi Arabia) | Generic Brands (✕ Unverified overseas slow transit without warranty)",
    "table-rows-ar": "الصف 1: 🥤 كوبان متنقلان مشمولان | خلاط زيلميكو (✓ كأسان كاملان من التريتان مع أغطية شرب) | الخلاطات العادية (✕ كأس واحد يتطلب الغسيل المستمر)\nالصف 2: 🌪️ 6 شفرات مسننة 3D | خلاط زيلميكو (✓ سحق متقن للثلج والفواكه المجمدة) | الخلاطات العادية (✕ شفرات ضعيفة تعلق مع التمر والثلج)\nالصف 3: 🔋 بطارية ضخمة 4000 مللي أمبير | خلاط زيلميكو (✓ تكفي لتحضير 18 كوباً بالشحنة الواحدة) | الخلاطات العادية (✕ بطارية 1200 مللي أمبير تفرغ بسرعة)\nالصف 4: 🍼 تريتان صحي 100% خالٍ من BPA | خلاط زيلميكو (✓ خامات غذائية نقية وآمنة للأطفال) | الخلاطات العادية (✕ بلاستيك رديء يتصبغ بالروائح)\nالصف 5: 🚚 شحن سريع لكافة المدن | خلاط زيلميكو (✓ توصيل خلال 7–8 أيام لكافة مدن المملكة) | الأجهزة المقلدة (✕ شحن بطيء لأسابيع دون ضمان ذهبي)",

    "marquee-text-en": "🚚 Fast 7–8 Days Delivery Across Saudi Arabia • 🛡️ 7-Day Golden Guarantee • 💳 Split in 4 with Tabby & Tamara • 🔒 100% Secure Mada & Apple Pay Checkout",
    "marquee-text-ar": "🚚 توصيل سريع خلال 7–8 أيام لكافة مدن المملكة • 🛡️ الضمان الذهبي 7 أيام • 💳 قسّم فاتورتك مع تابي وتمارا • 🔒 دفع آمن 100% عبر مدى وأبل باي",
    "cust-head-en": "OUR HAPPY CUSTOMERS<br>Real Dual-Cup Experiences Across Saudi Arabia<br>Read verified reviews from couples, roommates, and busy fitness enthusiasts.",
    "cust-head-ar": "تجارب عملائنا المعتمدة<br>قصص نجاح حقيقية لأزواج ورياضيين في مختلف مدن المملكة<br>تقييمات موثقة لعملاء وفروا وقتهم واستمتعوا بكوبين من العصير الطازج معاً كل صباح.",
    "rev-stats-en": "⭐️⭐️⭐️⭐️⭐️ 4.8 out of 5 Stars (Based on 138 Verified Purchases across Saudi Arabia)<br>97% would recommend to a friend • Fast 7–8 days delivery to Riyadh, Jeddah, Dammam & all Saudi cities.",
    "rev-stats-ar": "⭐️⭐️⭐️⭐️⭐️ 4.8 من 5 نجوم (استناداً إلى 138 تقييم موثق لعملاء داخل المملكة العربية السعودية)<br>97% يوصون بالخلاط لأصدقائهم • توصيل سريع وموثوق خلال 7–8 أيام للرياض، جدة، الدمام وكافة المدن.",
    "rel-head-en": "MORE FITNESS & KITCHEN ESSENTIALS<br>You May Also Like<br>Smart appliances designed to simplify healthy living—delivered in 7–8 days across Saudi Arabia.",
    "rel-head-ar": "المزيد من أجهزة التغذية واللياقة الصحية<br>منتجات مختارة قد تنال إعجابك<br>أجهزة مطبخية ذكية وعصرية صُممت لتسهيل حياتك الصحية — مع توصيل خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-title-en": "DuoCup Portable Double-Cup Blender & Travel Smoothie Maker | Zelmiqo® KSA",
    "seo-title-ar": "خلاط العصائر المحمول بنظام الكوبين المزدوجين DuoCup والشحن السريع | زيلميكو السعودية",
    "seo-desc-en": "Dual-cup portable rechargeable smoothie blender with two detachable Tritan bottles, 6 stainless blades, and 4,000mAh battery. Fast 7–8 days delivery across Saudi Arabia.",
    "seo-desc-ar": "خلاط محمول بنظام الكوبين الرياضيين المزدوجين من التريتان مع 6 شفرات لسحق الثلج وشحن سريع تايب سي. توصيل سريع خلال 7–8 أيام لكافة مدن المملكة مع تقسيط تابي وتمارا.",
    "seo-keywords-en": "double cup portable blender saudi arabia, 2 bottle smoothie maker ksa, dual bottle travel juicer, rechargeable usb blender 7-8 days delivery, tabby tamara juicers",
    "seo-keywords-ar": "خلاط كوبين متنقل السعودية, خلاط سموذي كاسين, خلاط فواكه محمول شحن, خلاط رياضي تريتان, تقسيط تابي وتمارا, متجر زيلميكو توصيل 7-8 ايام"
}

# -------------------------------------------------------------
# 3. Portable USB Citrus Juicer (PRD-14)
# -------------------------------------------------------------
p_citrus = {
    "hero-title-en": "FreshPress Wireless Automatic Citrus Juicer & Orange Extractor with USB Charge",
    "hero-title-ar": "عصارة الحمضيات والبرتقال الكهربائية اللاسلكية الأوتوماتيكية بضغطة زر",
    "hero-subtitle-en": "100% Pure Fresh Juice with Zero Hand Squeezing<br>Smart 360° omnidirectional motorized press extracts maximum juice from oranges, lemons, and pomegranates. Fast 7–8 days delivery across Saudi Arabia.",
    "hero-subtitle-ar": "عصير طبيعي 100% نقي وطازج بدون أي ضغط أو مجهود يدوي<br>عصر كهربائي ذكي 360° يستخلص كل قطرة عصير من البرتقال والليمون والرمان بضغطة زر، مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "hero-callout-en": "Wireless Hands-Free Electric Citrus Juicer",
    "hero-callout-ar": "عصارة حمضيات كهربائية لاسلكية بضغطة زر",
    "hero-bullets-en": "• 🍊 360° Automated Omnidirectional Squeezing\n• ⚡️ One-Touch Hands-Free Electric Operation\n• 🔋 Cordless USB Rechargeable Freedom\n• 🧼 Detachable Dishwasher-Safe Parts",
    "hero-bullets-ar": "• 🍊 عصر كهربائي شامل 360° يستخلص 95% من العصير\n• ⚡️ تشغيل أوتوماتيكي بلمسة زر واحدة بدون تعب اليدين\n• 🔋 بطارية لاسلكية قابلة للشحن عبر USB للاستخدام بأي مكان\n• 🧼 أجزاء قابلة للفك والغسيل السريع تحت الماء الجاري",
    
    "faq-head-en": "EFFORTLESS PURE CITRUS JUICE AT HOME<br>Freshly Squeezed Vitamin C in Seconds<br>No manual pressing, no sticky counters, and zero bitter rind taste. Fast 7–8 days delivery across Saudi Arabia.",
    "faq-head-ar": "عصير برتقال وحمضيات طازج بكل سهولة<br>فيتامين C نقي وصحي ينعش يومك في ثوانٍ معدودة<br>بدون ضغط يدوي مجهد، وبدون فوضى على طاولة المطبخ، وبدون طعم المرارة المزعج للقشر. توصيل سريع وموثوق خلال 7–8 أيام لكافة مناطق المملكة.",
    "faq-1-en": "How does the automatic squeezing mechanism work?<br>Simply cut your orange, lemon, or grapefruit in half, place it on the central cone, close the transparent dome, and press the button. The electric motor raises the cone, pressing out all juice automatically.",
    "faq-1-ar": "كيف تعمل آلية العصر الأوتوماتيكية بضغطة زر؟<br>فقط اقطع البرتقالة أو الليمونة إلى نصفين، وضع النصف فوق رأس العصر، وأغلق الغطاء الشفاف واضغط الزر، ليرتفع المحرك ويعصر كل قطرة تلقائياً دون أي جهد.",
    "faq-2-en": "Does it separate bitter peel oils and seeds from the juice?<br>Yes! The calibrated rotating cone presses only the juicy pulp sacs without crushing the bitter white pith or seeds, delivering pure, naturally sweet juice.",
    "faq-2-ar": "هل تفصل العصارة قشور البرتقال المرة والبذور عن العصير؟<br>نعم بالتأكيد! صُمم رأس العصر ليعصر الفصوص اللحمية الغنية بالعصير فقط دون طحن القشرة البيضاء المرة أو البذور، ليخرج العصير حلواً وصافياً وطبيعياً.",
    "faq-3-en": "Can it juice hard fruits like pomegranates?<br>Yes! Halved pomegranates press beautifully in the high-torque chamber, releasing vibrant antioxidant-rich ruby juice without staining your hands.",
    "faq-3-ar": "هل يمكن استخدامها لعصر الرمان؟<br>نعم بكل تأكيد! ضع نصف حبة الرمان داخل الحجرة، وسيقوم المحرك القوي باستخلاص العصير الياقوتي الغني بمضادات الأكسدة دون تلطيخ يديك أو ملابسك.",
    "faq-4-en": "Can I take it outdoors for desert camping (Kashta) or picnics?<br>Absolutely! The compact cordless design runs entirely on its internal rechargeable battery, making it a huge favorite for weekend Saudi picnics and beach trips.",
    "faq-4-ar": "هل يمكن أخذها في الكشتات والرحلات الخارجية بدون كهرباء؟<br>نعم تماماً! تصميمها اللاسلكي والبطارية المدمجة تجعلها الرفيق المثالي للكشتات والطلعات البرية والحدائق لتحضير عصير برتقال طازج وبارد في الهواء الطلق.",

    "twocol-head-en": "ONE-TOUCH AUTOMATIC SQUEEZING • PURE VITAMIN C<br>Fresh Citrus Juice Extracted to the Last Drop<br>Enjoy pure nutrition with zero effort and zero sticky hands. Fast 7–8 days delivery across Saudi Arabia.",
    "twocol-head-ar": "عصر أوتوماتيكي بلمسة واحدة • فيتامين C نقي وطبيعي<br>استخلاص كامل لكل قطرة عصير بدون أي إهدار<br>تمتع بعصير حمضيات طبيعي وصحي لك ولأطفالك بدون أي مجهود وبدون تلويث يديك، مع توصيل سريع وموثوق خلال 7–8 أيام لكافة مدن المملكة.",
    "twocol-cards-en": "Card 1: 🚚 Fast 7–8 Days Delivery\nCard 2: 🛡️ 7-Day Golden Guarantee\nCard 3: 💳 Secure Mada & Apple Pay",
    "twocol-cards-ar": "البطاقة 1: 🚚 توصيل سريع خلال 7–8 أيام\nالبطاقة 2: 🛡️ الضمان الذهبي 7 أيام\nالبطاقة 3: 💳 دفع آمن بمدى وأبل باي",

    "center-head-en": "360° ROTATING SLOW-MASTICATING EXTRACTOR<br>High-Torque Motor Presses Pure Juice Without Pulp Waste<br>Features a flip-up anti-drip juice spout so you can fill glasses directly or store juice in the chamber.",
    "center-head-ar": "عصر بطيء 360° يحافظ على كامل الفيتامينات<br>محرك عزم قوي يستخلص العصير النقي دون إهدار اللب<br>مزودة بصنبور مانع للتنقيط قابل للإغلاق لتعبئة الكؤوس مباشرة أو حبس العصير داخل الوعاء.",
    "center-b1-en": "360° Omnidirectional Motor Cone<br>Slow masticating pressure yields up to 95% juice extraction rate.",
    "center-b1-ar": "رأس عصر دوار 360°<br>عصر هيدروليكي بطيء يستخلص حتى 95% من عصارة الفاكهة ويترك القشرة جافة تماماً.",
    "center-b2-en": "One-Button Automatic Operation<br>Press once and watch the motorized lifter extract pure juice in 20 seconds.",
    "center-b2-ar": "تشغيل أوتوماتيكي بضغطة واحدة<br>اضغط الزر مرة واحدة وشاهد المحرك يعصر الفاكهة بالكامل في 20 ثانية بهدوء وسلاسة.",
    "center-b3-en": "Anti-Drip Silicone Spout<br>Flip the spout closed while juicing, then flip open to pour cleanly into your glass.",
    "center-b3-ar": "صنبور سيليكوني مانع للتنقيط<br>أغلق الصمام أثناء العصر، ثم افتحه ليصب العصير الصافي في كوبك بدون أي تسريب.",
    "center-b4-en": "USB Rechargeable Portability<br>Internal lithium battery powers over 20-25 whole oranges on a single USB charge.",
    "center-b4-ar": "بطارية قابلة للشحن عبر USB<br>بطارية ليثيوم داخلية تمنحك عصر أكثر من 20 إلى 25 برتقالة بالشحنة الواحدة.",

    "grid-head-en": "EVERYDAY BENEFITS YOU WILL NOTICE IMMEDIATELY<br>Natural Morning Energy for the Whole Family<br>No heavy arm pressure, no messy counters, and no sore wrists.",
    "grid-head-ar": "مزايا يومية تشعر بقيمتها فورياً<br>طاقة طبيعية وصحة لكل أفراد العائلة كل صباح<br>بدون إرهاق معصم اليد، وبدون فوضى على أسطح المطبخ، وبدون هدر حبات البرتقال.",
    "grid-b1-en": "Zero Wrist or Arm Strain<br>Ideal for seniors, busy parents, and anyone with joint stiffness or carpal tunnel.",
    "grid-b1-ar": "بدون أي إجهاد لليدين أو المعصم<br>مثالية لكبار السن والأمهات ومن يعانون من آلام المفاصل؛ المحرك يقوم بكل العمل عنك.",
    "grid-b2-en": "Extracts 30% More Juice<br>Mechanical spiral pressure extracts far more liquid than manual plastic hand reamers.",
    "grid-b2-ar": "تستخلص 30% عصير أكثر<br>الضغط الميكانيكي المنتظم يستخرج عصارة الفصوص كاملة مقارنة بالعصارات اليدوية البلاستيكية.",
    "grid-b3-en": "Perfect for Kashtas & Road Trips<br>Cordless compact shape packs into your picnic basket or camping gear effortlessly.",
    "grid-b3-ar": "مثالية للكشتات ورحلات البر<br>تصميم لاسلكي مدمج يوضع في سلة الرحلات لتحضير عصير برتقال طازج في قلب البر.",
    "grid-b4-en": "Rinses Clean in 10 Seconds<br>Detachable cone and clear chamber rinse spotless under a tap without scrubbing.",
    "grid-b4-ar": "تنظيف سريع بالماء في 10 ثوانٍ<br>فك رأس العصر والوعاء الشفاف واشطفهما تحت صنبور الماء الجاري بدون أي مجهود.",

    "table-head-en": "WHY CHOOSE ZELMIQO FRESHPRESS<br>Hands-Free Motorized Extraction vs Manual Squeezers<br>Compare our electric motor, rechargeable battery, and anti-drip spout with exhausting hand presses.",
    "table-head-ar": "لماذا يفضل عملاؤنا عصارة زيلميكو؟<br>عصر كهربائي مريح بالكامل مقابل العصارات اليدوية المرهقة<br>قارن بين العصر الآلي بضغطة زر والبطارية اللاسلكية لدينا مقابل العصارات اليدوية المتعبة.",
    "table-rows-en": "Row 1: ⚡️ One-Touch Electric Press | Zelmiqo (✓ Fully automated motorized hands-free squeezing) | Manual Squeezers (✕ Exhausting arm strain, slips on counter)\nRow 2: 🍊 95% Juice Extraction Rate | Zelmiqo (✓ Presses pulp completely dry with zero waste) | Manual Squeezers (✕ Leaves half the juice trapped in rind)\nRow 3: 🔋 Wireless Rechargeable | Zelmiqo (✓ Cordless freedom for kitchen, patio, or camping) | Corded Juicers (✕ Bound to wall outlets, bulky and heavy)\nRow 4: 🧼 Quick Detachable Rinse | Zelmiqo (✓ 3 parts disassemble and rinse in 10 seconds) | Heavy Juicers (✕ Dozens of sharp parts hard to scrub)\nRow 5: 🚚 Fast KSA Delivery | Zelmiqo (✓ Fast 7–8 days across Saudi Arabia) | Generic Brands (✕ Unverified slow transit with no local warranty)",
    "table-rows-ar": "الصف 1: ⚡️ عصر أوتوماتيكي بلمسة زر | عصارة زيلميكو (✓ محرك كهربائي يعصر الفاكهة بالكامل دون تعب) | العصارة اليدوية (✕ إجهاد شديد لليد والمعصم وتنزلق من الطاولة)\nالصف 2: 🍊 استخلاص 95% من العصير | عصارة زيلميكو (✓ تفرغ فصوص الفاكهة تماماً وتترك القشر جافاً) | العصارة اليدوية (✕ تترك نصف كمية العصير عالقاً بالقشرة)\nالصف 3: 🔋 لاسلكية قابلة للشحن | عصارة زيلميكو (✓ حرية تنقل كاملة للمطبخ، الحديقة، أو الكشتة) | العصارات السلكية (✕ مقيدة بمقبس الجدار وثقيلة الوزن)\nالصف 4: 🧼 فك وغسيل في 10 ثوانٍ | عصارة زيلميكو (✓ 3 أجزاء تنفك وتُشطف بالماء الجاري سريعاً) | العصارات الضخمة (✕ قطع حادة ومعقدة يصعب تنظيفها)\nالصف 5: 🚚 شحن سريع لكافة المدن | عصارة زيلميكو (✓ توصيل خلال 7–8 أيام لكافة مدن المملكة) | الأجهزة العادية (✕ شحن بطيء لأسابيع دون ضمان ذهبي)",

    "marquee-text-en": "🚚 Fast 7–8 Days Delivery Across Saudi Arabia • 🛡️ 7-Day Golden Guarantee • 💳 Split in 4 with Tabby & Tamara • 🔒 100% Secure Mada & Apple Pay Checkout",
    "marquee-text-ar": "🚚 توصيل سريع خلال 7–8 أيام لكافة مدن المملكة • 🛡️ الضمان الذهبي 7 أيام • 💳 قسّم فاتورتك مع تابي وتمارا • 🔒 دفع آمن 100% عبر مدى وأبل باي",
    "cust-head-en": "OUR HAPPY CUSTOMERS<br>Real Fresh Citrus Squeezing Stories Across Saudi Arabia<br>Read verified reviews from families, juice lovers, and desert campers.",
    "cust-head-ar": "تجارب عملائنا المعتمدة<br>قصص انتعاش حقيقية لعائلات في مختلف مدن المملكة<br>تقييمات موثقة لعملاء استمتعوا بعصير برتقال ورمان طبيعي وصحي كل صباح وبكل سهولة.",
    "rev-stats-en": "⭐️⭐️⭐️⭐️⭐️ 4.9 out of 5 Stars (Based on 152 Verified Purchases across Saudi Arabia)<br>98% would recommend to a friend • Fast 7–8 days delivery to Riyadh, Jeddah, Dammam & all Saudi cities.",
    "rev-stats-ar": "⭐️⭐️⭐️⭐️⭐️ 4.9 من 5 نجوم (استناداً إلى 152 تقييم موثق لعملاء داخل المملكة العربية السعودية)<br>98% يوصون بالعصارة لأصدقائهم • توصيل سريع وموثوق خلال 7–8 أيام للرياض، جدة، الدمام وكافة المدن.",
    "rel-head-en": "MORE HEALTH & REFRESHMENT ESSENTIALS<br>You May Also Like<br>Smart appliances designed to keep your kitchen fresh and healthy—delivered in 7–8 days across Saudi Arabia.",
    "rel-head-ar": "المزيد من أجهزة الانتعاش والتغذية الصحية<br>منتجات مختارة قد تنال إعجابك<br>أجهزة مطبخية ذكية وعصرية صُممت لتمنح عائلتك صحة ونشاطاً — مع توصيل خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-title-en": "FreshPress Wireless Automatic Citrus Juicer & Orange Extractor | Zelmiqo® KSA",
    "seo-title-ar": "عصارة الحمضيات والبرتقال الكهربائية اللاسلكية الأوتوماتيكية بضغطة زر | زيلميكو السعودية",
    "seo-desc-en": "Hands-free automatic electric citrus and orange juicer with USB rechargeable battery and 360° motor extraction. Fast 7–8 days delivery across Saudi Arabia.",
    "seo-desc-ar": "عصارة برتقال وحمضيات كهربائية أوتوماتيكية بضغطة زر واحدة وشحن USB مع عصر بطيء 360°. توصيل سريع خلال 7–8 أيام لكافة مدن المملكة مع تقسيط تابي وتمارا.",
    "seo-keywords-en": "automatic citrus juicer saudi arabia, electric orange squeezer ksa, wireless usb citrus extractor, hands free fruit juicer 7-8 days delivery, tabby tamara kitchen gadgets",
    "seo-keywords-ar": "عصارة برتقال كهربائية السعودية, عصارة حمضيات لاسلكية, عصارة رمان كهربائية, عصارة فواكه بضغطة زر, تقسيط تابي وتمارا, متجر زيلميكو توصيل 7-8 ايام"
}

# -------------------------------------------------------------
# 4. Cordless Handheld Car Vacuum Cleaner (PRD-06)
# -------------------------------------------------------------
p_carvac9k = {
    "hero-title-en": "TurboClean Pro Cordless Handheld Car Vacuum Cleaner (9,000Pa Cyclone Suction)",
    "hero-title-ar": "مكنسة السيارة اللاسلكية المحمولة بقوة شفط 9000 باسكال وفلتر HEPA",
    "hero-subtitle-en": "Powerful 9,000Pa Cyclone Suction for Sand, Crumbs & Pet Hair<br>High-speed brushless motor cleans car seats, air vents, and tight crevices with washable HEPA filter. Fast 7–8 days delivery across Saudi Arabia.",
    "hero-subtitle-ar": "قوة شفط إعصارية 9000 باسكال لتنظيف رمال البر والفتات والشعر<br>محرك قوي بدون فحمات ينظف مقاعد السيارة وفتحات المكيف والزوايا الضيقة مع فلتر HEPA قابل للغسيل، مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "hero-callout-en": "Cordless 9,000Pa Cyclone Car Vacuum",
    "hero-callout-ar": "مكنسة سيارة لاسلكية بقوة شفط 9000 باسكال",
    "hero-bullets-en": "• 🌪️ High-Power 9,000Pa Cyclone Suction\n• 🔋 Long-Life Cordless Rechargeable Battery\n• 🛡️ Washable & Reusable High-Density HEPA Filter\n• 🎯 Multi-Functional Crevice & Brush Nozzles",
    "hero-bullets-ar": "• 🌪️ شفط إعصاري جبار بقوة 9000 باسكال لسحب الرمال والأوساخ\n• 🔋 بطارية لاسلكية قوية قابلة للشحن بحرية تنقل تامة\n• 🛡️ فلتر HEPA متطور يحتجز 99.9% من الغبار وقابل للغسيل\n• 🎯 فوهات متعددة للزوايا الضيقة وفرشاة لمقاعد الجلد والمخمل",
    
    "faq-head-en": "POWERFUL CORDLESS VEHICLE CLEANING<br>Keep Your Car Interior Spotless in Minutes<br>Clear sand, coffee spills, biscuit crumbs, and dust effortlessly without tangled cords. Fast 7–8 days delivery across Saudi Arabia.",
    "faq-head-ar": "تنظيف لاسلكي قوي ومثالي لداخلية سيارتك<br>حافظ على مقصورة سيارتك نظيفة ومرتبة كالجديدة دائماً<br>تخلص من رمال الصحراء والرحلات، فتات البسكويت، والأتربة العالقة بسهولة وبدون أي أسلاك. توصيل سريع وموثوق خلال 7–8 أيام لكافة مناطق المملكة.",
    "faq-1-en": "Is 9,000Pa suction strong enough to pick up desert sand and heavy crumbs?<br>Yes! Powered by a 120W high-speed motor, 9,000Pa suction easily lifts heavy beach and desert sand, stones, biscuit crumbs, and pet hair embedded in carpets.",
    "faq-1-ar": "هل قوة الشفط 9000 باسكال كافية لسحب رمال البر والأوساخ الثقيلة؟<br>نعم بالتأكيد! بفضل محرك عالي الكفاءة بقدرة 120 واط، يولد شفطاً إعصارياً يسحب رمال الكشتات وحبيبات الحصى وفتات الأطعمة العالقة في الفرش والموكيت.",
    "faq-2-en": "How do I clean and maintain the included HEPA filter?<br>The HEPA filter unlocks with a twist. Simply rinse it under tap water, gently tap off excess water, and let it completely air dry before placing it back into the dust cup.",
    "faq-2-ar": "كيف يتم تنظيف فلتر HEPA المرفق مع المكنسة؟<br>يُفك الفلتر بلفّة خفيفة؛ يمكنك شطفه تحت صنبور الماء الجاري لإزالة الأتربة الناعمة، ثم تركه ليجف بالهواء تماماً قبل تركيبه واستخدامه مجدداً.",
    "faq-3-en": "How long does the battery last on a single full charge?<br>The high-density lithium battery provides approximately 25 to 30 minutes of continuous high-power suction, ample time to clean an entire sedan or large SUV.",
    "faq-3-ar": "كم تدوم بطارية المكنسة اللاسلكية بالشحنة الواحدة؟<br>تمنحك بطارية الليثيوم المتطورة من 25 إلى 30 دقيقة من الشفط القوي المتواصل، وهي مدة كافية جداً لتنظيف سيارة سيدان أو جيب SUV عائلي بالكامل.",
    "faq-4-en": "Can it also be used at home for sofas, keyboards, and drawers?<br>Yes! Thanks to its lightweight cordless build, it is fantastic for quickly cleaning laptop keyboards, window tracks, bedside drawers, and living room couch crevices.",
    "faq-4-ar": "هل يمكن استخدامها في المنزل لتنظيف الكنب ولوحة المفاتيح؟<br>نعم بالتأكيد! بفضل وزنها الخفيف وتصميمها اللاسلكي، تعد ممتازة لتنظيف كنب الصالة، أدراج المكاتب، زوايا النوافذ، ولوحة مفاتيح الكمبيوتر بكل سهولة.",

    "twocol-head-en": "SPOTLESS CABIN COMFORT • CORDLESS FREEDOM<br>Restore Showroom Cleanliness to Your Vehicle in Minutes<br>Tackle desert sand, crumbs, and dust without hunting for power outlets. Fast 7–8 days delivery across Saudi Arabia.",
    "twocol-head-ar": "نظافة وأناقة لمقصورة سيارتك • حرية لاسلكية مطلقة<br>استعد لمعان ونظافة وكالة سيارتك في دقائق معدودة<br>تخلص من رمال الرحلات وغبار الجو والفتات اليومي دون الحاجة لتوصيل أسلاك بالولاعة، مع توصيل سريع وموثوق خلال 7–8 أيام لكافة مدن المملكة.",
    "twocol-cards-en": "Card 1: 🚚 Fast 7–8 Days Delivery\nCard 2: 🛡️ 7-Day Golden Guarantee\nCard 3: 💳 Secure Mada & Apple Pay",
    "twocol-cards-ar": "البطاقة 1: 🚚 توصيل سريع خلال 7–8 أيام\nالبطاقة 2: 🛡️ الضمان الذهبي 7 أيام\nالبطاقة 3: 💳 دفع آمن بمدى وأبل باي",

    "center-head-en": "CYCLONIC AIRFLOW & HEPA PURIFICATION<br>High-Torque 120W Motor with Multiple Nozzle Attachments<br>Compact ergonomic grip balances weight effortlessly for reaching under pedals and seats.",
    "center-head-ar": "تدفق هواء إعصاري مع فلترة HEPA دقيقة<br>محرك قوي بقدرة 120 واط مع مجموعة فوهات مخصصة<br>قبضة مريحة وتوزيع وزن متوازن يتيح لك الوصول لأسفل المقاعد ودواسات البنزين بسلاسة.",
    "center-b1-en": "9,000Pa Cyclone Suction<br>Vortex airflow separates dirt from air, maintaining continuous strong suction power.",
    "center-b1-ar": "شفط إعصاري 9000 باسكال<br>تيار هوائي حلزوني يفصل الأوساخ عن الهواء ليحافظ على قوة شفط ثابتة لا تضعف.",
    "center-b2-en": "High-Efficiency HEPA Filter<br>Captures 99.9% of microscopic allergens, dust mites, and exhaust particulate.",
    "center-b2-ar": "فلتر HEPA فائق الكفاءة<br>يحتجز 99.9% من ذرات الغبار المجهرية ومسببات الحساسية لمنع خروجها للهواء.",
    "center-b3-en": "Long Crevice Nozzle<br>Reaches deep into tight side gaps between car center consoles and leather seats.",
    "center-b3-ar": "فوهة طويلة للزوايا الضيقة<br>تصل لأعمق الفتحات بين الكونسول الوسطي ومقاعد السيارة لشفط الأوساخ العالقة.",
    "center-b4-en": "Soft Dusting Brush Head<br>Gently cleans air condition vent louvers and infotainment screens without scratching.",
    "center-b4-ar": "فرشاة ناعمة للمكيف والشاشات<br>تنظف ريش فتحات المكيف وشاشات اللمس والعدادات بنعومة تامة وبدون أي خدش.",

    "grid-head-en": "EVERYDAY BENEFITS YOU WILL NOTICE IMMEDIATELY<br>A Clean, Fresh-Smelling Vehicle Every Day<br>Protect your car interior from permanent ground-in stains and grit.",
    "grid-head-ar": "مزايا يومية تشعر بفارقها فوراً<br>سيارة نظيفة ومعطرة تليق بك وبعائلتك كل يوم<br>احمِ أرضية ومقاعد سيارتك من تراكم الرمال والأوساخ التي تتلف الأقمشة والجلد.",
    "grid-b1-en": "Cleans Desert Sand Instantly<br>Removes beach, camping, and storm sand before it grinds into carpet weaves.",
    "grid-b1-ar": "شفط فوري لرمال البر والكشتات<br>يزيل رمال الصحراء والرحلات فوراً قبل أن تنغرس داخل نسيج الفرش والموكيت.",
    "grid-b2-en": "Kid & Snack Friendly<br>Instantly clean cereal, potato chips, and biscuit crumbs dropped in rear seats.",
    "grid-b2-ar": "مثالية لفتات وأطعمة الأطفال<br>نظف بقايا البسكويت والشيبس التي يسقطها الأطفال في المقاعد الخلفية بثوانٍ معدودة.",
    "grid-b3-en": "Stores in Door Pockets or Trunk<br>Compact lightweight cylinder stores neatly in glovebox, side door, or trunk organizer.",
    "grid-b3-ar": "تخزين مدمج في باب السيارة أو الشنطة<br>حجم أسطواني أنيق وخفيف يُحفظ بسهولة في جيب باب السيارة أو الدرج أو الشنطة الخلفية.",
    "grid-b4-en": "Cordless Freedom Everywhere<br>Clean car seats, home sofa cushions, and office desks with zero cord tangles.",
    "grid-b4-ar": "حرية لاسلكية في كل مكان<br>تنقل بها بحرية لتنظيف مقاعد السيارة، أو كنب المنزل، أو أرفف المكتب بدون أي أسلاك.",

    "table-head-en": "WHY CHOOSE ZELMIQO TURBOCLEAN<br>Real 9,000Pa Cyclone Suction Built for Saudi Dirt & Sand<br>Compare our brushless motor, washable HEPA filter, and cordless design with weak 12V plug-in vacs.",
    "table-head-ar": "لماذا يفضل السائقون مكنسة زيلميكو؟<br>شفط إعصاري 9000 باسكال صُمم لمقاومة رمال وغبار الخليج<br>قارن بين المحرك القوي وفلتر HEPA والبطارية اللاسلكية لدينا مقابل مكانس الولاعة السلكية الضعيفة.",
    "table-rows-en": "Row 1: 🌪️ 9,000Pa Real Suction | Zelmiqo (✓ Easily picks up heavy sand & gravel) | Generic 12V Vacs (✕ Weak 2,000Pa suction barely moves dust)\nRow 2: 🔋 Cordless Lithium Power | Zelmiqo (✓ 30 mins runtime anywhere with zero wires) | Generic 12V Vacs (✕ Tied to cigarette lighter, cord tangles)\nRow 3: 🛡️ Washable HEPA Filter | Zelmiqo (✓ Reusable filtration traps 99.9% dust) | Generic 12V Vacs (✕ Cheap paper filter clogs and blows dust out)\nRow 4: 🎯 Multi-Nozzle System | Zelmiqo (✓ Crevice tool, brush & wide head included) | Generic 12V Vacs (✕ Single flimsy nozzle that snaps)\nRow 5: 🚚 Fast KSA Delivery | Zelmiqo (✓ Fast 7–8 days across Saudi Arabia) | Generic Brands (✕ Unverified slow transit with no local warranty)",
    "table-rows-ar": "الصف 1: 🌪️ شفط حقيقي 9000 باسكال | مكنسة زيلميكو (✓ تسحب الرمال الثقيلة والحصى والفتات) | المكانس العادية (✕ شفط ضعيف 2000 باسكال لا يحرك الغبار)\nالصف 2: 🔋 بطارية لاسلكية قوية | مكنسة زيلميكو (✓ 30 دقيقة تشغيل بدون أي أسلاك مقيدة) | المكانس العادية (✕ مقيدة بسلك ولاعة السيارة المزعج والمعقد)\nالصف 3: 🛡️ فلتر HEPA قابل للغسيل | مكنسة زيلميكو (✓ فلترة دقيقة 99.9% ويُعاد غسيله بالماء) | المكانس العادية (✕ فلتر ورقي رديء يسرب الأتربة لخارج المكنسة)\nالصف 4: 🎯 ملحقات تنظيف متكاملة | مكنسة زيلميكو (✓ فوهة طويلة وفرشاة للمكيف والمقاعد) | المكانس العادية (✕ قطعة بلاستيكية واحدة ضعيفة وسهلة الكسر)\nالصف 5: 🚚 شحن سريع لكافة المدن | مكنسة زيلميكو (✓ توصيل خلال 7–8 أيام لكافة مدن المملكة) | الأجهزة المقلدة (✕ شحن بطيء لأسابيع دون ضمان ذهبي)",

    "marquee-text-en": "🚚 Fast 7–8 Days Delivery Across Saudi Arabia • 🛡️ 7-Day Golden Guarantee • 💳 Split in 4 with Tabby & Tamara • 🔒 100% Secure Mada & Apple Pay Checkout",
    "marquee-text-ar": "🚚 توصيل سريع خلال 7–8 أيام لكافة مدن المملكة • 🛡️ الضمان الذهبي 7 أيام • 💳 قسّم فاتورتك مع تابي وتمارا • 🔒 دفع آمن 100% عبر مدى وأبل باي",
    "cust-head-en": "OUR HAPPY CUSTOMERS<br>Real Car Cleaning Stories Across Saudi Arabia<br>Read verified reviews from car owners in Riyadh, Jeddah, and across the Kingdom.",
    "cust-head-ar": "تجارب عملائنا المعتمدة<br>قصص نظافة حقيقية لسيارات العملاء في مختلف مدن المملكة<br>تقييمات موثقة لسائقين تخلصوا من رمال الرحلات وفتات الأطعمة وحافظوا على نظافة سياراتهم.",
    "rev-stats-en": "⭐️⭐️⭐️⭐️⭐️ 4.9 out of 5 Stars (Based on 182 Verified Purchases across Saudi Arabia)<br>98% would recommend to a friend • Fast 7–8 days delivery to Riyadh, Jeddah, Dammam & all Saudi cities.",
    "rev-stats-ar": "⭐️⭐️⭐️⭐️⭐️ 4.9 من 5 نجوم (استناداً إلى 182 تقييم موثق لعملاء داخل المملكة العربية السعودية)<br>98% يوصون بالمكنسة لأصدقائهم • توصيل سريع وموثوق خلال 7–8 أيام للرياض، جدة، الدمام وكافة المدن.",
    "rel-head-en": "MORE AUTOMOTIVE CARE ACCESSORIES<br>You May Also Like<br>Smart automotive interior tools designed to keep your car looking brand new—delivered in 7–8 days across Saudi Arabia.",
    "rel-head-ar": "المزيد من أجهزة وملحقات العناية بالسيارات<br>منتجات مختارة قد تنال إعجابك<br>أدوات وحلول ذكية صُممت للحفاظ على نظافة وبريق مقصورة سيارتك — مع توصيل خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-title-en": "TurboClean Pro Cordless Handheld Car Vacuum Cleaner | Zelmiqo® KSA",
    "seo-title-ar": "مكنسة السيارة اللاسلكية المحمولة بقوة شفط 9000 باسكال وفلتر HEPA | زيلميكو السعودية",
    "seo-desc-en": "Powerful 9,000Pa cordless handheld car vacuum cleaner with washable HEPA filter, 120W motor, and crevice attachments. Fast 7–8 days delivery across Saudi Arabia.",
    "seo-desc-ar": "مكنسة سيارة لاسلكية محمولة بقوة شفط إعصارية 9000 باسكال وفلتر HEPA قابل للغسيل لتنظيف رمال البر والفتات. توصيل سريع خلال 7–8 أيام لكافة مدن المملكة مع تقسيط تابي وتمارا.",
    "seo-keywords-en": "car vacuum cleaner saudi arabia, cordless handheld car vacuum ksa, 9000pa portable car vac, washable hepa car vacuum 7-8 days delivery, tabby tamara car accessories",
    "seo-keywords-ar": "مكنسة سيارة لاسلكية السعودية, مكنسة سيارة قوية شحن, مكنسة شفط رمال البر, مكنسة سيارة متنقلة, تقسيط تابي وتمارا, متجر زيلميكو توصيل 7-8 ايام"
}

# -------------------------------------------------------------
# 5. Portable Wireless Car Vacuum & Air Duster 2-in-1 (PRD-15)
# -------------------------------------------------------------
p_provac = {
    "hero-title-en": "ProVac 2-in-1 Wireless Car Vacuum Cleaner & Air Duster (Brushless Motor)",
    "hero-title-ar": "مكنسة ومنفاخ هواء السيارة اللاسلكي 2 في 1 بمحرك براشلس توربيني",
    "hero-subtitle-en": "Dual-Function Vacuum Suction & High-Velocity Air Blower<br>Blasts dust out of tight air vents and keyboard keys, then suctions it clean with intense turbine power. Fast 7–8 days delivery across Saudi Arabia.",
    "hero-subtitle-ar": "وظيفة مزدوجة تجمع بين الشفط القوي والنفخ الهوائي التوربيني السريع<br>ينفخ الغبار الصعب من فتحات المكيف ومسارات الأبواب ثم يشفطه بقوة محرك براشلس متطورة، مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "hero-callout-en": "2-in-1 Vacuum Cleaner & High-Speed Air Duster",
    "hero-callout-ar": "مكنسة ومنفاخ هواء 2 في 1 بمحرك براشلس",
    "hero-bullets-en": "• 🌪️ Dual-Action: Powerful Vacuum & Air Blower\n• ⚡️ Ultra-High-Speed Brushless Turbine Motor\n• 🛡️ Washable Dual HEPA & Steel Mesh Filter\n• 🎯 6 Specialized Vacuum & Blower Nozzle Tips",
    "hero-bullets-ar": "• 🌪️ وظيفة مزدوجة: شفط إعصاري قوي ونفخ هوائي سريع\n• ⚡️ محرك براشلس توربيني فائق السرعة وعمر افتراضي طويل\n• 🛡️ فلترة مزدوجة بفلتر HEPA وشبكة فولاذية قابلة للغسيل\n• 🎯 6 فوهات متخصصة للشفط، النفخ، ونفخ ألعاب السباحة",
    
    "faq-head-en": "2-IN-1 VACUUM & AIR DUSTER VERSATILITY<br>Blow Away Hidden Dust, Then Suction It Clean<br>The ultimate car interior and tech detailing tool. Blast dust out of deep AC vents, then vacuum carpets spot-free. Fast 7–8 days delivery across Saudi Arabia.",
    "faq-head-ar": "مرونة فائقة تجمع بين قوة الشفط وقوة النفخ 2 في 1<br>انفخ الأتربة المستعصية من أعماق الفتحات ثم اشفطها فوراً<br>الأداة الاحترافية الأولى لتنظيف سيارتك وأجهزتك التقنية؛ انفخ الغبار من فتحات المكيف واشفط الفرش بدون أي جهد. توصيل سريع وموثوق خلال 7–8 أيام لكافة مناطق المملكة.",
    "faq-1-en": "How does the dual vacuum and air blower feature work?<br>The front port provides powerful vacuum suction to capture debris into the dust cup; the rear port attaches blower nozzles to blast high-velocity air at 45m/s.",
    "faq-1-ar": "كيف تعمل خاصية الشفط والنفخ المزدوجة في نفس الجهاز؟<br>الجهة الأمامية توفر شفطاً إعصارياً قوياً لتجميع الأوساخ في حاوية الغبار، بينما الجهة الخلفية يركب عليها فوهات النفخ لتطلق تيار هواء جبار بسرعة 45 متر/ثانية.",
    "faq-2-en": "Can it inflate air mattresses, swimming pool floats, and vacuum storage bags?<br>Yes! Included inflation nozzles let you blow up pool floats, camping air beds, and balloon arches, or vacuum-seal wardrobe compression bags in seconds.",
    "faq-2-ar": "هل يمكن استخدامه لنفخ مراتب الهواء وألعاب المسابح وتفريغ أكياس الملابس؟<br>نعم بالتأكيد! يأتي مع فوهات نفخ متخصصة لنفخ ألعاب السباحة، مراتب التخييم الهوائية، أو تفريغ الهواء من أكياس حفظ الملابس وتخزينها بسرعة فائقة.",
    "faq-3-en": "Why is a brushless motor superior to standard car vacuum motors?<br>Brushless motors produce 3X higher suction power, generate less heat, operate much quieter, and last for years without motor brush wear and tear.",
    "faq-3-ar": "لماذا يعد محرك البراشلس أفضل بكثير من محركات المكانس العادية؟<br>محركات البراشلس (بدون فحمات) تولد قوة شفط أعلى بثلاث مرات، ولا ترتفع حرارتها، وصوتها أهدأ بكثير، وتعيش لسنوات طويلة دون أي تلف للأجزاء الميكانيكية.",
    "faq-4-en": "How long does the battery last and how do I recharge it?<br>The high-capacity 4,000mAh lithium battery delivers up to 25–30 minutes of runtime and recharges rapidly using any standard Type-C mobile phone cable.",
    "faq-4-ar": "كم تدوم البطارية وكيف يتم شحنها؟<br>البطارية بسعة 4000 مللي أمبير تمنحك من 25 إلى 30 دقيقة تشغيل متواصل، وتُشحن بسرعة وسهولة عبر منفذ Type-C الحديث باستخدام شاحن جوالك العادي.",

    "twocol-head-en": "PRO DETAILING TECH • VACUUM & BLOW IN ONE<br>Deep Clean Crevices That Normal Vacuums Can't Reach<br>Blast dust out of tight air vents, window tracks, and seams, then suction it clean. Fast 7–8 days delivery across Saudi Arabia.",
    "twocol-head-ar": "تقنية تنظيف احترافية • شفط ونفخ في جهاز واحد<br>نظف أدق الزوايا والمسارات التي تعجز عنها المكانس التقليدية<br>انفخ الأتربة من فتحات المكيف ومسارات الأبواب ثم اشفطها بنقاء فوري، مع توصيل سريع وموثوق خلال 7–8 أيام لكافة مدن المملكة.",
    "twocol-cards-en": "Card 1: 🚚 Fast 7–8 Days Delivery\nCard 2: 🛡️ 7-Day Golden Guarantee\nCard 3: 💳 Secure Mada & Apple Pay",
    "twocol-cards-ar": "البطاقة 1: 🚚 توصيل سريع خلال 7–8 أيام\nالبطاقة 2: 🛡️ الضمان الذهبي 7 أيام\nالبطاقة 3: 💳 دفع آمن بمدى وأبل باي",

    "center-head-en": "DUAL-PORT TURBINE AERODYNAMICS<br>High-Velocity Brushless Core with 6 Pro Detailing Attachments<br>Precision aerospace-grade aluminum turbine fan generates intense suction and blowing velocity.",
    "center-head-ar": "ديناميكية هوائية مزدوجة المنافذ بمحرك توربيني<br>قلب محرك براشلس فائق السرعة مع 6 ملحقات تنظيف احترافية<br>مروحة توربينية من سبائك الألمنيوم تولد قوة شفط ونفخ هوائي جبار بسرعة استثنائية.",
    "center-b1-en": "Brushless High-Speed Motor<br>Spins at up to 75,000 RPM, delivering immense airflow and long motor lifespan.",
    "center-b1-ar": "محرك براشلس فائق السرعة<br>يدور بسرعة تصل إلى 75,000 دورة بالدقيقة ليمنحك قوة تدفق هوائي هائلة وعمراً طويلاً.",
    "center-b2-en": "Front Suction / Rear Blower<br>Seamlessly switch from vacuuming carpets to blasting dust out of dashboard vents.",
    "center-b2-ar": "شفط أمامي ونفخ خلفي<br>تحول فوري من شفط رمال الأرضيات إلى نفخ الغبار المتراكم داخل ريش فتحات التكييف.",
    "center-b3-en": "Dual Filtration HEPA System<br>Fine stainless steel mesh stops large grit while internal HEPA captures micro-dust.",
    "center-b3-ar": "نظام فلترة مزدوج متطور<br>شبكة فولاذية خارجية تحجز الحصى والرمال وفلتر HEPA داخلي يحتجز أدق جزيئات الغبار.",
    "center-b4-en": "6 Specialized Nozzles<br>Includes wide mouth, brush, crevice tube, narrow air blaster, and inflation tips.",
    "center-b4-ar": "6 فوهات احترافية متنوعة<br>تشمل فوهة الشفط العريضة، فرشاة المقاعد، فوهة الزوايا، فوهات النفخ الدقيقة ومحولات النفخ.",

    "grid-head-en": "EVERYDAY BENEFITS YOU WILL NOTICE IMMEDIATELY<br>The Ultimate Car & Workspace Detailing Tool<br>One compact handheld replaces compressed air cans, bulky vacuums, and tire inflators.",
    "grid-head-ar": "مزايا يومية تشعر بفارقها من أول استخدام<br>الأداة الشاملة لتنظيف السيارة والمكتب والأجهزة الذكية<br>جهاز واحد مدمج يغنيك عن علب الهواء المضغوط المكلفة والمكانس السلكية الكبيرة.",
    "grid-b1-en": "Saves Money on Canned Air<br>Never buy expensive, disposable compressed air spray cans for keyboards and electronics again.",
    "grid-b1-ar": "يوفر تكلفة علب الهواء المضغوط<br>انسَ شراء بخاخات الهواء المضغوط باهظة الثمن لتنظيف الكمبيوتر واللابتوب والكاميرات.",
    "grid-b2-en": "Deep AC Vent Dust Removal<br>Blasts out trapped desert dust from interior car air vents to keep cabin air smelling fresh.",
    "grid-b2-ar": "تنظيف عميق لفتحات التكييف<br>يطرد الأتربة العالقة داخل مجاري المكيف ليصبح هواء مقصورة السيارة نقياً ومنعشاً.",
    "grid-b3-en": "Inflates Pool & Camping Gear<br>Quickly pumps air into beach floats, children's pools, and outdoor air mattresses.",
    "grid-b3-ar": "نفخ ألعاب المسابح ومراتب البر<br>ينفخ عوامات الأطفال في الشاطئ ومراتب النوم الهوائية في الكشتات بسرعة ودون أي تعب.",
    "grid-b4-en": "Ultra-Compact Glovebox Size<br>Sleek metallic cylinder stores neatly in any center console, cup holder, or laptop bag.",
    "grid-b4-ar": "حجم مدمج يستقر في درج السيارة<br>تصميم أسطواني معدني أنيق وخفيف الوزن يناسب درج السيارة أو حقيبة اللابتوب بكل سهولة.",

    "table-head-en": "WHY CHOOSE ZELMIQO PROVAC 2-IN-1<br>Real Brushless Dual Vacuum & Blower Versatility<br>Compare our 75k RPM brushless turbine and 6 nozzles with single-function weak car vacuums.",
    "table-head-ar": "لماذا يفضل المحترفون جهاز زيلميكو برو فاك؟<br>قوة محرك براشلس ووظيفة مزدوجة تجمع الشفط والنفخ معاً<br>قارن بين سرعة التوربين 75 ألف دورة والملحقات الستة لدينا مقابل المكانس التقليدية محدودة الوظيفة.",
    "table-rows-en": "Row 1: 🌪️ 2-in-1 Vacuum + Air Duster | Zelmiqo (✓ Dual-port vacuum suction & 45m/s air blower) | Basic Car Vacs (✕ Weak vacuum only, cannot blow dust)\nRow 2: ⚡️ 75,000 RPM Brushless Motor | Zelmiqo (✓ Aerospace turbine power, zero motor wear) | Basic Car Vacs (✕ Brushed motor that overheats and burns out)\nRow 3: 🛡️ Dual HEPA & Steel Filter | Zelmiqo (✓ Double filtration protects motor from sand) | Basic Car Vacs (✕ Single paper filter that tears easily)\nRow 4: 🎯 6 Detailing Nozzles Included | Zelmiqo (✓ Vacuum heads, air dusters & inflator tips) | Basic Car Vacs (✕ 1-2 cheap plastic tips)\nRow 5: 🚚 Fast KSA Delivery | Zelmiqo (✓ Fast 7–8 days across Saudi Arabia) | Generic Brands (✕ Unverified slow transit with zero return guarantee)",
    "table-rows-ar": "الصف 1: 🌪️ 2 في 1 مكنسة ومنفاخ هواء | جهاز زيلميكو (✓ شفط قوي ونفخ هوائي سريع 45 م/ث) | المكانس العادية (✕ شفط ضعيف فقط ولا يمكنها نفخ الغبار)\nالصف 2: ⚡️ محرك براشلس 75,000 دورة | جهاز زيلميكو (✓ توربين ألمنيوم فائق القوة ولا يسخن) | المكانس العادية (✕ محرك فحمات قديم يسخن وتضعف قوته سريعاً)\nالصف 3: 🛡️ فلترة مزدوجة HEPA وفولاذ | جهاز زيلميكو (✓ حماية ثنائية للمحرك من رمال الصحراء) | المكانس العادية (✕ فلتر ورقي رديء يسد مجرى الهواء)\nالصف 4: 🎯 6 فوهات احترافية متنوعة | جهاز زيلميكو (✓ فوهات للشفط، فوهات للنفخ ومحولات للمسابح) | المكانس العادية (✕ فوهة أو فوهتان من البلاستيك الرديء)\nالصف 5: 🚚 شحن سريع لكافة المدن | جهاز زيلميكو (✓ توصيل خلال 7–8 أيام لكافة مدن المملكة) | الأجهزة المقلدة (✕ شحن بطيء لأسابيع دون ضمان ذهبي)",

    "marquee-text-en": "🚚 Fast 7–8 Days Delivery Across Saudi Arabia • 🛡️ 7-Day Golden Guarantee • 💳 Split in 4 with Tabby & Tamara • 🔒 100% Secure Mada & Apple Pay Checkout",
    "marquee-text-ar": "🚚 توصيل سريع خلال 7–8 أيام لكافة مدن المملكة • 🛡️ الضمان الذهبي 7 أيام • 💳 قسّم فاتورتك مع تابي وتمارا • 🔒 دفع آمن 100% عبر مدى وأبل باي",
    "cust-head-en": "OUR HAPPY CUSTOMERS<br>Real Car & Tech Detailing Stories Across Saudi Arabia<br>Read verified reviews from car enthusiasts, developers, and campers.",
    "cust-head-ar": "تجارب عملائنا المعتمدة<br>قصص موثقة من عشاق العناية بالسيارات والتقنية في مدن المملكة<br>تقييمات موثقة لعملاء استمتعوا بتنظيف فتحات المكيف ونفخ الغبار وشفط الفرش بكل سهولة واحترافية.",
    "rev-stats-en": "⭐️⭐️⭐️⭐️⭐️ 4.9 out of 5 Stars (Based on 164 Verified Purchases across Saudi Arabia)<br>98% would recommend to a friend • Fast 7–8 days delivery to Riyadh, Jeddah, Dammam & all Saudi cities.",
    "rev-stats-ar": "⭐️⭐️⭐️⭐️⭐️ 4.9 من 5 نجوم (استناداً إلى 164 تقييم موثق لعملاء داخل المملكة العربية السعودية)<br>98% يوصون بالجهاز لأصدقائهم • توصيل سريع وموثوق خلال 7–8 أيام للرياض، جدة، الدمام وكافة المدن.",
    "rel-head-en": "MORE AUTOMOTIVE & TECH ACCESSORIES<br>You May Also Like<br>Smart handheld accessories designed to keep your gear in showroom condition—delivered in 7–8 days across Saudi Arabia.",
    "rel-head-ar": "المزيد من أجهزة العناية بالسيارات والتقنية<br>منتجات مختارة قد تنال إعجابك<br>أجهزة ذكية وعصرية صُممت للحفاظ على نظافة وبريق سيارتك وأجهزتك — مع توصيل خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-title-en": "ProVac 2-in-1 Wireless Car Vacuum Cleaner & Air Duster | Zelmiqo® KSA",
    "seo-title-ar": "مكنسة ومنفاخ هواء السيارة اللاسلكي 2 في 1 بمحرك براشلس توربيني | زيلميكو السعودية",
    "seo-desc-en": "Dual-function 2-in-1 cordless car vacuum cleaner and high-speed air duster blower with 75,000 RPM brushless motor and 6 nozzles. Fast 7–8 days delivery across Saudi Arabia.",
    "seo-desc-ar": "مكنسة ومنفاخ هواء للسيارة 2 في 1 بمحرك براشلس توربيني 75,000 دورة بالدقيقة مع 6 فوهات متخصصة للشفط والنفخ. توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-keywords-en": "2 in 1 car vacuum and air duster saudi arabia, brushless car vacuum cleaner ksa, electric air duster blower, portable car detailing vac 7-8 days delivery, tabby tamara car gadgets",
    "seo-keywords-ar": "مكنسة ومنفاخ هواء 2 في 1 السعودية, مكنسة سيارة براشلس, منفاخ هواء للسيارة والكمبيوتر, مكنسة تنظيف فتحات المكيف, تقسيط تابي وتمارا, متجر زيلميكو"
}

# Generate Batch 4 Pages
generate_product_page("NutriBlend 6-Blade Portable Juicer", p_6blade, {}, "product-portable-6-blade-juicer.html")
generate_product_page("DuoCup Portable Double-Cup Juicer", p_doublecup, {}, "product-portable-double-cup-juicer.html")
generate_product_page("FreshPress Wireless Citrus Juicer", p_citrus, {}, "product-portable-usb-citrus-juicer.html")
generate_product_page("TurboClean Pro Cordless Car Vacuum", p_carvac9k, {}, "product-cordless-handheld-car-vacuum.html")
generate_product_page("ProVac 2-in-1 Wireless Car Vacuum & Duster", p_provac, {}, "product-portable-wireless-car-vacuum.html")
print("Batch 4 generation finished successfully!")
