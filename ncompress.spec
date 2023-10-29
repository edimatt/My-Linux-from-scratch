%global debug_package %{nil}
%define _build_id_links none
%define system_name ncompress

Name:           EDO%{system_name}
Version:        5.0
Release:        1%{?dist}
Summary:        A fast, simple LZW file compressor.
License:        Public Domain
Vendor:         %{_vendor}
URL:            https://vapier.github.io/ncompress
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel
Requires:       glibc
Provides:       %{name} = %{version}


%description
Compress is a fast, simple LZW file compressor. Compress does not
have the highest compression rate, but it is one of  the  fastest
programs  to  compress  data. Compress is the defacto standard in
the UNIX community for compressing files.  The ncompress code is,
and  will  continue to be, released into the public domain as the
original authors intended.  Also note that all  existing  patents
on the LZW algorithm have expired world‐wide.


%prep
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%make_build


%check


%install
%make_install PREFIX=%_prefix
# Uncompress and various z* utilities are already provided by the gzip package.
%__rm %{buildroot}%{_bindir}/z*
# %__rm %{buildroot}%{_bindir}/uncompress
%__rm %{buildroot}%{_mandir}/man1/z*
# %__rm %{buildroot}%{_mandir}/man1/uncompress.1


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/*
%_mandir/man1/*.1


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
