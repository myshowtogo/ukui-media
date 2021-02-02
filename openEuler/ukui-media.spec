%define debug_package %{nil}
Name:           ukui-media
Version:        3.0.2
Release:        3
Summary:        UKUI media utilities
License:        GPL-2+ GPL-3+ LGPL-2+ BSD-3-Clause
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

Autoreq : yes

BuildRequires: intltool
BuildRequires: qt5-qtbase-devel
BuildRequires: libcanberra-devel
BuildRequires: gsettings-qt-devel
BuildRequires: glib2-devel
BuildRequires: gsettings-qt-devel
BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: mate-desktop-devel >= 1.18
BuildRequires: libmatemixer-devel >= 1.18
BuildRequires: libxml2-devel
BuildRequires: mate-common >= 1.18
BuildRequires: qt5-qtsvg-devel
BuildRequires: libqtxdg-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qtmultimedia
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: qt5-qttools-devel

Requires: mate-desktop-libs >= 1.18
Requires: ukui-media-common = %{version}

Recommends: alsa-utils sound-theme-freedesktop

%description
 A simple and lightweight screensaver written by Qt5.
 The screensaver supports biometric auhentication which is
 provided by biometric-auth service.

%package common
Summary:	UKUI media utilities (common files)
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description common
 UKUI media utilities are the audio mixer and the volume
 control applet.
 .
 This package contains the common files.

%prep
%setup -q

%build
./autogen.sh --prefix=/usr --sysconfdir=/etc --libdir=/usr/lib64
make

cd %{_builddir}/%{name}-%{version}/ukui-volume-control-applet-qt
mkdir build && cd build
qmake-qt5 ..
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

cp -r %{_builddir}/%{name}-%{version}/ukui-volume-control-applet-qt/build/ukui-volume-control-applet-qt %{buildroot}/usr/bin/
# cp -r %{_builddir}/%{name}-%{version}/ukui-volume-control-applet-qt/ukui-media-control-led/build/ukui-media-control-led %{buildroot}/usr/bin/

mkdir -p %{buildroot}/usr/share/ukui-media/translations
cp -r %{_builddir}/%{name}-%{version}/ukui-volume-control-applet-qt/translations/*.qm %{buildroot}/usr/share/ukui-media/translations/

mkdir -p %{buildroot}/usr/share/ukui-media/img
cp -r %{_builddir}/%{name}-%{version}/ukui-volume-control-applet-qt/data/img/* %{buildroot}/usr/share/ukui-media/img/

mkdir -p %{buildroot}/usr/share/ukui-media/qss
cp -r %{_builddir}/%{name}-%{version}/ukui-volume-control-applet-qt/data/qss/* %{buildroot}/usr/share/ukui-media/qss/

cp -r %{_builddir}/%{name}-%{version}/ukui-volume-control-applet-qt/data/sounds/ukui-sound.xml %{buildroot}/usr/share/ukui-media/sounds
cp -r %{_builddir}/%{name}-%{version}/ukui-volume-control-applet-qt/data/sounds/ubuntu-sound.xml %{buildroot}/usr/share/ukui-media/sounds
cp -r %{_builddir}/%{name}-%{version}/ukui-volume-control-applet-qt/data/sounds/index.theme %{buildroot}/usr/share/sounds/ukui
cp -r %{_builddir}/%{name}-%{version}/ukui-volume-control-applet-qt/data/sounds/*.ogg %{buildroot}/usr/share/ukui-media/sounds

cp -r %{_builddir}/%{name}-%{version}/data/org.ukui.sound.gschema.xml %{buildroot}/usr/share/glib-2.0/schemas

mkdir -p %{buildroot}/usr/share/ukui-media/scripts
cp -r %{_builddir}/%{name}-%{version}/scripts/detection_output_mode.sh %{buildroot}/usr/share/ukui-media/scripts

cp -r %{_builddir}/%{name}-%{version}/data/org.ukui.media.sound.gschema.xml %{buildroot}/usr/share/glib-2.0/schemas

mkdir -p %{buildroot}/usr/lib/systemd/system
cp -r %{_builddir}/%{name}-%{version}/data/ukui-media-control-mute-led.service %{buildroot}/usr/lib/systemd/system

%clean
rm -rf $RPM_BUILD_ROOT

%post
set -e
glib-compile-schemas /usr/share/glib-2.0/schemas/


%files
%doc debian/changelog debian/copyright
%{_unitdir}/ukui-media-control-mute-led.service
%{_bindir}/ukui-volume-control
%{_bindir}/ukui-volume-control-applet
%{_bindir}/ukui-volume-control-applet-qt
%{_datadir}/applications/
%{_datadir}/ukui-media/translations/
%{_datadir}/ukui-media/img/
%{_datadir}/ukui-media/qss/
%{_datadir}/ukui-media/scripts/

%files common
%{_sysconfdir}/xdg/autostart/
%{_datadir}/locale/
%{_datadir}/man/*
%{_datadir}/ukui-media/icons
%{_datadir}/ukui-media/sounds/
%{_datadir}/sounds/*
%{_datadir}/glib-2.0/

%changelog
* Mon Feb 1 2021 lvhan <lvhan@kylinos.cn> - 3.0.2-3
- update to upstream version 3.0.1-1

* Mon Dec 7 2020 lvhan <lvhan@kylinos.cn> - 3.0.2-2
- fix vol icon bug

* Mon Oct 26 2020 douyan <douyan@kylinos.cn> - 3.0.2-1
- update to upstream version 3.0.1-1+1026

* Mon Sep 14 2020 douyan <douyan@kylinos.cn> - 2.0.4-1
- update to upstream version 2.0.4-2+0806

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 2.0.3-1
- Init package for openEuler
