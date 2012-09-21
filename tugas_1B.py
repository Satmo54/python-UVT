#!/usr/bin/env python2

## Fungsi ##
def jumlah_detik(jam1=0, menit1=0, detik1=0, jam2=0, menit2=0, detik2=0):
	total = (detik1 + menit1 * 60 + jam1 * 3600) - (detik2 + menit2 * 60 + jam2 * 3600)
	detik = total % 60
	menits = ( total - detik ) / 60
	menit = menits % 60
	jam = ( menits - menit ) / 60
	print "Selisih waktu adalah ", jam, "jam, " , menit, "menit, ", detik, "detik."

## masukan ##
w1_jam = 4
w1_menit = 20
w1_detik = 10

w2_jam = 10
w2_menit = 30
w2_detik = 20

jumlah_detik(w2_jam, w2_menit, w2_detik, w1_jam, w1_menit, w1_detik) 
