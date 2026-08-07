#!/usr/bin/env python3
"""Generates the 2027 Landlord Property Income Tax Calculator across
PropertyBrain's established language set (en, zh, ar, hi), matching the
existing per-language directory pattern used by section-24-calculator/.
Calculator logic/numbers are identical across languages; only UI strings,
FAQ copy and disclaimers are translated.
"""
import os

DOMAIN = 'https://propertybrain.uk'
ROOT = os.path.dirname(os.path.abspath(__file__))
SLUG = 'property-income-tax-2027-calculator'

LANGS = [
    {'code': 'en', 'hreflang': 'en-gb', 'dir_path': '', 'html_lang': 'en', 'nav_label': 'English'},
    {'code': 'zh', 'hreflang': 'zh', 'dir_path': 'zh/', 'html_lang': 'zh', 'nav_label': '中文'},
    {'code': 'ar', 'hreflang': 'ar', 'dir_path': 'ar/', 'html_lang': 'ar', 'nav_label': 'العربية'},
    {'code': 'hi', 'hreflang': 'hi', 'dir_path': 'hi/', 'html_lang': 'hi', 'nav_label': 'हिन्दी'},
]

T = {
'en': {
    'title': '2027 Landlord Property Income Tax Calculator | PropertyBrain',
    'description': 'See how the new isolated UK property income tax rates (22%/42%/47%, from 6 April 2027) compare to today’s rules under the Finance Bill 2025-26.',
    'og_title': '2027 Landlord Property Income Tax Calculator | PropertyBrain',
    'og_description': 'Compare today’s landlord tax bill against the new separate property income rates arriving in April 2027.',
    'breadcrumb': 'Property Income Tax 2027',
    'h1': '2027 Landlord Property Income Tax Calculator',
    'lead': 'From 6 April 2027, UK property income moves to its own separate tax rates — 22% basic, 42% higher, 47% additional — under the Finance Bill 2025-26, roughly 2 percentage points above today’s standard rates. Compare your bill today against the new rules.',
    'notice': '<strong>Not tax advice.</strong> These rates are not yet in force — they take effect from 6 April 2027, once the Finance Bill 2025-26 receives Royal Assent. Applies to England, Wales and Northern Ireland only; Scotland sets its own income tax and may adopt different property rates. This is a simplified illustrative model — it doesn’t account for the Personal Allowance taper above £100,000 or the Section 24 mortgage-interest finance-cost credit. For your net rental profit after mortgage interest, use our <a href="' + '{s24}' + '">Section 24 Calculator</a> first, then enter that figure below.',
    'card_header': 'Your Income',
    'label_other': 'Annual employment/other taxable income (£)',
    'label_property': 'Net rental profit for the year (£)',
    'results_header': 'Tax Comparison',
    'th_blank': '', 'th_today': 'Today (2026/27 rules)', 'th_2027': 'From 6 April 2027',
    'row_property_tax': 'Tax on property income',
    'row_total_tax': 'Total tax bill',
    'row_net_property': 'Net property profit after tax',
    'extra_label': 'Extra Tax From the 2027 Property Rates',
    'extra_sub': 'additional tax paid per year on your property income',
    'sec1_h': 'What are the new property income tax rates?',
    'sec1_p1': 'The Finance Bill 2025-26 introduces separate income tax rates for UK property income, defining "property income" in its own right and taxing it after employment, trading and other income, but before savings and dividend income. From 6 April 2027, property income will be taxed at 22% basic rate, 42% higher rate and 47% additional rate — about 2 percentage points above the standard 20%/40%/45% rates that apply to other income today.',
    'sec1_p2': 'These new bands apply in England, Wales and Northern Ireland. Scotland has its own devolved income tax system and will decide independently whether to match, diverge from, or align with the new property bands.',
    'sec2_h': 'Is this in force now?',
    'sec2_p1': 'No. As of 2026, property income is still taxed at the same standard rates as your other income (20%/40%/45%), simply added on top of your other earnings. The new isolated rates only take effect from 6 April 2027, once the Finance Bill 2025-26 receives Royal Assent — use the calculator above to see the difference this makes, but don’t plan your current-year filing around figures that aren’t law yet.',
    'sec3_h': 'How does this interact with Section 24?',
    'sec3_p1': 'Section 24 (the mortgage interest relief restriction) is a separate rule about how your taxable rental profit is calculated — it doesn’t let you deduct mortgage interest directly, only a 20% credit. This 2027 change is about what rate that profit is then taxed at, once you already know the figure. If you have mortgage interest to account for, work out your net profit with our <a href="' + '{s24}' + '">Section 24 Calculator</a> first, then bring that number here.',
    'sec4_h': 'Related tools',
    'related_1': 'Section 24 Calculator — work out your net rental profit after the mortgage interest credit',
    'related_2': 'Buy-to-Let Calculator — full BTL analysis including cashflow',
    'related_3': 'Rental Yield Calculator — gross and net yield for any property',
    'editorial': '<strong>PropertyBrain Editorial Team</strong> — cross-checked against the Finance Bill 2025-26 and House of Commons Library briefings on the new property income tax rates. Last verified: August 2026. This is not tax advice — always consult a qualified accountant for your personal position.',
    'faq_q1': 'What are the new property income tax rates from April 2027?',
    'faq_a1': 'From 6 April 2027, the Finance Bill 2025-26 introduces separate income tax rates for UK property income: 22% basic rate, 42% higher rate, and 47% additional rate — around 2 percentage points above today’s standard 20%/40%/45% rates. These apply in England, Wales and Northern Ireland; Scotland sets its own income tax and may set different property rates.',
    'faq_q2': 'Is this in force now?',
    'faq_a2': 'No, not yet in force as of 2026. The rates take effect from 6 April 2027, once the Finance Bill 2025-26 receives Royal Assent and passes into law.',
    'faq_q3': 'Does this replace Section 24 (the mortgage interest relief restriction)?',
    'faq_a3': 'No. Section 24 is a separate rule about how landlords calculate their taxable rental profit. These new property income rates are about what rate that profit is then taxed at, not how the profit itself is calculated.',
    'footer_line': 'PropertyBrain.uk is operated by <a href="https://eightfinity.net/" target="_blank" rel="noopener">EIGHTFINITY LTD</a>, a company registered in England and Wales (company no. 15528515), registered office 20 Wenlock Road, London, England, N1 7GU.',
    'footer_copyright': '© 2026 PropertyBrain.uk — Not financial advice.',
},
'zh': {
    'title': '2027年房东房产收入税计算器 | PropertyBrain',
    'description': '了解自2027年4月6日起新的英国房产收入独立税率（22%/42%/47%）与当前规则相比的差异，根据2025-26财政法案。',
    'og_title': '2027年房东房产收入税计算器 | PropertyBrain',
    'og_description': '比较您当前的房东税单与2027年4月即将推出的新独立房产收入税率。',
    'breadcrumb': '2027房产收入税',
    'h1': '2027年房东房产收入税计算器',
    'lead': '根据2025-26财政法案，自2027年4月6日起，英国房产收入将适用独立的税率——基本税率22%、高税率42%、附加税率47%，比当前标准税率高约两个百分点。请比较您当前的税单与新规则下的税单。',
    'notice': '<strong>不构成税务建议。</strong>这些税率尚未生效——将于2025-26财政法案获得皇家批准后从2027年4月6日起生效。仅适用于英格兰、威尔士和北爱尔兰；苏格兰有自己的所得税制度，可能会采用不同的房产税率。这是一个简化的示例模型——未考虑超过10万英镑收入的个人免税额递减，也未考虑第24条按贷款利息抵税的机制。如果您需要扣除按贷款利息，请先使用我们的<a href="{s224}">第24条计算器</a>计算出净利润，然后将该数字输入下方。',
    'card_header': '您的收入',
    'label_other': '年度工资/其他应税收入（英镑）',
    'label_property': '年度房租净利润（英镑）',
    'results_header': '税费对比',
    'th_blank': '', 'th_today': '当前（2026/27规则）', 'th_2027': '2027年4月6日起',
    'row_property_tax': '房产收入税额',
    'row_total_tax': '总税额',
    'row_net_property': '税后房产净利润',
    'extra_label': '2027新房产税率带来的额外税费',
    'extra_sub': '每年房产收入需额外支付的税款',
    'sec1_h': '新的房产收入税率是什么？',
    'sec1_p1': '2025-26财政法案引入了英国房产收入的独立所得税率，将“房产收入”单独定义，并在工资、贸易和其他收入之后、储蓄和股息收入之前征税。自2027年4月6日起，房产收入将按基本税率22%、高税率42%和附加税率47%征税——比当前适用于其他收入的20%/40%/45%标准税率高约两个百分点。',
    'sec1_p2': '这些新税阶适用于英格兰、威尔士和北爱尔兰。苏格兰有自己的下放所得税制度，将独立决定是否采用、偏离或与新的房产税阶保持一致。',
    'sec2_h': '现在已经生效了吗？',
    'sec2_p1': '还没有。截至2026年，房产收入仍按与其他收入相同的标准税率（20%/40%/45%）征税，仅简单叠加在其他收入之上。新的独立税率将于2025-26财政法案获得皇家批准后，从2027年4月6日起才正式生效——可使用上方计算器查看差异，但请勿基于尚未正式立法的数字安排当前年度的报税。',
    'sec3_h': '与第24条有何关系？',
    'sec3_p1': '第24条（按贷款利息税收抵免限制）是关于如何计算应税房租利润的单独规则——它不允许直接扣除按贷款利息，而只能获得20%的抵税额。这项2027年的变化则是关于该利润在确定后将按何种税率征税。如果您有按贷款利息需要考虑，请先使用我们的<a href="{s224}">第24条计算器</a>计算净利润，然后再将数字带到这里。',
    'sec4_h': '相关工具',
    'related_1': '第24条计算器——计算扣除按贷款利息抵税额后的房租净利润',
    'related_2': '出租投资计算器——完整的BTL分析，包括现金流',
    'related_3': '租金收益率计算器——任何房产的毛收益率和净收益率',
    'editorial': '<strong>PropertyBrain编辑团队</strong>——已对照2025-26财政法案及下院图书馆关于新房产收入税率的简报进行核实。最后验证时间：2026年8月。这不构成税务建议——具体情况请咨询合格会计师。',
    'faq_q1': '2027年4月起的新房产收入税率是什么？',
    'faq_a1': '自2027年4月6日起，2025-26财政法案将引入英国房产收入的独立所得税率：基本税率22%、高税率42%、附加税率47%，比当前标准的20%/40%/45%税率高约两个百分点。适用于英格兰、威尔士和北爱尔兰；苏格兰可能设定不同的房产税率。',
    'faq_q2': '现在已经生效了吗？',
    'faq_a2': '截至2026年尚未生效。该税率将在2025-26财政法案获得皇家批准并正式立法后，从2027年4月6日起生效。',
    'faq_q3': '这会取代第24条（按贷款利息税收抵免限制）吗？',
    'faq_a3': '不会。第24条是关于房东如何计算应税房租利润的单独规则。这些新的房产收入税率关乎该利润确定后将按何种税率征税，而非利润本身的计算方式。',
    'footer_line': 'PropertyBrain.uk 由 <a href="https://eightfinity.net/" target="_blank" rel="noopener">EIGHTFINITY LTD</a> 运营，该公司在英格兰和威尔士注册（公司编号15528515），注册办事处位于20 Wenlock Road, London, England, N1 7GU。',
    'footer_copyright': '© 2026 PropertyBrain.uk — 不构成财务建议。',
},
'ar': {
    'title': 'حاسبة ضريبة دخل الملاك العقارية 2027 | PropertyBrain',
    'description': 'اطّلع على كيفية مقارنة معدلات ضريبة دخل العقارات المنفصلة الجديدة (22%/42%/47%، اعتبارًا من 6 أبريل 2027) بالقواعد الحالية بموجب مشروع قانون المالية 2025-26.',
    'og_title': 'حاسبة ضريبة دخل الملاك العقارية 2027 | PropertyBrain',
    'og_description': 'قارن فاتورتك الضريبية الحالية بالمعدلات الجديدة المنفصلة التي ستطبّق في أبريل 2027.',
    'breadcrumb': 'ضريبة العقارات 2027',
    'h1': 'حاسبة ضريبة دخل الملاك العقارية 2027',
    'lead': 'اعتبارًا من 6 أبريل 2027، سينتقل دخل العقارات في المملكة المتحدة إلى معدلات ضريبية منفصلة خاصة به — 22% أساسي، 42% مرتفع، 47% إضافي — بموجب مشروع قانون المالية 2025-26، أي أعلى بنحو نقطتين مئويتين من المعدلات القياسية الحالية. قارن فاتورتك الحالية بالقواعد الجديدة.',
    'notice': '<strong>ليست نصيحة ضريبية.</strong> هذه المعدلات غير سارية المفعول بعد — ستصبح سارية المفعول اعتبارًا من 6 أبريل 2027 بعد حصول مشروع قانون المالية 2025-26 على الموافقة الملكية. تنطبق فقط على إنجلترا وويلز وآيرلندا الشمالية؛ لاسكتلندا لديها نظام ضريبي دخل منفصل وقد تعتمد معدلات عقارية مختلفة. هذا نموذج توضيحي مبسّط — لا يأخذ بعين الاعتبار تدرج الإعفاء الشخصي فوق 100,000 جنيه إسترليني، ولا ائتمان خصم المادة 24 المتعلق بفوائد الرهن العقاري. لمعرفة صافي الربح الإيجاري بعد فوائد الرهن، استخدم <a href="{s224}">حاسبة المادة 24</a> أولاً ثم أدخل ذلك الرقم أدناه.',
    'card_header': 'دخلك',
    'label_other': 'الدخل السنوي الخاضع للضريبة من الوظيفة/مصادر أخرى (ج.إ)',
    'label_property': 'صافي الربح الإيجاري السنوي (ج.إ)',
    'results_header': 'مقارنة الضريبة',
    'th_blank': '', 'th_today': 'اليوم (قواعد 2026/27)', 'th_2027': 'اعتبارًا من 6 أبريل 2027',
    'row_property_tax': 'ضريبة دخل العقارات',
    'row_total_tax': 'إجمالي الضريبة',
    'row_net_property': 'صافي ربح العقار بعد الضريبة',
    'extra_label': 'الضريبة الإضافية من معدلات العقارات لعام 2027',
    'extra_sub': 'ضريبة إضافية تُدفع سنويًا على دخل عقارك',
    'sec1_h': 'ما هي معدلات ضريبة دخل العقارات الجديدة؟',
    'sec1_p1': 'يقدّم مشروع قانون المالية 2025-26 معدلات ضريبية منفصلة لدخل العقارات في المملكة المتحدة، حيث يُعرّف “دخل العقارات” بشكل مستقل، ويُفرض عليه الضريبة بعد دخل الوظيفة والتجارة والدخل الآخر، ولكن قبل دخل الادخار والتوزيعات. اعتبارًا من 6 أبريل 2027، سيُفرض على دخل العقارات 22% كمعدل أساسي، 42% كمعدل مرتفع، 47% كمعدل إضافي — أي أعلى بنحو نقطتين مئويتين من المعدلات القياسية الحالية 20%/40%/45%.',
    'sec1_p2': 'تنطبق هذه الشرائح الجديدة على إنجلترا وويلز وآيرلندا الشمالية. ولدى اسكتلندا نظام ضريبي دخل منفصل خاص بها، وستقرر بشكل مستقل ما إذا كانت ستوافق مع شرائح العقارات الجديدة أو تختلف عنها.',
    'sec2_h': 'هل هذا ساري المفعول الآن؟',
    'sec2_p1': 'لا. في عام 2026، لا يزال دخل العقارات يُفرض عليه بنفس المعدلات القياسية لدخلك الآخر (20%/40%/45%)، ويُضاف ببساطة إلى دخلك الآخر. لن تسري المعدلات المنفصلة الجديدة إلا اعتبارًا من 6 أبريل 2027، بعد موافقة الملكة على مشروع قانون المالية 2025-26.',
    'sec3_h': 'كيف يرتبط هذا بالمادة 24؟',
    'sec3_p1': 'المادة 24 (قيد خصم فائدة فوائد الرهن العقاري) هي قاعدة منفصلة حول كيفية حساب ربحك الإيجاري الخاضع للضريبة — فهي لا تسمح لك بخصم فوائد الرهن مباشرة، بل فقط بخصم 20%. هذا التغيير لعام 2027 يتعلق بالمعدل الذي يُفرض على ذلك الربح بعد تحديده. إذا كان لديك فائدة قرضية يجب مراعاتها، استخدم <a href="{s224}">حاسبة المادة 24</a> أولاً ثم أدخل الرقم هنا.',
    'sec4_h': 'أدوات ذات صلة',
    'related_1': 'حاسبة المادة 24 — احسب صافي ربحك الإيجاري بعد خصم فائدة الرهن العقاري',
    'related_2': 'حاسبة الشراء للتأجير — تحليل كامل يشمل التدفق النقدي',
    'related_3': 'حاسبة العائد الإيجاري — العائد الإجمالي والصافي لأي عقار',
    'editorial': '<strong>فريق التحرير في PropertyBrain</strong> — تم التحقق مقابل مشروع قانون المالية 2025-26 وملخصات مكتبة مجلس العموم. آخر تحديث: أغسطس 2026. هذا ليس نصيحة ضريبية — استشر دائمًا محاسبًا مؤهلًا.',
    'faq_q1': 'ما هي معدلات ضريبة دخل العقارات الجديدة اعتبارًا من أبريل 2027؟',
    'faq_a1': 'اعتبارًا من 6 أبريل 2027، يُدخل مشروع قانون المالية 2025-26 معدلات ضريبية منفصلة لدخل العقارات في المملكة المتحدة: 22% أساسي، 42% مرتفع، 47% إضافي. تنطبق على إنجلترا وويلز وآيرلندا الشمالية؛ وقد تحدد اسكتلندا معدلات مختلفة.',
    'faq_q2': 'هل هذا ساري المفعول الآن؟',
    'faq_a2': 'لا، غير ساري المفعول بعد في عام 2026. ستطبّق المعدلات اعتبارًا من 6 أبريل 2027 بعد حصول مشروع قانون المالية 2025-26 على الموافقة الملكية ودخوله حيز التنفيذ.',
    'faq_q3': 'هل يحل هذا محل المادة 24؟',
    'faq_a3': 'لا. المادة 24 قاعدة منفصلة حول كيفية حساب الملاك لربحهم الإيجاري الخاضع للضريبة. هذه المعدلات الجديدة تتعلق بالمعدل الذي يُفرض على ذلك الربح بعد تحديده، وليس بطريقة حساب الربح نفسه.',
    'footer_line': 'PropertyBrain.uk تديرها <a href="https://eightfinity.net/" target="_blank" rel="noopener">EIGHTFINITY LTD</a>، شركة مسجلة في إنجلترا وويلز (رقم الشركة 15528515)، المكتب المسجل 20 Wenlock Road, London, England, N1 7GU.',
    'footer_copyright': '© 2026 PropertyBrain.uk — ليست نصيحة مالية.',
},
'hi': {
    'title': '2027 लैंडलॉर्ड प्रॉपर्टी इनकम टैक्स कैलकुलेटर | PropertyBrain',
    'description': 'देखें कि 2025-26 वित्त विधेयक के तहत 6 अप्रैल 2027 से नए अलग यूके प्रॉपर्टी इनकम टैक्स दर (22%/42%/47%) आज के नियमों से कैसे अलग हैं।',
    'og_title': '2027 लैंडलॉर्ड प्रॉपर्टी इनकम टैक्स कैलकुलेटर | PropertyBrain',
    'og_description': 'अप्रैल 2027 में आ रही नई अलग प्रॉपर्टी इनकम दरों की तुलना आज के आपके टैक्स बिल से करें।',
    'breadcrumb': 'प्रॉपर्टी इनकम टैक्स 2027',
    'h1': '2027 लैंडलॉर्ड प्रॉपर्टी इनकम टैक्स कैलकुलेटर',
    'lead': '2025-26 वित्त विधेयक के तहत 6 अप्रैल 2027 से, यूके प्रॉपर्टी इनकम अपनी खुद की अलग टैक्स दरों पर चला जाएगा — 22% बेसिक, 42% हायर, 47% एडीशनल — जो आज की मानक दरों से लगभग 2 प्रतिशत अधिक हैं। आज के अपने बिल की नए नियमों से तुलना करें।',
    'notice': '<strong>यह कर सलाह नहीं है।</strong> ये दरें अभी लागू नहीं हुई हैं — ये 2025-26 वित्त विधेयक को शाही स्वीकृति मिलने के बाद 6 अप्रैल 2027 से लागू होंगी। केवल इंग्लैंड, वेल्स और उत्तरी आयरलैंड पर लागू; स्कॉटलैंड की अपनी अलग आयकर व्यवस्था है और वह अलग प्रॉपर्टी दरें अपना सकती है। यह एक सरल उदाहरण मॉडल है — £100,000 से अधिक पर पर्सनल अलाउंस टेपर या सेक्शन 24 मॉर्गेज ब्याज क्रेडिट को शामिल नहीं करता। मॉर्गेज ब्याज के बाद अपने नेट रेंटल प्रॉफिट के लिए, पहले हमारा <a href="{s224}">सेक्शन 24 कैलकुलेटर</a> इस्तेमाल करें, फिर वह आंकड़ा यहां डालें।',
    'card_header': 'आपकी आय',
    'label_other': 'वार्षिक रोजगार/अन्य करयोग्य आय (£)',
    'label_property': 'वर्ष के लिए शुद्ध किराया लाभ (£)',
    'results_header': 'टैक्स तुलना',
    'th_blank': '', 'th_today': 'आज (2026/27 नियम)', 'th_2027': '6 अप्रैल 2027 से',
    'row_property_tax': 'प्रॉपर्टी आय पर टैक्स',
    'row_total_tax': 'कुल टैक्स बिल',
    'row_net_property': 'टैक्स के बाद शुद्ध प्रॉपर्टी लाभ',
    'extra_label': '2027 प्रॉपर्टी दरों से अतिरिक्त टैक्स',
    'extra_sub': 'आपकी प्रॉपर्टी आय पर प्रति वर्ष अतिरिक्त टैक्स',
    'sec1_h': 'नए प्रॉपर्टी इनकम टैक्स दर क्या हैं?',
    'sec1_p1': '2025-26 वित्त विधेयक यूके प्रॉपर्टी आय के लिए अलग आयकर दरें लाता है, "प्रॉपर्टी आय" को अपने आप में परिभाषित करता है, और इसे रोजगार, व्यापार और अन्य आय के बाद लेकिन बचत और लाभांश आय से पहले टैक्स किया जाता है। 6 अप्रैल 2027 से, प्रॉपर्टी आय पर 22% बेसिक, 42% हायर और 47% एडीशनल दर से टैक्स लगेगा — जो आज की मानक 20%/40%/45% दरों से लगभग 2 प्रतिशत अधिक हैं।',
    'sec1_p2': 'ये नई दरें इंग्लैंड, वेल्स और उत्तरी आयरलैंड पर लागू होती हैं। स्कॉटलैंड की अपनी आयकर प्रणाली है और वह स्वतंत्र रूप से तय करेगा कि नए प्रॉपर्टी दरों को अपनाए या नहीं।',
    'sec2_h': 'क्या यह अभी लागू है?',
    'sec2_p1': 'नहीं। 2026 तक, प्रॉपर्टी आय पर अभी भी आपकी अन्य आय के समान मानक दरों (20%/40%/45%) पर टैक्स लगता है, बस इसे आपकी अन्य आय में जोड़ दिया जाता है। नए अलग दर केवल 6 अप्रैल 2027 से लागू होंगे, जब 2025-26 वित्त विधेयक को शाही स्वीकृति मिल जाएगी।',
    'sec3_h': 'यह सेक्शन 24 से कैसे जुड़ा है?',
    'sec3_p1': 'सेक्शन 24 (मॉर्गेज ब्याज राहत प्रतिबंध) इस बारे में एक अलग नियम है कि आपका करयोग्य किराया लाभ कैसे गिना जाता है — यह आपको सीधे मॉर्गेज ब्याज की कटौती करने नहीं देता, बल्कि केवल 20% क्रेडिट देता है। 2027 का यह बदलाव इस बारे में है कि उस लाभ पर कितनी दर से टैक्स लगेगा। अगर आपको मॉर्गेज ब्याज का हिसाब रखना है, तो पहले हमारा <a href="{s224}">सेक्शन 24 कैलकुलेटर</a> इस्तेमाल करें।',
    'sec4_h': 'संबंधित उपकरण',
    'related_1': 'सेक्शन 24 कैलकुलेटर — मॉर्गेज ब्याज क्रेडिट के बाद अपना शुद्ध किराया लाभ जानें',
    'related_2': 'बाय-टू-लेट कैलकुलेटर — नकदी प्रवाह सहित पूर्ण BTL विश्लेषण',
    'related_3': 'रेंटल यील्ड कैलकुलेटर — किसी भी प्रॉपर्टी के लिए सकल और शुद्ध यील्ड',
    'editorial': '<strong>PropertyBrain संपादकीय टीम</strong> — 2025-26 वित्त विधेयक और हाउस ऑफ कॉमन्स लाइब्रेरी की जानकारी से मिलान किया गया। अंतिम सत्यापन: अगस्त 2026। यह कर सलाह नहीं है — हमेशा योग्य लेखाकार से परामर्श लें।',
    'faq_q1': 'अप्रैल 2027 से नए प्रॉपर्टी इनकम टैक्स दर क्या हैं?',
    'faq_a1': '6 अप्रैल 2027 से, 2025-26 वित्त विधेयक यूके प्रॉपर्टी आय के लिए अलग आयकर दरें लाता है: 22% बेसिक, 42% हायर, और 47% एडीशनल — जो आज की मानक 20%/40%/45% दरों से लगभग 2 प्रतिशत अधिक हैं। यह इंग्लैंड, वेल्स और उत्तरी आयरलैंड पर लागू होता है; स्कॉटलैंड अलग दरें तय कर सकता है।',
    'faq_q2': 'क्या यह अभी लागू है?',
    'faq_a2': 'नहीं, 2026 तक अभी लागू नहीं हुआ। 2025-26 वित्त विधेयक को शाही स्वीकृति मिलने के बाद 6 अप्रैल 2027 से यह दरें लागू होंगी।',
    'faq_q3': 'क्या यह सेक्शन 24 की जगह लेगा?',
    'faq_a3': 'नहीं। सेक्शन 24 इस बारे में अलग नियम है कि लैंडलॉर्ड अपना करयोग्य किराया लाभ कैसे निकालते हैं। ये नए प्रॉपर्टी दर इस बारे में हैं कि उस लाभ पर कितनी दर से टैक्स लगेगा, न कि लाभ खुद कैसे निकाला जाता है।',
    'footer_line': 'PropertyBrain.uk के संचालक <a href="https://eightfinity.net/" target="_blank" rel="noopener">EIGHTFINITY LTD</a> हैं, जो इंग्लैंड और वेल्स में पंजीकृत कंपनी है (कंपनी संख्या 15528515), पंजीकृत कार्यालय 20 Wenlock Road, London, England, N1 7GU।',
    'footer_copyright': '© 2026 PropertyBrain.uk — वित्तीय सलाह नहीं।',
},
}


