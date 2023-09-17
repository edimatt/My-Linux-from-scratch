%global debug_package %{nil}
%define _build_id_links none
%define system_name krb5

Name:           EDO%{system_name}
Version:        1.21.2
Release:        1%{?dist}
Summary:        MIT Kerberos V5.
License:        GPL
URL:            https://kerberos.org/dist/krb5/
Source0:        %{system_name}-%{version}.tar.gz
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


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
cd src
%_configure
%make_build


%install
cd src && %make_install
mv %{buildroot}%_datadir/examples %{buildroot}%_datadir/%{system_name}
rm -rf %{buildroot}%_mandir/cat*
rm -rf %{buildroot}%_datadir/et


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/*
%_sbindir/*
%_mandir/man*/*.*
%_mandir/man5/.k5*.5
%_libdir/lib*.so.*
%_libdir/%{system_name}/*
%_datadir/%{system_name}/*
%_datadir/locale/*/LC_MESSAGES/mit-%{system_name}.mo
%_localstatedir/%{system_name}kdc
%_localstatedir/run/%{system_name}kdc
 

%files devel
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc
%_includedir/%{system_name}/*
%_includedir/kadm5/*
%_includedir/gss*
%_includedir/k*.h
%_includedir/com_err.h
%_includedir/verto*.h
%_includedir/profile.h
%_includedir/gssapi.h


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
