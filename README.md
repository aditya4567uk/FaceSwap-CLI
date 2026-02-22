# FaceSwap-CLI
Light weight CLI code for faceswap

# Installation

<ul>
<li>Step 1 -  Create conda / venv (Python version 3.11) and activate it</li>
<li>Step 2 - Install facefusion - `pip install facefusionlib` (For CPU) | `pip install facefusionlib[gpu]` (For GPU)</li>
<li>Step 3 - Install ONNXRuntime (CPU)- `pip install onnxruntime` | Install ONNXRuntime (GPU) [If you have CUDA-CuDNN installed] - `pip install onnxruntime-gpu`</li>
<li>Step 4 - Clone(Download this project) this repo to your local system</li>
<li>Step 5 - Change `provider=DeviceProvider.GPU` to `provider=DeviceProvider.CPU` , if you don't have CUDA Installed</li>
<li>Step 6 - Run `python mewo.py` to get results</li>
</ul>

# END
