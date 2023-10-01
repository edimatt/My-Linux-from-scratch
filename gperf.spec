%global debug_package %{nil}
%define _build_id_links none
%define system_name gperf

Name:           EDO%{system_name}
Version:        3.1
Release:        1%{?dist}
Summary:        A perfect hash function generator.
License:        GPL
URL:            https://www.gnu.org/software/gperf
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOgcc
Requires:       glibc EDOgcc
AutoReqProv:    no


%description
GNU  gperf is a perfect hash function generator. For a given list
of strings, it produces a hash function and hash table,  in  form
of  C  or C++ code, for looking up a value depending on the input
string. The hash function is perfect, which means that  the  hash
table has no collisions, and the hash table lookup needs a single
string comparison only.

GNU gperf is highly customizable. There are options for  generat‐
ing  C  or C++ code, for emitting switch statements or nested ifs
instead of a hash table, and for tuning the algorithm employed by
gperf.


%prep
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --docdir=%{_docdir}/%{name}
%make_build


%install
%make_install


%check
make check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc %{system_name}.html
%_bindir/%{system_name}
%_mandir/man1/%{system_name}.1
%ghost %_infodir/dir
%_infodir/%{system_name}.info


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
