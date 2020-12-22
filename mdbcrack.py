fname = r"C:\Users\Administrator\Desktop\杨甫meter20201222.mdb"
# 未加密的文件0x42开始至0x61之前的每间隔一字节的数值
baseByte = [0xbe, 0xec, 0x65, 0x9c, 0xfe, 0x28, 0x2b, 0x8a, 0x6c, 0x7b, 0xcd, 0xdf, 0x4f, 0x13, 0xf7, 0xb1]
# 标志 0x62 处的数值
flagByte = 0x0c
# 定义密码字符串
password = '';
# 读取方式打开文件并复制给fs
fs = open(fname, 'rb')
fs.seek(0x14)
version = 'unknow'
ver = ord(fs.read(1))
if ver == 1:
    version = 'Access2000'
elif ver == 0:
    version = 'Access97'
fs.seek(0x42)
bs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
integer = 0
while integer < 33:
    tmpInt = ord(fs.read(1))
    bs[integer] = tmpInt
    integer = integer + 1
# 标记
flag = bs[32] ^ flagByte
# 开始循环
i = 0
while i < 16:
    b = (baseByte[i] ^ bs[i * 2])
    if i % 2 == 0 and ver == 1:
        b = b ^ flag;
    if b > 0:
        password = password + chr(b)
    i = i + 1
fs.close()
print(version)
print(password)

