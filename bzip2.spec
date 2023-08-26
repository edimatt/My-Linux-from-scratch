%global debug_package %{nil}
%define _build_id_links none
%define system_name bzip2

Name:           EDO%{system_name}
Version:        1.0.8
Release:        1%{?dist}
Summary:        Compression and decompression library.
License:        GPL
Vendor:         %{_vendor}
URL:            https://sourceware.org/bzip2/
Source0:        %{system_name}-%{version}.tar.xz
Patch0:         %{system_name}-%{version}-makefile.patch
AutoReqProv:    no
BuildRequires:  glibc-devel
Requires:       glibc %{name}-libs = %{version}
Provides:       %{name} = %{version}

%package libs
Summary:        Development tools for the %{system_name} library.
Provides:       %{name}-libs = %{version}
AutoReqProv:    no


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name}-libs = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
bzip2 is a freely available, patent free (see below), high‐quali‐
ty data compressor. It typically compresses files to  within  10%
to  15%  of the best available techniques (the PPM family of sta‐
tistical compressors), whilst being around twice as fast at  com‐
pression  and  six times faster at decompression. Why would I use
it?
    Because it compresses well. So it packs more stuff into  your
overfull disk drives, distribution CDs, backup tapes, USB sticks,
etc. And/or it reduces your customer download  times,  long  dis‐
tance network traffic, etc. It’s not the world’s fastest compres‐
sor, but it’s still fast enough to be very useful.
    Because it’s open‐source (BSD‐style license), and, as far  as
I know, patent‐free. (To the best of my knowledge. I can’t afford
to do a full patent search, so I  can’t  guarantee  this.  Caveat
emptor).  So you can use it for whatever you like. Naturally, the
source code is part of the distribution.
    Because it supports (limited) recovery from media errors.  If
you  are  trying to restore compressed data from a backup tape or
disk, and that data contains some errors, bzip2 may still be able
to decompress those parts of the file which are undamaged.
    Because  you already know how to use it. bzip2’s command line
flags are similar to those of GNU Gzip, so if you know how to use
gzip, you know how to use bzip2.
    Because it’s very portable. It should run on any 32 or 64‐bit
machine with an ANSI C compiler. The distribution should  compile
unmodified  on Unix and Win32 systems. Earlier versions have been
ported with little difficulty to a large number of weird and won‐
derful systems.

The  code is organised as a library with a programming interface.
The bzip2 program itself is a client of the library. You can  use
the library in your own programs, to directly read and write .bz2
files, or even just to compress data in memory  using  the  bzip2
algorithms.


%description  libs


%description  devel 


%prep
%setup -n %{system_name}-%{version}
%patch0 -p1


%build
%set_build_flags_with_rpath
%make_build -f Makefile-libbz2_so
%__make clean
%make_build


%check
make check


%install
%{__mkdir_p} %{buildroot}%{_libdir}
%make_install PREFIX=%{buildroot}%{_prefix} LIBDIR=%{buildroot}%{_libdir}
ln -sv libbz2.so.1.0 libbz2.so
cp -av libbz2.so* bzip2-shared %{buildroot}%{_libdir}



%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/bz*
%_bindir/bunzip2
%_mandir/man1/bz*.1


%files libs
%_libdir/libbz2.so.1.0
%_libdir/libbz2.so.%{version}
%_libdir/bzip2-shared
%_libdir/libbz2.a


%files devel
%_includedir/bzlib.h
%_libdir/libbz2.so


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
