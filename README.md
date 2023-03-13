RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)



İş Problemi (Business Problem)

Bir perakende alışveriş şirketi müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor.
Buna yönelik olarak müşterilerin davranışları tanımlanacak ve bu davranış öbeklenmelerine göre gruplar oluşturulacak..


Veri Seti Hikayesi


Veri seti son alışverişlerini 2020 - 2021 yıllarında OmniChannel(hem online hem offline alışveriş yapan) olarak yapan müşterilerin geçmiş alışveriş davranışlarından
elde edilen bilgilerden oluşmaktadır.

master_id: Eşsiz müşteri numarası
order_channel : Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile, Offline)
last_order_channel : En son alışverişin yapıldığı kanal
first_order_date : Müşterinin yaptığı ilk alışveriş tarihi
last_order_date : Müşterinin yaptığı son alışveriş tarihi
last_order_date_online : Muşterinin online platformda yaptığı son alışveriş tarihi
last_order_date_offline : Muşterinin offline platformda yaptığı son alışveriş tarihi
order_num_total_ever_online : Müşterinin online platformda yaptığı toplam alışveriş sayısı
order_num_total_ever_offline : Müşterinin offline'da yaptığı toplam alışveriş sayısı
customer_value_total_ever_offline : Müşterinin offline alışverişlerinde ödediği toplam ücret
customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
interested_in_categories_12 : Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi



GÖREVLER


GÖREV 1: Veriyi Anlama (Data Understanding) ve Hazırlama

            1. flo_data_20K.csv verisini okuyunuz.
            
            2. Veri setinde
            
                      a. İlk 10 gözlem,
                      
                      b. Değişken isimleri,
                      
                      c. Betimsel istatistik,
                      
                      d. Boş değer,
                      
                      e. Değişken tipleri, incelemesi yapınız.
                      
            3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Herbir müşterinin toplam
            
            alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.
            
            4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
            
            5. Alışveriş kanallarındaki müşteri sayısının, ortalama alınan ürün sayısının ve ortalama harcamaların dağılımına bakınız.
            
            6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.
            
            7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.
            
            8. Veri ön hazırlık sürecini fonksiyonlaştırınız.
            
           
           
