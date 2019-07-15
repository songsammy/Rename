import sys,zlib,os

def clacCRC32(x):
		fo = open(x, "rb")
		ff = fo.read(-1)
		nfn=str(hex(zlib.crc32(ff)& 0xffffffff))
		fo.close()
		nfn=nfn.replace("0x","").upper()
		return nfn
		
def getfl():
	fl=sys.argv
	del fl[0]
	return fl
	

fl=getfl()
for x in fl:
		nfn=clacCRC32(x)
		y=x.split("\\")
		z=y[-1].split(".")
		ext=z[-1]
		z=nfn+"."+ext
		y[-1]=z
		n=""
		for m in y:
			n=n+m+"\\"
		n=n[:-1]
		print(n)
		os.rename(x,n)