To run ci tests, you can use `source ci.sh` from the parent `civ-weave` directory.
This runs all CI using a GH action emulator called [Act](https://github.com/nektos/act).
To run individual steps of ci, you should use the poetry dev shell and running the required step (for example ruff).

### Tech that might be helpful
- FastUI: [FastUI](https://github.com/samuelcolvin/FastUI/) is a python framework for building user facing UIs. A demo is [here](https://fastui-demo.onrender.com/).
- Fooocus: [Foocus](https://github.com/lllyasviel/Fooocus) is an open source image generation software.
- Modal: [Modal](https://modal.com/) is a low setup service for running ai models in the cloud. Likely a candidate if Civ Weave used it's own models / non OpenAI models for generative workloads.
