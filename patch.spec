%global debug_package %{nil}
%define _build_id_links none
%define system_name patch

Name:           EDO%{system_name}
Version:        2.7.6
Release:        1%{?dist}
Summary:        Utility for modifying/upgrading files.
License:        GPL
URL:            https://www.gnu.org/software/patch
Source:         https://ftp.gnu.org/gnu/patch/%{system_name}-%{version}.tar.xz
BuildRequires:  rpm-build glibc-devel EDOattr-devel
Requires:       glibc EDOattr-libs
AutoReqProv:    no

%description
The patch program applies diff files to originals.  The diff com‐
mand is used to compare an original  to  a  changed  file.   Diff
lists  the changes made to the file.  A person who has the origi‐
nal file can then use the patch command with the diff file to add
the  changes  to  their original file (patching the file).  Patch
should be installed because it is a common way of  upgrading  ap‐
plications.


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
%_bindir/%{system_name}
%_mandir/man1/%{system_name}.1


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
