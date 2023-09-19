%global debug_package %{nil}
%define _build_id_links none
%define system_name diffutils

Name:           EDO%{system_name}
Version:        3.10
Release:        1%{?dist}
Summary:        Find differences between files.
License:        GPL
URL:            https://www.gnu.org/software/diffutils
Source:         %{system_name}-%{version}.tar.xz
BuildRequires:  rpm-build EDOlibiconv-devel
Requires:       glibc EDOlibiconv
AutoReqProv:    no

%description
GNU Diffutils is a package of several programs related to finding
differences between files.  Computer users often find occasion to
ask  how two files differ. Perhaps one file is a newer version of
the other file. Or maybe the two files started out  as  identical
copies  but  were  changed  by different people.  You can use the
diff command to show differences between two files, or each  cor‐
responding  file in two directories. diff outputs differences be‐
tween files line by line in any of several formats, selectable by
command  line  options. This set of differences is often called a
âdiffâ or âpatchâ. For files that are  identical,  diff  normally
produces  no  output;  for binary (non‐text) files, diff normally
reports only that they are different.  You can use the  cmp  com‐
mand to show the offsets and line numbers where two files differ.
cmp can also show all the characters that differ between the  two
files,  side by side.  You can use the diff3 command to show dif‐
ferences among three files. When two people have made independent
changes  to  a  common original, diff3 can report the differences
between the original and the two changed versions, and  can  pro‐
duce  a  merged file that contains both persons’ changes together
with warnings about conflicts.  You can use the sdiff command  to
merge two files interactively.


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
%doc NEWS README
%_bindir/cmp
%_bindir/*diff*
%_mandir/man1/cmp.1
%_mandir/man1/*diff*.1
%ghost %_infodir/dir
%_infodir/%{system_name}.info
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
