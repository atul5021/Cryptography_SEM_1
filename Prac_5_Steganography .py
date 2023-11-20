from stegano import lsb

imgpath=input('Enter the image name(with file extension) : ')
msg=input('Enter message to be hidden : ')
secret=lsb.hide(imgpath,msg)
secret.save('image_with_hidden_text.png')
print('Image containing message saved.')
clear_message=lsb.reveal("image_with_hidden_text.png")
print('Verifying the message from saved image : ',clear_message)


# install stegano
#pip install stegano
#!pip install stegano
