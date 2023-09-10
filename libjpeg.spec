%global debug_package %{nil}
%define _build_id_links none
%define system_name libjpeg

Name:           EDO%{system_name}
Version:        3.0.0
Release:        1%{?dist}
Summary:        JPEG image codec.
License:        GPL
URL:            https://libjpeg-turbo.org
Source0:        https://github.com/libjpeg-turbo/libjpeg-turbo/archive/refs/tags/%{system_name}-turbo-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build EDOgcc EDOnasm
Requires:       glibc
AutoReqProv:    no


%package devel
Summary:        Development tools.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
libjpeg‐turbo  is  a JPEG image codec that uses SIMD instructions
(MMX, SSE2, AVX2, Neon, AltiVec) to accelerate baseline JPEG com‐
pression  and decompression on x86, x86‐64, Arm, and PowerPC sys‐
tems, as well as progressive JPEG compression on x86, x86‐64, and
Arm  systems. On such systems, libjpeg‐turbo is generally 2‐6x as
fast as libjpeg, all else being equal. On other types of systems,
libjpeg‐turbo  can  still  outperform  libjpeg  by  a significant
amount, by virtue of its  highly‐optimized  Huffman  coding  rou‐
tines.  In  many  cases,  the performance of libjpeg‐turbo rivals
that of proprietary high‐speed JPEG codecs.

libjpeg‐turbo implements both the traditional libjpeg API as well
as the less powerful but more straightforward TurboJPEG API. lib‐
jpeg‐turbo also features colorspace extensions that allow  it  to
compress  from/decompress  to 32‐bit and big‐endian pixel buffers
(RGBX, XBGR, etc.), as well as a full‐featured Java interface.

libjpeg‐turbo was originally based on libjpeg/SIMD, an MMX‐accel‐
erated  derivative  of  libjpeg v6b developed by Miyasaka Masaru.
The TigerVNC and VirtualGL projects made numerous enhancements to
the codec in 2009, and in early 2010, libjpeg‐turbo spun off into
an independent project, with the goal of making  high‐speed  JPEG
compression/decompression technology available to a broader range
of users and developers. libjpeg‐turbo is an  ISO/IEC  and  ITU‐T
reference implementation of the JPEG standard.


%description devel
The libjpeg-turbo-devel  package contains  libraries and header files
for developing applications that use libjpeg-turbo.


%prep
%setup -n %{system_name}-turbo-%{version}


%build
%set_build_flags_with_rpath
mkdir build && cd build
cmake -G"Unix Makefiles" -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=%_prefix -DCMAKE_INSTALL_DOCDIR=%_docdir/%{name} -DCMAKE_C_COMPILER=%_bindir/gcc -DCMAKE_CXX_COMPILER=%_bindir/g++ -DCMAKE_CXX_FLAGS_RELEASE="$CXXFLAGS" -DCMAKE_C_FLAGS_RELEASE="$CFLAGS" -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" -DENABLE_STATIC=0 ..
%make_build


%install
cd build && %make_install


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/*
%_mandir/man1/*.1
%_libdir/%{system_name}.so.62*
%_libdir/libturbojpeg.so.0*
%_docdir/%{name}/*


%files devel
%_libdir/%{system_name}.so
%_libdir/libturbojpeg.so
%_libdir/pkgconfig/lib*jpeg.pc
%_libdir/cmake/%{system_name}-turbo/*.cmake
%_includedir/*.h


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
