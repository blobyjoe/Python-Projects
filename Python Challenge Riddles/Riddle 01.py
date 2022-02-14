s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

l = list(s)
n = ''

alph = 'abcdefghijklmnopqrstuvwxyzab'

for letter in l:
    if letter in alph:
        n += alph[(alph.index(letter) + 2)]
    else:
        n += letter

print(n)

# Translated result:
#i hope you didnt translate it by hand. thats what computers are for.
#doing it in by hand is inefficient and that's why this text is so long.
#using string.maketrans() is recommended. now apply on the url.
