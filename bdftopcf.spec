%global debug_package %{nil}
%define _build_id_links none
%define system_name bdftopcf

Name:           EDO%{system_name}
Version:        1.1.1
Release:        1%{?dist}
Summary:        Convert X font from Bitmap Distribution Format to Portable Compiled Format
License:        MIT
Vendor:         %{_vendor}
URL:            https://gitlab.freedesktop.org/xorg/util/bdftopcf
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOxorg-macros EDOxproto EDOfontsproto EDOpkg-config
Requires:       glibc
Provides:       %{name} = %{version}


%description
bdftopcf is a font compiler for the X server and font server.  Fonts
in Portable Compiled Format can be read by any architecture, although
the file is structured to allow one particular architecture to read
them directly without reformatting.  This allows fast reading on the
appropriate machine, but the files are still portable (but read more
slowly) on other machines.

%prep
%setup -q -n %{system_name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%_configure --docdir=%_docdir/%{name}
%make_build


%check


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
