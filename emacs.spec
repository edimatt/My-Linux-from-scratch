%global debug_package %{nil}
%define _build_id_links none
%define system_name emacs

Name:           EDOemacs
Version:        29.1
Release:        1%{?dist}
Summary:        GNU Emacs text editor.

License:        GPL
URL:            https://github.com/emacs-mirror/emacs
Source0:        %{system_name}-%{system_name}-%{version}.tar.gz

BuildRequires:  nettle-devel EDOzlib-devel giflib-devel libjpeg-turbo-devel gtk3-devel gnutls-devel libXpm-devel libjpeg-turbo-devel texinfo rpm-build EDOncurses-devel EDOlibffi-devel EDOxz-devel EDOsqlite-devel EDOzstd-devel
Requires:       atk at-spi2-atk at-spi2-core bzip2-libs cairo cairo-gobject dbus-libs fontconfig freetype fribidi gdk-pixbuf2 giflib glib2 glibc EDOgmp gnutls graphite2 gtk3 harfbuzz jbigkit-libs json-glib libblkid libbrotli libcap libdatrie libepoxy EDOlibffi libgcc libgcrypt libgpg-error libicu libidn2 libjpeg-turbo libmount libpng libselinux libstdc++ libstemmer libtasn1 libthai libtiff libtracker-sparql libunistring libwayland-client libwayland-cursor libwayland-egl libwebp libX11 libX11-xcb libXau libxcb libXcomposite libXcursor libXdamage libXext libXfixes libXi libXinerama libxkbcommon libxml2 libXrandr libXrender EDOzstd lz4-libs EDOncurses-libs nettle p11-kit pango EDOpcre EDOpcre2 pixman EDOsqlite-libs systemd-libs EDOxz-libs EDOzlib
Provides:       %{name} = %{version}
AutoReqProv:    no


%description
GNU Emacs text editor.

%prep
%autosetup -n %{system_name}-%{system_name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%configure --disable-silent-rules --with-native-compilation --with-sound=yes --with-json=ifavailable
%make_build


%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/*
%_mandir/man1/*
%_prefix/libexec/%{system_name}/*
%_includedir/%{system_name}-module.h
%_libdir/systemd/user/%{system_name}.service
%_datadir/%{system_name}/*
%_datadir/metainfo/%{system_name}.metainfo.xml
%_datadir/applications/%{system_name}*
%_infodir/*
%_datadir/icons/*
%_libdir/%{system_name}/%{version}/native-lisp/*

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
