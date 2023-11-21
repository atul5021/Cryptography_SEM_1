import hmac
import hashlib
import secrets
#Initial sent message
sent_msg = input('Enter message:')
key = secrets.token_bytes(100)
s_md_1 =hmac.new(key=key,msg=sent_msg.encode(),digestmod=hashlib.md5)
init_msg_digest = s_md_1.hexdigest()

# Received Message
received = sent_msg
r_md_1 =hmac.new(key=key,msg=received.encode(),digestmod=hashlib.md5)
recv_msg_digest = r_md_1.hexdigest()
#Comparing sent and received messages
print("----Before Tampering----")
print('Is the message received without any tampering:',hmac.compare_digest(init_msg_digest,recv_msg_digest))

#Tampered Message
tampered_msg = sent_msg[1:]
md_2 =hmac.new(key=key,msg=tampered_msg.encode(),digestmod=hashlib.md5)
tampered_msg_digest = md_2.hexdigest()

#Comparing after tampering
print("----After Tampering----")
print('Is the message received without any tampering:',hmac.compare_digest(init_msg_digest,tampered_msg_digest))
