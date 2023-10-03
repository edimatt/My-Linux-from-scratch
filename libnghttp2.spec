%global debug_package %{nil}
%define _build_id_links none
%define system_name nghttp2

Name:           EDO%{system_name}
Version:        1.56.0
Release:        1%{?dist}
Summary:        HTTP/2 C library
License:        GPL
Vendor:         %{_vendor}
URL:            https://nghttp2.org
Source0:        https://github.com/nghttp2/nghttp2/%{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOxz-devel EDOopenssl-devel EDOgcc EDOjansson-devel EDOlibxml2-devel EDOzlib-devel EDOpython
Requires:       glibc EDOxz-libs EDOopenssl-libs EDOgcc EDOjansson EDOlibxml2 EDOzlib EDOpython
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
nghttp2 is an implementation of HTTP/2 and its header compression
algorithm HPACK in C.

The framing layer of HTTP/2 is implemented as a form of  reusable
C  library.  On  top  of that, we have implemented HTTP/2 client,
server and proxy. We have also developed load test and benchmark‐
ing tool for HTTP/2.

We  have  participated  in  httpbis  working  group  since HTTP/2
draft‐04, which is the first implementation draft. Since then  we
have  updated  nghttp2 library constantly to latest specification
and nghttp2 is now one of the most mature HTTP/2 implementations.

All C APIs are fully documented.

HTTP/2 utilizes header compression method called HPACK. We  offer
HPACK encoder and decoder are available as public API.


%description devel


%prep
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --with-python_prefix=%_prefix --with-libxml2 --with-jansson --with-zlib --with-openssl --docdir=%_docdir/%{name} 
%make_build


%check
make check


%install
%make_install
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_datadir}/%{system_name}/*


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc README.rst
%_bindir/*flatehd
%_mandir/man1/nghttp*.1
%_mandir/man1/h2load.1
%_libdir/lib%{system_name}.so.14*
%_datadir/%{system_name}/*


%files devel
%_includedir/%{system_name}/%{system_name}*.h
%_libdir/lib%{system_name}*.so
%_libdir/lib%{system_name}*.la
%_libdir/pkgconfig/lib%{system_name}.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
