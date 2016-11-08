# bluetoothctl

Author: Richard Jay Tea
Email: richardjaytea@gmail.com

Implemented the wrapper from Egor Fedorov from ReachView and the pexpect package to allow a Raspberry Pi to stream audio from a connected bluetooth device and it's auxiliary port.

The Pi was designed to scan for MAC addresses of bluetooth devices and save the current desired address in a save file. It is then able to connect to saved addresses and transfer audio from the bluetooth device to the auxiliary of the Pi.

Pexpect bluetoothctl wrapper by Egor Fedorov: 
https://gist.github.com/egorf/66d88056a9d703928f93
