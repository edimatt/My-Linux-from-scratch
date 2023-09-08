%global debug_package %{nil}
%define _build_id_links none
%define system_name perl

Name:           EDO%{system_name}
Version:        5.38.0
Release:        1%{?dist}
Summary:        Perl scripting language.
License:        GPL
URL:            https://www.perl.org
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build glibc-devel
Requires:       glibc
AutoReqProv:    no


%description
Perl  is a highly capable, feature‐rich programming language with
over 30 years of development. Perl runs  on  over  100  platforms
from  portables to mainframes and is suitable for both rapid pro‐
totyping and large scale development projects.
"Perl" is a family of languages, "Raku" (formerly known as  "Perl
6")  is  part  of the family, but it is a separate language which
has its own development team. Its existence  has  no  significant
impact on the continuing development of "Perl".


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
./Configure -des -Dprefix=%_prefix                 \
                 -Dvendorprefix=%_prefix           \
                 -Dman1dir=%_mandir/man1           \
                 -Dman3dir=%_mandir/man3           \
                 -Dpager="/usr/bin/less -isR"      \
                 -Dcc=%_bindir/gcc                 \
                 -Doptimize="$CFLAGS"              \
                 -Dlibpth="%_libdir"               \
                 -Dprivlib=%_libdir/%{system_name}5/%{version}           \
                 -Dsitelib=%_libdir/%{system_name}5/site_perl/%{version} \
                 -Darchname=%_build                                      \
                 -Duseshrplib                                            \
                 -Dusethreads
%make_build


%install
%make_install
find %{buildroot}%{_libdir}/%{system_name}5 -name '*.so' -exec chmod +w {} \;


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/*
%_mandir/man1/*.1
%_mandir/man3/*.3
%_libdir/%{system_name}5/%{version}/*
%_libdir/%{system_name}5/site_perl/%{version}/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
