%global debug_package %{nil}
%define _build_id_links none

Name:           vim
Version:        9.0.1258
Release:        1%{?dist}
Summary:        vim text editor.
License:        GPL
URL:            https://github.com/vim/vim
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ncurses-devel pcre2-devel /usr/bin/pathfix.py 

%package enhanced
Summary: A version of the VIM editor which includes recent enhancements.
Requires: pcre2 ncurses-libs glibc
Provides: vim
AutoReqProv:    no

%package common
Summary: The common files needed by any version of the VIM editor.
Requires: vim-enhanced
AutoReqProv:    no

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

%description enhanced
Install  the  vim‐enhanced package if you’d like to use a version
of the VIM editor which includes recently added enhancements like
interpreters for the Python and Perl scripting languages.  You’ll
also need to install the vim‐common package.

%description common
The vim‐common package contains files which every VIM binary will
need in order to run.

If you are installing vim‐enhanced or vim‐X11, you’ll  also  need
to install the vim‐common package.

%prep
%setup -n %{name}-%{version}
%configure

%build
%make_build


%install
%make_install
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%_datadir/vim/vim90/tools/demoserver.py

%clean
rm -rf $RPM_BUILD_ROOT


%files enhanced
%_bindir/ex
%_bindir/rview
%_bindir/rvim
%_bindir/vim
%_bindir/view
%_bindir/vimdiff
%_bindir/vimtutor


%files common
%_bindir/xxd
%_mandir/*
%_datadir/%name/*
%_datadir/applications/%{name}.desktop
%_datadir/applications/g%{name}.desktop
%_datadir/icons/*

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
