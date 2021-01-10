# ロボットシステム学課題２
##  概要
講義で作成したノードを改造し、ミニゲームを製作しました。
##  動作環境
- Ubuntu 20.04 LTS
- ROS version noetic
##  使用した道具
- Raspberry Pi 4
##  実行動画
<https://youtu.be/tOdbqqPCZ0U>
##  インストール方法
インストールは以下の手順で行ってください。
```
cd ~/catkin_ws/src
git clone https://github.com/Isamu-Nakajima/mypkg.git
cd ..
catkin_make
```
##  使用方法
あらかじめ別ターミナルで
```
roscore
```
を実行した上で
```
roslaunch mypkg mypkg.launch
```
を実行してください。以降はプログラムに従ってください。
##  ライセンス
BSD 3-Clause License
