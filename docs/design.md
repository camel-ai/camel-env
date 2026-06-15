# Core design of the camel-env environment as service


## Design

The design is aimed to decouple the environment from training framework. 

An environment is defined as a triplet, i.e., (instruction, sandboxes, verification/[reward_fn])

### Aim:

    1. Serves as middleman between training framework and various datasets of environments.

    2. Customizable agents, reward_fn and sandboxes

    3. All configurable via yaml.

    4. Unified trainnig and evaluation.

    5. Environment as service. 

    6. Co-evolve repo and AI tool i.e., claude/ codex, agnostic to specific tools.


### Architecture

