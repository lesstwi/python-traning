import sys
print("くら寿司分割用プログラム(125円～店舗用)")
print("このプログラムで数値を入力するときは半角で入力してください。0皿の時は0と入力してください。空欄ですとエラーになります。")
sushi1251 = input("125円寿司の皿数を入力してください")
sushi1301 = input("130円寿司の皿数を入力してください")
sushi1401 = input("140円寿司の皿数を入力してください")
sushi1501 = input("150円寿司の皿数を入力してください")
sushi1801 = input("180円寿司の皿数を入力してください")
sushi1901 = input("190円寿司の皿数を入力してください")
sushi2001 = input("200円寿司の皿数を入力してください")
sushi2201 = input("220円寿司の皿数を入力してください")
sushi2501 = input("250円寿司の皿数を入力してください")
sushi2701 = input("270円寿司の皿数を入力してください")
sushi2901 = input("290円寿司の皿数を入力してください")
sushi3701 = input("370円寿司の皿数を入力してください")
print("わかりました。")
print("それでは計算します。")
sushi125 = int(sushi1251)
sushi130 = int(sushi1301)
sushi140 = int(sushi1401)
sushi150 = int(sushi1501)
sushi180 = int(sushi1801)
sushi190 = int(sushi1901)
sushi200 = int(sushi2001)
sushi220 = int(sushi2201)
sushi250 = int(sushi2501)
sushi270 = int(sushi2701)
sushi290 = int(sushi2901)
sushi370 = int(sushi3701)
print("125円寿司が",sushi125,"皿、130円寿司が",sushi130,"皿、140円寿司が",sushi140,"皿、150円寿司が",sushi150,"皿、180円寿司が",sushi180,"皿、190円寿司が",sushi190,"皿、200円寿司が",sushi200,"皿、220円寿司が",sushi220,"皿、250円寿司が",sushi250,"皿、270円寿司が",sushi270,"皿、290円寿司が",sushi290,"皿、370円寿司が",sushi370,"皿ですね。")
result = (125*sushi125)+(130*sushi130)+(140*sushi140)+(150*sushi150)+(180*sushi180)+(190*sushi190)+(200*sushi200)+(220*sushi220)+(250*sushi250)+(270*sushi270)+(290*sushi290)+(370*sushi370)
result2 = int(result)
print("合計は", result2, "円です")
print("割り勘をしますか？")
warikan = input("[y](します)か[n](しません)で入力してください")
if warikan == "y":
  warikanninzuu = input("割り勘する人数を入力してください")
  warikanninzuu1 = int(warikanninzuu)
  warikansho = result2//warikanninzuu1
  warikanamari = result2-(warikansho*warikanninzuu1)
  print("一人当たり", warikansho,"円で、あまりは",warikanamari,"円です。")
else:
  sys.exit()