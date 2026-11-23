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
# 1. Bionic Finger Neck Massager (PRD-05)
# -------------------------------------------------------------
p_neck_massager = {
    "hero-title-en": "Bionic Finger Shiatsu Neck & Shoulder Kneading Massager with Heat",
    "hero-title-ar": "جهاز مساج وتدليك الرقبة والأكتاف الحيوي 4D مع تدفئة حرارية",
    "hero-subtitle-en": "Real Human-Touch Shiatsu Kneading & Soothing Heat<br>Melts away desk-work neck tension, shoulder stiffness, and fatigue in 15 minutes. Fast 7–8 days delivery across Saudi Arabia.",
    "hero-subtitle-ar": "تدليك شياتسو يحاكي حركة الأصابع الحقيقية مع تدفئة مهدئة<br>يزيل تشنجات الرقبة وإجهاد الأكتاف وساعات الجلوس الطويلة في 15 دقيقة، مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "hero-callout-en": "4D Human-Touch Kneading & Thermal Relief",
    "hero-callout-ar": "تدليك 4D يحاكي أصابع اليد وتدفئة مريحة",
    "hero-bullets-en": "• 🖐️ 4D Bionic Finger Kneading Nodes\n• 🌡️ Soothing 42°C Infrared Heat\n• 🔄 Bi-Directional Auto-Reversing Nodes\n• 🔋 Cordless & Rechargeable Freedom",
    "hero-bullets-ar": "• 🖐️ رؤوس تدليك 4D تحاكي أصابع المعالج المحترف\n• 🌡️ تدفئة حرارية 42° لتفكيك العقد العضلية المتشنجة\n• 🔄 دوران ثنائي الاتجاه يعكس حركته تلقائياً\n• 🔋 تصميم لاسلكي قابل لإعادة الشحن والتنقل",
    
    "faq-head-en": "PROFESSIONAL SHIATSU THERAPY AT HOME<br>Relieve Chronic Desk & Commute Neck Strain<br>Engineered to mimic real human thumbs kneading deep into trapezoids and cervical spine. Fast 7–8 days delivery across Saudi Arabia.",
    "faq-head-ar": "جلسة مساج شياتسو احترافية براحة منزلك<br>تخلص من آلام الرقبة وتصلب الأكتاف اليومي<br>صُمم خصيصاً ليحاكي ضغط أصابع المعالج الطبيعي بعمق في عضلات الرقبة والكتفين. توصيل سريع وموثوق خلال 7–8 أيام لكافة مناطق المملكة.",
    "faq-1-en": "How does bionic kneading feel compared to vibrating cushions?<br>Unlike weak vibrations that only buzz skin surface, our bionic 4D nodes grip, roll, and knead deep muscle fibers, physically releasing trapped knots and tension.",
    "faq-1-ar": "ما الفرق بين التدليك الحيوي ووسائد الاهتزاز العادية؟<br>وسائد الاهتزاز تهتز سطحياً فقط، بينما رؤوس التدليك الحيوية 4D تمسك بالعضلات وتفرك العقد العضلية بعمق حقيقي يفكك التشنج مثل أيدي المعالج المتخصص.",
    "faq-2-en": "Is the infrared heat therapy safe on bare skin?<br>Yes, the gentle 42°C constant temperature improves local blood flow and relaxes rigid tendons without burning or overheating delicate neck skin.",
    "faq-2-ar": "هل التدفئة الحرارية آمنة ولطيفة على البشرة؟<br>نعم تماماً، التدفئة بدرجة 42° حرارة علاجية مدروسة ومريحة تنشط الدورة الدموية وترخي الأربطة المتشنجة بأمان تام ودون أي سخونة مزعجة.",
    "faq-3-en": "Can I use it on my lower back, calves, and thighs?<br>Absolutely! The flexible ergonomic strap design allows you to position the massager effortlessly across your lower lumbar, hamstrings, or calves.",
    "faq-3-ar": "هل يمكن استخدامه لأسفل الظهر والساقين والفخذين؟<br>نعم بالتأكيد! تصميم الأحزمة المريحة والمقبض المرن يتيح لك تثبيته بسهولة على فقرات أسفل الظهر، أو عضلات الساق والكتف حسب حاجتك.",
    "faq-4-en": "Does it operate cordlessly without staying plugged in?<br>Yes! It features a heavy-duty rechargeable battery delivering up to 7–8 soothing massage cycles on a single charge for use anywhere.",
    "faq-4-ar": "هل يعمل الجهاز لاسلكياً دون الحاجة للبقاء متصلاً بالكهرباء؟<br>نعم! مزود ببطارية ليثيوم قوية قابلة لإعادة الشحن تمنحك من 7 إلى 8 جلسات مساج كاملة بالشحنة الواحدة لتسترخي في أي مكان بالمنزل أو المكتب.",

    "twocol-head-en": "TARGETED DEEP TISSUE RELIEF • YOUR PERSONAL MASSEUSE<br>Melt Away Daily Stress in a Soothing 15-Minute Session<br>Restore comfortable posture and neck mobility after long office hours or highway drives. Fast 7–8 days delivery across Saudi Arabia.",
    "twocol-head-ar": "تخفيف عميق لتشنجات العضلات • مدلكك الشخصي في منزلك<br>تخلص من إجهاد وتعب اليوم في جلسة تدليك مريحة مدتها 15 دقيقة<br>استعد مرونة رقبتك وراحتك بعد ساعات الدوام الطويلة أو القيادة في الزحام، مع توصيل سريع وموثوق خلال 7–8 أيام لكافة مدن المملكة.",
    "twocol-cards-en": "Card 1: 🚚 Fast 7–8 Days Delivery\nCard 2: 🛡️ 14-Day Golden Guarantee\nCard 3: 💳 Secure Mada & Apple Pay",
    "twocol-cards-ar": "البطاقة 1: 🚚 توصيل سريع خلال 7–8 أيام\nالبطاقة 2: 🛡️ الضمان الذهبي 14 يوماً\nالبطاقة 3: 💳 دفع آمن بمدى وأبل باي",

    "center-head-en": "4D BIOMECHANICAL KNEADING MASSAGE<br>Deep Finger Pressure with Calibrated Thermal Comfort<br>Wrap-around shoulder harness lets you pull to control custom massage intensity effortlessly.",
    "center-head-ar": "تدليك ميكانيكي حيوي بتقنية 4D المتطورة<br>ضغط أصابع عميق مع تدفئة حرارية مدروسة<br>تصميم حزام الكتف المزدوج يتيح لك سحب المقابض للتحكم بقوة الضغط والعمق بكل سلاسة.",
    "center-b1-en": "4D Bionic Finger Nodes<br>Multi-contact rotating nodes replicate authentic masseur grip-and-release motions.",
    "center-b1-ar": "رؤوس تدليك 4D حيوية<br>رؤوس تدليك ناعمة تدور وتضغط بمرونة تحاكي حركة أصابع اليدين الحقيقية بدقة.",
    "center-b2-en": "Calibrated 42°C Thermal Soothing<br>Penetrates deep into tight cervical muscles to dissolve stubborn knotting.",
    "center-b2-ar": "تدفئة حرارية لطيفة 42°<br>تتغلغل بعمق في عضلات الرقبة المتيبسة لتذيب العقد والتشنج وتعيد الحيوية.",
    "center-b3-en": "Dual Rotating Directions<br>Automatically alternates clockwise and counter-clockwise every 60 seconds.",
    "center-b3-ar": "دوران مزدوج تلقائي<br>يعكس اتجاه الدوران تلقائياً كل دقيقة لتدليك متوازن يشمل كافة زوايا العضلة.",
    "center-b4-en": "Whisper-Quiet Pure Copper Motor<br>Delivers high torque kneading power without loud disturbing mechanical humming.",
    "center-b4-ar": "محرك نحاسي هادئ جداً<br>عزم قوي يدلك العضلات بقوة واسترخاء تام بدون أي ضجيج أو إزعاج.",

    "grid-head-en": "EVERYDAY BENEFITS YOU WILL FEEL IMMEDIATELY<br>Total Relaxation from Neck to Lower Back<br>Transform stiff posture and tired muscles into relaxed vitality every evening.",
    "grid-head-ar": "مزايا يومية تشعر بفرقها فورياً<br>استرخاء شامل يبدأ من الرقبة وحتى أسفل الظهر<br>تخلص من انحناء الكتفين والإجهاد اليومي واستعد نشاطك وراحتك في كل مساء.",
    "grid-b1-en": "Immediate Neck Pain Relief<br>Releases painful muscle spasms caused by looking down at mobile screens.",
    "grid-b1-ar": "راحة فورية من ألم الرقبة<br>يفكك التشنجات الناتجة عن إمالة الرأس المستمرة للنظر في شاشة الجوال واللابتوب.",
    "grid-b2-en": "Better Sleep Quality<br>Evening relaxation promotes deeper, uninterrupted sleep and stress-free rest.",
    "grid-b2-ar": "نوم هانئ وأكثر عمقاً<br>جلسة مساج قبل النوم ترخي الأعصاب وتساعدك على الاستغراق بنوم هادئ ومريح.",
    "grid-b3-en": "Hands-Free Ergonomic Straps<br>Wear the straps around your arms so you can read, work, or relax freely.",
    "grid-b3-ar": "أحزمة مريحة بدون استخدام اليدين<br>ضع ذراعيك في المقابض براحة لمتابعة القراءة أو مشاهدة التلفاز أثناء المساج.",
    "grid-b4-en": "Breathable Hypoallergenic Fabric<br>Removable, washable mesh cover stays cool and gentle against warm skin.",
    "grid-b4-ar": "قماش شبكي ناعم وقابل للتنفس<br>غطاء قابل للفك والغسيل، ناعم على البشرة ويمنع التعرق أثناء التدفئة.",

    "table-head-en": "WHY CHOOSE ZELMIQO BIONICTOUCH<br>Authentic Deep-Tissue Kneading You Can Feel<br>Compare our mechanical 4D fingers and thermal copper engine with cheap vibration belts.",
    "table-head-ar": "لماذا يفضل عملاؤنا جهاز مساج زيلميكو؟<br>تدليك عميق حقيقي تشعر بفرقه من أول دقيقة<br>قارن بين رؤوس التدليك الحيوية 4D والتدفئة المعتمدة لدينا مقابل أحزمة الاهتزاز الرخيصة.",
    "table-rows-en": "Row 1: 🖐️ 4D Bionic Kneading | Zelmiqo (✓ Real thumb-like gripping & kneading) | Vibration Belts (✕ Weak buzzing surface vibrations)\nRow 2: 🌡️ 42°C Infrared Heat | Zelmiqo (✓ Built-in thermal deep-tissue therapy) | Vibration Belts (✕ No heating or dangerously hot coils)\nRow 3: 🔋 Cordless Rechargeable | Zelmiqo (✓ Long-life lithium battery, 8 sessions) | Vibration Belts (✕ Must remain tied to wall socket)\nRow 4: 🤫 Quiet Motor Power | Zelmiqo (✓ High-torque brushless copper motor) | Vibration Belts (✕ Annoying loud buzzing noise)\nRow 5: 🚚 Fast KSA Delivery | Zelmiqo (✓ Fast 7–8 days across Saudi Arabia) | Generic Brands (✕ Weeks of unverified slow shipping)",
    "table-rows-ar": "الصف 1: 🖐️ مساج 4D حيوي حقيقي | جهاز زيلميكو (✓ ضغط وفرك عميق يحاكي حركة الأصابع) | أحزمة الاهتزاز (✕ طنين واهتزاز سطحي عديم الفائدة)\nالصف 2: 🌡️ تدفئة حرارية 42° | جهاز زيلميكو (✓ حرارة علاجية آمنة تريح العضلات) | أحزمة الاهتزاز (✕ بدون تدفئة أو أسلاك حرارية خطيرة)\nالصف 3: 🔋 بطارية لاسلكية قوية | جهاز زيلميكو (✓ ليثيوم تدوم 8 جلسات متتالية بالشحنة) | أحزمة الاهتزاز (✕ مقيدة بسلك جداري قصير يمنع الحركة)\nالصف 4: 🤫 هدوء تام أثناء الاستخدام | جهاز زيلميكو (✓ محرك نحاسي قوي بدون أي صوت مزعج) | أحزمة الاهتزاز (✕ صوت طنين واهتزاز عالي يسبب الصداع)\nالصف 5: 🚚 شحن سريع لكافة المدن | جهاز زيلميكو (✓ توصيل خلال 7–8 أيام لكافة مدن المملكة) | الأجهزة العادية (✕ انتظار أسابيع طويلة دون ضمان محلي)",

    "marquee-text-en": "🚚 Fast 7–8 Days Delivery Across Saudi Arabia • 🛡️ 14-Day Golden Guarantee • 💳 Split in 4 with Tabby & Tamara • 🔒 100% Secure Mada & Apple Pay Checkout",
    "marquee-text-ar": "🚚 توصيل سريع خلال 7–8 أيام لكافة مدن المملكة • 🛡️ الضمان الذهبي 14 يوماً • 💳 قسّم فاتورتك مع تابي وتمارا • 🔒 دفع آمن 100% عبر مدى وأبل باي",
    "cust-head-en": "OUR HAPPY CUSTOMERS<br>Real Neck & Shoulder Relief Stories Across Saudi Arabia<br>Read verified reviews from office professionals and drivers who eliminated tension.",
    "cust-head-ar": "تجارب عملائنا المعتمدة<br>قصص راحة حقيقية لموظفين وسائقين في مدن المملكة<br>تقييمات موثقة لعملاء تخلصوا من آلام الرقبة وتصلب الأكتاف واستعادوا نشاطهم اليومي.",
    "rev-stats-en": "⭐️⭐️⭐️⭐️⭐️ 4.9 out of 5 Stars (Based on 156 Verified Purchases across Saudi Arabia)<br>98% would recommend to a friend • Fast 7–8 days delivery to Riyadh, Jeddah, Dammam & all Saudi cities.",
    "rev-stats-ar": "⭐️⭐️⭐️⭐️⭐️ 4.9 من 5 نجوم (استناداً إلى 156 تقييم موثق لعملاء داخل المملكة العربية السعودية)<br>98% يوصون بالجهاز لأصدقائهم • توصيل سريع وموثوق خلال 7–8 أيام للرياض، جدة، الدمام وكافة المدن.",
    "rel-head-en": "MORE WELLNESS INNOVATIONS TO EXPLORE<br>You May Also Like<br>Smart health and relaxation essentials designed to restore your vitality—delivered in 7–8 days across Saudi Arabia.",
    "rel-head-ar": "المزيد من ابتكارات الراحة والاسترخاء<br>منتجات مختارة قد تنال إعجابك<br>أجهزة صحية ذكية متوافقة ومثالية لتجديد نشاطك اليومي — مع توصيل خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-title-en": "Bionic Finger Shiatsu Neck & Shoulder Kneading Massager | Zelmiqo® KSA",
    "seo-title-ar": "جهاز مساج وتدليك الرقبة والأكتاف الحيوي 4D مع تدفئة حرارية | زيلميكو السعودية",
    "seo-desc-en": "Human-touch 4D bionic finger neck and shoulder kneading massager with 42°C infrared heat. Relieves desk strain and tension. Fast 7–8 days delivery across Saudi Arabia.",
    "seo-desc-ar": "جهاز تدليك الرقبة والأكتاف 4D يحاكي أصابع اليدين مع تدفئة حرارية علاجية 42°. يزيل آلام وتشنجات الرقبة مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-keywords-en": "bionic neck massager saudi arabia, shiatsu shoulder kneading massager ksa, heated neck pillow, cordless cervical massager 7-8 days delivery, tabby tamara wellness devices",
    "seo-keywords-ar": "جهاز مساج الرقبة والكتف السعودية, جهاز تدليك شياتسو, مخدة مساج حرارية, علاج تشنج الرقبة, تقسيط تابي وتمارا, متجر زيلميكو توصيل 7-8 ايام"
}

