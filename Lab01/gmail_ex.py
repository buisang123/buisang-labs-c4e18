from gmail import GMail
from gmail import Message
from random import choice
gmail =  GMail("sangbuiduc123@gmail.com","sang1998")

html_content = """
<p style="text-align: center;">cộng h&ograve;a x&atilde; hội chủ nghĩa việt nam</p>
<p style="text-align: center;">độc lập - tự do - hạnh ph&uacute;c&nbsp;</p>
<p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></p>
<p>k&iacute;nh gửi: giảng vi&ecirc;n&nbsp;</p>
<p>em t&ecirc;n l&agrave; : B&ugrave;i Đức Sang</p>
<p>h&ocirc;m nay {{work}} n&ecirc;n em xin ph&eacute;p cho em nghỉ buổi học h&ocirc;m nay</p>
<p>sang</p>"

"""
# placeholder
sickness = ["đạu bụng","gãy tay","sốt"]
reason = choice(sickness)
html_content = html_content.replace("{{work}}",reason)
msg = Message("test message",to = "20130075@student.hust.edu.vn",html = html_content)
gmail.send(msg)
