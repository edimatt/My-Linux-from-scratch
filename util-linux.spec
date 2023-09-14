%global debug_package %{nil}
%define _build_id_links none
%define system_name util-linux

Name:           EDO%{system_name}
Version:        2.39.2
Release:        1%{?dist}
Summary:        Random collection of Linux utilities.
License:        GPL
URL:            https://github.com/util-linux/util-linux
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build
Requires:       glibc
Provides:       %{name} = %{version} EDOlibuuid = %{version} EDOlibblkid = %{version} EDOlibmount = %{version} EDOlibsmartcols = %{version} EDOlibfdisk = %{version}
AutoReqProv:    no


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version} EDOlibuuid-devel = %{version} EDOlibblkid-devel = %{version} EDOlibmount-devel = %{version} EDOlibsmartcols-devel = %{version} EDOlibfdisk-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
util-linux is a random collection of Linux utilities


%description devel


%prep
%setup -n %{system_name}-%{version}
# We use system autoconf 2.69
./autogen.sh


%build
%_configure --disable-makeinstall-chown --docdir=%_docdir/%{name}
%make_build


%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/*
%_sbindir/*
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo
%_datadir/bash-completion/completions/*
%_docdir/%{name}/*
%_libdir/lib*.so.1*


%files devel
%_libdir/lib*.so
%_libdir/lib*.la
%_libdir/pkgconfig/*.pc
%_includedir/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