# -------------------------------------------------------------
# 2. Smart Fascia Massage Gun (PRD-16)
# -------------------------------------------------------------
p_massage_gun = {
    "hero-title-en": "ProPercuss 9-Speed Deep Tissue Fascia Massage Gun with LCD Touchscreen",
    "hero-title-ar": "مسدس تدليك العضلات العميق الاحترافي بـ 9 سرعات وشاشة لمس ذكية",
    "hero-subtitle-en": "Pro-Athlete Percussive Recovery & Deep Tissue Relief<br>High-torque brushless motor delivers 3,200 RPM deep muscle penetration to dissolve soreness. Fast 7–8 days delivery across Saudi Arabia.",
    "hero-subtitle-ar": "استشفاء عضلي احترافي وتخفيف فوري لإجهاد التمارين<br>محرك قوي بدون فحمات يمنحك 3,200 ضربة في الدقيقة لفك تصلب العضلات المتشنجة، مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "hero-callout-en": "Pro Percussive Gun with 9 Speed Levels",
    "hero-callout-ar": "مسدس مساج احترافي بتسع سرعات ذكية",
    "hero-bullets-en": "• ⚡️ Powerful 3,200 RPM Percussive Motor\n• 🎚️ 9 Smart Adjustable Speed Levels\n• 📱 High-Definition LCD Touchscreen\n• 🎯 4 Specialized Therapy Massage Heads",
    "hero-bullets-ar": "• ⚡️ محرك عزم فائق يولد 3,200 ضربة تدليك بالدقيقة\n• 🎚️ 9 مستويات سرعة متدرجة للإحماء والاستشفاء\n• 📱 شاشة لمس LCD ذكية لعرض السرعة والبطارية\n• 🎯 4 رؤوس تدليك مخصصة لجميع مجموعات العضلات",
    
    "faq-head-en": "PROFESSIONAL ATHLETIC RECOVERY AT HOME<br>Relieve Muscle Soreness & Accelerate Recovery<br>Target tight fascia, lactic acid buildup, and post-gym stiffness with calibrated percussive therapy. Fast 7–8 days delivery across Saudi Arabia.",
    "faq-head-ar": "استشفاء رياضي متقدم لعضلاتك في المنزل<br>تخلص من حمض اللاكتيك وألم التمارين الشاقة فوراً<br>علاج اهتزازي عميق يخترق الأنسجة العضلية ويسرع الشفاء بعد النادي والعمل الشاق. توصيل سريع وموثوق خلال 7–8 أيام لكافة مناطق المملكة.",
    "faq-1-en": "How does deep tissue percussion relieve muscle soreness?<br>Percussive pulses travel 12mm deep into muscle tissue, increasing oxygenated blood flow, breaking down lactic acid adhesions, and restoring joint flexibility.",
    "faq-1-ar": "كيف يساعد التدليك الإيقاعي على تسريع استشفاء العضلات؟<br>تصل الضربات الإيقاعية لعمق 12 ملم داخل الأنسجة العضلية، مما ينشط تدفق الدم المحمل بالأكسجين ويفتت ترسبات حمض اللاكتيك المسببة للألم.",
    "faq-2-en": "What is the function of each of the 4 included heads?<br>Ball head: for large muscle groups (quads, glutes); U-shaped head: for spine and Achilles tendon; Bullet head: for pinpoint trigger knots and palms; Flat head: for overall relaxation.",
    "faq-2-ar": "ما هي استخدامات الرؤوس الأربعة المرفقة مع الجهاز؟<br>الرأس الكروي للعضلات الكبيرة (الأفخاذ والظهر)، ورأس U المحيطي لفقرات العمود الفقري وأوتار القدم، والرأس المدبب لنقاط الألم العميقة، والرأس المسطح للاسترخاء العام.",
    "faq-3-en": "Is it suitable for non-athletes who sit at desks all day?<br>Yes! Speeds 1–3 provide gentle tension relief for tight lower backs, calf cramping, and neck stiffness caused by sedentary desk work or long highway driving.",
    "faq-3-ar": "هل الجهاز مفيد لغير الرياضيين ولمن يجلسون ساعات طويلة؟<br>نعم بالتأكيد! السرعات من 1 إلى 3 مثالية لإرخاء عضلات أسفل الظهر، وتخفيف شد الساقين، وتصلب الرقبة الناتج عن الجلوس المكتبي أو القيادة الطويلة.",
    "faq-4-en": "How long does the rechargeable battery last on one charge?<br>The high-capacity 2,500mAh lithium battery provides up to 6 hours of continuous runtime, easily covering 2–3 weeks of daily 15-minute recovery sessions.",
    "faq-4-ar": "كم تدوم بطارية الجهاز القابلة لإعادة الشحن؟<br>تحتوي على بطارية ليثيوم متطورة بسعة 2,500 مللي أمبير تدوم حتى 6 ساعات تشغيل متواصل، مما يكفيك لـ 2 إلى 3 أسابيع من الجلسات اليومية بالشحنة الواحدة.",

    "twocol-head-en": "ATHLETE-GRADE PERCUSSION • RAPID PAIN RELIEF<br>Transform Your Post-Workout Recovery in 10 Minutes<br>Shatter muscle knots, boost mobility, and relieve deep fatigue. Fast 7–8 days delivery across Saudi Arabia.",
    "twocol-head-ar": "مساج إيقاعي رياضي • تسكين سريع لألم العضلات<br>حسّن استشفاء عضلاتك بعد التمرين في 10 دقائق فقط<br>فكك العقد العضلية واستعد مرونة جسمك ونشاطك بدون ألم، مع توصيل سريع وموثوق خلال 7–8 أيام لكافة مدن المملكة.",
    "twocol-cards-en": "Card 1: 🚚 Fast 7–8 Days Delivery\nCard 2: 🛡️ 14-Day Golden Guarantee\nCard 3: 💳 Secure Mada & Apple Pay",
    "twocol-cards-ar": "البطاقة 1: 🚚 توصيل سريع خلال 7–8 أيام\nالبطاقة 2: 🛡️ الضمان الذهبي 14 يوماً\nالبطاقة 3: 💳 دفع آمن بمدى وأبل باي",

    "center-head-en": "PRECISION PERCUSSIVE ENGINEERING<br>Deep Penetration with Brushless Motor Whisper Tech<br>Silicone anti-slip ergonomic handle ensures comfortable, controlled grip during high-intensity sessions.",
    "center-head-ar": "هندسة إيقاعية دقيقة لعضلاتك<br>اختراق عميق للأنسجة مع محرك صامت فائق القوة<br>مقبض سيليكوني مانع للانزلاق يمنحك ثباتاً تاماً وتحكماً مريحاً حتى مع السرعات العالية.",
    "center-b1-en": "High-Torque Brushless Motor<br>Delivers up to 3,200 percussions per minute without stalling under heavy pressure.",
    "center-b1-ar": "محرك عزم قوي بدون فحمات<br>يمنحك حتى 3,200 ضربة إيقاعية بالدقيقة بقوة ثابتة لا تتوقف حتى مع الضغط العضلي الشديد.",
    "center-b2-en": "9 Speed Adjustment Tiers<br>Dial from gentle muscle wakeup (tier 1) to deep fascia breakdown (tier 9).",
    "center-b2-ar": "9 مستويات سرعة ذكية<br>تدرج مريح يبدأ من الإحماء الخفيف (المستوى 1) وصولاً لفك العقد العضلية العميقة (المستوى 9).",
    "center-b3-en": "Smart LCD Touch Display<br>Sensitive touch panel shows current speed tier and precise battery level.",
    "center-b3-ar": "شاشة لمس LCD ذكية<br>لوحة تحكم تعمل باللمس تعرض سرعة التدليك المختارة ونسبة البطارية المتبقية بدقة.",
    "center-b4-en": "Type-C Fast Charging<br>Charge anywhere with universal Type-C cables, power banks, or car chargers.",
    "center-b4-ar": "شحن سريع عبر منفذ Type-C<br>اشحن مسدسك بسهولة عبر كابل تايب سي في المنزل أو السيارة أو شاحن الجوال المتنقل.",

    "grid-head-en": "EVERYDAY BENEFITS YOU WILL FEEL IMMEDIATELY<br>Faster Recovery and Peak Athletic Performance<br>Say goodbye to morning muscle stiffness and enjoy lighter, energized limbs.",
    "grid-head-ar": "مزايا يومية تشعر بفارقها فوراً<br>استشفاء أسرع وأداء بدني ورياضي متفوق<br>ودّع تيبس العضلات الصباحي واستمتع بجسم خفيف ونشاط متجدد طوال اليوم.",
    "grid-b1-en": "Eliminate Post-Gym Soreness<br>Flushes out lactic acid after heavy gym lifting, running, or padel matches.",
    "grid-b1-ar": "القضاء على ألم ما بعد التمرين<br>يساعد على تصريف حمض اللاكتيك بعد تمارين الحديد، الجري، أو مباريات البادل الشاقة.",
    "grid-b2-en": "Relieves Sedentary Back Pain<br>Loosens tight hip flexors and lower back strain after long desk shifts.",
    "grid-b2-ar": "تخفيف ألم الظهر من الجلوس<br>يرخي عضلات أسفل الظهر وأربطة الحوض المشدودة نتيجة الجلوس المكتبي الطويل.",
    "grid-b3-en": "Increases Joint Range of Motion<br>Pre-workout percussive warmup prepares tendons and minimizes injury risks.",
    "grid-b3-ar": "زيادة مرونة وحركة المفاصل<br>إحماء إيقاعي قبل التمارين يجهز الأوتار ويقلل فرص التمزقات والإصابات الرياضية.",
    "grid-b4-en": "Quiet Acoustic Operation<br>Quiet-glide tech lets you massage muscles in the bedroom or living room without noise.",
    "grid-b4-ar": "تشغيل هادئ بدون إزعاج<br>تقنية كتم الصوت الحديثة تتيح لك استخدامه في الصالة أو غرفة النوم دون إزعاج من حولك.",

    "table-head-en": "WHY CHOOSE ZELMIQO PROPERCUSS<br>Engineered for True Deep-Tissue Penetration<br>Compare our brushless motor torque and amplitude against cheap vibrating massage toys.",
    "table-head-ar": "لماذا يفضل الرياضيون مسدس زيلميكو؟<br>قوة وعمق حقيقي لاختراق الأنسجة العضلية<br>قارن بين عزم المحرك بدون فحمات وعمق الضربات لدينا مقابل أجهزة الاهتزاز البلاستيكية الضعيفة.",
    "table-rows-en": "Row 1: ⚡️ 12mm Percussive Amplitude | Zelmiqo (✓ Deep tissue fascia penetration) | Cheap Guns (✕ Shallow 4-6mm surface buzzing)\nRow 2: 🎚️ 9 Speed Touch Screen | Zelmiqo (✓ LCD touch panel with fine control) | Cheap Guns (✕ 1-3 clunky physical buttons)\nRow 3: 🔇 Whisper Brushless Motor | Zelmiqo (✓ Under 45dB quiet glide system) | Cheap Guns (✕ Loud rattling plastic vibration noise)\nRow 4: 🔋 6h Lithium Runtime | Zelmiqo (✓ 2,500mAh high-density battery) | Cheap Guns (✕ Dies after 20 minutes under pressure)\nRow 5: 🚚 Fast KSA Delivery | Zelmiqo (✓ Fast 7–8 days across Saudi Arabia) | Generic Brands (✕ Unverified overseas shipping without warranty)",
    "table-rows-ar": "الصف 1: ⚡️ عمق ضربات 12 ملم | مسدس زيلميكو (✓ اختراق حقيقي للأنسجة العضلية العميقة) | الأجهزة الرخيصة (✕ اهتزاز سطحي ضعيف بعمق 4 ملم فقط)\nالصف 2: 🎚️ 9 سرعات بشاشة لمس | مسدس زيلميكو (✓ لوحة تحكم ذكية وشاشة LCD واضحة) | الأجهزة الرخيصة (✕ أزرار ميكانيكية بدائية بـ 3 سرعات فقط)\nالصف 3: 🔇 محرك هادئ فائق التطور | مسدس زيلميكو (✓ صوت هادئ أقل من 45 ديسيبل) | الأجهزة الرخيصة (✕ صوت مزعج واهتزاز يرج اليدين)\nالصف 4: 🔋 بطارية تدوم 6 ساعات | مسدس زيلميكو (✓ سعة 2,500 مللي أمبير تدوم لأسابيع) | الأجهزة الرخيصة (✕ تفرغ بطاريتها بعد 20 دقيقة عند الضغط)\nالصف 5: 🚚 شحن سريع لكافة المدن | مسدس زيلميكو (✓ توصيل خلال 7–8 أيام لكافة مدن المملكة) | الأجهزة المقلدة (✕ انتظار أسابيع طويلة دون أي ضمان محلي)",

    "marquee-text-en": "🚚 Fast 7–8 Days Delivery Across Saudi Arabia • 🛡️ 14-Day Golden Guarantee • 💳 Split in 4 with Tabby & Tamara • 🔒 100% Secure Mada & Apple Pay Checkout",
    "marquee-text-ar": "🚚 توصيل سريع خلال 7–8 أيام لكافة مدن المملكة • 🛡️ الضمان الذهبي 14 يوماً • 💳 قسّم فاتورتك مع تابي وتمارا • 🔒 دفع آمن 100% عبر مدى وأبل باي",
    "cust-head-en": "OUR HAPPY CUSTOMERS<br>Real Muscle Recovery Experiences Across Saudi Arabia<br>Read verified reviews from fitness enthusiasts and athletes who upgraded their routine.",
    "cust-head-ar": "تجارب عملائنا المعتمدة<br>نتائج استشفاء حقيقية لرياضيين في مختلف مدن المملكة<br>تقييمات موثقة لعملاء استعادوا نشاط عضلاتهم وتخلصوا من الإجهاد مع مسدس مساج زيلميكو.",
    "rev-stats-en": "⭐️⭐️⭐️⭐️⭐️ 4.9 out of 5 Stars (Based on 168 Verified Purchases across Saudi Arabia)<br>98% would recommend to a friend • Fast 7–8 days delivery to Riyadh, Jeddah, Dammam & all Saudi cities.",
    "rev-stats-ar": "⭐️⭐️⭐️⭐️⭐️ 4.9 من 5 نجوم (استناداً إلى 168 تقييم موثق لعملاء داخل المملكة العربية السعودية)<br>98% يوصون بالجهاز لأصدقائهم • توصيل سريع وموثوق خلال 7–8 أيام للرياض، جدة، الدمام وكافة المدن.",
    "rel-head-en": "MORE RECOVERY ESSENTIALS TO EXPLORE<br>You May Also Like<br>Smart health devices designed to keep your body primed and active—delivered in 7–8 days across Saudi Arabia.",
    "rel-head-ar": "المزيد من أجهزة الاستشفاء البدني<br>منتجات مختارة قد تنال إعجابك<br>أجهزة رياضية وصحية ذكية صُممت لدعم لياقتك ونشاطك اليومي — مع توصيل خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-title-en": "ProPercuss 9-Speed Deep Tissue Fascia Massage Gun | Zelmiqo® KSA",
    "seo-title-ar": "مسدس تدليك العضلات العميق الاحترافي بـ 9 سرعات وشاشة لمس ذكية | زيلميكو السعودية",
    "seo-desc-en": "High-torque 3,200 RPM deep tissue percussive massage gun with 9 speed tiers, LCD touchscreen, and 4 therapy heads. Fast 7–8 days delivery across Saudi Arabia.",
    "seo-desc-ar": "مسدس مساج احترافي لتدليك العضلات 3,200 ضربة بالدقيقة مع 9 سرعات وشاشة لمس LCD. استشفاء عضلي سريع مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-keywords-en": "massage gun saudi arabia, deep tissue fascia gun ksa, muscle recovery percussive tool, 9 speed massage gun 7-8 days delivery, tabby tamara gym recovery devices",
    "seo-keywords-ar": "مسدس مساج العضلات السعودية, جهاز تدليك العضلات الاحترافي, مسدس فاشيا رياضي, علاج ألم العضلات, تقسيط تابي وتمارا, متجر زيلميكو توصيل 7-8 ايام"
}

