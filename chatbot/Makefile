create project:
	rasa init --no-prompt

train nlu:
	rasa train nlu

train core:
	rasa train

interactive:
	rasa interactive	

talk to the assistant on the command line:
	rasa shell

start action server:
	rasa run actions --debug

start rasa server:
	rasa run -m models --enable-api --cors "*" --endpoints endpoints.yml --debug
test intent cross_validation:
	rasa test nlu -u data/nlu.md --config config.yml --cross-validation
	
Evaluating a Core Model:
	rasa test core --stories test_stories.md --out results

Comparing NLU Pipelines:

rasa test nlu --config pretrained_embeddings_spacy.yml supervised_embeddings.yml
  --nlu data/nlu.md --runs 3 --percentages 0 25 50 70 90

