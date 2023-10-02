%global debug_package %{nil}
%define _build_id_links none
%define system_name aspell

Name:           EDO%{system_name}
Version:        0.60.8
Release:        1%{?dist}
Summary:        Free and Open Source spell checker.
License:        GPL
URL:            http://aspell.net
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build EDOgcc EDOncurses-devel
Requires:       bash glibc EDOgcc EDOncurses-libs
AutoReqProv:    no

%description
GNU  Aspell  is  a Free and Open Source spell checker designed to
eventually replace Ispell. It can either be used as a library  or
as an independent spell checker. Its main feature is that it does
a superior job of suggesting possible  replacements  for  a  mis‐
spelled  word  than  just about any other spell checker out there
for the English language. Unlike Ispell, Aspell can  also  easily
check  documents in UTF‐8 without having to use a special dictio‐
nary. Aspell will also do its best to respect the current  locale
setting.  Other  advantages over Ispell include support for using
multiple dictionaries at once and intelligently handling personal
dictionaries when more than one Aspell process is open at once.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%configure --docdir=%_docdir/%{name}
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/*
%_mandir/man1/*.1
%_libdir/lib*spell.*
%_libdir/%{system_name}*
%_includedir/*spell*
%ghost %_infodir/dir
%_infodir/%{system_name}*
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