# -------------------------------------------------------------
# 3. USB Coffee Mug Warmer (PRD-18)
# -------------------------------------------------------------
p_mug_warmer = {
    "hero-title-en": "ThermoDesk Smart Heated Beverage Coaster & Mug Warmer with 3 Temps",
    "hero-title-ar": "قاعدة تسخين الأكواب والمشروبات الذكية للمكتب مع 3 درجات حرارة",
    "hero-subtitle-en": "Keep Your Coffee, Tea & Karak Hot All Day Long<br>Smart constant temperature heating plate with 3 custom warmth levels and auto-shutoff safety. Fast 7–8 days delivery across Saudi Arabia.",
    "hero-subtitle-ar": "حافظ على حرارة قهوتك وشاهيك وشاي الكرك طازجاً وساخناً طوال اليوم<br>قاعدة تسخين ذكية بثلاث درجات حرارة وميزة أمان الإغلاق التلقائي، مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "hero-callout-en": "Smart Mug Warmer with 3 Heating Tiers",
    "hero-callout-ar": "قاعدة تسخين أكواب ذكية بثلاث مستويات حرارة",
    "hero-bullets-en": "• ☕️ 3 Calibrated Temp Settings (55°C, 65°C, 75°C)\n• ⏱️ Smart 8-Hour Auto-Shutoff Timer\n• 🛡️ Spill-Proof Tempered Glass Surface\n• 🔌 Universal Safe USB / Type-C Power",
    "hero-bullets-ar": "• ☕️ 3 درجات حرارة مضبوطة بدقة (55°، 65°، 75° مئوية)\n• ⏱️ مؤقت أمان ذكي يغلق تلقائياً بعد 8 ساعات\n• 🛡️ سطح زجاجي حراري مقاوم للانسكاب وسهل التنظيف\n• 🔌 تشغيل USB آمن ومتوافق مع المكاتب والمنازل",
    
    "faq-head-en": "PERFECT WARMTH FOR EVERY WORKDAY SIP<br>Never Drink Cold Coffee or Lukewarm Tea Again<br>Designed for Saudi coffee connoisseurs, Karak lovers, and busy professionals. Fast 7–8 days delivery across Saudi Arabia.",
    "faq-head-ar": "رشفة دافئة ومثالية طوال ساعات دوامك<br>انسَ القهوة الباردة وإعادة تسخين الشاي بالميكروويف<br>صُممت خصيصاً لعشاق القهوة المختصة وشاي الكرك وأصحاب الأعمال في المكاتب والمنازل. توصيل سريع وموثوق خلال 7–8 أيام لكافة مناطق المملكة.",
    "faq-1-en": "What types of cups and mugs work best on this warming coaster?<br>It works best with flat-bottom mugs made of ceramic, glass, stainless steel, or enameled metal. Flat surfaces ensure optimal heat transfer.",
    "faq-1-ar": "ما هي أنواع الأكواب التي تتوافق مع قاعدة التسخين؟<br>تعمل بكفاءة عالية مع الأكواب ذات القاعدة المسطحة المصنوعة من السيراميك، الزجاج، الستانلس ستيل، أو الأكواب المعدنية لضمان التوصيل الحراري الأمثل.",
    "faq-2-en": "What temperature should I select for coffee versus tea?<br>55°C is ideal for keeping Saudi warm milk and green tea gentle; 65°C keeps Americano and latte perfectly hot; 75°C keeps robust black tea and Karak piping hot.",
    "faq-2-ar": "ما هي درجة الحرارة الأنسب للقهوة مقابل الشاي؟<br>درجة 55° مثالية للحليب والشاي الأخضر الدافئ، و 65° مثالية للقهوة الأمريكية واللاتيه، بينما 75° مثالية للشاي الأسود وشاي الكرك ليبقى ساخناً كأنه صُب للتو.",
    "faq-3-en": "Is the surface safe if coffee or water accidentally spills on it?<br>Yes! The heating plate is sealed beneath waterproof, explosion-proof tempered glass. Simply wipe clean with a tissue or dry cloth.",
    "faq-3-ar": "هل السطح آمن ومقاوم لانسكاب السوائل أو القهوة بالخطأ؟<br>نعم تماماً! السطح مصنوع من زجاج حراري صلب مقاوم للماء والحرارة العالية، ويمكن مسح أي قطرات منسكبة بمنديل بكل سهولة وأمان.",
    "faq-4-en": "What if I forget to turn it off before leaving the office?<br>Built-in microcomputer protection automatically shuts down the heating plate after 8 hours of continuous operation, giving you complete peace of mind.",
    "faq-4-ar": "ماذا لو نسيت إطفاء القاعدة عند مغادرة المكتب؟<br>القاعدة مزودة بنظام أمان إلكتروني ذكي يغلق الجهاز تلقائياً بعد 8 ساعات من التشغيل المتواصل، مما يمنحك راحة بال تامة وسلامة مطلقة.",

    "twocol-head-en": "DESK ESSENTIAL • EVERY SIP HOT & DELICIOUS<br>Keep Your Favorite Drink at the Ideal Drinking Temperature<br>Focus on your work, calls, or gaming without rushing your coffee before it gets cold. Fast 7–8 days delivery across Saudi Arabia.",
    "twocol-head-ar": "قطعة أساسية لمكتبك • كل رشفة ساخنة وطازجة<br>حافظ على حرارة مشروبك المفضل بنفس اللذة لساعات طويلة<br>ركز في مهام عملك واجتماعاتك دون أن تقلق من برودة كوب القهوة على مكتبك، مع توصيل سريع وموثوق خلال 7–8 أيام لكافة مدن المملكة.",
    "twocol-cards-en": "Card 1: 🚚 Fast 7–8 Days Delivery\nCard 2: 🛡️ 14-Day Golden Guarantee\nCard 3: 💳 Secure Mada & Apple Pay",
    "twocol-cards-ar": "البطاقة 1: 🚚 توصيل سريع خلال 7–8 أيام\nالبطاقة 2: 🛡️ الضمان الذهبي 14 يوماً\nالبطاقة 3: 💳 دفع آمن بمدى وأبل باي",

    "center-head-en": "INTELLIGENT CONSTANT TEMPERATURE WARMING<br>Precise Microcomputer Heat Control with 3 Levels<br>Sleek, minimalist aesthetic looks gorgeous beside laptops, monitors, and modern executive desks.",
    "center-head-ar": "تسخين حراري ذكي بثبات فائق<br>تحكم إلكتروني دقيق بدرجات الحرارة عبر 3 مستويات<br>تصميم عصري أنيق ومدمج يضفي لمسة فخامة على طاولة مكتبك بجوار اللابتوب والشاشات.",
    "center-b1-en": "3 Temperature Presets<br>Toggle between 55°C (Warm), 65°C (Hot), and 75°C (Piping Hot) with one touch.",
    "center-b1-ar": "3 درجات حرارة ذكية<br>تنقل بلمسة واحدة بين 55° (دافئ)، 65° (ساخن)، و 75° (شديد السخونة).",
    "center-b2-en": "Tempered Glass Panel<br>Scratch-resistant, waterproof heating surface transfers warmth evenly and rapidly.",
    "center-b2-ar": "سطح زجاجي حراري صلب<br>مقاوم للخدش والماء ويوصل الحرارة لقاعدة الكوب بسرعة وتوزيع متجانس.",
    "center-b3-en": "8-Hour Safety Auto-Off<br>Built-in smart timer prevents overheating and saves electricity automatically.",
    "center-b3-ar": "إغلاق أمان تلقائي بعد 8 ساعات<br>مؤقت ذكي مدمج يوقف التسخين تلقائياً لتوفير الطاقة وحماية المكتب.",
    "center-b4-en": "Low Energy Consumption<br>Consumes only 20W of power, warming your mug for hours for pennies of electricity.",
    "center-b4-ar": "استهلاك كهرباء منخفض واقتصادي<br>يعمل بقدرة 20 واط فقط ليمنحك ساعات من الدفء بأقل استهلاك للطاقة.",

    "grid-head-en": "EVERYDAY BENEFITS YOU WILL NOTICE FROM DAY ONE<br>A Better Coffee Ritual for Your Daily Routine<br>No more microwave reheats that ruin coffee aroma and tea flavor balance.",
    "grid-head-ar": "مزايا يومية تشعر بقيمتها من أول يوم<br>روتين قهوة أرقى وأكثر متعة في يومك المكتبي<br>ودّع تسخين الميكروويف الذي يفسد طعم ونكهة القهوة الفاخرة وشاي الصباح.",
    "grid-b1-en": "Preserves Fresh Taste & Aroma<br>Gentle constant heat keeps coffee tasting freshly poured without bitter burning.",
    "grid-b1-ar": "يحافظ على نكهة ورائحة القهوة<br>الحرارة الهادئة تمنع مرارة الحرق وتبقي المشروب بطعمه الطازج اللذيذ.",
    "grid-b2-en": "Zero Microwave Trips<br>Saves you getting up repeatedly during busy meetings or deep focus work blocks.",
    "grid-b2-ar": "بدون الذهاب للمطبخ كل نصف ساعة<br>يوفر وقتك أثناء الاجتماعات والعمل المركز بدلاً من تكرار إعادة تسخين الكوب.",
    "grid-b3-en": "Warms Mugs, Wax & Candle Melts<br>Versatile surface also gently melts aroma waxes and essential oil cups.",
    "grid-b3-ar": "متعدد الاستخدامات للشموع والمشروبات<br>يمكن استخدامه أيضاً لإذابة وتدفئة الشموع العطرية الفواحة لنشر الروائح بالمكتب.",
    "grid-b4-en": "Compact & Quiet Desk Footprint<br>Silent solid-state heating produces zero fan hum or ticking noise.",
    "grid-b4-ar": "حجم مدمج وتشغيل صامت 100%<br>تسخين إلكتروني صامت تماماً بدون أي صوت مراوح أو طنين يشوش على تركيزك.",

    "table-head-en": "WHY CHOOSE ZELMIQO THERMODESK<br>Smart Digital Temperature Control Built to Last<br>Compare our 3 temp modes, tempered glass, and 8h timer with dangerous basic metal warmers.",
    "table-head-ar": "لماذا يفضل عملاؤنا قاعدة تسخين زيلميكو؟<br>تحكم رقمي ذكي وأمان فائق صُمم ليدوم<br>قارن بين خيارات الحرارة الثلاثة والسطح الزجاجي الآمن لدينا مقابل القواعد المعدنية الخطيرة.",
    "table-rows-en": "Row 1: ☕️ 3 Custom Temps (55/65/75°C) | Zelmiqo (✓ Exact digital warmth for every drink) | Cheap Warmers (✕ Barely warm 40°C plate)\nRow 2: ⏱️ 8-Hour Auto-Shutoff | Zelmiqo (✓ Built-in safety microchip) | Cheap Warmers (✕ No timer, major fire hazard)\nRow 3: 🛡️ Tempered Glass Surface | Zelmiqo (✓ Waterproof & shatter-resistant) | Cheap Warmers (✕ Unsealed metal that shorts on spill)\nRow 4: 🔌 Energy-Efficient 20W | Zelmiqo (✓ Eco-friendly low power draw) | Cheap Warmers (✕ Inefficient high-wattage power suck)\nRow 5: 🚚 Fast KSA Delivery | Zelmiqo (✓ Fast 7–8 days across Saudi Arabia) | Generic Brands (✕ Unverified slow transit without warranty)",
    "table-rows-ar": "الصف 1: ☕️ 3 درجات حرارة (55/65/75°) | قاعدة زيلميكو (✓ حرارة كافية ومضبوطة لكل نوع مشروب) | القواعد الرخيصة (✕ حرارة ضعيفة لا تتجاوز 40°)\nالصف 2: ⏱️ إغلاق أمان تلقائي 8 ساعات | قاعدة زيلميكو (✓ شريحة أمان إلكترونية تمنع الحرائق) | القواعد الرخيصة (✕ تظل مشتعلة دائماً وتشكل خطراً)\nالصف 3: 🛡️ سطح زجاجي حراري معزول | قاعدة زيلميكو (✓ مقاوم للماء والتسرب والخدوش) | القواعد الرخيصة (✕ صفائح معدنية تتعطل فور سكب السوائل)\nالصف 4: 🔌 موفرة للطاقة 20 واط | قاعدة زيلميكو (✓ استهلاك كهربائي ذكي وآمن) | القواعد الرخيصة (✕ استهلاك عشوائي يرفع حرارة السلك)\nالصف 5: 🚚 شحن سريع لكافة المدن | قاعدة زيلميكو (✓ توصيل خلال 7–8 أيام لكافة مدن المملكة) | الأجهزة العادية (✕ شحن بطيء لأسابيع دون ضمان ذهبي)",

    "marquee-text-en": "🚚 Fast 7–8 Days Delivery Across Saudi Arabia • 🛡️ 14-Day Golden Guarantee • 💳 Split in 4 with Tabby & Tamara • 🔒 100% Secure Mada & Apple Pay Checkout",
    "marquee-text-ar": "🚚 توصيل سريع خلال 7–8 أيام لكافة مدن المملكة • 🛡️ الضمان الذهبي 14 يوماً • 💳 قسّم فاتورتك مع تابي وتمارا • 🔒 دفع آمن 100% عبر مدى وأبل باي",
    "cust-head-en": "OUR HAPPY CUSTOMERS<br>Real Desk & Coffee Upgrade Stories Across Saudi Arabia<br>Read verified reviews from executives, developers, and tea lovers who love warm sips.",
    "cust-head-ar": "تجارب عملائنا المعتمدة<br>قصص نجاح وترقية لمكاتب العمل في مختلف مدن المملكة<br>تقييمات موثقة لموظفين وعشاق القهوة استمتعوا بمشروبات دافئة ولذيذة طوال اليوم.",
    "rev-stats-en": "⭐️⭐️⭐️⭐️⭐️ 4.8 out of 5 Stars (Based on 145 Verified Purchases across Saudi Arabia)<br>96% would recommend to a friend • Fast 7–8 days delivery to Riyadh, Jeddah, Dammam & all Saudi cities.",
    "rev-stats-ar": "⭐️⭐️⭐️⭐️⭐️ 4.8 من 5 نجوم (استناداً إلى 145 تقييم موثق لعملاء داخل المملكة العربية السعودية)<br>96% يوصون بالقاعدة لأصدقائهم • توصيل سريع وموثوق خلال 7–8 أيام للرياض، جدة، الدمام وكافة المدن.",
    "rel-head-en": "COMPLETE YOUR DESK & WORKSPACE SETUP<br>You May Also Like<br>Smart desktop tech accessories designed to elevate your daily productivity—delivered in 7–8 days across Saudi Arabia.",
    "rel-head-ar": "أكمل تجهيزات مكتبك العصري الفاخر<br>منتجات مختارة قد تنال إعجابك<br>ملحقات مكتبية ذكية صُممت لتعزيز راحتك وإنتاجيتك اليومية — مع توصيل خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-title-en": "ThermoDesk Smart Heated Beverage Coaster & Mug Warmer | Zelmiqo® KSA",
    "seo-title-ar": "قاعدة تسخين الأكواب والمشروبات الذكية للمكتب مع 3 درجات حرارة | زيلميكو السعودية",
    "seo-desc-en": "Smart desktop heated mug warmer with 3 temperature settings (55/65/75°C), tempered glass, and 8-hour auto-shutoff. Fast 7–8 days delivery across Saudi Arabia.",
    "seo-desc-ar": "قاعدة تسخين الأكواب والمشروبات الذكية للمكتب مع 3 درجات حرارة ومؤقت أمان 8 ساعات. تحافظ على حرارة القهوة والشاي مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-keywords-en": "coffee mug warmer saudi arabia, smart cup heating coaster ksa, desktop beverage warmer, tea warmer plate 7-8 days delivery, tabby tamara office accessories",
    "seo-keywords-ar": "قاعدة تسخين الاكواب السعودية, سخان اكواب مكتبي, سخان فنجان القهوة, قاعدة تسخين الشاي, تقسيط تابي وتمارا, متجر زيلميكو توصيل 7-8 ايام"
}

