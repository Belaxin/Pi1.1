for i in range(0,9):
    print(i,chr(i))

ret = input("zadaj retazec: ")
posun = int(input("zadaj posun"))
for i in range(len(ret),):
    print(f"{ret[i]}:{ord(ret[i])}")

# sifrovanie cezarovou sifrov
ret_kod = ''
samohlaska = 0
spoluhlaska = 0
for i in range(len(ret)):
    print(f"{ret[i]}:{chr(ord(ret[i])+posun)}")
    ret_kod += chr(ord(ret[i])+posun)
print(f"zakodovany retazec je: {ret_kod}")
