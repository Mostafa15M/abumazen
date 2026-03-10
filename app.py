from flask import Flask, render_template, request

app = Flask(__name__)

# بيانات مركز القليوبي المعتمدة
COMPANY_INFO = {
    'name': 'القليوبي للأسفنج والفوم',
    'domain': 'qalyoubysponge.com',
    'phone': '01003316023',
    'address': 'شبين القناطر - القليوبية'
}

# قائمة المنتجات (الأسعار تقريبية تقدر تعدلها هنا)
PRODUCTS = {
    'foam_colors': {'name': 'فوم ألوان (جميع الكثافات)', 'price': 160},
    'med_sponge': {'name': 'إسفنج متوسط (للأنتريهات)', 'price': 8500},
    'high_density': {'name': 'إسفنج ضغط عالي (مراتب وركن)', 'price': 11000},
    'tools': {'name': 'مستلزمات تنجيد (إبر، خيوط، شريط)', 'price': 0}
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        p_type = request.form.get('p_type')
        l = float(request.form.get('l', 0))
        w = float(request.form.get('w', 0))
        t = float(request.form.get('t', 0))
        
        # حساب الحجم بالمتر المكعب
        volume = (l * w * t) / 1000000
        total_price = volume * PRODUCTS[p_type]['price']
        
        result = {
            'p_name': PRODUCTS[p_type]['name'],
            'price': round(total_price, 2) if total_price > 0 else "تواصل معنا للسعر",
            'wa_link': f"https://wa.me/201003316023?text=طلب من موقع {COMPANY_INFO['domain']}: محتاج {PRODUCTS[p_type]['name']} مقاس {l}x{w} سم"
        }
        
    return render_template('index.html', info=COMPANY_INFO, products=PRODUCTS, result=result)

if __name__ == '__main__':
    # تشغيل على بورت 80 للدومين
    app.run(host='0.0.0.0', port=80)
