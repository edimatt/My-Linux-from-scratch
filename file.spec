%global debug_package %{nil}
%define _build_id_links none
%define system_name file

Name:           EDO%{system_name}
Version:        5.45
Release:        1%{?dist}
Summary:        File type guesser.
License:        GPL
URL:            https://www.darwinsys.com/file
Source:         http://ftp.astron.com/pub/file/%{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOzstd-devel EDOxz-devel EDObzip2-devel EDOzlib-devel

Requires:       %{name}-libs
AutoReqProv:    no


%package libs
Summary:        Development tools for the %{system_name} library.
Requires:       glibc EDOzstd EDOxz-libs EDObzip2-libs EDOzlib
Provides:       %{name}-libs = %{version}
AutoReqProv:    no


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name}-libs = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
The  file  command  is "a file type guesser", that is, a command‐
line tool that tells you in words what kind of data a  file  con‐
tains.  Unlike most GUI systems, command‐line UNIX systems ‐ with
this program leading the charge ‐ don’t rely on  filename  exten‐
tions  to tell you the type of a file, but look at the file’s ac‐
tual contents. This is, of course, more reliable, but requires  a
bit of I/O.


%description libs


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc NEWS
%_bindir/%{system_name}
%_mandir/man1/%{system_name}.1


%files libs
%_libdir/libmagic.so.1*
%_datadir/misc/magic.mgc
%_mandir/man4/magic.4


%files devel
%_libdir/libmagic.so
%_libdir/libmagic.la
%_includedir/magic.h
%_libdir/pkgconfig/libmagic.pc
%_mandir/man3/libmagic.3


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
