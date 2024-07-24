%global debug_package %{nil}
%define _build_id_links none
%define system_name gtest

Name:           EDO%{system_name}
Version:        1.15
Release:        1%{?dist}
Summary:        Google's C++ test framework
License:        BSD
URL:            https://github.com/google/googletest
Source:         %{system_name}-%{version}.tar.xz
BuildRequires:  rpm-build glibc-devel EDOgcc
Requires:       glibc EDOgcc
AutoReqProv:    no

%description


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=%_prefix -DCMAKE_C_COMPILER=%_bindir/gcc -DCMAKE_CXX_COMPILER=%_bindir/g++ -DCMAKE_CXX_FLAGS_RELEASE="$CXXFLAGS" -DCMAKE_C_FLAGS_RELEASE="$CFLAGS" -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" -DBUILD_SHARED_LIBS=ON ..
%make_build


%install
cd build && %make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%dir %_includedir/gmock
%dir %_includedir/gtest
%dir %_libdir/cmake/GTest
%_includedir/gmock/*
%_includedir/gtest/*
%_libdir/cmake/GTest/*
%_libdir/libgmock*.so*
%_libdir/libgtest*.so*
%_libdir/pkgconfig/gmock*.pc
%_libdir/pkgconfig/gtest*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
