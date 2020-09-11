from cabocha_json import CabochaJSON


# 形態素解析
def get_token(result):
    token = []
    for idx in result.keys():
        token.extend(list(result[idx]["token"].keys()))

    return token


# 文節解析
def get_chunk(result):
    chunk = []
    for idx in result.keys():
        chunk.append(result[idx]["chunk"])

    return chunk


# 係り受け解析
def get_dependency(result):
    dependency = []
    for idx in result.keys():
        link_idx = result[idx]["link"]
        if link_idx == "-1":
            continue
        source = result[idx]["chunk"]
        link = result[link_idx]["chunk"]
        dependency.append((source, link))

    return dependency


# トリプル抽出
def get_triple(result):
    # 文節に指定した品詞名があるか確認
    def check_pos(chunk_idx, check_name, pos):
        tokens = result[chunk_idx]["token"]
        for token in tokens.keys():
            if tokens[token][check_name] == pos:
                return True

        return False

    # 指定した助詞があるか確認
    def check_paricle(chunk_idx, pos_name):
        tokens = result[chunk_idx]["token"]
        for token in tokens.keys():
            if token == pos_name:
                return True

        return False

    triple = {"subject": None, "verb": None, "object": None}
    for idx in result.keys():
        if check_pos(idx, "pos", "名詞"):
            if check_paricle(idx, "が") or check_paricle(idx, "は"):
                triple["subject"] = result[idx]["chunk"]
                continue

            if check_paricle(idx, "を"):
                triple["object"] = result[idx]["chunk"]
                continue

        if check_pos(idx, "pos", "動詞"):
            if check_paricle(idx, "。"):
                triple["verb"] = result[idx]["chunk"]
                continue

    return triple


if __name__ == "__main__":
    sentence = "太郎は花子が読んでいる本を次郎に渡した。"
    cabocha = CabochaJSON()
    cabocha.parse_save(sentence, "output.json")

    result = cabocha.parse(sentence)

    print(f"入力文:\n{sentence}")
    print(f"形態素解析:\n{get_token(result)}")
    print(f"文節解析:\n{get_chunk(result)}")
    print(f"係り受け解析\n{get_dependency(result)}")
    print(f"トリプル抽出\n{get_triple(result)}")