def render(lang):
    code = lang['code']
    t = T[code]
    dir_prefix = '../' if lang['dir_path'] else ''
    s24 = dir_prefix + 'section-24-calculator/'
    notice = t['notice'].replace('{s224}', s24).replace('{s24}', s24)
    sec1_p2 = t.get('sec1_p2', '')
    sec3_p1 = t['sec3_p1'].replace('{s224}', s24).replace('{s24}', s24)

    lang_menu = ''.join(
        '<a href="{url}" hreflang="{hl}"{active}>{label}</a>'.format(
            url=DOMAIN + '/' + l['dir_path'] + SLUG + '/',
            hl=l['hreflang'],
            active=' class="active"' if l['code'] == code else '',
            label=l['nav_label'],
        ) for l in LANGS
    )

    hreflang_links = '\n'.join(
        '<link rel="alternate" hreflang="{hl}" href="{url}">'.format(
            hl=l['hreflang'], url=DOMAIN + '/' + l['dir_path'] + SLUG + '/'
        ) for l in LANGS
    ) + '\n<link rel="alternate" hreflang="x-default" href="{url}">'.format(url=DOMAIN + '/' + SLUG + '/')

    canonical = DOMAIN + '/' + lang['dir_path'] + SLUG + '/'
    home = dir_prefix if dir_prefix else '/'

    faq_schema = (
        '{"@context":"https://schema.org","inLanguage":"' + code + '","@type":"FAQPage","mainEntity":['
        '{"@type":"Question","name":' + repr(t['faq_q1']).replace("'", '"') + ',"acceptedAnswer":{"@type":"Answer","text":' + repr(t['faq_a1']).replace("'", '"') + '}},'
        '{"@type":"Question","name":' + repr(t['faq_q2']).replace("'", '"') + ',"acceptedAnswer":{"@type":"Answer","text":' + repr(t['faq_a2']).replace("'", '"') + '}},'
        '{"@type":"Question","name":' + repr(t['faq_q3']).replace("'", '"') + ',"acceptedAnswer":{"@type":"Answer","text":' + repr(t['faq_a3']).replace("'", '"') + '}}'
        ']}'
    )

    return '''<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('consent','default',{{'ad_storage':'denied','ad_user_data':'denied','ad_personalization':'denied','analytics_storage':'denied'}});</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
{hreflang_links}
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_description}">
<meta property="og:url" content="{canonical}">
<link rel="icon" type="image/svg+xml" href="{home}assets/favicon.svg">
<link rel="stylesheet" href="{home}assets/css/style.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","inLanguage":"{code}","@type":"WebApplication","name":"{h1}","url":"{canonical}","description":"{description}","applicationCategory":"FinanceApplication","offers":{{"@type":"Offer","price":"0","priceCurrency":"GBP"}},"areaServed":[{{"@type":"Country","name":"England"}},{{"@type":"Country","name":"Wales"}},{{"@type":"Country","name":"Northern Ireland"}}]}}
</script>
<script type="application/ld+json">
{faq_schema}
</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9748936508682808" crossorigin="anonymous"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-VGJC6YVK43"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-VGJC6YVK43');</script>
</head>
<body>
<div id="cookie-banner">
  <p>We use cookies to improve your experience. <a href="{home}cookies/">Learn more</a>.</p>
  <div class="cookie-btns"><button class="btn-cookie-accept" id="cookie-accept">Accept</button><button class="btn-cookie-decline" id="cookie-decline">Decline</button></div>
</div>

<header class="site-header">
  <div class="container">
    <div class="site-header__inner">
      <a href="{home}" class="site-header__logo">Property<span>Brain</span></a>
      <nav class="site-nav">
        <a href="{home}buy-to-let-calculator/">BTL Calculator</a>
        <a href="{home}stamp-duty-calculator/">Stamp Duty</a>
        <a href="{home}mortgage-calculator/">Mortgage</a>
        <a href="{home}rental-yield-calculator/">Yield</a>
        <a href="{home}sa-airbnb-calculator/">SA/Airbnb</a>
        <a href="{home}bridging-finance-calculator/">Bridging</a>
        <a href="{home}section-24-calculator/">Section 24</a>
        <a href="{sslug}" aria-current="page">2027 Property Tax</a>
        <a href="{home}free-tools/">Free Tools</a>
        <a href="{home}guide/">Guide</a>
      </nav><div class="lang-switcher"><button type="button" class="lang-switcher__btn" aria-haspopup="true" aria-expanded="false" onclick="this.parentElement.classList.toggle('open')">{nav_label} ▾</button><div class="lang-switcher__menu">{lang_menu}</div></div>
    </div>
  </div>
</header>

<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="{home}">Home</a> › {breadcrumb}</div>
    <h1>{h1}</h1>
    <p>{lead}</p>
  </div>
</section>

<main class="main-content">
  <div class="container">
    <div class="notice">{notice}</div>

    <div class="calc-layout">
      <div>
        <div class="card">
          <div class="card__header">{card_header}</div>
          <div class="card__body">
            <div class="form-group">
              <label>{label_other}</label>
              <div class="input-wrap has-prefix"><span class="input-prefix">£</span><input type="number" id="other_income" value="35000" min="0"></div>
            </div>
            <div class="form-group">
              <label>{label_property}</label>
              <div class="input-wrap has-prefix"><span class="input-prefix">£</span><input type="number" id="property_profit" value="15000" min="0"></div>
            </div>
          </div>
        </div>
      </div>

      <div>
        <div class="results-panel">
          <div class="results-panel__header">{results_header}</div>
          <div class="results-panel__body">
            <div class="table-wrap">
              <table class="data-table" aria-label="{th_today}, {th_2027} reference table">
                <thead>
                  <tr><th scope="col">{th_blank}</th><th scope="col">{th_today}</th><th scope="col">{th_2027}</th></tr>
                </thead>
                <tbody>
                  <tr><td>{row_property_tax}</td><td id="r_prop_tax_today">—</td><td id="r_prop_tax_2027">—</td></tr>
                  <tr><td>{row_total_tax}</td><td id="r_total_today">—</td><td id="r_total_2027">—</td></tr>
                  <tr><td>{row_net_property}</td><td id="r_net_today">—</td><td id="r_net_2027">—</td></tr>
                </tbody>
              </table>
            </div>
            <div class="result-hero" style="margin-top:1.25rem;background:#fef2f2;border-radius:0.5rem;padding:1rem">
              <div class="result-hero__label" style="color:#dc2626">{extra_label}</div>
              <div class="result-hero__value" id="r_extra_tax" style="color:#dc2626">£0</div>
              <div class="result-hero__sub">{extra_sub}</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <section class="faq-section">
      <h2>{sec1_h}</h2>
      <div class="card" style="margin-bottom:2rem"><div class="card__body"><p>{sec1_p1}</p><p>{sec1_p2}</p></div></div>

      <h2>{sec2_h}</h2>
      <div class="card" style="margin-bottom:2rem"><div class="card__body"><p>{sec2_p1}</p></div></div>

      <h2>{sec3_h}</h2>
      <div class="card" style="margin-bottom:2rem"><div class="card__body"><p>{sec3_p1}</p></div></div>

      <h2>{sec4_h}</h2>
      <div class="card" style="margin-bottom:2rem">
        <div class="card__body">
          <ul>
            <li><a href="{home}section-24-calculator/">{related_1}</a></li>
            <li><a href="{home}buy-to-let-calculator/">{related_2}</a></li>
            <li><a href="{home}rental-yield-calculator/">{related_3}</a></li>
          </ul>
        </div>
      </div>
    </section>

    <div class="notice">{editorial}</div>
    <details class="faq-item"><summary>{faq_q1}</summary><div class="faq-body"><p>{faq_a1}</p></div></details>
    <details class="faq-item"><summary>{faq_q2}</summary><div class="faq-body"><p>{faq_a2}</p></div></details>
    <details class="faq-item"><summary>{faq_q3}</summary><div class="faq-body"><p>{faq_a3}</p></div></details>

    <div class="ad-slot">Advertisement</div>
  </div>
</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand"><div class="footer-brand__name">Property<span>Brain</span></div><p>Free UK property investment calculators. Not financial advice.</p></div>
      <div class="footer-links"><h4>Calculators</h4><ul><li><a href="{home}buy-to-let-calculator/">Buy-to-Let</a></li><li><a href="{home}stamp-duty-calculator/">Stamp Duty</a></li><li><a href="{home}section-24-calculator/">Section 24</a></li><li><a href="{sslug}">2027 Property Tax</a></li></ul></div>
      <div class="footer-links"><h4>Info</h4><ul><li><a href="{home}guide/">Guide</a></li><li><a href="{home}free-tools/">Free Tools</a></li><li><a href="{home}about/">About</a></li><li><a href="{home}privacy/">Privacy</a></li><li><a href="{home}terms/">Terms</a></li></ul></div>
    </div>
    <div class="footer-bottom"><span>{footer_line}</span><span>{footer_copyright}</span><span><a href="https://propertyalert.uk">PropertyAlert.uk</a></span></div>
  </div>
</footer>

<script src="{home}assets/js/calculators.js"></script>
<script>
(function () {{
  var PA = 12570, BASIC_LIMIT = 50270, HIGHER_LIMIT = 125140;
  function sliceTax(start, end, rBasic, rHigher, rAdd) {{
    var bounds = [0, PA, BASIC_LIMIT, HIGHER_LIMIT, Infinity];
    var rates = [0, rBasic, rHigher, rAdd];
    var tax = 0;
    for (var i = 0; i < 4; i++) {{
      var segStart = Math.max(start, bounds[i]);
      var segEnd = Math.min(end, bounds[i + 1]);
      if (segEnd > segStart) tax += (segEnd - segStart) * rates[i];
    }}
    return tax;
  }}
  function fmtM(n) {{ return '£' + Math.round(n).toLocaleString('en-GB'); }}

  function calc() {{
    var otherIncome = parseFloat(document.getElementById('other_income').value) || 0;
    var propertyProfit = parseFloat(document.getElementById('property_profit').value) || 0;

    var totalToday = sliceTax(0, otherIncome + propertyProfit, 0.20, 0.40, 0.45);
    var otherAlone = sliceTax(0, otherIncome, 0.20, 0.40, 0.45);
    var propTaxToday = totalToday - otherAlone;
    var netToday = propertyProfit - propTaxToday;

    var otherTax2027 = sliceTax(0, otherIncome, 0.20, 0.40, 0.45);
    var propTax2027 = sliceTax(otherIncome, otherIncome + propertyProfit, 0.22, 0.42, 0.47);
    var total2027 = otherTax2027 + propTax2027;
    var net2027 = propertyProfit - propTax2027;

    var extraTax = total2027 - totalToday;

    document.getElementById('r_prop_tax_today').textContent = fmtM(propTaxToday);
    document.getElementById('r_total_today').textContent = fmtM(totalToday);
    document.getElementById('r_net_today').textContent = fmtM(netToday);
    document.getElementById('r_prop_tax_2027').textContent = fmtM(propTax2027);
    document.getElementById('r_total_2027').textContent = fmtM(total2027);
    document.getElementById('r_net_2027').textContent = fmtM(net2027);
    document.getElementById('r_extra_tax').textContent = fmtM(extraTax);
  }}
  document.querySelectorAll('input,select').forEach(function (el) {{
    el.addEventListener('change', calc);
    el.addEventListener('input', calc);
  }});
  calc();
}})();
</script>
</body>
</html>
'''.format(
        html_lang=lang['html_lang'], title=t['title'], description=t['description'],
        canonical=canonical, hreflang_links=hreflang_links, og_title=t['og_title'],
        og_description=t['og_description'], home=home, code=code, h1=t['h1'],
        faq_schema=faq_schema, cookie='', notice=notice, card_header=t['card_header'],
        label_other=t['label_other'], label_property=t['label_property'],
        results_header=t['results_header'], th_blank=t['th_blank'], th_today=t['th_today'],
        th_2027=t['th_2027'], row_property_tax=t['row_property_tax'], row_total_tax=t['row_total_tax'],
        row_net_property=t['row_net_property'], extra_label=t['extra_label'], extra_sub=t['extra_sub'],
        sec1_h=t['sec1_h'], sec1_p1=t['sec1_p1'], sec1_p2=sec1_p2, sec2_h=t['sec2_h'], sec2_p1=t['sec2_p1'],
        sec3_h=t['sec3_h'], sec3_p1=sec3_p1, sec4_h=t['sec4_h'], related_1=t['related_1'],
        related_2=t['related_2'], related_3=t['related_3'], editorial=t['editorial'],
        faq_q1=t['faq_q1'], faq_a1=t['faq_a1'], faq_q2=t['faq_q2'], faq_a2=t['faq_a2'],
        faq_q3=t['faq_q3'], faq_a3=t['faq_a3'], footer_line=t['footer_line'],
        footer_copyright=t['footer_copyright'], breadcrumb=t['breadcrumb'], lead=t['lead'],
        nav_label=lang['nav_label'], lang_menu=lang_menu,
        sslug=(dir_prefix if dir_prefix else '/') + SLUG + '/',
    )


def main():
    for lang in LANGS:
        html = render(lang)
        out_dir = os.path.join(ROOT, lang['dir_path'], SLUG)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, 'index.html')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print('wrote', os.path.relpath(out_path, ROOT), len(html), 'bytes')


if __name__ == '__main__':
    main()
