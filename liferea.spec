%global debug_package %{nil}
%define _build_id_links none

Name:           liferea
Version:        1.14.0
Release:        1%{?dist}
Summary:        liferea rss feed reader.

License:        GPL
URL:            https://github.com/lwindolf/liferea
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  rpm-build libxslt-devel libpsl-devel libsoup-devel sqlite-devel gobject-introspection-devel libpeas-devel gsettings-desktop-schemas-devel json-glib-devel webkit2gtk3-devel
Requires:       atk at-spi2-atk at-spi2-core bzip2-libs cairo cairo-gobject dbus-libs enchant2 fontconfig freetype fribidi gdk-pixbuf2 glib2 glibc gobject-introspection graphite2 gstreamer1 gstreamer1-plugins-base gtk3 harfbuzz harfbuzz-icu hyphen json-glib keyutils-libs krb5-libs lcms2 libatomic libblkid libbrotli libcap libcom_err libdatrie libepoxy libffi libgcc libgcrypt libglvnd libglvnd-egl libglvnd-glx libglvnd-opengl libgpg-error libicu libidn2 libjpeg-turbo libmount libpeas libpng libpsl libseccomp libsecret libselinux libsoup libstdc++ libstemmer libtasn1 libthai libtracker-sparql libunistring libwayland-client libwayland-cursor libwayland-egl libwayland-server libwebp libwpe libX11 libX11-xcb libXau libxcb libXcomposite libXcursor libXdamage libXext libXfixes libXi libXinerama libxkbcommon libxml2 libXrandr libXrender libxslt libzstd lz4-libs openjpeg2 openssl-libs orc pango pcre pcre2 pixman sqlite-libs systemd-libs webkit2gtk3 webkit2gtk3-jsc woff2 wpebackend-fdo xz-libs zlib
AutoReqProv:    no

%description
Liferea  is a desktop feed reader/news aggregator that brings to‐
gether all of the content from your favorite subscriptions into a
simple interface that makes it easy to organize and browse feeds.
Its GUI is similar to a desktop mail/news client, with an  embed‐
ded web browser.

%prep
%autosetup -n %{name}-%{version}
./autogen.sh
%configure

%build
%make_build


%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/%{name}*
%_mandir/man*
%_mandir/it/man1/%name.1
%_datadir/%name/*
%_datadir/GConf/gsettings/%name.convert
%_datadir/applications/net.sourceforge.%name.desktop
%_datadir/dbus-1/services/net.sourceforge.%name.service
%_datadir/glib-2.0/schemas/net.sf.%name.gschema.xml
%_datadir/icons/*
%_datadir/locale/*
%_datadir/metainfo/net.sourceforge.%name.appdata.xml
%_libdir/%name/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
