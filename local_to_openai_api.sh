CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 vllm serve Qwen/QwQ-32B \
  --served-model-name QwQ-32B \
  --host 0.0.0.0 \
  --port 8001 \
  --dtype auto \
  --tensor-parallel-size 8