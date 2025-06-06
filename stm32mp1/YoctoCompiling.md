#### Forked from: https://github.com/darkquesh/stm32mp1
# Development on STM32MP157A-DK1 board  
# How to Use Yocto Project to Create a Custom Linux Image

### STM32MP157A-DK1 Development Kit - Yocto kirkstone
#### September 2022  


# Creating a Custom Linux Image

### Tutorials

- https://www.youtube.com/playlist?list=PLEBQazB0HUyTpoJoZecRK6PpDG31Y7RPB
- https://www.digikey.com/en/maker/projects/intro-to-embedded-linux-part-2-yocto-project/2c08a1ad09d74f20b9844e566d332da
- https://www.cocoacrumbs.com/blog/2021-10-15-building-a-linux-distro-for-the-stm32mp157a-dk1/
- https://bootlin.com/blog/building-a-linux-system-for-the-stm32mp1-basic-system/

### Required Hardware

- STM32MP157A-DK1 Development Kit
- USB-C to USB-A power cable
- Micro USB to USB-A cable for connecting to the board via terminal
- A minimum of 8 GB SD card
- At least 4 GB of RAM on your host PC

### Required Software

#### Tried and Tested to WSL2 Environment (Note: Limitation of swap storage can be changed in .wslconfig file usually in C:\Users\<name>\.wslconfig)

You will need Linux for this project, as all of the tools we are using must be run in Linux. How-
ever, the steps shown below are tested in Ubuntu 20.04 using dual-boot. While you can set up a
virtual Linux machine (e.g. Oracle VM VirtualBox) to build a Linux image, it would take way
longer time than installing Ubuntu natively on your PC. You may follow the tutorials given be-
low for installing Ubuntu on a virtual machine or alongside another OS (like Windows).

Dual-boot (_recommended_): https://www.tecmint.com/install-ubuntu-alongside-with-windows-dual-boot

Virtualbox: https://itsfoss.com/install-linux-in-virtualbox

Also, you should allocate more than 70 GB disk space to download and build source files


### 1.1 Install Dependencies

Boot into Ubuntu on your host computer and run the following commands.

```
sudo apt update
sudo apt upgrade
sudo apt install -y bc build-essential chrpath cpio diffstat gawk git texinfo
wget gdisk python3 python3-pip gedit nano
sudo apt install -y libssl-dev
```
Because the Yocto Project tools rely on the "python" command, you will likely need to alias
"python" to "python3". Edit your .bashrc file:

```
gedit ~/.bashrc
```
Scroll to the bottom and add the following to a new line

```
alias python=python3
```
Save and exit (’esc’ followed by entering ":wq"). Re-run the .bashrc script to update your shell:

```
source ~/.bashrc
```
### 1.2 Download Layers

Download the Yocto Project poky reference distribution:

```
mkdir -p ~/Projects/yocto
cd ~/Projects/yocto
git clone https://git.yoctoproject.org/poky.git
cd poky
```
You will want your poky layer branch to match the branches of all other third-party layers you
download (such as the STM32MP1 BSP). You can view the available poky release names here:
https://wiki.yoctoproject.org/wiki/Releases. We are going to have all layers be on the "kirk-stone" branch.

```
git checkout kirkstone
```
Next, you will want to download the STM32MP board support package (BSP) as a separate
layer:


```
cd ~/Projects/yocto
git clone https://github.com/STMicroelectronics/meta-st-stm32mp
cd meta-st-stm32mp
git checkout kirkstone
```
View the readme to see what other layers are needed for this particular BSP:

```
less README
```
In there, you can see that we need the meta-openembedded layer. Specifically, we need the meta-oe and meta-python layers in the meta-openembedded layer. Also, install any dependencies mentioned in that file.

```
cd ~/Projects/yocto
git clone https://github.com/openembedded/meta-openembedded.git
cd meta-openembedded
git checkout kirkstone
```
### 1.3 Configure Build

To start using bitbake you need to source the "oe-init-build-env" script located into poky/ directory. So you should do something like thiseverytime using bitbake:

```
cd ~/Projects/yocto
source poky/oe-init-build-env build-mp1
```
You can view the layers that will be included in the build with the following:

```
bitbake-layers show-layers
```
You should only have the default poky layers to start. We need to edit bblayers.conf in our build to add the necessary STM32MP BSP and dependency layers:

