%global debug_package %{nil}
%define _build_id_links none
%define system_name libevent

Name:           EDO%{system_name}
Version:        2.1.12
Release:        1%{?dist}
Summary:        Abstract asynchronous event notification library.
License:        GPL
Vendor:         %{_vendor}
URL:            https://libevent.org
Source0:        %{system_name}-%{version}-stable.tar.gz
Patch0:         %{system_name}-%{version}-event_rpcgen.patch
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
The libevent API provides a mechanism to execute a callback func‐
tion when a specific event occurs on a file descriptor or after a
timeout  has been reached. libevent is meant to replace the asyn‐
chronous event loop found in event driven network servers. An ap‐
plication just needs to call event_dispatch() and can then add or
remove events dynamically without  having  to  change  the  event
loop.


%description devel
This package contains the header files and libraries for developing
with %{system_name}.


%prep
%setup -n %{system_name}-%{version}-stable
%patch0 -p1
./autogen.sh


%build
%set_build_flags_with_rpath
%configure --enable-static=no --disable-openssl
%make_build


%check
make check


%install
%make_install prefix=%_prefix libdir=%_libdir


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/%{system_name}*.so.*


%files devel
%_bindir/event_rpcgen.py
%_includedir/ev*
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/pkgconfig/%{system_name}*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
