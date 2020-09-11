import json
import CaboCha
from pathlib import Path


class CabochaJSON:
    def __init__(self):
        super().__init__()
        self.cabocha = CaboCha.Parser("-f1 -n1")

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

            result[str(chunk_idx)]["token"][token.surface] = {
                "pos": token.feature_list(0),
                "pos1": token.feature_list(1),
                "pos2": token.feature_list(2),
                "pos3": token.feature_list(3),
                "conjugated_type": token.feature_list(4),
                "conjugated_form": token.feature_list(5),
                "base": token.feature_list(6),
                "reading": token.feature_list(7),
                "pronunciation": token.feature_list(8),
                "ner": token.ne,
            }

        return result

    def parse_save(self, sentence, file="output.json"):
        result = self.parse(sentence)

        output = {"sentence": sentence, "result": result}

        if Path(file).suffix != ".json":
            file += ".json"

        with open(file, "w") as f:
            json.dump(output, f, indent=4, ensure_ascii=False)
