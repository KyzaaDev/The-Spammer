![Python](https://img.shields.io/badge/python-3.6%2B-blue)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20termux-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)


# 🧨 The-Spammer
**The-Spammer** adalah tool sederhana yang digunakan untuk melakukan spamming ke API Telegram. Endpoint API biasanya didapat dari hasil reverse engineering terhadap malware atau trojan yang terhubung ke Telegram sebagai *Command & Control*


![No Image Found!](https://i.imgur.com/cpzIBOs_d.png?maxwidth=520&shape=thumb&fidelity=high)

**⚠️ Gunakan hanya untuk tujuan edukasi dan riset!**

## 📦*Requirements*
- Python 3.x
- Python ```pip3```


## ⚙️*Installation*
1. Clone repository *The-Spammer*:
<pre>https://github.com/KyzaaDev/The-Spammer.git</pre>

2. Masuk ke directory project:
<pre>cd The-Spammer</pre>

3. Install Depedencies:
<pre>pip install -r requirements.txt</pre>

4. Jalankan bantuan:
<pre>python3 spam.py -h</pre>

## *Features*
### 🔗 URL
Endpoint Telegram API yang akan menjadi target spam
- Wajib diisi: --url <API_URL>
- Example: 
<pre>python3 spam.py --url https://api.telegram.org/bot<token>/sendMessage?chat_id=<id>&text=</pre>

**⚠️ Endpoint hanya contoh!, masukkan endpoint secara lengkap.**


### 🔁 Loop
Jumlah pengulangan pesan yang dikirim. Default: ```250```
- Opsi: ```--loop <jumlah>```
- Example: 
<pre>python3 spam.py <API_URL> --loop 3</pre>

### ⏱️ Delay
Jeda antar pesan yang dikirim (dalam detik). Default: ```2 detik```
- Opsi: ```--delay <detik>```
- Example: 
<pre>python3 spam.py --url <API_URL> --delay 3</pre>

### 🧪 Full usage example
Contoh penggunaan dengan loop 13 kali dan delay 5 detik:
<pre>python3 spam.py <API_URL> --loop 13 --delay 5</pre>

## 📜Legal disclaimer
<pre lang="markdown">Dengan menggunakan alat ini, Anda menyatakan bahwa Anda telah membaca, memahami, dan menyetujui ketentuan berikut: Alat ini disediakan "apa adanya" tanpa jaminan, pengembang tidak bertanggung jawab atas kerusakan atau kerugian, Anda bertanggung jawab penuh atas penggunaan, dan alat ini hanya untuk edukasi dan penelitian. Anda melepaskan pengembang dari segala tuntutan, klaim, atau kerugian yang timbul dari penggunaan alat ini. Pastikan Anda memiliki izin yang tepat dan mematuhi kebijakan API Telegram serta peraturan yang berlaku.</pre>