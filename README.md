# 画像用スクレイピングプログラム

指定したワード で yahoo の 画像検索 から 画像 を取得する。


## yahooの画像検索を使用する理由

-  yahooは1度のスクレイピングにおける画像の取得量が最も多かった
    - yahoo : 約600枚
    - google : 約250枚
    - bing : 約200枚
-  画像の取得が行いやすい


## 制作手順

1. 基本的な動作のプログラムを作成する
1. 処理を小さな関数に分割していく <- いまここ
1. 例外処理を追加する
1. 複数入力への対応させる
1. 取得する画像のダブり対策をする