%global debug_package %{nil}
%define _build_id_links none
%define system_name msgpack

Name:           EDOpython-%{system_name}
Version:        1.0.8
Release:        1%{?dist}
Summary:        Efficient binary serialization format.
License:        Apache 2.0
URL:            https://mesonbuild.com
Source:         %{system_name}-%{version}.tar.xz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython
AutoReqProv:    no


%description
MessagePack  is an efficient binary serialization format. It lets
you exchange data among multiple languages like  JSON.  But  it’s
faster  and  smaller.  This package provides CPython bindings for
reading and writing MessagePack data.


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