```
gedit conf/bblayers.conf
```

Update the BBLAYERS variable to be the following (change <username> to your actual user-name):

```
BBLAYERS ?= " \
/home/<username>/Projects/yocto/poky/meta \
/home/<username>/Projects/yocto/poky/meta-poky \
/home/<username>/Projects/yocto/poky/meta-yocto-bsp \
/home/<username>/Projects/yocto/meta-openembedded/meta-oe \
/home/<username>/Projects/yocto/meta-openembedded/meta-python \
/home/<username>/Projects/yocto/meta-st-stm32mp \
"
```
Save and exit. Check the layers again with:

```
bitbake-layers show-layers
```
You can view the available machine names and settings in∼ _/Projects/yocto/meta-st-stm32mp/conf/machine_. We will use "stm32mp1" for our build. To do this, edit local.conf:

```
gedit conf/local.conf
```
Change the MACHINE variable to the following (comment out the "qemu" emulator and add "stm32mp1" as the machine):

```
#MACHINE ??= “qemux86-64”
MACHINE = “stm32mp1”
```
  
### 1.4 Configure Kernel

Now that your build system is set up, you can make changes to the kernel. To do that, enter:

```
bitbake -c menuconfig virtual/kernel
```
Note that the first time you run bitbake for a particular build, it will take some time parsing all the required metadata. This could take 15 minutes or more, depending on your host computer, so be patient. After it finishes, you should be presented with a menu.
  
