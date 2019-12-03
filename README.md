# text_gen
generate text in various ways


## マルコフ連鎖
### markov_chain.py
#### 使い方
※日本語の形態素解析エンジンのMeCabのインストールが必要です。

```Python
from markov_chain import MarkovChain

text = 'なるべく長い日本語の文章。'
markov = MarkovChain(order=2)
markov.make_model(text)
print(markov.make_sentence())
```

- class __MarkovChain__(order=2)  
 N階マルコフ連鎖で文章生成を行うクラスです。  
 - order \[int\]  
  N階マルコフ連鎖のNにあたります。指定した値の分だけ単語を使用し、次の単語を確率に従って選択します。
  デフォルト値は２です。

- method MarkovChain.__make_model__(text)    
　N階マルコフ連鎖を利用したモデルを生成します。  
　戻り値は無く、インスタンス変数のMarkovChain.modelを作成します。  
　複数回呼び出された時はMarkovChain.modelに追記します。  
　- text \[str\]  
　 モデルの元になる文章です。文が句点「。」で区切れれていない場合、うまく動作しないことがあります。  

- method MarkovChain.__make_sentence__(sentence_num=5, seed="\[BOS\]", max_words = 1000)  
  作成したモデルを元に文章を生成します。MarkovChain.make_modelを先に呼び出していない場合、失敗します。  
  - sentence_num \[int\]  
   作成する文の数です。指定された値と同じ数の句点「。」が出現した時点で文章生成を終了します。  
   デフォルト値は５です。  
  - seed \[str\]  
   最初の単語を指定できます。モデル作成に使用した文章内に指定した単語が含まれていない場合、文章生成に失敗します。  
   デフォルト値は"\[BOS\]"です。  
  - max_words \[int\]  
   生成する文章の最大単語数です。指定した値と同じ数の単語が選ばれた時点で文章生成を終了します。  
   sentence_numの終了条件より優先されます。  
   デフォルト値は1000です。   
