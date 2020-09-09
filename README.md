# Cabocha-json
Cabochaの出力結果をjsonファイルに保存

入力文: 太郎は花子が読んでいる本を次郎に渡した。

``````
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
``````
