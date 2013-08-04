# url: http://www.pythonchallenge.com/pc/def/map.html

from string import maketrans

alphabet = "abcdefghijklmnopqrstuvwxyz"
translate_alphabet = "cdefghijklmnopqrstuvwxyzab"
translate = maketrans(alphabet, translate_alphabet)
input_ = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp."
          "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle."
          "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
print input_.translate(translate)

input2_ = "map"
print input2_.translate(translate)
