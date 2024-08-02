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
Provides:       %{name} = %{version}
AutoReqProv:    no


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%cmake_setup -DSPDLOG_BUILD_SHARED=ON
%cmake_build


%install
%cmake_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/lib%{system_name}.so.*


%files devel
%_includedir/%{system_name}/*
%_libdir/lib%{system_name}.so
%_libdir/cmake/%{system_name}/*.cmake
%_libdir/pkgconfig/%{system_name}.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
