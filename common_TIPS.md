kaggleに共通したTIPS

# 【2位入賞】ずんだもんとめたんで学ぶKaggle 入門 & 参戦記 Part 1【Petfinderコンペ】【修正版】

あるNotebookの最新verでは，クイックセーブされており実行結果がない場合があるのだ．
そのときは「Version k of n」をクリックし，1個前のコミットされたものを見るのだ．

テストデータのサイズは普通公開されるので，Discussionを漁るのだ．

画像コンペは有名なNNが使われるので，前処理や損失関数の設計の工夫で差が出やすいのだ

## CVについて
CVの目的は，訓練データ→ 訓練データと検証データに分割し，手元でスコアの検証をすること

CVせずに，LBのスコアにフィットするのは危険．

なぜならLBはテストデータの少数（例: 25%)しか使っていないため．
残り75%のテストデータのスコアで競うので，25%のデータに特化してたら悲惨なのだ．

手元のCV評価をLBよりも信じるのだ．CV評価とLBが乖離してたら危ないサインかも．
でも分からないときは分からない．「Trust CV」は理想なのだ．

### k-foldについて
平均だけでなく各foldのスコアも注目
各foldのスコアがばらついていたら注意．LBとCV評価が比例しない可能性があるため．だからといって，これを解決するのは難しい...

## 最初
良さそうなカーネル（ノートブック）を改良して，CVスコアを上げられるだけ上げて，最初の提出をするのだ．
(手元でパラメータチューニングしてスコアがどれくらい上がるか見るのだ．)

それで順調に上がるなら，別モデルを試したり，アンサンブルがキーのコンペになるのだ．

しかしもし，途中でスコアが頭打ちになったり，LBと変な差が出たら，致命的な何かに気づけていない可能性があるのだ．例えば，
* 外部データ
* データに対する何らかの傾向

kaggleのために最新論文を追って実装するのはコスパ悪い．15位~20位で，超上位に入りたいときにやるものなのだ．

ビギナー勢が上位に結構いたら，何か気づかないと系の匂いがするのだ．


# 【2位入賞】ずんだもんとめたんで学ぶKaggle 入門 & 参戦記 Part 2【Petfinderコンペ】【修正版】

## kaggle コマンドの設定
``` bash
$ which pip
~/.pyenv/shims/pip
$ pip install kaggle
$ open https://www.kaggle.com/<your-username>/account
```
ページ内の API という項目に Create New API Token というボタンがあるのでそれを押す。
すると、自分用の設定ファイル (kaggle.json) がダウンロードされる。

あとはダウンロードした設定ファイルを所定の場所(~/.kaggle)において完了
``` bash
$ mkdir -p ~/.kaggle
$ mv kaggle.json ~/.kaggle
$ chmod 600 ~/.kaggle/kaggle.json
$ kaggle -v
Kaggle API 1.5.12
```
参考：[Kaggle をコマンドラインで操作する](https://blog.amedama.jp/entry/2018/05/03/031551)

## データのダウンロード
コンペティションに必要なデータのダウンロード
``` bash
$ mkdir input  # input というフォルダ名が推奨
$ cd input/
$ kaggle competitions download -c <competition-name>
# 403 - Forbidden が出力された場合，「accept the Terms and Condition」忘れの可能性あり
$ unzip -d <dataset_name>/ <dataset_name>.zip
```
実行したいノートブックに必要なデータもダウンロードするのだ．必要なデータはノートブックの\[Data\]タブをクリックして確認するのだ．

## ノートブックのダウンロード
「Copy API command」で得られたコマンドをそのまま実行すれば，ノートブックはダウンロードできるのだ．

`kaggle kernels pull <notebook>` になっているコマンドなのだ．

ノートブックのフォルダ名はinputと同じ階層に作るのだ．名前は任意でよくて，僕は「protos」か「notebook」にしているのだ．

``` bash
$ mkdir protos
$ cd protos
$ kaggle kernels pull <notebook>
```
## フォルダ・ファイル名にハイフン「-」がある場合



## 【2位入賞】ずんだもんとめたんで学ぶKaggle 入門 & 参戦記 Part 3【Petfinderコンペ】【修正版】