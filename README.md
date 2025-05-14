# QuizApp
# 📚 Masaüstü Quiz Uygulaması

Bu uygulama, farklı konularda quiz çözme ve konu anlatımı desteğiyle öğrencilerin öğrenmesini hedefleyen bir masaüstü eğitim teknolojileri projesidir. Kullanıcılar sisteme kayıt olup giriş yaptıktan sonra quiz çözebilir, konu anlatım içeriklerini görüntüleyebilir ve kendi avatarlarını seçerek kişiselleştirilmiş bir deneyim yaşayabilirler.

---

## 🚀 Proje Amacı

Bu uygulama, kullanıcıların eğlenceli ve etkileşimli bir şekilde öğrenmelerini sağlamak amacıyla geliştirilmiştir. Özellikle ilkokul ve ortaokul düzeyindeki öğrencilerin hem teorik bilgiye erişmesini hem de testler ile pekiştirme yapmasını sağlar.

---

## 🧩 Uygulama Özellikleri

- ✅ **Kullanıcı Kaydı ve Girişi**  
  Yeni kullanıcılar sisteme kayıt olabilir, mevcut kullanıcılar giriş yapabilir.

- 📚 **Konu Anlatımı Ekranı**  
  JSON dosyasında tanımlı olan konular başlıklar halinde listelenir ve her konuya ait açıklama görüntülenebilir.

- ❓ **Quiz Ekranı**  
  Kullanıcılar, belirli bir konuda çoktan seçmeli soruları çözebilir ve doğru-yanlış geri bildirimleri alabilir.

- 🏆 **Sonuç Ekranı**  
  Quiz sonunda kullanıcıya puanı ve başarı durumu gösterilir.

- 🧑‍🎨 **Avatar Seçimi**  
  Kullanıcılar, profillerinde kullanmak üzere karikatür tarzı avatarlar seçebilir.

---

## 🛠 Kullanılan Teknolojiler

| Teknoloji | Açıklama |
|----------|----------|
| **Python** | Uygulamanın temel programlama dili |
| **Tkinter** | Grafiksel kullanıcı arayüzü oluşturmak için kullanıldı |
| **JSON** | Quiz verisi, kullanıcılar ve konu içerikleri bu formatta saklanır |
| **PIL (Pillow)** | Avatar görsellerini yüklemek ve düzenlemek için |

---

## 📂 Dosya Yapısı

```plaintext
quiz_app/
│
├── main.py               # Ana uygulama dosyası
├── users.json            # Kayıtlı kullanıcıların bilgileri
├── quiz_data.json        # Quiz soruları ve cevapları
├── topics.json           # Konu anlatımı içerikleri
├── avatars/              # Kullanıcı avatarlarının görselleri
└── README.md             # Proje hakkında genel bilgiler
