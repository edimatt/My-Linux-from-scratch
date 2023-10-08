%global debug_package %{nil}
%define _build_id_links none
%define system_name expat

Name:           EDO%{system_name}
Version:        2.5.1
Release:        1%{?dist}
Summary:        A C99 library for parsing XML 1.0 Fourth Edition.
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/libexpat/libexpat
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel
Requires:       glibc
Provides:       %{name} = %{version}


%package devel
Summary:        Libraries and header files to develop applications using expat.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
This  is Expat, a C99 library for parsing XML 1.0 Fourth Edition,
started by James Clark in 1997. Expat is  a  stream‐oriented  XML
parser. This means that you register handlers with the parser be‐
fore starting the parse. These handlers are called when the pars‐
er  discovers  the  associated  structures  in the document being
parsed. A start tag is an example of the kind of  structures  for
which you may register handlers.

Expat supports the following compilers:

    GNU GCC >=4.5
    LLVM Clang >=3.5
    Microsoft Visual Studio >=15.0/2017 (rolling ${today} minus 5
years)

Windows users can use  the  expat‐win32bin‐*.*.*.{exe,zip}  down‐
load, which includes both pre‐compiled libraries and executables,
and source code for developers.

Expat is free software. You may copy, distribute, and  modify  it
under the terms of the License contained in the file COPYING dis‐
tributed with this package. This license is the same as the MIT/X
Consortium license.


%description devel
The expat‐devel package contains the libraries, include files and
documentation to develop XML applications with expat.


%prep
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
pushd expat
# Building from git clone
./buildconf.sh
%configure  --disable-static \
            --docdir=%_docdir/%{system_name}-%{version}
%make_build
popd


%check
cd expat && make check


%install
cd expat && %make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/xmlwf
%_libdir/lib%{system_name}*.so.1*


%files devel
%_includedir/%{system_name}*.h
%_libdir/lib%{system_name}*.so
%_libdir/lib%{system_name}*.la
%_libdir/cmake/%{system_name}-*
%_libdir/pkgconfig/%{system_name}.pc
%_docdir/%{system_name}-%{version}/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
