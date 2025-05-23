# coding=utf-8
# Copyright (c) 2019, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Model parallel utility interface."""

from .cross_entropy import vocab_parallel_cross_entropy

from .data import broadcast_data

from .initialize import destroy_model_parallel
from .initialize import get_data_parallel_group
from .initialize import get_data_parallel_rank
from .initialize import get_data_parallel_world_size
from .initialize import get_model_parallel_group
from .initialize import get_model_parallel_rank
from .initialize import get_model_parallel_src_rank
from .initialize import get_model_parallel_world_size
from .initialize import initialize_model_parallel
from .initialize import model_parallel_is_initialized

from .layers import ColumnParallelLinear
from .layers import RowParallelLinear
from .layers import VocabParallelEmbedding

from .mappings import copy_to_model_parallel_region
from .mappings import gather_from_model_parallel_region
from .mappings import reduce_from_model_parallel_region
from .mappings import scatter_to_model_parallel_region

from .operation import mp_split_model, mp_split_model_rank0, mp_split_model_receive

try:
    import torch
    assert torch.cuda.is_available() # or set get_cuda_rng_tracker to None
    #from deepspeed.runtime.activation_checkpointing.checkpointing import checkpoint, get_cuda_rng_tracker, model_parallel_cuda_manual_seed
    from deepspeed.runtime.activation_checkpointing.checkpointing import get_cuda_rng_tracker, model_parallel_cuda_manual_seed
    from torch.utils.checkpoint import checkpoint
except Exception as e:
    from sat.helpers import print_rank0
    print_rank0(str(e), level="DEBUG")
    print_rank0("DeepSpeed/CUDA is not installed, fallback to Pytorch checkpointing.", level="INFO")
    from torch.utils.checkpoint import checkpoint
    get_cuda_rng_tracker = None
    model_parallel_cuda_manual_seed = lambda x: None
