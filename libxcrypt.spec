%global debug_package %{nil}
%define _build_id_links none
%define system_name libxcrypt

Name:           EDO%{system_name}
Version:        4.4.36
Release:        1%{?dist}
Summary:        Password hashing library.
License:        GPL
URL:            https://github.com/besser82/libxcrypt
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build glibc-devel
Requires:       glibc
AutoReqProv:    no


%package devel
Summary:        Development tools.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
libxcrypt  is  a modern library for one‐way hashing of passwords.
It supports a wide variety of both modern and historical  hashing
methods:  yescrypt,  gost‐yescrypt,  scrypt, bcrypt, sha512crypt,
sha256crypt,  md5crypt,   SunMD5,   sha1crypt,   NT,   bsdicrypt,
bigcrypt,  and  descrypt.  It provides the traditional Unix crypt
and crypt_r interfaces, as well as a set of  extended  interfaces
pioneered  by  Openwall Linux, crypt_rn, crypt_ra, crypt_gensalt,
crypt_gensalt_rn, and crypt_gensalt_ra.

libxcrypt is intended to be used by login(1), passwd(1), and oth‐
er similar programs; that is, to hash a small number of passwords
during an interactive authentication dialogue with a human. It is
not  suitable  for use in bulk password‐cracking applications, or
in any other situation where speed is more important than careful
handling  of  sensitive  data. However, it is intended to be fast
and lightweight enough for use in servers that must  field  thou‐
sands of login attempts per minute.


%description devel
The libxcrypt-devel  package contains  libraries and header files
for developing applications that use libxcrypt.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --disable-static             \
            --enable-hashes=strong,glibc \
            --enable-obsolete-api=no     \
            --disable-failure-tokens
%make_build


%install
%make_install


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/libcrypt.so.2*
%_mandir/man5/crypt*.5


%files devel
%_libdir/libcrypt.so
%_libdir/libcrypt.la
%_libdir/pkgconfig/lib*crypt.pc
%_mandir/man3/crypt*.3
%_includedir/*crypt.h


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
