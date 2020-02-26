umount /dev/shm && mount -t tmpfs shm /dev/shm

# using local electron module instead of the global electron lets you
# easily control specific version dependency between your app and electron itself.
# the syntax below starts an X istance with ONLY our electronJS fired up,
# it saves you a LOT of resources avoiding full-desktops envs

rm /tmp/.X0-lock &>/dev/null || true

if [ ! -c /dev/fb1 ] && [ "$TFT" = "1" ]; then
  modprobe spi-bcm2708 || true
  modprobe fbtft_device name=pitft verbose=0 rotate=${TFT_ROTATE:-0} || true
  sleep 1
  mknod /dev/fb1 c $(cat /sys/class/graphics/fb1/dev | tr ':' ' ') || true
  python3 new_video.py
  #FRAMEBUFFER=/dev/fb1 startx /usr/src/app/node_modules/electron/dist/electron /usr/src/app --enable-logging
else
  python3 new_video.py
  startx new_video.py --enable-logging
fi
