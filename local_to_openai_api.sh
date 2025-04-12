CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve Qwen/QwQ-32B \
  --served-model-name QwQ-32B \
  --host 0.0.0.0 \
  --port 8001 \
  --dtype auto \
  --max_num_seqs 256 \
  --max_num_batched_tokens 1024 \
  --tensor-parallel-size 4
