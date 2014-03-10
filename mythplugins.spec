# Requires autofinder is confused, requires nonexistent packages (mythtv-mythweb)
%if %{_use_internal_dependency_generator}
%define __noautoreq 'pear(.*)'
%else
%define _requires_exceptions pear*
%endif

%define gitversion v0.25.2-16-gd5192
%define fixesdate 0
%define rel 2

%if %{fixesdate}
%define release %{fixesdate}.%{rel}
%else
%define release %{rel}
%endif

#####################
# Hardcode PLF build
%define build_plf 0
#####################

%if %{build_plf}
%define extrarelsuffix plf
%define distsuffix plf
%endif

Summary:	Official MythTV plugins
Name:		mythplugins
Version:	0.26.0
Release:	%{release}%{?extrarelsuffix}
License:	GPLv2
Group:		Video
Url:		http://www.mythtv.org/
Source0:	ftp://ftp.osuosl.org/pub/mythtv/%{name}-%{version}.tar.bz2
%if %{fixesdate}
Patch1:		fixes-%{gitversion}.patch
%endif
Patch100:	0100-lame-Allow-building-without-lame-libraries.patch

# (cg) Ditto for the perl-DateTime-Format-ISO pkg
BuildRequires:	perl(Class::Factory::Util)
BuildRequires:	perl-XML-XPath
BuildRequires:	perl-Image-Size
BuildRequires:	perl-Date-Manip
BuildRequires:	perl-DateTime-Format-ISO8601
BuildRequires:	perl-SOAP-Lite
BuildRequires:	perl-XML-Simple
BuildRequires:	python-curl
BuildRequires:	python-oauth
# (cg) Remove these once they are required in the python-mythtv package
BuildRequires:	python-lxml
BuildRequires:	python-mysql
BuildRequires:	mythtv-devel >= %{version}
BuildRequires:	python-mythtv >= %{version}
BuildRequires:	cdda-devel
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(id3tag)
BuildRequires:	pkgconfig(libcdaudio)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libvisual-0.4)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(udev)
%if %{build_plf}
BuildRequires:	lame-devel
BuildRequires:	faad2-devel
%endif

%description
Mythplugins for MythTV.

%if %{build_plf}
This package is in restricted because it contains software that supports
codecs that may be covered by software patents.
%endif

%package -n mythtv-plugin-browser
Summary:	Full web browser for MythTV
Group:		Video
Obsoletes:	mythbrowser < 0.20a-7
Requires:	mythtv-frontend >= %{version}

%description -n mythtv-plugin-browser
MythBrowser is a full web browser for MythTV.

%package -n mythtv-plugin-gallery
Summary:	Gallery/slideshow module for MythTV
Group:		Video
Requires:	mythtv-frontend >= %{version}
Obsoletes:	mythgallery < 0.20a-7

%description -n mythtv-plugin-gallery
A gallery/slideshow module for MythTV.

%package -n mythtv-plugin-game
Summary:	Game frontend for MythTV
Group:		Video
Requires:	mythtv-frontend >= %{version}
Obsoletes:	mythgame < 0.20a-7

%description -n mythtv-plugin-game
A game frontend for MythTV.

%package -n mythtv-plugin-music
Summary:	The music player add-on module for MythTV
Group:		Video
#Requires:	cdparanoia
Requires:	mythtv-frontend >= %{version}
Obsoletes:	mythmusic < 0.20a-7

%description -n mythtv-plugin-music
The music player add-on module for MythTV.

%if %{build_plf}
This package is in restricted because it contains software that supports
codecs that may be covered by software patents.
%endif

%package -n mythtv-plugin-netvision
Summary:	NetVision for MythTV
Group:		Video
Requires:	mythtv-frontend >= %{version}

%description -n mythtv-plugin-netvision
NetVision for MythTV. View popular media website content.

%package -n mythtv-plugin-news
Summary:	RSS News feed plugin for MythTV
Group:		Video
Requires:	mythtv-frontend >= %{version}
Obsoletes:	mythnews < 0.20a-7

%description -n mythtv-plugin-news
An RSS News feed plugin for MythTV.

%package -n mythtv-plugin-weather
Summary:	MythTV module that displays a weather forecast
Group:		Video
Requires:	mythtv-frontend >= %{version}
Obsoletes:	mythweather < 0.20a-7

%description -n mythtv-plugin-weather
A MythTV module that displays a weather forcast.

%package -n mythtv-mythweb
Summary:	The web interface to MythTV
Group:		Video
Requires:	mythtv-backend >= %{version}
Requires:	php-mythtv >= %{version}
Requires:	apache-mod_php
Obsoletes:	mythweb < 0.20a-7

%description -n mythtv-mythweb
The web interface to MythTV.

%package -n mythtv-plugin-zoneminder
Summary:	Security camera plugin for MythTV
Group:		Video
Requires:	mythtv-frontend >= %{version}

