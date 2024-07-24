%global debug_package %{nil}
%define _build_id_links none
%define system_name spdlog

Name:           EDO%{system_name}
Version:        1.14.1
Release:        1%{?dist}
Summary:        Very fast, header-only/compiled, C++ logging library.
License:        MIT
URL:            https://github.com/gabime/spdlog
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOgcc
Requires:       glibc EDOgcc
AutoReqProv:    no


%description


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=%_prefix -DCMAKE_CXX_COMPILER=%_bindir/g++ -DCMAKE_CXX_FLAGS_RELEASE="$CXXFLAGS" -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" -DSPDLOG_BUILD_SHARED=ON ..
%make_build


%install
cd build && %make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_includedir/%{system_name}/*
%_libdir/cmake/%{system_name}/*.cmake
%_libdir/lib%{system_name}.so*
%_libdir/pkgconfig/%{system_name}.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
