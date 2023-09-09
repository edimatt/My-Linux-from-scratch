%global debug_package %{nil}
%define _build_id_links none
%define system_name cppcheck

Name:           EDO%{system_name}
Version:        2.11.99
Release:        1%{?dist}
Summary:        Static analysis tool for C/C++ code
License:        GPL
Vendor:         %{_vendor}
URL:            https://cppcheck.sourceforge.io
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgcc EDOpcre-devel EDOlibiconv-devel
Requires:       glibc EDOgcc EDOpcre EDOlibiconv
Provides:       %{name} = %{version}


%description
Cppcheck  is  a static analysis tool for C/C++ code. It provides
unique code analysis to detect bugs and focuses on detecting  un‐
defined behaviour and dangerous coding constructs. The goal is to
have very few false positives. Cppcheck is designed to be able to
analyze  your C/C++ code even if it has non‐standard syntax (com‐
mon in embedded projects).

Cppcheck is available both as open‐source (this page) and as  Cp‐
pcheck  Premium  with  extended functionality and support. Please
visit www.cppchecksolutions.com for more information and purchase


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
mkdir build && cd build
cmake -DUSE_MATCHCOMPILER=ON -DHAVE_RULES=ON -DCMAKE_INSTALL_PREFIX=%_prefix FILESDIR=%_datadir/%{system_name} -DPCRE_LIBRARY=%_libdir/libpcre.so -DCMAKE_DISABLE_PRECOMPILE_HEADERS=on -DCMAKE_CXX_FLAGS="$CXXFLAGS" CMAKE_CXX_FLAGS_RELEASE="$CXXFLAGS" HAVE_RULES=yes ..
%make_build


%check


%install
cd build && %make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}
%_datadir/Cppcheck/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
