# 🐍 Python Reverse Shell (Basit Geri Kabuk Arka Kapısı)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Socket-TCP-green?style=for-the-badge&logo=pypi">
  <img src="https://img.shields.io/badge/Amaç-Eğitimsel-red?style=for-the-badge">
</p>

---

## 📺 Detaylı Anlatım: YouTube Videosu

Bu depo, **Python socket** modülü kullanılarak geliştirilen ve siber güvenlik eğitimlerinde temel teşkil eden bir **Reverse Shell (Geri Kabuk)** arka kapısı uygulamasının kodlarını içermektedir. Projenin tüm detaylarını, kodun adım adım yazılışını ve çalışma mantığını aşağıdaki videodan izleyebilirsiniz.

<p align="center">
  <a href="http://www.youtube.com/watch?v=wj76ClEge_s">
     
  </a>
  <br>
  <a href="http://www.youtube.com/watch?v=wj76ClEge_s">
    <h3>▶️ PYTHON İLE KENDİ VİRÜSÜMÜ YAZDIM | EĞİTİM AMAÇLI</h3>
  </a>
  <br>
  **Kanal:** Furares | **Yayın Tarihi:** 2025-11-26 | **Süre:** 23:29
</p>

---

## 💡 Proje Özeti

Bu proje, bir saldırgan (Listener) ve bir hedef sistem (Backdoor) arasındaki iletişimi modelleyerek, saldırganın hedef sistemden bir bağlantı almasını ve uzaktan komutları yürütebilmesini sağlar.

### Temel Özellikler
* **TCP Bağlantısı:** Python'ın standart `socket` kütüphanesi üzerinden güvenilir TCP bağlantısı kurma.
* **Uzaktan Komut Yürütme:** `subprocess` modülü ile hedef makinede kabuk komutlarını çalıştırabilme.
* **JSON Veri Transferi:** Veri bütünlüğünü korumak için komut ve sonuç çıktılarının JSON formatında gönderilip alınması.
* **CD Komutu Desteği:** `os` kütüphanesi ile çalışma dizinini değiştirebilme yeteneği.

---

## 🚨 Yasal Uyarı ve Sorumluluk Reddi

<p align="center">
    <b>BU YAZILIM YALNIZCA SİBER GÜVENLİK EĞİTİMİ VE FARKINDALIĞI İÇİN GELİŞTİRİLMİŞTİR.</b>
</p>

* Bu projedeki kodların amacı, **savunma mekanizmalarını anlamak** ve kötü niyetli yazılımların çalışma prensiplerini öğrenmektir.
* Bu yazılımın **izniniz veya yetkiniz olmayan** herhangi bir sistem, ağ veya cihaza karşı kullanılması **kesinlikle yasa dışıdır ve suç teşkil eder.**
* Projenin geliştiricisi/paylaşanı, bu kodun herhangi bir yasa dışı kullanımından kaynaklanacak **zararlardan veya hukuki sonuçlardan sorumlu değildir.**
* Kullanıcı, bu kodun etik ve yasal çerçeveler içerisinde kullanılmasından **tamamen kendisi sorumludur.**