%description -n mythtv-plugin-zoneminder
A security camera plugin for MythTV.

%package -n mythtv-plugin-archive
Summary:	Creates DVDs from your recorded shows
Group:		Video
Requires:	dvd+rw-tools
Requires:	dvdauthor
Requires:	ffmpeg
Requires:	mjpegtools
Requires:	python-imaging
Requires:	python-mysql
Requires:	mythtv-frontend >= %{version}
%if %{build_plf}
Requires:	transcode
%endif
Requires:	cdrkit-genisoimage
Obsoletes:	mytharchive < 0.20a-7

%description -n mythtv-plugin-archive
MythArchive is a plugin for MythTV that lets you create DVDs
from your recorded shows, MythVideo files and any video files
available on your system. It can also archive recordings in a
proprietary format that archives not only the file but also all the
associated metadata like title, description and cut list information
which will mean you can create backups of myth recordings which can
later be restored or it will also allow you to move recordings
between myth systems without losing any of the metadata. It is a
complete rewrite of the old MythBurn bash scripts, now using python,
and the mythfrontend UI plugin.

%prep
%setup -q
%apply_patches

%build
./configure \
	--prefix=%{_prefix} \
	--enable-all \
	--libdir-name=%{_lib} \
%if %{build_plf}
	--enable-mp3lame
%else
	--disable-mp3lame
%endif

%make

%install
%makeinstall INSTALL_ROOT=%{buildroot}

#mythgallery
mkdir -p %{buildroot}%{_localstatedir}/lib/pictures
#mythmusic
mkdir -p %{buildroot}%{_localstatedir}/lib/mythmusic

install -d -m755 %{buildroot}%{_var}/www/mythweb
install -m644 mythweb/*.php %{buildroot}%{_var}/www/mythweb
install -m755 mythweb/*.pl %{buildroot}%{_var}/www/mythweb

for dir in classes includes js modules skins ; do
  cp -r mythweb/$dir %{buildroot}%{_var}/www/mythweb
done

install -d -m755 %{buildroot}%{_localstatedir}/lib/mythweb/data
ln -s %{_localstatedir}/lib/mythweb/data %{buildroot}%{_var}/www/mythweb/data

# Create a default configuration for mythweb
install -d -m755 %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d
install -m644 mythweb/mythweb.conf.apache %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/mythweb.conf

perl -pi -e's|<Directory "/var/www/html|<Directory "%{_var}/www/mythweb|' %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/mythweb.conf
perl -pi -e's|#    RewriteBase    /mythweb|    RewriteBase    /mythweb|' %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/mythweb.conf

cat >> %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/mythweb.conf <<EOF

# ROSA Customisations (be in sync with very sane Mageia's ones)

Alias /mythweb %{_var}/www/mythweb
<Directory %{_var}/www/mythweb>
    Require host 127.0.0.1
</Directory>
EOF

mkdir -p %{buildroot}%{_docdir}/mythtv-plugin-{browser,gallery,game,music,netvision,news,weather,video,zoneminder}

%files -n mythtv-plugin-browser
%doc mythbrowser/README mythbrowser/COPYING mythbrowser/AUTHORS
%{_libdir}/mythtv/plugins/libmythbrowser.so
%{_datadir}/mythtv/i18n/mythbrowser_*.qm
%{_datadir}/mythtv/themes/default*/browser-ui.xml
%{_datadir}/mythtv/themes/default*/mb_*.png

%files -n mythtv-plugin-gallery
%doc mythgallery/README*
%{_libdir}/mythtv/plugins/libmythgallery.so
%{_datadir}/mythtv/i18n/mythgallery_*.qm
%{_datadir}/mythtv/themes/default*/gallery*
%{_localstatedir}/lib/pictures

%files -n mythtv-plugin-game
%doc mythgame/romdb*
%{_libdir}/mythtv/plugins/libmythgame.so
%{_datadir}/mythtv/i18n/mythgame_*.qm
%{_datadir}/mythtv/game_settings.xml
%{_datadir}/mythtv/themes/default*/game*
%dir %{_datadir}/mythtv/metadata
%{_datadir}/mythtv/metadata/Game

