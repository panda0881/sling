import json
import subprocess

test_sentences = ['I love you', "It's so difficult to use Sling."]
result = list()
for test_sentence in test_sentences:
    command = "bazel-bin/nlp/parser/tools/parse --logtostderr    --parser=sempar.flow --text=" + test_sentence + " --indent=2"
    tmp_out = subprocess.check_output(command)
    current_result = json.loads(tmp_out)
    result.append(current_result)

with open('parsed_result.json', 'w') as f:
    json.dump(result, f)

print('end')
