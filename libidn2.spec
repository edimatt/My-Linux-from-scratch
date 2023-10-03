%global debug_package %{nil}
%define _build_id_links none
%define system_name libidn2

Name:           EDO%{system_name}
Version:        2.3.4
Release:        1%{?dist}
Summary:        Libidn2 is a free software implementation of IDNA2008, Punycode and Unicode TR46.
License:        LGPL
Vendor:         %{_vendor}
URL:            https://ftpmirror.gnu.org/libidn
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOlibunistring-devel EDOlibiconv-devel
Requires:       glibc EDOlibunistring EDOlibiconv
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
The  library  contains functionality to convert internationalized
domain names to and from ASCII Compatible  Encoding  (ACE).   The
API consists of two main functions, idn2_to_ascii_8z for convert‐
ing data from UTF‐8  to  ASCII  Compatible  Encoding  (ACE),  and
idn2_to_unicode_8z8z  to  convert  ACE  names  into UTF‐8 format.
There are several variations of these main functions,  which  ac‐
cept UTF‐32, or input in the local system encoding. All functions
assume zero‐terminated strings.  This library is backwards  (API)
compatible  with the libidn library.  Replacing the idna.h header
with idn2.h into a program is sufficient to switch  the  applica‐
tion from IDNA2003 to IDNA2008 as supported by this library.  Li‐
bidn2 is believed to be a complete IDNA2008 and TR46  implementa‐
tion, it contains an extensive test‐suite, and is included in the
continuous fuzzing project OSS‐Fuzz.  You can check  the  current
test  code  coverage  here  and the current fuzzing code coverage
here.


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
%__mkdir_p %{buildroot}%{_docdir}
%make_install
%__mv %{buildroot}%{_datadir}/gtk-doc/html/%{system_name} %{buildroot}%{_docdir}/%{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/idn2
%_mandir/man1/idn2.1
%_libdir/%{system_name}.so.0*
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo
%_docdir/%{name}/*


%files devel
%_includedir/idn2.h
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/pkgconfig/%{system_name}.pc
%_mandir/man3/idn2_*.3
%ghost %_infodir/dir
%_infodir/%{system_name}.info


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
