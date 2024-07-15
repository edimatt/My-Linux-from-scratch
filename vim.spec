%global debug_package %{nil}
%global _preprocessor_defines %{nil}
%define _build_id_links none
%define system_name vim

Name:           EDO%{system_name}
Version:        9.1.0516
Release:        1%{?dist}
Summary:        vim text editor.
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/vim/vim
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOncurses-devel EDOpcre2-devel EDOattr-devel EDOacl-devel EDOlua-devel EDOperl EDOpython-devel EDOtcl-devel EDOutil-linux-devel EDOlibxcrypt-devel EDOzlib-devel /usr/bin/pathfix.py 
Requires:       glibc libSM libICE libXt libX11 libXau glibc libxcb EDOncurses-libs libselinux EDOacl-libs EDOlua-libs EDOperl glibc EDOpython-libs EDOtcl EDOutil-linux EDOpcre2 EDOattr-libs EDOlibxcrypt EDOzlib
Provides:       %{name} = %{version}

%description
Vim is a greatly improved version of the good old UNIX editor Vi.
Many new features have been added: multi‐level undo, syntax high‐
lighting,  command  line  history,  on‐line help, spell checking,
filename completion,  block  operations,  script  language,  etc.
There  is also a Graphical User Interface (GUI) available. Still,
Vi compatibility is maintained, those who have Vi  "in  the  fin‐
gers"  will feel at home. See runtime/doc/vi_diff.txt for differ‐
ences with Vi.

This editor is very useful for editing programs and  other  plain
text  files.  All commands are given with normal keyboard charac‐
ters, so those who can type with ten fingers can work very  fast.
Additionally,  function keys can be mapped to commands by the us‐
er, and the mouse can be used.


%prep
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --enable-luainterp=yes --with-lua-prefix=%_prefix --enable-perlinterp=yes --enable-python3interp=yes --enable-tclinterp=yes --enable-multibyte
%make_build


%install
%make_install
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%_datadir/vim/vim91/tools/demoserver.py


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/ex
%_bindir/rview
%_bindir/rvim
%_bindir/vim
%_bindir/view
%_bindir/vimdiff
%_bindir/vimtutor
%_bindir/xxd
%_mandir/*
%_datadir/%{system_name}/*
%_datadir/applications/%{system_name}.desktop
%_datadir/applications/g%{system_name}.desktop
%_datadir/icons/*

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
