import shelve

f = open("xxxxxxx029", 'r')
data = f.readlines()

nim = data[0].strip()
tanggal_lahir = data[1].strip()
nama = data[2].strip()

f = shelve.open("Thoriq")
f['nim']= nim.strip() 
f['tgl_lahir']=tanggal_lahir.strip()
f['nama']=nama.strip()
f.close()
