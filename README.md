# E-DNSRESOLVER
This a simple code for begineers to learn how "Dns Resolver" work using Python

دعوني أشرح هذا الكود للمبتدئين:

يستخدم الكود المكتبة dns.resolver للقيام بحل أسماء النطاقات (DNS) إلى عناوين IP.
الدالة resolve_dns_with_dnspython(domain_name) تقوم بحل اسم النطاق المعطى إلى عنوان IP.
إذا نجح الحل، سيتم طباعة عنوان IPv4 المرتبط بالنطاق.
إذا فشل الحل (مثل عدم وجود النطاق أو عدم وجود سجلات DNS)، سيتم طباعة رسالة خطأ.
