import qrcode

#take user input >UPI

upi_id = input('Enter your UPI Id: ')

phonpe_url = f'upi://pay?pa={upi_id}&pn=Recepient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recepient%20Name&mc=1234'
gpay_url = f'upi://pay?pa={upi_id}&pn=Recepient%20Name&mc=1234'

#generating qr codes
phonpe_qr = qrcode.make(phonpe_url)
paytm_qr = qrcode.make(paytm_url)
gpay_qr = qrcode.make(gpay_url)

#saving qr codes

phonpe_qr.save('phonpe_qr.png')
# paytm_qr.save('paytm_qr.png')
# gpay_qr.save('gpay_qr.png')

#show qr

phonpe_qr.show()
# paytm_qr.show()
# gpay_qr.show()