# -------------------------------------------------------------
# 4. Wireless Weather Station Alarm Clock (PRD-19)
# -------------------------------------------------------------
p_weather = {
    "hero-title-en": "MeteoTouch Wireless Color Touchscreen Weather Station & Dual Alarm Clock",
    "hero-title-ar": "محطة الأرصاد الجوية المنزلية الذكية اللاسلكية بشاشة لمس ملونة ومنبه",
    "hero-subtitle-en": "Real-Time Indoor & Outdoor Temperature, Humidity & Barometric Forecast<br>Precision wireless remote sensor tracks climate metrics, comfort levels, and moon phases. Fast 7–8 days delivery across Saudi Arabia.",
    "hero-subtitle-ar": "متابعة دقيقة لدرجات الحرارة والرطوبة الداخلية والخارجية وتوقعات الطقس<br>حساس لاسلكي خارجي يرصد تقلبات الجو ومستويات الراحة وأطوار القمر بدقة، مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "hero-callout-en": "Wireless Color Weather Station with Remote Sensor",
    "hero-callout-ar": "محطة أرصاد جوية ملونة بحساس لاسلكي خارجي",
    "hero-bullets-en": "• 🌡️ Dual Indoor/Outdoor Temp & Humidity Sensors\n• 🌈 Vivid Full-Color Backlit Touchscreen Display\n• ☁️ Smart 12-Hour Atmospheric Barometer Forecast\n• ⏰ Dual Alarms with Gentle Snooze Function",
    "hero-bullets-ar": "• 🌡️ قراءة فورية للحرارة والرطوبة داخل الغرفة وخارجها\n• 🌈 شاشة ملونة واضحة تعمل باللمس بإضاءة خلفية مريحة\n• ☁️ رصد ذكي للضغط الجوي وتوقعات الطقس القادمة\n• ⏰ منبه مزدوج ذكي مع خاصية الغفوة وتاريخ وتقويم",
    
    "faq-head-en": "PRECISE METEOROLOGICAL MONITORING FOR YOUR HOME<br>Plan Your Day with Exact Local Climate Data<br>Know whether to pack a jacket, adjust AC, or check outdoor heat before heading out in Riyadh or Jeddah. Fast 7–8 days delivery across Saudi Arabia.",
    "faq-head-ar": "رصد دقيق لأحوال الطقس والجو داخل منزلك وخارجه<br>خطط ليومك بثقة استناداً لبيانات مناخية حية وموثوقة<br>اعرف درجات الحرارة بدقة واضبط تكييف منزلك قبل الخروج في الرياض أو جدة أو الشرقية. توصيل سريع وموثوق خلال 7–8 أيام لكافة مناطق المملكة.",
    "faq-1-en": "How far can the outdoor sensor transmit climate data back to the base station?<br>The high-frequency 433MHz wireless transmitter sends accurate data up to 60 meters (200 feet) in open areas, easily penetrating exterior walls and courtyard doors.",
    "faq-1-ar": "ما هو مدى الاتصال اللاسلكي بين الحساس الخارجي والشاشة؟<br>يعمل بتردد لاسلكي متطور 433 ميجاهرتز بمدى يصل إلى 60 متراً، ويخترق الجدران الخارجية ونوافذ الفناء ليرسل البيانات للشاشة بدون أي تأخير.",
    "faq-2-en": "How does the station forecast local weather changes?<br>Equipped with an internal electronic barometer, it tracks atmospheric pressure changes over 12 hours to predict sunny, cloudy, rainy, or stormy conditions with 85%+ accuracy.",
    "faq-2-ar": "كيف تتوقع المحطة حالة الطقس القادمة محلياً؟<br>تحتوي على بارومتر رقمي مدمج يقيس التغيرات في الضغط الجوي على مدار 12 ساعة ليتوقع الأجواء المشمسة، الغائمة، الرعدية أو الماطرة بدقة فائقة.",
    "faq-3-en": "Can it be powered by both USB cable and batteries?<br>Yes! Plug it into any USB port for continuous screen illumination, or insert 3x AAA batteries for completely cordless bedside or wall-mounted operation.",
    "faq-3-ar": "هل تعمل المحطة بكابل USB وبطاريات جافة معاً؟<br>نعم بالتأكيد! يمكنك توصيلها بكابل USB لإضاءة الشاشة باستمرار، أو استخدام بطاريات AAA لتشغيل لاسلكي مدمج على طاولة السرير أو تعليقها على الحائط.",
    "faq-4-en": "Does it display indoor humidity to monitor dry AC air?<br>Yes! It displays real-time indoor relative humidity percentage and a comfort index icon (Dry/Comfort/Wet), helping you maintain healthy bedroom and nursery humidity.",
    "faq-4-ar": "هل تقيس نسبة الرطوبة الداخلية لمعرفة جفاف هواء المكيف؟<br>نعم! تعرض نسبة الرطوبة الداخلية مع مؤشر الراحة الذكي (جاف / مريح / رطب)، لتساعدك في ضبط أجهزة الترطيب والحفاظ على هواء صحي لغرف الأطفال والنوم.",

    "twocol-head-en": "SMART HOME CLIMATE MONITOR • ELEGANT TOUCH DISPLAY<br>Your Personal Meteorologist on Your Nightstand or Wall<br>Track temperature extremes, room humidity, and time at a single glance. Fast 7–8 days delivery across Saudi Arabia.",
    "twocol-head-ar": "مراقبة ذكية لمناخ منزلك • شاشة لمس ملونة وفاخرة<br>راصدك الجوي الشخصي على طاولة سريرك أو معلقاً بجدار الصالة<br>تابع تقلبات الحرارة والرطوبة والوقت بلمحة واحدة في الصباح، مع توصيل سريع وموثوق خلال 7–8 أيام لكافة مدن المملكة.",
    "twocol-cards-en": "Card 1: 🚚 Fast 7–8 Days Delivery\nCard 2: 🛡️ 14-Day Golden Guarantee\nCard 3: 💳 Secure Mada & Apple Pay",
    "twocol-cards-ar": "البطاقة 1: 🚚 توصيل سريع خلال 7–8 أيام\nالبطاقة 2: 🛡️ الضمان الذهبي 14 يوماً\nالبطاقة 3: 💳 دفع آمن بمدى وأبل باي",

    "center-head-en": "PRECISION ATMOSPHERIC TELEMETRY<br>Vivid Color Screen with Wireless Remote Transmitter<br>Foldable kickstand and rear hanging notch allow versatile table placement or wall mounting.",
    "center-head-ar": "أجهزة قياس جوية متطورة وفائقة الدقة<br>شاشة ملونة زاهية مع حساس خارجي لاسلكي مقاوم للعوامل الجوية<br>حامل خلفي قابل للطي وفتحة تعليق تتيح لك وضعها على الطاولة أو تثبيتها على الجدار بأناقة.",
    "center-b1-en": "Dual Temp & Humidity Channels<br>Simultaneously monitors inside room climate and shaded outdoor patio conditions.",
    "center-b1-ar": "قناتان للحرارة والرطوبة<br>ترصد في نفس اللحظة حرارة ورطوبة غرفتك مع حرارة الحوش أو الشرفة الخارجية بدقة.",
    "center-b2-en": "12-Hour Weather Forecast<br>Clear visual icons (Sun, Clouds, Rain, Storm) keep you ahead of regional sandstorms and rain.",
    "center-b2-ar": "توقعات طقس لـ 12 ساعة مقبلة<br>أيقونات رسومية واضحة (شمس، غيوم، مطر، عواصف) لتستعد مسبقاً لأي تقلبات جوية.",
    "center-b3-en": "Touch Backlight Control<br>Gentle top touch-sensor activates illuminated screen for easy midnight reading.",
    "center-b3-ar": "زر لمس علوي للإضاءة<br>حساس لمس علوي يضيء الشاشة فورياً بلمسة خفيفة لقراءة مريحة للعين في الظلام.",
    "center-b4-en": "Dual Alarms & Calendar<br>Configure two independent wake-up alarms with 5-minute snooze and perpetual calendar.",
    "center-b4-ar": "منبه مزدوج مع تقويم وتاريخ<br>اضبط موعدين للاستيقاظ لأيام الدوام والعطلات مع غفوة 5 دقائق وتقويم دائم.",

    "grid-head-en": "EVERYDAY BENEFITS YOU WILL NOTICE IMMEDIATELY<br>Total Control Over Your Indoor Comfort & Routine<br>Create optimal living conditions for babies, sensitive sleepers, and family health.",
    "grid-head-ar": "مزايا يومية تشعر بقيمتها فورياً<br>تحكم كامل في راحة منزلك وصحة عائلتك اليومية<br>اضبط البيئة المثالية لغرف نوم الأطفال وكبار السن وتنفس هواءً صحياً ومريحاً.",
    "grid-b1-en": "Healthier Indoor Air Quality<br>Know when room air gets too dry from continuous AC cooling so you can run humidifiers.",
    "grid-b1-ar": "جودة هواء صحية داخل الغرف<br>اعرف فوراً متى يصبح هواء الغرفة جافاً بفعل التكييف المستمر لتشغيل أجهزة الترطيب.",
    "grid-b2-en": "Smart Outdoor Trip Prep<br>Check real patio temperatures before school drop-offs or outdoor family outings.",
    "grid-b2-ar": "استعداد مثالي قبل الخروج<br>تحقق من الحرارة الخارجية الحقيقية قبل ذهاب الأطفال للمدرسة أو تجهيز رحلات البر.",
    "grid-b3-en": "Sleek Modern Home Decor<br>Vibrant HD color display adds high-tech aesthetic charm to your nightstand or desk.",
    "grid-b3-ar": "قطعة ديكور ذكية وعصرية<br>شاشة ملونة نابضة بالحياة تضفي لمسة تكنولوجية فاخرة على طاولة السرير أو المكتب.",
    "grid-b4-en": "Moon Phase & Comfort Icons<br>Follow lunar calendar cycles and seasonal shifts with automated astronomical algorithms.",
    "grid-b4-ar": "مؤشر أطوار القمر ومستوى الراحة<br>تابع دورات القمر والراحة الجوية اليومية بحسابات فلكية وبرمجية مؤتمتة ودقيقة.",

    "table-head-en": "WHY CHOOSE ZELMIQO METEOTOUCH<br>Laboratory-Grade Precision Sensor Accuracy<br>Compare our color touchscreen, barometric forecasting, and remote sensor with basic monotone clocks.",
    "table-head-ar": "لماذا يفضل عملاؤنا محطة أرصاد زيلميكو؟<br>دقة حساسات معتمدة وبيانات مناخية حية وموثوقة<br>قارن بين الشاشة الملونة التفاعلية وتوقعات البارومتر لدينا مقابل الساعات الرقمية البدائية.",
    "table-rows-en": "Row 1: 🌡️ Dual In/Out Sensors | Zelmiqo (✓ Wireless 60m remote outdoor transmitter) | Monotone Clocks (✕ Indoor only, zero outdoor data)\nRow 2: 🌈 HD Color Touchscreen | Zelmiqo (✓ High-contrast vivid segmented panel) | Monotone Clocks (✕ Dull grey LCD hard to read at night)\nRow 3: ☁️ Barometric Forecast | Zelmiqo (✓ Real 12h atmospheric trend forecast) | Monotone Clocks (✕ Fixed clock with zero weather metrics)\nRow 4: ⏰ Dual Alarms + Snooze | Zelmiqo (✓ Workday & weekend alarms with touch snooze) | Monotone Clocks (✕ Single shrill alarm with no snooze)\nRow 5: 🚚 Fast KSA Delivery | Zelmiqo (✓ Fast 7–8 days across Saudi Arabia) | Generic Brands (✕ Unverified slow shipping with no guarantee)",
    "table-rows-ar": "الصف 1: 🌡️ حساسان للداخل والخارج | محطة زيلميكو (✓ حساس خارجي لاسلكي يغطي 60 متراً) | الساعات العادية (✕ تقيس حرارة الغرفة فقط بدون حساس خارجي)\nالصف 2: 🌈 شاشة لمس ملونة زاهية | محطة زيلميكو (✓ وضوح فائق وزوايا رؤية مريحة ليلاً ونهاراً) | الساعات العادية (✕ شاشة رمادية باهتة لا تُقرأ في الظلام)\nالصف 3: ☁️ توقعات بارومترية ذكية | محطة زيلميكو (✓ رصد حقيقي لتغيرات الضغط والطقس القادم) | الساعات العادية (✕ ساعة عادية بدون أي بيانات للأرصاد)\nالصف 4: ⏰ منبه مزدوج وتقويم | محطة زيلميكو (✓ منبهان منفصلان للدوام والعطلة وغفوة لمس) | الساعات العادية (✕ منبه واحد بصوت حاد وبدون غفوة)\nالصف 5: 🚚 شحن سريع لكافة المدن | محطة زيلميكو (✓ توصيل خلال 7–8 أيام لكافة مدن المملكة) | الأجهزة العادية (✕ شحن بطيء لأسابيع دون ضمان ذهبي)",

    "marquee-text-en": "🚚 Fast 7–8 Days Delivery Across Saudi Arabia • 🛡️ 14-Day Golden Guarantee • 💳 Split in 4 with Tabby & Tamara • 🔒 100% Secure Mada & Apple Pay Checkout",
    "marquee-text-ar": "🚚 توصيل سريع خلال 7–8 أيام لكافة مدن المملكة • 🛡️ الضمان الذهبي 14 يوماً • 💳 قسّم فاتورتك مع تابي وتمارا • 🔒 دفع آمن 100% عبر مدى وأبل باي",
    "cust-head-en": "OUR HAPPY CUSTOMERS<br>Real Weather & Smart Home Experiences Across Saudi Arabia<br>Read verified reviews from homeowners in Riyadh, Jeddah, and the Eastern Province.",
    "cust-head-ar": "تجارب عملائنا المعتمدة<br>قصص موثقة من أصحاب المنازل في مختلف مدن المملكة<br>تقييمات موثوقة لعملاء راقبوا مناخ منازلهم بدقة واستمتعوا بتوقعات طقس حية كل صباح.",
    "rev-stats-en": "⭐️⭐️⭐️⭐️⭐️ 4.8 out of 5 Stars (Based on 118 Verified Purchases across Saudi Arabia)<br>95% would recommend to a friend • Fast 7–8 days delivery to Riyadh, Jeddah, Dammam & all Saudi cities.",
    "rev-stats-ar": "⭐️⭐️⭐️⭐️⭐️ 4.8 من 5 نجوم (استناداً إلى 118 تقييم موثق لعملاء داخل المملكة العربية السعودية)<br>95% يوصون بالمحطة لأصدقائهم • توصيل سريع وموثوق خلال 7–8 أيام للرياض، جدة، الدمام وكافة المدن.",
    "rel-head-en": "SMART LIVING TECH TO COMPLEMENT YOUR HOME<br>You May Also Like<br>Intelligent household accessories designed to simplify your everyday life—delivered in 7–8 days across Saudi Arabia.",
    "rel-head-ar": "أجهزة ذكية متطورة تكمل راحة منزلك<br>منتجات مختارة قد تنال إعجابك<br>ملحقات منزلية ذكية صُممت لتسهيل يومك وراحتك — مع توصيل خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-title-en": "MeteoTouch Wireless Color Touchscreen Weather Station | Zelmiqo® KSA",
    "seo-title-ar": "محطة الأرصاد الجوية المنزلية الذكية اللاسلكية بشاشة لمس ملونة ومنبه | زيلميكو السعودية",
    "seo-desc-en": "Smart wireless color touchscreen weather station with remote sensor, barometer forecast, indoor/outdoor temp & humidity, and dual alarms. Fast 7–8 days delivery across Saudi Arabia.",
    "seo-desc-ar": "محطة أرصاد جوية منزلية لاسلكية ملونة مع حساس خارجي لقياس درجات الحرارة والرطوبة وتوقعات الطقس ومنبه. توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-keywords-en": "wireless weather station saudi arabia, color touchscreen thermometer hygrometer ksa, outdoor remote climate sensor, home barometer clock 7-8 days delivery, tabby tamara smart living",
    "seo-keywords-ar": "محطة ارصاد جوية منزلية السعودية, مقياس حرارة ورطوبة لاسلكي, ساعة منبه ذكية مع طقس, رصد درجات الحرارة, تقسيط تابي وتمارا, متجر زيلميكو توصيل 7-8 ايام"
}

