%global debug_package %{nil}
%define _build_id_links none
%define system_name brotli

Name:           EDO%{system_name}
Version:        1.1.0
Release:        1%{?dist}
Summary:        JPEG image codec.
License:        MIT
URL:            https://github.com/google/brotli
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build glibc-devel
Requires:       %{name}-libs = %{version}
AutoReqProv:    no


%package libs
Summary:        Brotli libraries
Requires:       glibc
Provides:       %{name}-libs = %{version}
AutoReqProv:    no


%package devel
Summary:        Development tools.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
Brotli  is  a generic‐purpose lossless compression algorithm that
compresses data using a combination of a modern  variant  of  the
LZ77  algorithm,  Huffman  coding and 2nd order context modeling,
with a compression ratio comparable to the best currently  avail‐
able  general‐purpose compression methods. It is similar in speed
with deflate but offers more dense compression.
The specification of the Brotli Compressed Data Format is defined
in RFC 7932.
Brotli  is  open‐sourced  under  the MIT License, see the LICENSE
file.


%description libs



%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=%_prefix -DCMAKE_INSTALL_DOCDIR=%_docdir/%{name} -DCMAKE_C_COMPILER=%_bindir/gcc -DCMAKE_CXX_COMPILER=%_bindir/g++ -DCMAKE_CXX_FLAGS_RELEASE="$CXXFLAGS" -DCMAKE_C_FLAGS_RELEASE="$CFLAGS" -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" -DENABLE_STATIC=0 ..
%make_build


%install
cd build && %make_install


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%license LICENSE
%_bindir/%{system_name}


%files libs
%_libdir/lib%{system_name}*.so.1*


%files devel
%_libdir/lib%{system_name}*.so
%_libdir/pkgconfig/lib%{system_name}*.pc
%_includedir/%{system_name}/*.h



%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
