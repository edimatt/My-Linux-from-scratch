%global debug_package %{nil}
%global _warning_options %{nil}
%define _build_id_links none
%define system_name expect

Name:           EDO%{system_name}
Version:        5.45.4
Release:        1%{?dist}
Summary:        A program-script interaction and testing utility.
License:        GPL
URL:            https://sourceforge.net/projects/expect
Source:         %{system_name}-%{version}.tar.xz
BuildRequires:  rpm-build glibc-devel EDOgcc EDOtcl-devel
Requires:       glibc EDOtcl
AutoReqProv:    no


%description
Expect  is a tool for automating interactive applications such as
telnet, ftp, passwd, fsck, rlogin, tip, etc. Expect is also  use‐
ful for testing these same applications.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --docdir=%_docdir/%{name}
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc NEWS
%_bindir/*
%_mandir/man1/*.1
%_mandir/man3/lib%{system_name}.3
%_includedir/%{system_name}*.h
%_includedir/tcldbg.h
%_libdir/%{system_name}%{version}/*



%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
