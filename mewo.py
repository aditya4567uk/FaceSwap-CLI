print("hello i am dev")
print("\n # NOTE YOU ARE GETTING `MODEL NOT FOUND .ONNX` OR SIMILAR ERRORS, THEN IT MEANS SOME MODELS ARE NOT DOWNLOADED, THEN COPY THE NAME OF MODEL WHICH IS NOT FOUND SEACH THE EXACT NAME ON HUGGINGFACE AND DOWNLOAD THOSE ONNX MODEL AND PLACE IT TO -> `C:\Users\<YOUR USERNAME>\miniconda3\envs\myenv\Lib\site-packages\.assets\models` \n")
from facefusionlib import swapper
from facefusionlib.swapper import DeviceProvider

input_path = "ash.png"  # The face you want to swap
target_path = "tmh.jpg"  # The pic where you want the input face to be swapped

result = swapper.swap_face(
    source_paths=[input_path],
    target_path=target_path,
    provider=DeviceProvider.GPU,  # Change it to DeviceProvider.CPU if you don't have CUDA/ROCm/MTX Driver
    detector_score=0.65,
    mask_blur=0.7,
    skip_nsfw=False,
    landmarker_score=0.5,
)
print(type(result))
print("The path of swapped image is :", result)  # SUBSCRIBE :)

