%global debug_package %{nil}
%define _build_id_links none
%define _build x86_64-edo-linux-gnu
%define _host x86_64-edo-linux-gnu
%define system_name annobin

Name:           EDO%{system_name}
Version:        12.24
Release:        1%{?dist}
Summary:        Annobin gcc plugin.
License:        GPL
Vendor:         %{_vendor}
URL:            https://sourceware.org/annobin
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel
Requires:       glibc
Provides:       %{name} = %{version}

%description


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
# Uncomment the below only if annobin is not yet installed for the current compiler.
# export CFLAGS="$(echo $CFLAGS | sed -e 's/-Werror=format-security//g' -e 's_-specs=/usr/lib/rpm/redhat/redhat-annobin-cc1__g')"
# export CXXFLAGS="$CFLAGS"
%_configure --docdir=%_docdir/%{name}
%make_build


%install
%make_install
cp doc/annotation.proposal.txt .
pushd %{buildroot}%{_libdir}/gcc/%{_build}/13.2.0/plugin
cp %{system_name}.so.0.0.0 gcc-%{system_name}.so.0.0.0
ln -s gcc-%{system_name}.so.0.0.0 gcc-%{system_name}.so.0
ln -s gcc-%{system_name}.so.0.0.0 gcc-%{system_name}.so
popd


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc COPYING3 LICENSE README.md annotation.proposal.txt
%_bindir/annocheck
%_includedir/libannocheck.h
%_libdir/gcc/%{_build}/13.2.0/plugin/*%{system_name}.so
%_libdir/gcc/%{_build}/13.2.0/plugin/*%{system_name}.so.0
%_libdir/gcc/%{_build}/13.2.0/plugin/*%{system_name}.so.0.0.0
%_libdir/libannocheck.la
%_libdir/libannocheck.so
%_libdir/libannocheck.so.0
%_libdir/libannocheck.so.0.0.0
%_libdir/pkgconfig/libannocheck.pc
%_infodir/%{system_name}.info
%ghost %_infodir/dir
%_mandir/man1/%{system_name}.1
%_mandir/man1/annocheck.1
%_mandir/man1/built-by.1
%_mandir/man1/check-abi.1
%_mandir/man1/hardened.1
%_mandir/man1/run-on-binaries-in.1


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-

