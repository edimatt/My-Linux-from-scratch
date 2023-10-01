%global debug_package %{nil}
%define _build_id_links none
%define system_name psmisc

Name:           EDO%{system_name}
Version:        23.6
Release:        1%{?dist}
Summary:        Miscellaneous utilities that use the proc file-system.
License:        GPL
URL:            https://gitlab.com/psmisc/psmisc
Source:         %{system_name}-v%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel
Requires:       glibc
AutoReqProv:    no


%description
A package of small utilities that use the proc file-system.

fuser - Identifies processes using files or sockets
killall - kills processes by name, e.g. killall -HUP named
prtstat - prints statistics of a process
pslog - prints log path(s) of a process
pstree - shows the currently running processes as a tree
peekfd - shows the data travelling over a file descriptor


%prep
%setup -q -n %{system_name}-v%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%_configure --enable-selinux 
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING NEWS README
%_bindir/killall
%_bindir/pslog
%_bindir/prtstat
%_bindir/pstree*
%_bindir/peekfd
%_bindir/fuser
%_mandir/man1/killall.1
%_mandir/man1/pslog.1
%_mandir/man1/prtstat.1
%_mandir/man1/pstree.1
%_mandir/man1/peekfd.1
%_mandir/man1/fuser.1
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
