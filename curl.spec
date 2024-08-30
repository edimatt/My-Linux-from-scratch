%global debug_package %{nil}
%define _build_id_links none
%define system_name curl

Name:           EDO%{system_name}
Version:        8.9.1
Release:        1%{?dist}
Summary:        Free and easy-to-use client-side URL transfer library
License:        LGPL-2
Vendor:         %{_vendor}
URL:            https://curl.se/libcurl
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDObrotli-devel EDOkrb5-devel EDOlibiconv-devel EDOlibidn2-devel EDOlibpsl-devel EDOlibunistring-devel EDOnghttp2-devel EDOopenssl-devel EDOzlib-devel EDOzstd-devel
Requires:       glibc EDObrotli-libs EDOkrb5 EDOlibiconv EDOlibidn2 EDOlibpsl EDOlibunistring EDOnghttp2 EDOopenssl-libs EDOzlib EDOzstd
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
libcurl  is  a  free and easy‐to‐use client‐side URL transfer li‐
brary, supporting DICT, FILE, FTP, FTPS, GOPHER,  GOPHERS,  HTTP,
HTTPS,  IMAP, IMAPS, LDAP, LDAPS, MQTT, POP3, POP3S, RTMP, RTMPS,
RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS,  TELNET,  TFTP,  WS  and
WSS.  libcurl supports SSL certificates, HTTP POST, HTTP PUT, FTP
uploading, HTTP form based upload, proxies, HTTP/2, HTTP/3, cook‐
ies,  user+password  authentication (Basic, Digest, NTLM, Negoti‐
ate, Kerberos), file transfer resume, http  proxy  tunneling  and
more!

libcurl  is  highly  portable, it builds and works identically on
numerous platforms, including Solaris, NetBSD, FreeBSD,  OpenBSD,
Darwin,  HPUX,  IRIX, AIX, Tru64, Linux, UnixWare, HURD, Windows,
Amiga, OS/2, BeOs, macOS, Ultrix, QNX, OpenVMS, RISC  OS,  Novell
NetWare, DOS and more...

libcurl is free, thread‐safe, IPv6 compatible, feature rich, well
supported, fast, thoroughly documented and  is  already  used  by
many known, big and successful companies.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%configure --with-openssl --enable-optimize --with-gssapi --enable-threaded-resolver --disable-static
%make_build


%check
%__make test


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}
%_libdir/lib%{system_name}*.so.4*
%_mandir/man1/%{system_name}*.1


%files devel
%_bindir/%{system_name}-config
%_mandir/man3/*curl*.3
%_mandir/man3/CURL*.3
%_includedir/%{system_name}/*.h
%_libdir/lib%{system_name}*.so
%_libdir/lib%{system_name}*.la
%_libdir/pkgconfig/lib%{system_name}*.pc
%_datadir/aclocal/lib%{system_name}*.m4


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
