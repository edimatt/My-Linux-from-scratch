%global debug_package %{nil}
%define _build_id_links none
%define system_name grep

Name:           EDO%{system_name}
Version:        3.11
Release:        1%{?dist}
Summary:        Pattern matching utilities.
License:        GPL
URL:            https://www.gnu.org/software/grep
Source:         %{system_name}-%{version}.tar.xz
BuildRequires:  rpm-build EDOlibiconv-devel EDOpcre2-devel
Requires:       glibc EDOlibiconv EDOpcre2
AutoReqProv:    no

%description
The  GNU  versions of commonly used grep utilities. Grep searches
through textual input for lines which contain a match to a speci‐
fied pattern and then prints the matching lines. GNU’s grep util‐
ities include grep, egrep and fgrep.

GNU grep is needed by many scripts, so it shall be  installed  on
every system.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --enable-threads=posix
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/*%{system_name}
%_mandir/man1/%{system_name}.1
%ghost %_infodir/dir
%_infodir/%{system_name}.info
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
