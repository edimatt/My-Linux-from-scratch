%global debug_package %{nil}
%define _build_id_links none
%define system_name gawk

Name:           EDO%{system_name}
Version:        5.2.2
Release:        1%{?dist}
Summary:        The GNU version of the AWK text processing utility

License:        GPL
URL:            https://www.gnu.org/software/gawk
Source0:        %{system_name}-%{version}.tar.xz

BuildRequires:  rpm-build glibc-devel EDOpcre-devel EDOxz-devel EDOzlib-devel
Requires:       glibc EDOpcre EDOxz-libs EDOzlib
Provides:       %{name} = %{version}
AutoReqProv:    no


%description
The gawk package contains the GNU version of AWK text processing utility. AWK is
a programming language designed for text processing and typically used as a data
extraction and reporting tool.

The gawk utility can be used to do quick and easy text pattern matching,
extracting or reformatting. It is considered to be a standard Linux tool for
text processing.


%prep
%autosetup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%configure
%make_build


%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/%{system_name}*
%_bindir/awk
%_includedir/%{system_name}api.h
%_mandir/man1/%{system_name}*.1
%_mandir/man1/pm-%{system_name}.1
%_mandir/man3/*
%ghost %_infodir/dir
%_infodir/%{system_name}*
%_infodir/pm-%{system_name}.info
%_datadir/awk/*
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo
%_libdir/%{system_name}/*.so
%_libexecdir/awk/*
%_sysconfdir/profile.d/%{system_name}*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
