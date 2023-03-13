###############################################################
# RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)
###############################################################

###############################################################
# Veri Seti Hikayesi
###############################################################

# Veri seti son alışverişlerini 2020 - 2021 yıllarında OmniChannel(hem online hem offline alışveriş yapan) olarak yapan müşterilerin geçmiş alışveriş davranışlarından
# elde edilen bilgilerden oluşmaktadır.

# master_id: Eşsiz müşteri numarası
# order_channel : Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile, Offline)
# last_order_channel : En son alışverişin yapıldığı kanal
# first_order_date : Müşterinin yaptığı ilk alışveriş tarihi
# last_order_date : Müşterinin yaptığı son alışveriş tarihi
# last_order_date_online : Muşterinin online platformda yaptığı son alışveriş tarihi
# last_order_date_offline : Muşterinin offline platformda yaptığı son alışveriş tarihi
# order_num_total_ever_online : Müşterinin online platformda yaptığı toplam alışveriş sayısı
# order_num_total_ever_offline : Müşterinin offline'da yaptığı toplam alışveriş sayısı
# customer_value_total_ever_offline : Müşterinin offline alışverişlerinde ödediği toplam ücret
# customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
# interested_in_categories_12 : Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi

###############################################################
# GÖREVLER
###############################################################

# GÖREV 1: Veriyi Anlama (Data Understanding) ve Hazırlama
           # 1. flo_data_20K.csv verisini okuyunuz.
           # 2. Veri setinde
                     # a. İlk 10 gözlem,
                     # b. Değişken isimleri,
                     # c. Betimsel istatistik,
                     # d. Boş değer,
                     # e. Değişken tipleri, incelemesi yapınız.
           # 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Herbir müşterinin toplam
           # alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.
           # 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
           # 5. Alışveriş kanallarındaki müşteri sayısının, ortalama alınan ürün sayısının ve ortalama harcamaların dağılımına bakınız.
           # 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.
           # 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.
           # 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.


import datetime as dt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
pd.set_option('display.max_columns', None) #tüm sütunları göster
pd.set_option('display.max_rows', None) #tüm satırları göster
pd.set_option('display.width',500)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# 1. flo_data_20K.csv verisini okuyunuz.
df_ = pd.read_csv("C:/Users/.../flo_data_20k.csv")
df = df_.copy()

# 2. Veri setinde
df.head(10)
df.columns
df.describe().T
df.isnull().sum()

# 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir.
# Herbir müşterinin toplam alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.

#order_num_total_ever_online, order_num_total_ever_offline


#order_num_total_ever (müşterinin toplam sipariş sayısı) (Freq)
df["order_num_total_ever"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]


#customer_value_total_ever_offline, customer_value_total_ever_online

# Müşterinin alışverişlerinde ödediği toplam ücret (monetary)
#customer_value_total_ever
df["customer_value_total_ever"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]


# 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.

df.dtypes

for col in df.columns:
    if "date" in col:
        df[col] = pd.to_datetime(df[col])


# 5. Alışveriş kanallarındaki müşteri sayısının, ortalama alınan ürün sayısının ve ortalama harcamaların dağılımına bakınız.
df.groupby("order_channel").agg({"master_id" : ["count"],
                                "order_num_total_ever":["mean"],
                                 "customer_value_total_ever":["mean"]}).head()

# 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.

df.groupby("master_id").agg({"customer_value_total_ever": "sum"}).sort_values("customer_value_total_ever", ascending=False).head(10)


# 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.

df.groupby("master_id").agg({"order_num_total_ever": "sum"}).sort_values("order_num_total_ever", ascending=False).head(10)


# 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.

def check_df(dataframe, head=5):
    print("############## Shape #############")
    print(dataframe.shape)
    print("############## Type #############")
    print(dataframe.dtypes)
    print("############## Head #############")
    print(dataframe.head(head))
    print("############## Tail #############")
    print(dataframe.tail(head))
    print("############## NA #############")
    print(dataframe.isnull().sum())
    print("############## Quantiles #############")
    print(dataframe.describe([0, 0.05, 0.5, 0.95, 0.99, 1]).T)

check_df(df)



def pre_df(dataframe):
    df["order_num_total_ever"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
    df["customer_value_total_ever"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]

    for col in df.columns:
        if "date" in col:
            df[col] = pd.to_datetime(df[col])
    return df

pre_df(df)


df.head()


# GÖREV 2: RFM Metriklerinin Hesaplanması

# Adım 1: Recency, Frequency ve Monetary tanımlarını yapınız.
# Adım 2: Müşteri özelinde Recency, Frequency ve Monetary metriklerini hesaplayınız.
# Adım 3: Hesapladığınız metrikleri rfm isimli bir değişkene atayınız.
# Adım 4: Oluşturduğunuz metriklerin isimlerini recency, frequency ve monetary olarak değiştiriniz.
# recency değerini hesaplamak için analiz tarihini maksimum tarihten 2 gün sonrası seçebilirsiniz


# matematiksel karşılığı
# R: analizin yapıldığı tarih - müşterinin son satın almasının yapıldığı tarih
# F: müşterinin yaptığı toplam satın alma
# M: toplam satınalmalar neticesinde bıraktığı toplam satınalma değeridir.

# Recency
df["last_order_date"].max() #Timestamp('2021-05-30 00:00:00') - 1.6.2021

today_date = dt.datetime(2021,6,1)
type(today_date)

rfm = df.groupby("master_id").agg({"last_order_date": lambda last_order_date: (today_date - last_order_date.max()).days,
                                    "order_num_total_ever": lambda order_num_total_ever: order_num_total_ever,
                                    "customer_value_total_ever": lambda customer_value_total_ever: customer_value_total_ever.sum()}) 



rfm.columns = ["recency", "frequency","monetary"]
rfm.head()

# GÖREV 3: RF ve RFM Skorlarının Hesaplanması

#Adım 1: Recency, Frequency ve Monetary metriklerini qcut yardımı ile 1-5 arasında skorlara çeviriniz.
#Adım 2: Bu skorları recency_score, frequency_score ve monetary_score olarak kaydediniz.


rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels= [5,4,3,2,1])
rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels= [1,2,3,4,5])
rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels= [1,2,3,4,5])

