# List of packages and resources used or to be used.

## Packages

- Setup [Sourcery](https://docs.sourcery.ai/Guides/Code-Reviews/) automate code quality
- LangChain has build in [Cache](https://python.langchain.com/en/latest/modules/models/llms/examples/llm_caching.html) and Advanced Caching with [GPTCache](https://github.com/zilliztech/GPTCache)
- [Async LLM calls](https://python.langchain.com/en/latest/modules/models/llms/examples/async_llm.html)
- Use [Fake LLM Wrapper](https://python.langchain.com/en/latest/modules/models/llms/examples/fake_llm.html) for unit tests.
- Read [LLM config from YAML file](https://python.langchain.com/en/latest/modules/models/llms/examples/llm_serialization.html)
- [Stream response](https://python.langchain.com/en/latest/modules/models/llms/examples/streaming_llm.html)
- [Question Answering](https://docs.langchain.com/docs/use-cases/qa-docs) needed to work with existing code
- [Extraction](https://docs.langchain.com/docs/use-cases/extraction) via a schema and PrompTemplate

## Questions
- How to do loops in LangChain?


## Interesting tool
- [Fly](https://fly.io/) used to deploy apps all other the world used [here](https://github.com/sullivan-sean/chat-langchainjs)
- [Tox](https://github.com/tox-dev/tox) used to run tests in multiple environments, used in https://github.com/AstraZeneca/magnus-core/blob/main/tox.ini Also consider [Nox](https://nox.thea.codes/en/stable/) used in  https://github.com/pyca/cryptography/blob/main/noxfile.py
- [Pre-commit]()https://pre-commit.com/) used to run checks before commiting, used in https://github.com/bokeh/bokeh/blob/branch-3.2/.pre-commit-config.yaml
- [Mega linter](https://github.com/oxsecurity/megalinter)
- [DVC](https://github.com/iterative/dvc)
- [Great Expectations](https://github.com/great-expectations/great_expectations) Always know what to expect from your data.