# -------------------------------------------------------------
# 5. Foldable Car Windshield Sun Shade (PRD-08)
# -------------------------------------------------------------
p_sun_shade = {
    "hero-title-en": "TitaniumShield Foldable Car Windshield Sun Shade Umbrella (UPF 50+)",
    "hero-title-ar": "مظلة الزجاج الأمامي العازلة للحرارة وأشعة الشمس للسيارات",
    "hero-subtitle-en": "Blocks 99% UV Rays & Drops Cabin Heat by up to 30°C<br>Military-grade titanium silver reflective coating pops open like an umbrella in 3 seconds. Fast 7–8 days delivery across Saudi Arabia.",
    "hero-subtitle-ar": "حجب 99% من الأشعة فوق البنفسجية وخفض حرارة مقصورة السيارة حتى 30°<br>طبقة تيتانيوم فضية عاكسة للحرارة تُفتح وتُغلق مثل المظلة في 3 ثوانٍ، مع توصيل سريع خلال 7–8 أيام لكافة مدن المملكة.",
    "hero-callout-en": "Titanium UV Windshield Sun Shade Umbrella",
    "hero-callout-ar": "مظلة حماية زجاج السيارة بطبقة التيتانيوم العاكسة",
    "hero-bullets-en": "• 🛡️ UPF 50+ Titanium-Silver Thermal Coating\n• ☂️ Instant 3-Second Umbrella Open/Fold Action\n• 🚗 Prevents Dashboard Cracking & Melting\n• 🪶 10 High-Tensile Steel Ribs & Leather Pouch",
    "hero-bullets-ar": "• 🛡️ طبقة تيتانيوم فضية UPF 50+ تعكس حرارة الصيف الحارقة\n• ☂️ فتح وإغلاق فوري في 3 ثوانٍ مثل مظلة المطر تماماً\n• 🚗 تحمي طبلون ومقاعد السيارة الجلدية من التشقق والتلف\n• 🪶 10 أضلاع فولاذية قوية ومقاومة مع جراب جلدي فاخر",
    
    "faq-head-en": "BEAT THE 50°C SAUDI SUMMER SUN IN SECONDS<br>Step Into a Cool, Protected Car Cabin Every Afternoon<br>Eliminate burning steering wheels, boiling leather seats, and dangerous dashboard fading. Fast 7–8 days delivery across Saudi Arabia.",
    "faq-head-ar": "قهر حرارة صيف المملكة الـ 50° في ثوانٍ معدودة<br>اركب سيارتك بمقصورة باردة ومحمية حتى في ذروة الظهيرة<br>تخلص نهائياً من سخونة الدركسون الحارقة، المقاعد الجلدية الملتهبة، وتشقق الطبلون. توصيل سريع وموثوق خلال 7–8 أيام لكافة مناطق المملكة.",
    "faq-1-en": "How does the umbrella mechanism work compared to bulky foil shades?<br>Instead of folding awkward flimsy cardboard that collapses in the heat, our umbrella design pops open smoothly with one push and folds down neatly into a compact glovebox pouch.",
    "faq-1-ar": "كيف تعمل آلية المظلة مقارنة بستائر الكرتون والقصدير التقليدية؟<br>بدلاً من طي الستائر الكرتونية المزعجة التي تسقط بفعل الحرارة، تتميز هذه المظلة بآلية مظلة المطر؛ تفتحها بضغطة زر وتطويها في جراب صغير يناسب درج السيارة.",
    "faq-2-en": "Will the umbrella shaft scratch my dashboard or infotainment screen?<br>No! It features a 360° bendable silicone-wrapped flexible shaft that bends away from sensitive touchscreens and delicate air vent louvers.",
    "faq-2-ar": "هل يمكن لمقبض المظلة أن يخدش شاشة السيارة أو الطبلون؟<br>لا إطلاقاً! صُمم المقبض بقضيب مرن ومغلف بالكامل بالسيليكون ينثني بزاوية 360° ليتفادى ملامسة الشاشات الحساسة وفتحات التكييف تماماً.",
    "faq-3-en": "Does it fit SUVs, sedans, and trucks in Saudi Arabia?<br>Yes! It is available in calibrated Universal Sedan and Large SUV/Truck dimensions that provide edge-to-edge windshield coverage for Camry, Accord, Tahoe, Patrol, Land Cruiser, and more.",
    "faq-3-ar": "هل تناسب سيارات السيدان والجيوب (SUV) والوانيتات في المملكة؟<br>نعم! صُممت بأبعاد هندسية قياسية تغطي الزجاج الأمامي من الحافة للحافة بكفاءة لسيارات كامري، أكورد، تاهو، باترول، لاندكروزر وكافة الموديلات.",
    "faq-4-en": "How much does it actually lower cabin interior temperature?<br>By reflecting radiant infrared heat before it penetrates windshield glass, it lowers dashboard surface temperature by up to 30°C and cuts AC cool-down time by 60%.",
    "faq-4-ar": "كم تخفض المظلة من حرارة مقصورة السيارة فعلياً؟<br>من خلال عكس أشعة الشمس فوق البنفسجية قبل اختراق الزجاج، تخفض حرارة سطح الطبلون حتى 30 درجة مئوية، وتجعل مكيف السيارة يبرد المقصورة بضعف السرعة.",

    "twocol-head-en": "ULTIMATE CAR CABIN HEAT PROTECTION • OPENS IN 3 SECONDS<br>Never Touch a Scorching Hot Steering Wheel Again<br>Protect your vehicle investment against blistering gulf heat with military-grade reflective shielding. Fast 7–8 days delivery across Saudi Arabia.",
    "twocol-head-ar": "حماية قصوى لمقصورة سيارتك من الشمس • فتح في 3 ثوانٍ<br>انسَ حرارة الدركسون الحارقة ومقاعد الجلد الملتهبة نهائياً<br>احمِ داخلية سيارتك الفاخرة من شمس الخليج الحارقة بطبقة تيتانيوم عاكسة، مع توصيل سريع وموثوق خلال 7–8 أيام لكافة مدن المملكة.",
    "twocol-cards-en": "Card 1: 🚚 Fast 7–8 Days Delivery\nCard 2: 🛡️ 14-Day Golden Guarantee\nCard 3: 💳 Secure Mada & Apple Pay",
    "twocol-cards-ar": "البطاقة 1: 🚚 توصيل سريع خلال 7–8 أيام\nالبطاقة 2: 🛡️ الضمان الذهبي 14 يوماً\nالبطاقة 3: 💳 دفع آمن بمدى وأبل باي",

    "center-head-en": "TITANIUM-SILVER INFRARED HEAT REFLECTOR<br>Military UPF 50+ Thermal Shielding with 10 Steel Ribs<br>Compact foldable footprint stores effortlessly inside door pockets or center console glove compartments.",
    "center-head-ar": "طبقة تيتانيوم فضية عاكسة للأشعة تحت الحمراء<br>عزل حراري UPF 50+ مع 10 أضلاع فولاذية متينة<br>حجم مدمج بعد الطي يستقر بسهولة في جيوب الأبواب أو درج التابلوه بدون أخذ أي مساحة.",
    "center-b1-en": "UPF 50+ Titanium Coating<br>Multi-layer optical silver fabric reflects 99% of damaging UV rays and harsh glare.",
    "center-b1-ar": "طبقة تيتانيوم UPF 50+<br>نسيج فضي بصري متعدد الطبقات يعكس 99% من الأشعة فوق البنفسجية الحارقة.",
    "center-b2-en": "10 Reinforced Steel Ribs<br>Aviation-grade black alloy skeleton withstands intense cabin heat without warping.",
    "center-b2-ar": "10 أضلاع فولاذية معززة<br>هيكل عالي الصلابة يتحمل درجات حرارة السيارات المرتفعة دون أن ينحني أو ينكسر.",
    "center-b3-en": "360° Bendable Handle<br>Soft silicone-coated shaft flexes easily to avoid touching dashboards and consoles.",
    "center-b3-ar": "مقبض مرن يدور 360°<br>قضيب مغلف بالسيليكون ينثني بمرونة تامة ليحمي شاشة اللمس والديكورات من أي خدوش.",
    "center-b4-en": "Instant Push-Button Operation<br>Pops open in 3 seconds and collapses down instantly just like a regular rain umbrella.",
    "center-b4-ar": "فتح وإغلاق بضغطة واحدة<br>تفتح بالكامل في 3 ثوانٍ وتُطوى فورياً بنفس طريقة مظلات المطر السلسة.",

    "grid-head-en": "EVERYDAY BENEFITS YOU WILL NOTICE IMMEDIATELY<br>Step Into Comfort and Keep Your Car Looking Brand New<br>Preserve resale value by shielding leather, electronics, and plastic trims.",
    "grid-head-ar": "مزايا يومية تشعر بقيمتها من أول استخدام<br>اركب سيارتك براحة تامة وحافظ على لمعان داخليتها كالجديدة<br>احمِ قيمة سيارتك عند البيع بحماية المقاعد الجلدية والشاشات من التلف والبهتان.",
    "grid-b1-en": "Cool Cabin from the First Minute<br>Car interior stays significantly cooler, so AC delivers freezing air immediately.",
    "grid-b1-ar": "مقصورة باردة من أول دقيقة<br>تبقى حرارة السيارة الداخلية معتدلة؛ فيعمل المكيف بكفاءة تبريد فورية بدون معاناة.",
    "grid-b2-en": "Protects Leather from Cracking<br>Prevents sun damage, color fading, and premature cracking on luxury leather seats.",
    "grid-b2-ar": "حماية الجلد من التشقق والجفاف<br>تمنع جفاف المقاعد الجلدية وتغير لونها وتلاشي نعومتها بسبب أشعة الشمس المركزة.",
    "grid-b3-en": "No More Scorching Steering Wheel<br>Touch your steering wheel, shift knob, and seatbelts without burning your palms.",
    "grid-b3-ar": "لا مزيد من سخونة الدركسون الحارقة<br>امسك مقود السيارة وحزام الأمان براحة تامة دون الحاجة للانتظار حتى يبرد.",
    "grid-b4-en": "Compact Glovebox Storage<br>Includes a sleek faux-leather pouch that slips neatly into any door side pocket.",
    "grid-b4-ar": "تخزين مدمج في درج التابلوه<br>مرفقة بجراب جلدي أنيق يحفظها بحجم صغير جداً يناسب درج السيارة أو جيب الباب.",

    "table-head-en": "WHY CHOOSE ZELMIQO TITANIUMSHIELD<br>Real Heat Reflection Engineered for Saudi Summers<br>Compare our 10-rib umbrella structure and bendable shaft with floppy generic folding screens.",
    "table-head-ar": "لماذا يفضل السائقون مظلة زيلميكو؟<br>عزل حراري حقيقي صُمم خصيصاً لمقاومة صيف الخليج<br>قارن بين هيكل المظلة ذو الـ 10 أضلاع والمقبض المرن لدينا مقابل الستائر الكرتونية الرخيصة.",
    "table-rows-en": "Row 1: 🛡️ Titanium UPF 50+ Coating | Zelmiqo (✓ Real 99% UV & infrared heat reflection) | Generic Shades (✕ Thin reflective layer tears easily)\nRow 2: ☂️ 3-Second Umbrella Action | Zelmiqo (✓ Quick pop-open & collapse mechanism) | Generic Shades (✕ Annoying folding coils that snap)\nRow 3: 🚗 360° Flexible Shaft | Zelmiqo (✓ Soft bendable rod protects touchscreen) | Generic Shades (✕ Rigid metal pole scratches dashboard)\nRow 4: 🪶 10 High-Tensile Ribs | Zelmiqo (✓ Aviation alloy ribs hold shape firmly) | Generic Shades (✕ Weak 6-8 ribs that collapse under heat)\nRow 5: 🚚 Fast KSA Delivery | Zelmiqo (✓ Fast 7–8 days across Saudi Arabia) | Generic Brands (✕ Unverified slow transit with no return guarantee)",
    "table-rows-ar": "الصف 1: 🛡️ طبقة تيتانيوم UPF 50+ | مظلة زيلميكو (✓ عزل حقيقي يعكس 99% من حرارة الشمس) | الستائر العادية (✕ طبقة رقيقة تتمزق وتتفتت بالحرارة)\nالصف 2: ☂️ فتح وإغلاق في 3 ثوانٍ | مظلة زيلميكو (✓ آلية مظلة سريعة وعملية للغاية) | الستائر العادية (✕ طي معقد ومزعج يسقط من الزجاج)\nالصف 3: 🚗 مقبض مرن ينثني 360° | مظلة زيلميكو (✓ قضيب سيليكوني يحمي الشاشات من الخدش) | الستائر العادية (✕ قضيب معدني صلب قد يجرح الطبلون)\nالصف 4: 🪶 10 أضلاع فولاذية صلبة | مظلة زيلميكو (✓ هيكل ألمنيوم قوي يثبت المظلة بدقة) | الستائر العادية (✕ أضلاع ضعيفة تتشوه بعد أيام قليلة)\nالصف 5: 🚚 شحن سريع لكافة المدن | مظلة زيلميكو (✓ توصيل خلال 7–8 أيام لكافة مدن المملكة) | المنتجات المقلدة (✕ شحن بطيء لأسابيع دون ضمان ذهبي)",

    "marquee-text-en": "🚚 Fast 7–8 Days Delivery Across Saudi Arabia • 🛡️ 14-Day Golden Guarantee • 💳 Split in 4 with Tabby & Tamara • 🔒 100% Secure Mada & Apple Pay Checkout",
    "marquee-text-ar": "🚚 توصيل سريع خلال 7–8 أيام لكافة مدن المملكة • 🛡️ الضمان الذهبي 14 يوماً • 💳 قسّم فاتورتك مع تابي وتمارا • 🔒 دفع آمن 100% عبر مدى وأبل باي",
    "cust-head-en": "OUR HAPPY CUSTOMERS<br>Real Car Heat Protection Experiences Across Saudi Arabia<br>Read verified reviews from car owners in Riyadh, Qassim, Makkah, and Dammam.",
    "cust-head-ar": "تجارب عملائنا المعتمدة<br>قصص حماية حقيقية لسيارات العملاء في مختلف مناطق المملكة<br>تقييمات موثقة لسائقين تخلصوا من حرارة الصيف الحارقة وحافظوا على برودة مقصورة سياراتهم.",
    "rev-stats-en": "⭐️⭐️⭐️⭐️⭐️ 4.9 out of 5 Stars (Based on 194 Verified Purchases across Saudi Arabia)<br>98% would recommend to a friend • Fast 7–8 days delivery to Riyadh, Jeddah, Dammam & all Saudi cities.",
    "rev-stats-ar": "⭐️⭐️⭐️⭐️⭐️ 4.9 من 5 نجوم (استناداً إلى 194 تقييم موثق لعملاء داخل المملكة العربية السعودية)<br>98% يوصون بالمظلة لأصدقائهم • توصيل سريع وموثوق خلال 7–8 أيام للرياض، جدة، الدمام وكافة المدن.",
    "rel-head-en": "MORE AUTOMOTIVE ACCESSORIES TO EXPLORE<br>You May Also Like<br>Smart automotive interior essentials designed to upgrade your daily drive—delivered in 7–8 days across Saudi Arabia.",
    "rel-head-ar": "المزيد من ملحقات السيارات الذكية<br>منتجات مختارة قد تنال إعجابك<br>إكسسوارات وحلول ذكية للسيارات صُممت لحماية سيارتك وراحتك اليومية — مع توصيل خلال 7–8 أيام لكافة مدن المملكة.",
    "seo-title-en": "TitaniumShield Foldable Car Windshield Sun Shade Umbrella | Zelmiqo® KSA",
    "seo-title-ar": "مظلة الزجاج الأمامي العازلة للحرارة وأشعة الشمس للسيارات | زيلميكو السعودية",
    "seo-desc-en": "Foldable titanium silver car windshield sun shade umbrella with UPF 50+ heat block, 10 steel ribs, and 360° bendable handle. Fast 7–8 days delivery across Saudi Arabia.",
    "seo-desc-ar": "مظلة زجاج السيارة الأمامي العازلة للحرارة وأشعة الشمس بطبقة تيتانيوم UPF 50+ وهيكل 10 أضلاع فولاذية. توصيل سريع خلال 7–8 أيام لكافة مدن المملكة مع تقسيط تابي وتمارا.",
    "seo-keywords-en": "car sun shade umbrella saudi arabia, titanium windshield sunshade ksa, car heat blocker umbrella, foldable car umbrella 7-8 days delivery, tabby tamara car accessories",
    "seo-keywords-ar": "مظلة سيارة للزجاج الامامي السعودية, شمسية سيارة تيتانيوم, عازل حراري لسيارات, حماية طبلون السيارة من الشمس, تقسيط تابي وتمارا, متجر زيلميكو توصيل 7-8 ايام"
}

# Generate Batch 3 Pages
generate_product_page("Bionic Finger Neck Massager", p_neck_massager, {}, "product-bionic-finger-neck-massager.html")
generate_product_page("Smart Fascia Massage Gun", p_massage_gun, {}, "product-smart-fascia-massage-gun.html")
generate_product_page("USB Coffee Mug Warmer", p_mug_warmer, {}, "product-usb-coffee-mug-warmer.html")
generate_product_page("Wireless Weather Station Alarm", p_weather, {}, "product-wireless-weather-station-alarm.html")
generate_product_page("Foldable Car Sun Shade", p_sun_shade, {}, "product-foldable-car-sun-shade.html")
print("Batch 3 generation finished successfully!")
