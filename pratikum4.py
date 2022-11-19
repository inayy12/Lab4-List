NAMA = []
NIM = []
Tugas = []
UTS = []
UAS = []
Total =[]

while True:
    Nama=input('Nama :')
    NAMA.append(Nama)
    nim=int(input('NIM : '))
    NIM.append(nim)
    nTugas = float(input('NIilai Tugas : '))
    Tugas.append(nTugas)
    uts=float(input('Nilai UTS : '))
    UTS.append(uts)
    uas=float(input('Nilai UAS : '))
    UAS.append(uts)
    nAkhir=(int(nTugas)*.3)+(int(uts)*.35)+(int(uas)*.35)
    Total.append(nAkhir)

    lagi=''
    while lagi !='Y'and lagi !='T':
        lagi = input('Tambah data(Y/T)?')
        if lagi == 'T':
             print ('='*58)
             print('|No|\tNAMA\t| NIM |Tugas|UTS|UAS|Total|')
             print('='*58)
        for i in range(len(NIM)):
            mn='|%d.|\t%s\t' % (i+1, NAMA[i])
            im='|%d' % NIM[i]
            tg='|%d' % Tugas[i]
            ut='  |%d' % UTS[i]
            us=' |%d' % UAS[i]
            ak=' |%2f' % Total[i]
            ov='|'
            join =mn+im+tg+ut+us+ak+ov
            print(join)

            break