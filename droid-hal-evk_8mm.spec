# These and other macros are documented in dhd/droid-hal-device.inc
%define device evk_8mm
%define vendor fsl
%define vendor_pretty Freescale
%define device_pretty IMX8M Mini
%define installable_zip 1
%define droid_target_aarch64 1

%define straggler_files \
/bugreports\
/cache\
/d\
/product\
/sdcard\
%{nil}

%include rpm/dhd/droid-hal-device.inc
