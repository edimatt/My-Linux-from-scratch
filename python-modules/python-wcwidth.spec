%global debug_package %{nil}
%define _build_id_links none
%define system_name wcwidth

Name:           EDOpython-%{system_name}
Version:        0.2.13
Release:        1%{?dist}
Summary:        Measures the displayed width of unicode strings in a terminal
License:        MIT 
URL:            https://pypi.org/project/%{system_name}/
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython
AutoReqProv:    no
BuildArch:      noarch


%description
This  library  is  mainly for CLI programs that carefully produce
output for Terminals, or make pretend to be an emulator.

Problem Statement: The printable length of most strings are equal
to  the number of cells they occupy on the screen 1 character : 1
cell. However, there are categories of characters that  occupy  2
cells (full‐wide), and others that occupy 0 cells (zero‐width).

Solution:  POSIX.1‐2001  and POSIX.1‐2008 conforming systems pro‐
vide wcwidth(3) and wcswidth(3) C functions of which this  python
moduleâs  functions  precisely  copy.  These functions return the
number of cells a unicode string is expected to occupy.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath


%install
%pip_install


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_libdir}/python3.12/site-packages/%{system_name}*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
