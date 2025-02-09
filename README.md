Build Process:
1. Start pi with qnx
2. Get wifi working on it
3. ping qnxpi.local -> check if you can ssh into it
4. make a build directory under qnxuser (after sshing into qnxuser)
5. Mount rpi build directory :
   user@system:~/documents/qnx/QNX_CAR/c_target$ sudo sshfs -o allow_other,default_permissions qnxuser@qnxpi.local:build .
6. source qnxsdp-env.sh
7. build files in c_host using ./build.sh file.cpp (This goes into the c_target directory which is the mounted filesystem)
8. Run files on rpi.  

Note (You will need a header file called rpi_gpio.h to compile these files)
