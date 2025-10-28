import qrcode
from  PIL import Image  # needed for .show()

# Taking UPI ID as a input
upi_id = "8080536055@ybl"
note = "Payment for services"


# upi://pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# Define the payment URL based on UPI ID and the payment App
# you can modify these URLs based on the payment apps to want to suopprt


upi_url = f"upi://pay?pa={upi_id}&pn=Teju%20Chapekar&cu=INR&tn={note.replace(' ', '%20')}"

# Create QR codes for each payment app
qr = qrcode.QRCode(
    version=2,
    box_size = 10,
    border=4
)

qr.add_data(upi_url)
qr.make(fit=True)
img = qr.make_image(fill_color="green", back_color="white")

# change colour using fill_color and back)color
phonepay_qr = qr.make_image(fill_color="pink", back_color= "white")
paytm_qr = qr.make_image(fill_color="purple", back_color="white")
google_pay_qr = qr.make_image (fill_color="blue", back_color="white")

# save the qr code to image file
phonepay_qr.save('phonepay_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# Display the qr codes(you may need to install PIL/pillow librery)
phonepay_qr.show()
paytm_qr.show()
google_pay_qr.show()