%global debug_package %{nil}
%define _build_id_links none
%define system_name colm

Name:           EDO%{system_name}
Version:        0.14.7
Release:        1%{?dist}
Summary:        Colm - COmputer Language Machinery
License:        MIT
URL:            https://github.com/adrian-thurston/colm
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build EDOgcc
Requires:       glibc EDOgcc EDOcolm-libs
AutoReqProv:    no


%package libs
Summary:        Colm libraries
Requires:       glibc
Provides:       %{name}-libs = %{version}
AutoReqProv:    no


%package devel
Summary:        Development tools.
Requires:       %{name}-libs = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
Colm  is  a  programming  language  designed for the analysis and
transformation of computer languages.  Colm is influenced primar‐
ily by TXL.


%description libs


%description devel


%prep
%setup -n %{system_name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%configure --enable-static=yes --enable-manual --datadir=%_datadir/%{system_name}
%make_build


%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/%{system_name}*
%_docdir/%{system_name}/*


%files libs
%_libdir/libfsm-*.so
%_libdir/lib%{system_name}-*.so
%_libdir/libfsm.a
%_libdir/lib%{system_name}.a



%files devel
%_libdir/libfsm.so
%_libdir/libfsm.la
%_libdir/lib%{system_name}.so
%_libdir/lib%{system_name}.la
%_includedir/aapl/*
%_includedir/libfsm/*
%_includedir/%{system_name}/*
%_datadir/%{system_name}/rlhc*
%_datadir/%{system_name}/ril.lm
%_datadir/%{system_name}/runtests



%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
