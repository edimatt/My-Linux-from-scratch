%global debug_package %{nil}
%define _build_id_links none
%define system_name tk

Name:           EDO%{system_name}
Version:        8.6.13
Release:        1%{?dist}
Summary:        Graphical user interface toolkit.
License:        GPL
Vendor:         %{_vendor}
URL:            https://www.tcl.tk
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOtcl-devel EDOzlib-devel libX11-devel libxcb-devel libXau-devel
Requires:       glibc EDOtcl EDOzlib libX11 libxcb libXau
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
Tk  is  a  graphical user interface toolkit that takes developing
desktop applications to a  higher  level  than  conventional  ap‐
proaches.  Tk  is the standard GUI not only for Tcl, but for many
other dynamic languages, and can produce  rich,  native  applica‐
tions  that  run  unchanged  across  Windows, Mac OS X, Linux and
more.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
export TK_LIBRARY=%_libdir/%{system_name}8.6
export CFLAGS_OPTIMIZE=
export CFLAGS="$CFLAGS -lm"
cd unix && %_configure --enable-64bit --enable-shared --enable-threads && %make_build


%install
cd unix && %make_install
chmod +w %{buildroot}%{_libdir}/lib%{system_name}8.6.so
cd %{buildroot}%{_bindir} && ln -sfv %{system_name}sh8.6 %{system_name}sh && cd -
cd %{buildroot}%{_libdir} && ln -sfv lib%{system_name}8.6.so lib%{system_name}.so && cd -
rm -f %{buildroot}%{_mandir}/man3/gmon.out


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}sh
%_bindir/wish8.6
%_mandir/man1/wish.1
%_libdir/%{system_name}8.6/*
%_libdir/lib%{system_name}8.6.so


%files devel
%_includedir/*%{system_name}*.h
%_libdir/lib%{system_name}.so
%_libdir/lib%{system_name}*.a
%_libdir/%{system_name}Config.sh
%_libdir/pkgconfig/%{system_name}.pc
%_mandir/man3/Tk_*.3
%_mandir/man3/Ttk*.3
%_mandir/man3/F*.3
%_mandir/man3/MeasureChar.3
%_mandir/mann/*.n


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
