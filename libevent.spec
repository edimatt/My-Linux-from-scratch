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
Patch0:         %{system_name}-%{version}-stable-libdir.patch
AutoReqProv:    no
BuildRequires:  glibc-devel EDOopenssl-devel EDOmbedtls-devel
Requires:       glibc EDOopenssl-libs EDOmbedtls
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
%setup -q -n %{system_name}-%{version}-stable
%patch0 -p1


%build
%set_build_flags_with_rpath
mkdir _build && cd _build
cmake -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=%_prefix -DCMAKE_C_COMPILER=%_bindir/gcc -DCMAKE_CXX_COMPILER=%_bindir/g++ -DCMAKE_CXX_FLAGS_RELEASE="$CXXFLAGS" -DCMAKE_C_FLAGS_RELEASE="$CFLAGS" -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" ..
%make_build


%check


%install
cd _build
%make_install prefix=%_prefix libdir=%_libdir
%__mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_bindir}/*


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/%{system_name}*.so.*
%_libdir/%{system_name}*.a


%files devel
%_bindir/event_rpcgen.py
%_includedir/ev*
%_libdir/%{system_name}*.so
%_libdir/pkgconfig/%{system_name}*.pc
%_libdir/cmake/%{system_name}/*.cmake


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