%files -n mythtv-plugin-music
%doc mythmusic/AUTHORS mythmusic/COPYING mythmusic/README* mythmusic/musicdb
%{_datadir}/mythtv/music_settings.xml
%{_datadir}/mythtv/musicmenu.xml
%{_libdir}/mythtv/plugins/libmythmusic.so
%{_localstatedir}/lib/mythmusic
%{_datadir}/mythtv/i18n/mythmusic_*.qm
%{_datadir}/mythtv/themes/default/ff_button*.png
%{_datadir}/mythtv/themes/default*/mm_*.png
%{_datadir}/mythtv/themes/default*/mm-*.png
%{_datadir}/mythtv/themes/default/music-*.png
%{_datadir}/mythtv/themes/default*/*music*.xml
%{_datadir}/mythtv/themes/default/next_button*.png
%{_datadir}/mythtv/themes/default/pause_button*.png
%{_datadir}/mythtv/themes/default/play_button*.png
%{_datadir}/mythtv/themes/default/prev_button*.png
%{_datadir}/mythtv/themes/default/rew_button*.png
%{_datadir}/mythtv/themes/default/selectionbar.png
%{_datadir}/mythtv/themes/default/stop_button*.png
%{_datadir}/mythtv/themes/default/track_info_background.png
%{_datadir}/mythtv/themes/default/miniplayer_background.png
%{_datadir}/mythtv/themes/default-wide/music-sel-bg.png

%files -n mythtv-plugin-netvision
%doc mythnetvision/README mythnetvision/ChangeLog mythnetvision/AUTHORS
%{_bindir}/mythfillnetvision
%{_libdir}/mythtv/plugins/libmythnetvision.so
%{_datadir}/mythtv/i18n/mythnetvision_*.qm
%{_datadir}/mythtv/mythnetvision
%{_datadir}/mythtv/netvisionmenu.xml
%{_datadir}/mythtv/themes/default*/netvision*.xml

%files -n mythtv-plugin-news
%doc mythnews/AUTHORS mythnews/COPYING mythnews/ChangeLog mythnews/README*
%{_libdir}/mythtv/plugins/libmythnews.so
%{_datadir}/mythtv/i18n/mythnews_*.qm
%{_datadir}/mythtv/mythnews
%{_datadir}/mythtv/themes/default*/news*
%{_datadir}/mythtv/themes/default/enclosures.png
%{_datadir}/mythtv/themes/default/need-download.png
%{_datadir}/mythtv/themes/default/podcast.png

%files -n mythtv-plugin-weather
%doc mythweather/AUTHORS mythweather/COPYING mythweather/README*
%{_libdir}/mythtv/plugins/libmythweather.so
%{_datadir}/mythtv/i18n/mythweather_*.qm
%{_datadir}/mythtv/mythweather
%{_datadir}/mythtv/themes/default/cloudy.png
%{_datadir}/mythtv/themes/default/fair.png
%{_datadir}/mythtv/themes/default/flurries.png
%{_datadir}/mythtv/themes/default/fog.png
%{_datadir}/mythtv/themes/default/logo.png
%{_datadir}/mythtv/themes/default/lshowers.png
%{_datadir}/mythtv/themes/default/mcloudy.png
%{_datadir}/mythtv/themes/default/pcloudy.png
%{_datadir}/mythtv/themes/default/rainsnow.png
%{_datadir}/mythtv/themes/default/showers.png
%{_datadir}/mythtv/themes/default/snowshow.png
%{_datadir}/mythtv/themes/default/sunny.png
%{_datadir}/mythtv/themes/default/thunshowers.png
%{_datadir}/mythtv/themes/default/unknown.png
%{_datadir}/mythtv/themes/default*/mw*.png
%{_datadir}/mythtv/themes/default*/weather-ui.xml
%{_datadir}/mythtv/weather_settings.xml

%files -n mythtv-mythweb
%doc mythweb/README* mythweb/LICENSE mythweb/INSTALL mythweb/mythweb.conf.*
%{_var}/www/mythweb
%dir %{_localstatedir}/lib/mythweb
%attr(-,apache,apache) %{_localstatedir}/lib/mythweb/data
%config(noreplace) %{_sysconfdir}/httpd/conf/webapps.d/mythweb.conf

%files -n mythtv-plugin-zoneminder
%doc mythzoneminder/README mythzoneminder/COPYING mythzoneminder/AUTHORS
%{_bindir}/mythzmserver
%{_libdir}/mythtv/plugins/libmythzoneminder.so
%{_datadir}/mythtv/zonemindermenu.xml
%{_datadir}/mythtv/themes/default*/zoneminder*.xml
%{_datadir}/mythtv/themes/default*/mz_*.png
%{_datadir}/mythtv/i18n/mythzoneminder_*.qm

%files -n mythtv-plugin-archive
%{_bindir}/mytharchivehelper
%{_libdir}/mythtv/plugins/libmytharchive.so
%{_datadir}/mythtv/archive*.xml
%{_datadir}/mythtv/mytharchive
%{_datadir}/mythtv/themes/default/ma_*.png
%{_datadir}/mythtv/themes/default/mytharchive-ui.xml
%{_datadir}/mythtv/themes/default/mythburn-ui.xml
%{_datadir}/mythtv/themes/default/mythnative-ui.xml
%{_datadir}/mythtv/themes/default-wide/mytharchive-ui.xml
%{_datadir}/mythtv/themes/default-wide/mythburn-ui.xml
%{_datadir}/mythtv/themes/default-wide/mythnative-ui.xml
%{_datadir}/mythtv/i18n/mytharchive_*.qm

