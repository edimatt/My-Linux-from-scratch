# my-linux-from-scratch

This is my attempt to build an entire linux distribution from scratch by compiling all the OS components from source code, starting from the compiler itself. Gcc 13.2.0 is used.

The approach taken is to produce rpm packages from the source tarballs instead of just building the source code and copying the files to destination (approach taken by the Linux from scratch project). This is done for 2 reasons:

* Document everything as code inside the spec files (dependencies, patches, fixes and customizations etc).
* Clear vision: using RPMs, it is possible to see any file in the filesystem to which package they belong.
* Produce binary packages that can be directly deployed everywhere without recompiling. A custom dnf repository can be used for that.
* Having a bleeding edge, optimized distribution with the latest software.
