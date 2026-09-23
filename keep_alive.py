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

ពេលបង្កើត file `keep_alive.py` នេះរួចរាល់ហើយ (ហើយក្នុង `show_bot.py` មានកូដ `from keep_alive import keep_alive` និងហៅ `keep_alive()` ធម្មតា)[cite: 10] នោះ Render នឹងអាច Build និង Deploy បានជោគជ័យដោយគ្មានបញ្ហាអ្វីទៀតទេបង!
