print("これより、列車の予約をおこないます。")
print("ご希望の列車の種類を教えてください。")
traintype = input("新幹線の場合は半角でshinkansen、特急の場合は半角でlimitedexp,普通列車の場合は半角でnomalを入力してください。※新幹線のみ対応")
if traintype == "shinkansen":
  print("新幹線をご希望ですね！")
  print("次に希望の種別を選択してください。")
  shinkansentype = input("はやぶさかやまびこかをひらがなで入力してください。")
  print("次に希望の新幹線の番号を半角でを入力してください。")
  shinkansenressya = input("希望の新幹線の番号を入力")
  print("ありがとうございます。以下の通り予約を承ります。")
  print(shinkansentype, shinkansenressya, "号で予約を承ります。")
  kakunin = input("よろしければ、yesを入力してください")
  if kakunin == "yes":
    print("予約を承りました")
  else:
    print("予約が完了しませんでした")
