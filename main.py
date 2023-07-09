meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            'IFYKYK': 'Tanggapan jika seseorang memberi tau jika orang tersebut mengetahuinya'
            }
word = input('ketik kata yg tdk kamu mengerti menggunakan huruf kapital semua!')

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('a')
