# Cabocha-json
Cabochaの出力結果をjsonファイルで保存

## インストール
事前に[cabocha](https://taku910.github.io/cabocha/)の環境構築が必要です．
```
pip install git+https://github.com/blue-tree-0/cabocha-json
```


## 使い方

### コード
```
from cabocha_json import CabochaJSON

sentence = "太郎は花子が読んでいる本を次郎に渡した。"
cabocha = CabochaJSON()

# cabochaの出力結果を辞書型で出力
result = cabocha.parse(sentence)

# cabochaの出力結果をoutput.jsonに保存
cabocha.parse_save(sentence, "output.json")
```

###  output.json
```
{
    "sentence": "太郎は花子が読んでいる本を次郎に渡した。",
    "result": {
        "0": {
            "chunk": "太郎は",
            "link": "5",
            "token": {
                "太郎": {
                    "pos": "名詞",
                    "pos1": "固有名詞",
                    "pos2": "人名",
                    "pos3": "名",
                    "conjugated_type": "*",
                    "conjugated_form": "*",
                    "base": "太郎",
                    "reading": "タロウ",
                    "pronunciation": "タロー",
                    "ner": "B-PERSON"
                },
                "は": {
                    "pos": "助詞",
                    "pos1": "係助詞",
                    "pos2": "*",
                    "pos3": "*",
                    "conjugated_type": "*",
                    "conjugated_form": "*",
                    "base": "は",
                    "reading": "ハ",
                    "pronunciation": "ワ",
                    "ner": "O"
                }
            }
        },
        ...
    }
}
```
