%global debug_package %{nil}
%define _build_id_links none
%define system_name zlib

Name:           EDO%{system_name}
Version:        1.3
Release:        1%{?dist}
Summary:        Compression and decompression library.
License:        GPL
Vendor:         %{_vendor}
URL:            https://zlib.net
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgmp-devel EDOmpfr-devel
Requires:       glibc EDOgmp EDOmpfr
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
zlib  is designed to be a free, general‐purpose, legally unencum‐
bered ‐‐ that is, not covered by any patents  ‐‐  lossless  data‐
compression  library  for  use on virtually any computer hardware
and operating system. The zlib data  format  is  itself  portable
across  platforms. Unlike the LZW compression method used in Unix
compress(1) and in the GIF image format, the  compression  method
currently  used  in zlib essentially never expands the data. (LZW
can double or triple the file size in extreme cases.) zlib’s mem‐
ory  footprint  is  also independent of the input data and can be
reduced, if necessary, at some cost in compression. A  more  pre‐
cise, technical discussion of both points is available on another
page.


%description devel
The zlib-devel package contains the header files and libraries needed
to develop programs that use the zlib compression and decompression
library.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --prefix=%_prefix --libdir=%_libdir
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/libz.a
%_libdir/libz.so.1
%_libdir/libz.so.1.3


%files devel
%_includedir/%{system_name}.h
%_includedir/zconf.h
%_libdir/libz.so
%_libdir/pkgconfig/%{system_name}.pc
%_mandir/man3/%{system_name}.3


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
