ret = input("Zadaj retazec: ")
samohlaska = 0
spoluhlaska = 0
for i in range(len(ret)):
    if (ret[i] in 'áaéeíiýyóoúäôu'):
        samohlaska += 1
    elif (ret[i] in 'ďdťtňnľšžlčchgkjbmprsvzf'):
        spoluhlaska += 1

print(f"spoluhlaskiek je {spoluhlaska}, samohlasiek je {samohlaska}")