rfm.head()
#Adım 3: recency_score ve frequency_score’u tek bir değişken olarak ifade ediniz ve RF_SCORE olarak kaydediniz.
rfm["RF_SCORE"] = (rfm["recency_score"].astype(str) +
                    rfm["frequency_score"].astype(str))


rfm["RF_SCORE"].head()

# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması

#Adım 1: Oluşturulan RF skorları için segment tanımlamaları yapınız.

seg_map = {
    r'[1-2][1-2]': 'hibernating', 
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}


#Adım 2: Aşağıdaki seg_map yardımı ile skorları segmentlere çeviriniz.

rfm['segment'] = rfm['RF_SCORE'].replace(seg_map, regex=True)

# GÖREV 5: Aksiyon zamanı!
           # 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.

rfm[["segment", "recency","frequency", "monetary"]].groupby("segment").agg("mean")


# 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulun ve müşteri id'lerini csv ye kaydediniz.
# a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
# tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Sadık müşterilerinden(champions,loyal_customers),
# ortalama 250 TL üzeri ve kadın kategorisinden alışveriş yapan kişiler özel olarak iletişim kuralacak müşteriler. Bu müşterilerin id numaralarını csv dosyasına
# yeni_marka_hedef_müşteri_id.cvs olarak kaydediniz.



target_customers = rfm[((rfm['segment'] == 'champions') | (rfm['segment'] == 'loyal_customers'))]
avg_spent = target_customers.groupby('master_id')['monetary'].mean().reset_index()
avg_spent.head()
qualified_customers = avg_spent[avg_spent['monetary'] >= 250]
female_cat = df[df['interested_in_categories_12'].str.contains('KADIN')]
target_customers = qualified_customers.merge(female_cat, on='master_id')

target_customers.head()
target_customers[["master_id"]].to_csv("yeni_marka_hedef_müşteri_id", index=False)


# GÖREV 6: Tüm süreci fonksiyonlaştırınız.

def pre_df(dataframe):
    df["order_num_total_ever"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]

    df["customer_value_total_ever"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]

    for col in df.columns:
        if "date" in col:
            df[col] = pd.to_datetime(df[col])
    return df

pre_df(df)

def create_rfm(dataframe, csv=False): 

        # RFM METRIKLERININ HESAPLANMASI
    today_date = dt.datetime(2021,6,1)
    rfm = df.groupby("master_id").agg(
        {"last_order_date": lambda last_order_date: (today_date - last_order_date.max()).days,
         # son alışveriş tarihi: bugünün tarihinden müşterinin en son satın alma tarihini çıkar. gün cinsinden ifade et.
         "order_num_total_ever": lambda order_num_total_ever: order_num_total_ever,
         # kaç fatura var, kaç kez alışveriş yapılmış
         "customer_value_total_ever": lambda customer_value_total_ever: customer_value_total_ever.sum()})

    rfm.columns = ['recency', 'frequency', "monetary"]


    # RFM SKORLARININ HESAPLANMASI
    rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
    rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
    rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])

    # cltv_df skorları kategorik değere dönüştürülüp df'e eklendi
    rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) +
                        rfm['frequency_score'].astype(str))


    # SEGMENTLERIN ISIMLENDIRILMESI
    seg_map = {
        r'[1-2][1-2]': 'hibernating',
        r'[1-2][3-4]': 'at_risk',
        r'[1-2]5': 'cant_loose',
        r'3[1-2]': 'about_to_sleep',
        r'33': 'need_attention',
        r'[3-4][4-5]': 'loyal_customers',
        r'41': 'promising',
        r'51': 'new_customers',
        r'[4-5][2-3]': 'potential_loyalists',
        r'5[4-5]': 'champions'
    }

    rfm['segment'] = rfm['RFM_SCORE'].replace(seg_map, regex=True)
    rfm = rfm[["recency", "frequency", "monetary", "segment"]]


    if csv: # eğer csv argümanında "True" girilirse şunu yap
        rfm.to_csv("rfm.csv") # rmf in csv dosyasını oluştur.

    return rfm

df = df_.copy()

rfm_new = create_rfm(df)
rfm_new.head()
