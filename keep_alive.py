import os
from threading import Thread
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def _run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = Thread(target=_run, daemon=True)
    t.start()
```[cite: 8, 9]

### 🛠️ ជំហានត្រូវធ្វើ៖
1. សូមលុបកូដចាស់ក្នុង file **`keep_alive.py`** ចោលឱ្យអស់ស្អាត។
2. Copy កូដខាងលើនេះទៅដាក់ជំនួសវិញដោយប្រយ័ត្នប្រយែង (ធានាថាមិនមានសញ្ញាចម្លែក ឬអក្សរបន្ថែមទេ)។
3. Save ទុក ហើយ Render នឹងធ្វើការ Deploy ឡើងវិញដោយស្វ័យប្រវត្តិ ពេលនោះវានឹងដំណើរការជោគជ័យតែម្ដងបង!
