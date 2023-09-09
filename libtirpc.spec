%global debug_package %{nil}
%define _build_id_links none
%define system_name libtirpc

Name:           EDO%{system_name}
Version:        1.3.3
Release:        1%{?dist}
Summary:        NTIRPC - Transport-independent RPC (TI-RPC)
License:        GPL
Vendor:         %{_vendor}
URL:            https://sourceforge.net/projects/libtirpc
Source0:        %{system_name}-%{version}.tar.bz2
AutoReqProv:    no
BuildRequires:  glibc-devel 
Requires:       glibc
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
The  libtirpc  package  contains  libraries that support programs
that use the Remote Procedure Call (RPC)  API.  It  replaces  the
RPC, but not the NIS library entries that used to be in glibc.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --sysconfdir=%_sysconfdir  \
            --disable-static           \
            --disable-gssapi
%make_build


%check
# make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/%{system_name}*.so.3*


%files devel
%_includedir/tirpc/*
%_libdir/%{system_name}.so
%_libdir/%{system_name}.la
%_libdir/pkgconfig/%{system_name}*.pc
%_sysconfdir/netconfig
%_sysconfdir/bindresvport.blacklist
%_mandir/man3/*.3t
%_mandir/man5/netconfig.5

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
