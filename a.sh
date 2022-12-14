# https://cocoinit23.com/docker-gpu-error-response-from-daemon-linux-runtime-spec-devices-could-not-select-device-driver-with-capabilities-gpu/
# docker container run –gpus all をした時のエラー解消用スクリプト


curl -s -L https://nvidia.github.io/nvidia-container-runtime/gpgkey | \
  sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list
sudo apt update
sudo apt install nvidia-container-runtime
service docker restart