![virtual_kernel_menuconfig](https://user-images.githubusercontent.com/56772428/210803513-627ec975-6ef5-47b2-8b78-0e8b14f73f58.jpeg)

  
You can change various kernel settings. However, we will leave everything at their defaults for now, so just select Exit and press ’enter’.

To make kernel changes permanent whenever you modify the kernel, you should run:

```
bitbake -c savedefconfig virtual/kernel
```
     
### 1.5 Build Image

Now, it is time to actually build your image! We need to choose an image to build from various images that are supported by the default poky installation here:https://docs.yoctoproject.org/ref-manual/images.html  
For now, we won’t need any extra packages, so we’ll skip adding the OpenSTLinux layer and just focus on the bare minimum, which is provided by the core-image-minimal image. Once you have everything configured to your liking, just run the following command:

```
bitbake core-image-weston
```
The first time you build an image with bitbake, it will likely take many hours (the first build might take around 2-3 hours). One big advantage of the Yocto Project is that it builds everything in stages and layers. If you make any changes (e.g. add a layer, change to a different image, tweak kernel settings), subsequent builds will take far less time. This speeds up development process when you are trying to add low-level support in Linux.

If you want to start over (e.g. you press ’ctrl + c’ or something gets corrupted/tainted)

```
bitbake -c cleanall core-image-weston
```
To clean out everything

```
rm -rf tmp
```
Once building is complete without any errors, you can find all of the output images in the deploy folder:

```
ls tmp/deploy/images/stm32mp
```

# Final Image for SD Card

### 2.1 Creating the Final Image

Finally, we can begin deploying the final image and flash it to an SD card for booting the system. In most cases, booting into Linux requires several bootloader programs to run in sequence. This is known as a "boot chain" or "boot sequence". For embedded Linux, this process will often look something like this:

ROM > First Stage Bootloader (FSBL) > Second Stage Bootloader (SSBL) > Kernel

While it is possible to format partitions manually, there is a script that does it automatically. First, stand in the following directory:

```
cd ~/Projects/yocto/build-mp1/tmp/deploy/images/stm32mp1/scripts
```
A _create_sdcard_from_flashlayout.sh_ script can be found in that folder. Let us choose _FlashLayout_sdcard_stm32mp157a-dk1-extensible.tsv_ to create the image by executing this command line:

```
./create_sdcard_from_flashlayout.sh ../flashlayout_core-image-minimal/extensible/FlashLayout_sdcard_stm32mp157a-dk1-extensible.tsv
```
   
### 2.2 Flashing the Image to SD Card

ST recommends using their STM32CubeProgrammer to flash the SD card. However, we will do things manually so you can get an idea of how to configure an SD card with the various image files.

Navigate to the output directory for your images:

```
cd ~/Projects/yocto/build-mp1/tmp/deploy/images/stm32mp
```
From here, you can figure out which image files ST would use to flash an SD card by looking at the flashlayout_core-image-minimal/trusted/FlashLayout_sdcard_stm32mp157a-dk1-trusted.tsv file in a text editor.

```
gedit flashlayout_core-image-minimal/trusted/FlashLayout_sdcard_stm32mp157a-dk1-trusted.tsv
```  
   
  ![flash_partitions](https://user-images.githubusercontent.com/56772428/210804263-d1e07e10-f960-4431-8c37-66f9bdf30e8d.jpeg)
  
This will show you the name of the image files to use for the FSBL, metadata, SSBL, bootfs, vendorfs, rootfs and userfs.

To flash the final image, plug your SD card into your host computer and check where it is mounted. We can use `sudo fdisk -l` or `lsblk` command for that.

In my case, the SD card is mounted at/dev/mmcblk0.

Make sure to unmount any partitions that were automounted when you plugged in the SD card. (Using sudo umount /dev/mmcblk0 or through GUI like gparted or file system).
As we will be writing to the SD card, any previous data and partitions should be formatted. To do that run this line:

```
sudo fdisk /dev/mmcblk0
```
  
   ![fdisk_partitions](https://user-images.githubusercontent.com/56772428/210804362-575f914b-c791-4715-bba4-45dfa29ae90e.jpeg)

   
In fdisk, perform the following actions:


- ’p’ to view the partitions
- ’d’ to delete a partition
    **-** Select one of the partitions
    **-** Repeat this process until all partitions have been deleted
- If your SD card is not a GPT layout, you will need to change it to GPT.
    **-** Type ’p’ and look at "Disklabel type." It should say "gpt"
    **-** ’g’ to change the layout to GPT
- ’w’ to write changes to the SD card and exit

You can confirm that the changes were made by entering the `lsblk` command again.

Now we can flash the SD card:

```
sudo dd if =../flashlayout_core-image-minimal/extensible/../../FlashLayout_sdcard_stm32mp157a-dk1-extensible.raw of=/dev/mmcblk0 bs=8M conv=fdatasync status=progress oflag=direct
```
   
   ![partitions_script](https://user-images.githubusercontent.com/56772428/210804435-2c17f96e-ec67-4cf3-a7e0-8f4d26922a5d.jpeg)


# Testing the Image

### 3.1 Boot into Linux

Plug the SD card into the STM32MP157A-DK1 board. Connect a USB micro cable from your host computer to the ST-LINK (CN11) port on the board. On your host computer, enter the
following:

```
sudo apt install picocom
sudo picocom -b 115200 /dev/ttyACM1
```
`/ttyACM1` part might be different on your host PC, so you could also try `/ttyACM0`. If you wish to exit picocom, press [Ctrl][A] followed by [Ctrl][X].

If everything went well, you should see the FSBL (TF-A) post a few lines to the console followed by the SSBL (U-Boot). U-Boot will launch the kernel, and after a few seconds, you should be presented with a login prompt. Enter "root" (no password) to gain access to Linux.
  
   ![picocom](https://user-images.githubusercontent.com/56772428/210804509-26b23067-5228-4e57-91a2-7ede521da66a.png)


## Adding Build Tools

The core-image-minimal system is installed with minimal packages, as suggested by its name. Although it does not have any basic tools such as apt, gcc or nano package; we can add them by configuring our build.

First, navigate to this directory and edit _local.conf_ :

```
cd ~/Projects/yocto/build-mp1/conf
gedit local.conf
```
   
   ![local conf-add-build](https://user-images.githubusercontent.com/56772428/210804621-232d4386-0872-4b42-9a04-8e009453bb70.jpeg)

  
Add the following lines:

```
IMAGE_INSTALL:append = " packagegroup-core-buildessential"
IMAGE_INSTALL:append = " nano"
IMAGE_INSTALL:append = " apt"
IMAGE_INSTALL:append = " i2c-tools"
IMAGE_INSTALL:append = " libgpiod libgpiod-dev libgpiod-tools"
```
The first line will append the typical GCC build tools. The second line will add the Nano editor (in case you prefer not to work with the VI editor that is part of the minimal Linux system).

Also, pay attention to syntax changes in newer versions while changing build configurations: https://docs.yoctoproject.org/next/migration-guides/migration-3.4.html

Now rebuild the Linux system and flash it to an SD Card (you can follow 1.5 and 2.1). If all went well, you can now use GCC and the Nano editor natively on your stm32mp157a-dk1 board.


# Creating Custom Layer and Image

Until now, we built our Linux image, flashed it onto an SD card and boot into Linux on the stm32mp157a-dk1 board. In this chapter, we will walk through the process of creating your own layer in the Yocto project and using it to make changes to the Linux image. Specifically, we will expand the rootfs size (to give you more space for modules, packages, and applications).

### 5.1 Default Image Recipes

The poky reference distribution comes with a main image recipe that is used during the bitbake build process in order to construct the Linux image. Up until now, we have been working with core-image-minimal as our target image. core-image-minimal inherits the core-image class recipe, which can be found here

```
cd ~/Projects/yocto/poky/meta
gedit classes/core-image.bbclass
```
Note that it is a class recipe (.bbclass), which acts as a template for other recipes to import (or "inherit"). It assigns various packagegroups to _IMAGE_INSTALL_ , which is an important variable used to tell bitbake what things to include in our image (e.g. what modules and packages to include).  
Look at the core-image-minimal recipe to see what was being included in our previous builds:

```
gedit recipes-core/images/core-image-minimal.bb
```
  
   ![bbclass1](https://user-images.githubusercontent.com/56772428/210804790-999b2816-eb39-480a-9191-0c9a860de8d3.jpeg)
  
   
### 5.2 Create Custom Layer

One of the main advantages of the Yocto Project is its ability to pull in source material from a variety of places (git repositories, websites, local files, etc.). Most of this is accomplished by keeping files (e.g. metadata, recipes) in "layers." We previously downloaded the poky and meta-st-stm32mp board support package (BSP) layers.

By creating your own layer, you can easily keep it under version control (e.g. git) so that you can easily configure custom images for future builds. This is especially important if you are creating a product and want to reproduce the full image at any time during production. All you need to do is create a build directory, include your layer (along with other required layers, such as poky and the BSP), and call "bitbake <name-of-image>".  

Start by enabling the OpenEmbedded build environment again:

```
cd ~/Projects/yocto
source poky/oe-init-build-env build-mp1
```
Then, create a custom layer that sits at the same directory level as our other layers:

```
cd ~/Projects/yocto
bitbake-layers create-layer meta-custom
```
The "bitbake-layers" tool automatically constructs the appropriate directory structure for our layer and gives us an example recipe in `../meta-custom/recipes-example/example/example_0.1.bb`. Feel free to open and look at that example.

### 5.3 Create Custom Image

Instead of using core-image-minimal, we are going to write a recipe that builds a custom image.  
Start by creating the following directory structure:

```
cd meta-custom
mkdir -p recipes-core/images
```
Then, we shall copy the core-image-minimal.bb recipe to use a starting point for our custom recipe:

```
cp ../poky/meta/recipes-core/images/core-image-minimal.bb
recipes-core/images/custom-image.bb
gedit recipes-core/images/custom-image.bb
```
You may change the custom recipe to add a user and password; but we will leave it as it is for now.


### 5.4 Add Layer to Build Process

We need to add our custom layer to the build process. Do that with the following:

```
cd ../build-mp1/
gedit conf/bblayers.conf
```
Add "/home/<username>/Projects/yocto/meta-custom \" to the BBLAYERS variable.
  
   ![custom-layer1](https://user-images.githubusercontent.com/56772428/210804908-446334a7-c1b2-4a79-9fa7-69b87c5777bc.jpeg)
  
Next, we are going to include some features to our custom image.

```
cd ../build-mp1/
gedit conf/local.conf
```
  
   ![extra_image_features](https://user-images.githubusercontent.com/56772428/210805012-3cde2e21-767a-42e7-b1fa-167fb18df6bd.jpeg)
   
Make sure that _debug-tweaks_ is enabled and append this line to the configuration file:

`EXTRA_IMAGE_FEATURES += "hwcodecs tools-sdk tools-debug splash ssh-server-openssh
package-management"`

You can view the IMAGE_FEATURES variable with the following command:
  
   ![image_features](https://user-images.githubusercontent.com/56772428/210805075-5cb1e491-45e5-4599-b172-abf69c2759ee.jpeg)
  
Moreover, you can check out other image features here:https://docs.yoctoproject.org/ref-manual/features.html?highlight=extra_image_features.


# Device Tree Patches

If you look at the [datasheet for the STM32MP157D-DK1 development board](https://www.st.com/resource/en/user_manual/um2637-discovery-kits-with-increasedfrequency-800-mhz-stm32mp157-mpus-stmicroelectronics.pdf), you can see that there are 6 I2C busses available. By default I2C ports 1 and 4 are enabled and used to control other components on the board. We want to enable port 5 (as it is broken out to the Raspberry Pi-style header on the board) and use it to communicate with a temperature sensor. SDA is on top header (CN2) pin 3 and SCL is on pin 5.

   ![pinout](https://user-images.githubusercontent.com/56772428/210805368-92ff97f3-80d1-4210-91a2-31acef2a7967.jpeg)
   
If you look at the [STM32MP157 reference manual](https://www.st.com/resource/en/reference_manual/dm00327659-stm32mp157-advanced-arm-based-32-bit-mpus-stmicroelectronics.pdf), you can see that I2C port 5 is controlled by registers starting at memory address 0x40015000.
  
   ![i2c5_memory](https://user-images.githubusercontent.com/56772428/210805430-04ff75eb-41db-4f42-abf8-a651daa3bde1.jpeg)
  
### 6.1 Create Device Tree Patch

On your host computer, navigate to the build directory and copy the device tree source (.dts) file to a temporary working directory. Then, create a copy of the original. Open it to make changes. Feel free to look through this guide to learn more about device trees.

```
cd ~/Projects/yocto/build-mp1/
cp tmp/work-shared/stm32mp1/kernel-source/arch/arm/boot/dts/stm32mp157a-dk1.dts
~/Documents
cd ~/Documents
cp stm32mp157a-dk1.dts stm32mp157a-dk1.dts.orig
gedit stm32mp157a-dk1.dts
```

### 6.2 Enable I<sup>2</sup>C and FDCAN

At the bottom of the file, add the following device tree nodes in order to enable I2C5 and FD-CAN1:

```
&i2c5 {
pinctrl-names = "default", "sleep";
pinctrl-0 = <&i2c5_pins_a>;
pinctrl-1 = <&i2c5_sleep_pins_a>;
i2c-scl-rising-time-ns = <185>;
i2c-scl-falling-time-ns = <20>;
clock-frequency = <100000>;
status = "okay";
};
   
&m_can1 {
pinctrl-names = "default", "sleep";
pinctrl-0 = <&m_can1_pins_a>;
pinctrl-1 = <&m_can1_sleep_pins_a>;
status = "okay";
};
```
   
   ![device-tree-patch](https://user-images.githubusercontent.com/56772428/210805527-ede657db-4d4e-4140-a80e-999583c505cf.jpeg)
    
Save and exit. Then, create a diff patch. Note the "–no-index" argument allows us to perform `git diff` on two different files that are not part of a git repository.

```
git diff --no-index stm32mp157a-dk1.dts.orig stm32mp157a-dk1.dts > 0001-add-i2c5-userspace-dts.patch
```
However, because bitbake expects such diff files to be part of a repository, we need to make a couple of manual changes to the file so that it will be applied to the correct file (in a particular directory structure in the working area of build-mp1/tmp/). Open the file with:

```
gedit 0001-add-i2c5-userspace-dts.patch
```
Change the file header so that it points to the correct file locations:

```
--- a/arch/arm/boot/dts/stm32mp157a-dk1.dts
+++ b/arch/arm/boot/dts/stm32mp157a-dk1.dts
```
   
  ![patch_file](https://user-images.githubusercontent.com/56772428/210805625-316d400b-fa19-4234-a7f3-b429f289f9b6.jpeg)
   
### 6.3 Applying Patch to Device Tree

Enable our build environment and navigate to the custom layer we created earlier:

```
cd ~/Projects/yocto/
source poky/oe-init-build-env build-mp1/
cd ../meta-custom/
```

Create a directory structure for kernel recipes. The naming is important! The patch file must be in "linux/<machine-name>."

```
mkdir -p recipes-kernel/linux/stm32mp1/
```
Now, we copy our patch file:

```
cp ~/Documents/0001-add-i2c5-userspace-dts.patch recipes-kernel/linux/stm32mp1/
```
You can run the following to discover the name of the kernel we are working with:

```
oe-pkgdata-util lookup-recipe kernel
```
It should say "linux-stm32mp". In the linux/ directory, create a custom .bbappend file (which will be added to our main kernel recipe). Once again, the name is important! It must be "<kernel-name>_version.bbappend". We can use ’%’ as the version number to be a wildcard that matches any version of that file.

```
gedit recipes-kernel/linux/linux-stm32mp_%.bbappend
```  
   
In this file, add the following lines, which tell the kernel recipe to look in "this directory" (the directory containing this .bbappend file) and apply the patch to the kernel.

```
FILESEXTRAPATHS_prepend := "${THISDIR}:"
SRC_URI += "file://0001-add-i2c5-userspace-dts.patch"
```
  
   ![append_patch](https://user-images.githubusercontent.com/56772428/210805734-a9e79d19-1fb1-43d2-8e03-f3b52d9a7ea4.jpeg)

   
### 6.4 Enable i2cdetect and can-utils

In order to send and receive CAN data, we need the _can-utils_ package. First, navigate to the following directory:

```
cd ~/Projects/yocto/build-mp1/conf
gedit local.conf
```
Then, append these lines to the end of the file:


```
IMAGE_INSTALL:append = " can-utils"
IMAGE_INSTALL:append = " curl"
IMAGE_INSTALL:append = " gnupg"
```
   
Your final _local.conf_ file should look like this  
   
   ![can-utils](https://user-images.githubusercontent.com/56772428/210805901-d5676a82-b210-4cf1-a994-54a910d31620.jpeg)

   
To test a I<sup>2</sup>C sensor, we want to probe it on the I2C bus. The easiest way to do that is with the i2cdetect tool, which comes with busybox. However, it is not enabled by default for our image, so we need to enable it.

Navigate to the build folder and bring up the busybox menuconfig screen:

```
cd ../build-mp1
bitbake -c menuconfig busybox
```
In there, head to _Miscellaneous Utilities_ , highlight i2cdetect and the other i2c utilities, and press Y to enable. It should have an asterisk [∗] in the select box to denote that the tools will be included with busybox in the next build.
  
   ![busybox](https://user-images.githubusercontent.com/56772428/210805965-ec34a8e1-0314-4a16-8447-85044d0566a7.jpeg)
  
Select Exit with the arrow keys and press ’enter’ to leave that screen. Do that again to exit menuconfig. Save the configuration when asked.


# Building Custom Image

### 7.1 Build and Flash the Custom Image

Build the custom image:

```
bitbake custom-image
```  
   
When the build process is finished, flash the image onto the SD card as discussed previously.
    
```
cd ~/Projects/yocto/build-mp1/tmp/deploy/images/stm32mp1/scripts  
./create_sdcard_from_flashlayout.sh ../flashlayout_custom-image/extensible/FlashLayout_sdcard_stm32mp157a-dk1-extensible.tsv  
sudo dd if =../flashlayout_custom-image/extensible/../../FlashLayout_sdcard_stm32mp157fadk1-extensible.raw of=/dev/mmcblk0 bs=8M conv=fdatasync status=progress oflag=direct
```  
   
### 7.2 Testing I<sup>2</sup>C and FDCAN

#### 7.2.1 I<sup>2</sup>C Tools and Sensor Connection

Plug the SD card into your stm32mp157a-dk1 and boot it up. Connect to the serial terminalwith the following (you may need to change ttyACM1 to some other device file):

```
sudo picocom -b 115200 /dev/ttyACM1
```  
   
Log in to the board with "root" and run the following command line:

```
ls -l /sys/bus/i2c/devices
```
   
   ![i2cdetect_test](https://user-images.githubusercontent.com/56772428/210806040-7f41f0f0-19ac-4ced-860d-37ab3042a6ad.jpeg)

  
This should show you which device files (in /dev/) are symbolically linked to i2c ports/drivers on the main processor. In my case, /dev/i2c-1 is linked to I2C-5 (address 0x40015000), which is the port we just enabled.

Assuming that we have connected Waveshare MLX90640 thermal imaging camera (0x33 address) to the I2C5 pins on the board, we should be able to run the following command. Note
that the bus number (1) should match the device file number.

```
i2cdetect -y 1
```
   
   ![i2cdetect2](https://user-images.githubusercontent.com/56772428/210806107-4877bd9f-fcfb-4ce5-8226-821b5ebf81fa.jpeg)
    
   
If all goes well, you should see 0x33 being reported on the bus, which means you can communicate with the MLX90640!

#### 7.2.2 FDCAN Initialisation and Loopback Test

To communicate with the CAN-FD bus on your stm32mp157a-dk1 board, you can refer to the following tutorial: https://github.com/darkquesh/stm32mp1/blob/main/fdcan.md

# Compiling QT Framework for creation of GUI
### Download the layer for Qt5  
    cd ~/Projects/yocto
    git clone https://github.com/meta-qt5/meta-qt5  
    cd meta-qt5  
    git checkout kirkstone  

### Then, edit the layer config file  
    cd ~/Projects/yocto/build-mp1  
    gedit conf/bblayers.conf

### Change BBLAYERS with the following
>BBLAYERS ?= " \
>  /home/dell/Projects/yocto/poky/meta \\  
>  /home/dell/Projects/yocto/poky/meta-poky \\  
>  /home/dell/Projects/yocto/poky/meta-yocto-bsp \\  
>  /home/dell/Projects/yocto/meta-openembedded/meta-oe \\  
>  /home/dell/Projects/yocto/meta-openembedded/meta-python \\  
>  /home/dell/Projects/yocto/meta-st-stm32mp \\  
>  /home/dell/Projects/yocto/meta-custom \\  
>  /home/dell/Projects/yocto/meta-qt5 \\    
>  "

### Rebuild the custom image

```
bitbake custom-image
```  
   
When the build process is finished, flash the image onto the SD card.
    
```
cd ~/Projects/yocto/build-mp1/tmp/deploy/images/stm32mp1/scripts  
./create_sdcard_from_flashlayout.sh ../flashlayout_custom-image/extensible/FlashLayout_sdcard_stm32mp157a-dk1-extensible.tsv  
sudo dd if =../flashlayout_custom-image/extensible/../../FlashLayout_sdcard_stm32mp157fadk1-extensible.raw of=/dev/mmcblk0 bs=8M conv=fdatasync status=progress oflag=direct
```  

### save and exit, and run:

    bitbake meta-toolchain-qt5
   
## References


[1] STM32MP15 Discovery kits - getting started, STMicroelectronics Wiki, https://wiki.st.com/stm32mpu/wiki/STM32MP15_Discovery_kits_-_getting_started
  
[2] stm32mp157a-dk1 User Manual, STMicroelectronics, https://www.st.com/resource/en/user_manual/um2637-discovery-kits-with-increasedfrequency-800-mhz-stm32mp157-mpus-stmicroelectronics.pdf
  
[3] stm32mp157a-dk1 Reference Manual, STMicroelectronics, https://www.st.com/resource/en/reference_manual/dm00327659-stm32mp157-advanced-arm-based-32-bit-mpus-stmicroelectronics.pdf
  
[4] Yocto Project Reference Manual, Linux Foundation and Yocto Project, https://docs.yoctoproject.org/ref-manual/index.html
  
[5] Github, https://github.com/darkquesh/stm32mp1


<br>

## Extra Resources
### Reference of this tutorial
Although a bit outdated, the Digikey's tutorial on STM32MP1 board is also quite useful (which mine is based on): [Introduction to Embedded Linux | Digikey](https://www.youtube.com/playlist?list=PLEBQazB0HUyTpoJoZecRK6PpDG31Y7RPB)  
### Device tree usage
https://elinux.org/Device_Tree_Usage


[1]: <https://www.st.com/en/microcontrollers-microprocessors/stm32mp1-series.html> "STM32MP1"
- https://wiki.dh-electronics.com/index.php/Add_Yocto_SDK_with_QT5_to_QT_Creator  
- https://www.emsyslabs.com/how-to-compile-linux-using-yocto-for-stm32mp1/  
- https://wiki.st.com/stm32mpu/wiki/How_to_build_and_use_an_SDK_for_QT  
- https://medium.com/@BradenSunwold/how-to-set-up-stm32mp1-with-qt-part-1-7576eec8f1fe  
- https://embeddeduse.com/2020/06/19/qt-embedded-systems-2-build-qt-sdk-with-yocto/  
- https://doc.qt.io/Boot2Qt/b2qt-meta-qt6.html  
