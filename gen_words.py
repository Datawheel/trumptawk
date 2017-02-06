# coding: utf-8
import os
import json
tmp = [{"word": x.split(".mp4")[0]} for x in os.listdir('words') if ".mp4" in x]
output_str = "var words = {};".format(json.dumps(tmp))
with open("words.js", "w") as f:
    f.write(output_str)
