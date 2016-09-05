# amdgpu-pro-opencl-rpm
Just the opencl libraries from AMDGPU-Pro in rpm form.

##Disclamer

This is just a workaround until AMD open sources it's openCL code, which will hopefully happen in 2017, but no guarentees of course. Note that I don't speak for AMD, I just based this guess on something an AMD employee told me recently.

If you want something stable, i would advise using the current opensource implementation (*Clover*), or wait for the code to be open sourced in the (hopefully) near future.

AMDGPU Pro is compiled for Ubuntu, not Fedora or variants, thus it may not work.
I don't use openCL and I have not tested it. I based this solely on a guide I found here:

http://www.gearsongallium.com/?p=2960

Feel free to fork this and/or make pull requests :)

##Build Instructions:

1) Download the binaries from the following website and save them to ~/rpmbuild/SOURCES:

```
http://support.amd.com/en-us/kb-articles/Pages/AMD-Radeon-GPU-PRO-Linux-Beta-Driver%E2%80%93Release-Notes.aspx
```

2) Build:

```
rpmbuild -ba amdgpu-pro-opencl.spec
```

##Use Instructions:

To avoid conflicts with *Clover*, library files are placed in a separate folder. Just specify the *LD_LIBRARY_PATH* as */usr/lib64/amdgpu-pro-opencl/* for the application you are using and it should load those.

For example:

```
LD_LIBRARY_PATH=/usr/lib64/amdgpu-pro-opencl/ clinfo
```

Which should show *"AMD Accelerated Parallel Processing"* instead of *"Clover"*.
