
# sentences=None, size=100, alpha=0.025, window=5, min_count=5,
#         sample=0, seed=1, workers=1, min_alpha=0.0001, sg=1, hs=1, negative=0,
#         cbow_mean=0, hashfxn=hash, iter=1
#Default configuration

#Konfigurazio aukera hauek Josuk pasatako fitxategitik ateratakoak dira.
#/sc06a1/users/jgoicoechea009/00-run-CorSGwiki-48Conb.pl
#Oraingoz hs eta negative ukitu gabe... Ea nola doazen lehen esperimentuak

confs=[]
confs.append([200, 0.025, 2, 5, 0, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
confs.append([200, 0.025, 5, 5, 0, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
confs.append([200, 0.025, 2, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
confs.append([200, 0.025, 5, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])

confs.append([250, 0.025, 2, 5, 0, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
confs.append([250, 0.025, 5, 5, 0, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
confs.append([250, 0.025, 2, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
confs.append([250, 0.025, 5, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])

confs.append([300, 0.025, 2, 5, 0, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
confs.append([300, 0.025, 5, 5, 0, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
confs.append([300, 0.025, 2, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
confs.append([300, 0.025, 5, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])

confs.append([350, 0.025, 2, 5, 0, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
confs.append([350, 0.025, 5, 5, 0, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
confs.append([350, 0.025, 2, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
confs.append([350, 0.025, 5, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])

confs.append([200, 0.025, 2, 5, 0, 1, 30, 0.0001, 1, 1, 0, 1, hash, 1])
confs.append([200, 0.025, 5, 5, 0, 1, 30, 0.0001, 1, 1, 0, 1, hash, 1])
confs.append([200, 0.025, 2, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 1, hash, 1])
confs.append([200, 0.025, 5, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 1, hash, 1])

confs.append([250, 0.025, 2, 5, 0, 1, 30, 0.0001, 1, 1, 0, 1, hash, 1])
confs.append([250, 0.025, 5, 5, 0, 1, 30, 0.0001, 1, 1, 0, 1, hash, 1])
confs.append([250, 0.025, 2, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 1, hash, 1])
confs.append([250, 0.025, 5, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 1, hash, 1])

confs.append([300, 0.025, 2, 5, 0, 1, 30, 0.0001, 1, 1, 0, 1, hash, 1])
confs.append([300, 0.025, 5, 5, 0, 1, 30, 0.0001, 1, 1, 0, 1, hash, 1])
confs.append([300, 0.025, 2, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 1, hash, 1])
confs.append([300, 0.025, 5, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 1, hash, 1])

confs.append([350, 0.025, 2, 5, 0, 1, 30, 0.0001, 1, 1, 0, 1, hash, 1])
confs.append([350, 0.025, 5, 5, 0, 1, 30, 0.0001, 1, 1, 0, 1, hash, 1])
confs.append([350, 0.025, 2, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 1, hash, 1])
confs.append([350, 0.025, 5, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 1, hash, 1])

#confs.append([400, 0.025, 2, 5, 0, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
#confs.append([400, 0.025, 5, 5, 0, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
#confs.append([400, 0.025, 2, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
#confs.append([400, 0.025, 5, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])

#confs.append([450, 0.025, 2, 5, 0, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
#confs.append([450, 0.025, 5, 5, 0, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
#confs.append([450, 0.025, 2, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
#confs.append([450, 0.025, 5, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])

#confs.append([500, 0.025, 2, 5, 0, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
#confs.append([500, 0.025, 5, 5, 0, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
#confs.append([500, 0.025, 2, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])
#confs.append([500, 0.025, 5, 5, 1e-5, 1, 30, 0.0001, 1, 1, 0, 0, hash, 1])


def main():
    conf=confs[0]
    strconf=[str(i) for i in conf]
    print 'vectors_'+'---'.join(strconf)+'.bin'


if __name__ == '__main__':main()
