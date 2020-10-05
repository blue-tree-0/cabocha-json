import json
import CaboCha
from pathlib import Path


class CabochaJSON:
    def __init__(self, option="-f1 -n1"):
        super().__init__()
        self.option = option
        self.cabocha = CaboCha.Parser(self.option)
        self.token_feature_name_list = [
            "pos",
            "pos1",
            "pos2",
            "pos3",
            "conjugated_type",
            "conjugated_form",
            "base",
            "reading",
            "pronunciation",
        ]

    def parse(self, sentence):
        result = {}
        tree = self.cabocha.parse(sentence)
        chunk_idx = -1
        for token_idx in range(tree.token_size()):
            token = tree.token(token_idx)
            chunk = token.chunk
            if chunk is not None:
                chunk_surface = "".join(
                    [
                        tree.token(ti).surface
                        for ti in range(
                            chunk.token_pos, chunk.token_pos + chunk.token_size
                        )
                    ]
                )
                chunk_idx += 1
                result[str(chunk_idx)] = {}
                result[str(chunk_idx)]["chunk"] = chunk_surface
                result[str(chunk_idx)]["link"] = str(chunk.link)
                result[str(chunk_idx)]["token"] = {}

            token_feature_list = [
                token.feature_list(fi)
                for fi in range(len(self.token_feature_name_list))
            ]
            result[str(chunk_idx)]["token"][token.surface] = dict(
                zip(self.token_feature_name_list, token_feature_list)
            )
            result[str(chunk_idx)]["token"][token.surface]["ner"] = token.ne

        return result

    def parse_save(self, sentence, file="output.json"):
        result = self.parse(sentence)

        output = {"sentence": sentence, "result": result}

        if Path(file).suffix != ".json":
            file += ".json"

        with open(file, "w") as f:
            json.dump(output, f, indent=4, ensure_ascii=False)
