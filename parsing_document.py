import json
import subprocess

test_sentences = ['test', 'I love you', "It's so difficult to use Sling."]
result = list()
for test_sentence in test_sentences:
    command = 'bazel-bin/nlp/parser/tools/parse --logtostderr --parser=sempar.flow --text="' + test_sentence + '" --indent=2'
    print('current command:', command)
    tmp_out = subprocess.check_output([command], shell=True)
    print(tmp_out.decode('utf-8'))
    # tmp_output = tmp_out.stdout.decode('utf-8')
    # print('current output', tmp_output)
    print('tmp_out:', tmp_out)
    tmp_output = tmp_out.decode('utf-8').replace('\n', '')
    print('tmp_output:', tmp_output)
    current_result = json.loads(tmp_output)
    result.append(current_result)

with open('parsed_result.json', 'w') as f:
    json.dump(result, f)

print('end')
