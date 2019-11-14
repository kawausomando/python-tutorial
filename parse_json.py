import json
x = [1, 'kawasuo', 'list']

print(json.dumps(x))
# [1, "kawasuo", "list"]

with open('sample.json', 'w') as f:
    # sample.jsonへ書き込み
    json.dump(x, f)

with open('sample.json', 'r') as f:
    # sample.jsonから読み込み
    print(json.load(f))
    # [1, "kawasuo", "list"]
