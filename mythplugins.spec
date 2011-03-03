%define name    mythplugins
%define version 0.24
%define gitversion v0.24-199-g53677
%define fixesdate 20110303
%define rel 1

%define required_myth %{version}

%if %{fixesdate}
%define release %mkrel %fixesdate.%rel
%else
%define release %mkrel %rel
%endif

%define build_plf		0

%bcond_with plf
%if %with plf
%if %mdvver >= 201100
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%endif
%define distsuffix		plf
%define build_plf		1
%endif

BuildRequires:	mesagl-devel
BuildRequires:	libmyth-devel >= %{required_myth}
BuildRequires:  python-mythtv >= %{required_myth}
BuildRequires:	libvisual-devel
BuildRequires:	fftw-devel
BuildRequires:	SDL-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libexif-devel
BuildRequires:	id3tag-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libflac-devel
BuildRequires:	libcdaudio-devel
BuildRequires:	libcdda-devel
BuildRequires:	tiff-devel
BuildRequires:	mysql-devel
BuildRequires:	taglib-devel
BuildRequires:  python-curl
BuildRequires:  python-oauth
BuildRequires:  perl-XML-XPath
BuildRequires:  perl-Image-Size
BuildRequires:  perl-Date-Manip
BuildRequires:  perl-DateTime-Format-ISO8601
BuildRequires:  perl-SOAP-Lite
BuildRequires:  perl-XML-Simple
%if %build_plf
BuildRequires:	lame-devel
BuildRequires:	libfaad2-devel
%endif
# (cg) Remove these once they are required in the python-mythtv package
BuildRequires:  python-lxml
BuildRequires:  python-mysql
# (cg) Ditto for the perl-DateTime-Format-ISO pkg
BuildRequires:  perl(Class::Factory::Util)


Summary: 	Official MythTV plugins
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}%{?extrarelsuffix}
URL: 		http://www.mythtv.org/
License: 	GPL
Group: 		Video
Source0:	%{name}-%{version}.tar.bz2

%if %{fixesdate}
Patch1: fixes-%{gitversion}.patch
%endif
# (cg) git format-patch --start-number 100 --relative=mythplugins fixes/0.24..mga-0.24-patches
Patch100: 0100-lame-Allow-building-without-lame-libraries.patch

BuildRoot: 	%{_tmppath}/%{name}-root

%description
Mythplugins for MythTV.

%if %with plf
This package is in PLF because it contains software that supports
codecs that may be covered by software patents.
%endif

%package -n mythtv-plugin-browser
Summary:	Full web browser for MythTV
URL: 		http://www.mythtv.org/
Group:		Video
Obsoletes:	mythbrowser < 0.20a-7
Requires:	mythtv-frontend >= %{required_myth}

%description -n mythtv-plugin-browser
MythBrowser is a full web browser for MythTV.

%package -n mythtv-plugin-gallery
Summary: 	Gallery/slideshow module for MythTV
Group: 		Video
Requires:	mythtv-frontend >= %{required_myth}
Obsoletes:	mythgallery < 0.20a-7

%description -n mythtv-plugin-gallery
A gallery/slideshow module for MythTV.

%package -n mythtv-plugin-game
Summary: 	Game frontend for MythTV
Group: 		Video
Requires:	mythtv-frontend >= %{required_myth}
Obsoletes:	mythgame < 0.20a-7

%description -n mythtv-plugin-game
A game frontend for MythTV.

%package -n mythtv-plugin-music
Summary: 	The music player add-on module for MythTV
Group: 		Video
#Requires:	cdparanoia
Requires:	mythtv-frontend >= %{required_myth}
Obsoletes:	mythmusic < 0.20a-7

%description -n mythtv-plugin-music
The music player add-on module for MythTV.

%if %with plf
This package is in PLF because it contains software that supports
codecs that may be covered by software patents.
%endif

%package -n mythtv-plugin-netvision
Summary:  NetVision for MythTV
Group:    Video
Requires: mythtv-frontend >= %{required_myth}

%description -n mythtv-plugin-netvision
NetVision for MythTV. View popular media website content.

%package -n mythtv-plugin-news
Summary: 	RSS News feed plugin for MythTV
Group: 		Video
Requires:	mythtv-frontend >= %{required_myth}
Obsoletes:	mythnews < 0.20a-7

%description -n mythtv-plugin-news
An RSS News feed plugin for MythTV.

%package -n mythtv-plugin-weather
Summary: 	MythTV module that displays a weather forecast
Group: 		Video
Requires:	mythtv-frontend >= %{required_myth}
Obsoletes:	mythweather < 0.20a-7

%description -n mythtv-plugin-weather
A MythTV module that displays a weather forcast.

%package -n mythtv-mythweb
Summary: 	The web interface to MythTV
Group: 		Video
Requires:	mythtv-backend >= %{required_myth}
Requires: 	mod_php >= 2.0.54
Requires:	php-mysql
%if %mdkversion < 201010
Requires(post):   rpm-helper
Requires(postun):   rpm-helper
%endif
Obsoletes:	mythweb < 0.20a-7
# Requires autofinder is confused, requires nonexistent packages
%define _requires_exceptions pear*

%description -n mythtv-mythweb
The web interface to MythTV.

%package -n mythtv-plugin-video
Summary: 	Generic video/DVD player frontend module for MythTV
Group: 		Video
Requires:	mythtv-frontend >= %{required_myth}
Requires:	mplayer
%if %build_plf
Requires:      transcode
Requires:      %mklibname dvdcss 2
%endif
Obsoletes:	mythvideo < 0.20a-7
Provides:  mythtv-plugin-dvd = %{version}-%{release}
Obsoletes: mythtv-plugin-dvd < %{version}-%{release}


%description -n mythtv-plugin-video
A generic video and DVD player frontend module for MythTV.

%package -n mythtv-plugin-zoneminder
Summary:  Security camera plugin for MythTV
Group:    Video
Requires: mythtv-frontend >= %{required_myth}

%description -n mythtv-plugin-zoneminder
A security camera plugin for MythTV.

%package -n mythtv-plugin-archive
Summary: 	Creates DVDs from your recorded shows
Group: 		Video
Requires:	dvd+rw-tools
Requires:	dvdauthor
Requires:	ffmpeg
Requires:	mjpegtools
Requires:	python-imaging
Requires:	python-mysql
Requires:	mythtv-frontend >= %{required_myth}
%if %build_plf
Requires:	transcode
%endif
%if %mdkversion >= 200710
Requires:	cdrkit-genisoimage
%else
Requires:	mkisofs
%endif
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

# Fix /mnt/store -> /var/lib/mythmusic
perl -pi -e's|/mnt/store/music|%{_localstatedir}/lib/mythmusic|' mythmusic/mythmusic/globalsettings.cpp
# Fix /mnt/store -> /var/lib/mythvideo
perl -pi -e's|/share/Movies/dvd|%{_localstatedir}/lib/mythvideo|' mythvideo/mythvideo/globalsettings.cpp

perl -pi -e's|{PREFIX}/lib$|{PREFIX}/%{_lib}|' settings.pro

%build
%configure --enable-all --libdir-name=%{_lib} \
%if %build_plf
	--enable-mp3lame
%else
	--disable-mp3lame
%endif

%make

%install

rm -rf %{buildroot}

INSTALL_ROOT=%{buildroot}; export INSTALL_ROOT
%makeinstall

#mythgallery
mkdir -p %{buildroot}%{_localstatedir}/lib/pictures
#mythmusic
mkdir -p %{buildroot}%{_localstatedir}/lib/mythmusic
#mythvideo
mkdir -p %{buildroot}%{_localstatedir}/lib/mythvideo

install -d -m755 %{buildroot}%{_var}/www/mythweb
install -m644 mythweb/*.php %{buildroot}%{_var}/www/mythweb
install -m755 mythweb/*.pl %{buildroot}%{_var}/www/mythweb

for dir in classes includes js modules skins ; do
  cp -r mythweb/$dir %{buildroot}%{_var}/www/mythweb
done

install -d -m755 %{buildroot}%{_localstatedir}/lib/mythweb/data
ln -s %{_localstatedir}/lib/mythweb/data %{buildroot}%{_var}/www/mythweb/data

# Create a default configuration for mythweb
cp mythweb/mythweb.conf.apache mythweb/mythweb.conf
perl -pi -e's|<Directory "/var/www/html" >|<Directory "%{_var}/www/mythweb" >|' mythweb/mythweb.conf
perl -pi -e's|#    RewriteBase    /mythweb|    RewriteBase    /mythweb|' mythweb/mythweb.conf

install -d -m755 %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d
cat > %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/mythweb.conf <<EOF
Alias /mythweb %{_var}/www/mythweb

<Directory %{_var}/www/mythweb>
    Order allow,deny
    Deny from all
</Directory>
EOF

mkdir -p %{buildroot}{%_docdir}/mythtv-plugin-{browser,gallery,game,music,netvision,news,weather,video,zoneminder}


%clean
rm -rf %{buildroot}

%post -n mythtv-mythweb
%if %mdkversion < 201010
%_post_webapp
%endif

%postun -n mythtv-mythweb
%if %mdkversion < 201010
%_postun_webapp
%endif

%files -n mythtv-plugin-browser
%defattr(-,root,root,-)
%doc mythbrowser/README mythbrowser/COPYING mythbrowser/AUTHORS
%{_libdir}/mythtv/plugins/libmythbrowser.so
%{_datadir}/mythtv/i18n/mythbrowser_*.qm
%{_datadir}/mythtv/themes/default*/browser-ui.xml
%{_datadir}/mythtv/themes/default*/mb_*.png

%files -n mythtv-plugin-gallery
%defattr(-,root,root,-)
%doc mythgallery/README*
%{_libdir}/mythtv/plugins/libmythgallery.so
%{_datadir}/mythtv/i18n/mythgallery_*.qm
%{_datadir}/mythtv/themes/default*/gallery*
%{_localstatedir}/lib/pictures

%files -n mythtv-plugin-game
%defattr(-,root,root,-)
%doc mythgame/romdb*
%{_libdir}/mythtv/plugins/libmythgame.so
%{_datadir}/mythtv/i18n/mythgame_*.qm
%{_datadir}/mythtv/game_settings.xml
%{_datadir}/mythtv/themes/default*/game*
%dir %{_datadir}/mythtv/metadata
%{_datadir}/mythtv/metadata/Game

%files -n mythtv-plugin-music
%defattr(-,root,root,-)
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
%{_datadir}/mythtv/themes/default*/music-ui.xml
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
%defattr(-,root,root,-)
%doc mythnetvision/README mythnetvision/ChangeLog mythnetvision/AUTHORS
%{_bindir}/mythfillnetvision
%{_libdir}/mythtv/plugins/libmythnetvision.so
%{_datadir}/mythtv/i18n/mythnetvision_*.qm
%{_datadir}/mythtv/mythnetvision
%{_datadir}/mythtv/netvisionmenu.xml
%{_datadir}/mythtv/themes/default*/netvision*.xml

%files -n mythtv-plugin-news
%defattr(-,root,root,-)
%doc mythnews/AUTHORS mythnews/COPYING mythnews/ChangeLog mythnews/README*
%{_libdir}/mythtv/plugins/libmythnews.so
%{_datadir}/mythtv/i18n/mythnews_*.qm
%{_datadir}/mythtv/mythnews
%{_datadir}/mythtv/themes/default*/news*
%{_datadir}/mythtv/themes/default/enclosures.png
%{_datadir}/mythtv/themes/default/need-download.png
%{_datadir}/mythtv/themes/default/podcast.png


%files -n mythtv-plugin-weather
%defattr(-,root,root,-)
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
%defattr(-,root,root,-)
%doc mythweb/README* mythweb/LICENSE mythweb/INSTALL mythweb/mythweb.conf.*
%{_var}/www/mythweb
%dir %{_localstatedir}/lib/mythweb
%attr(-,apache,apache) %{_localstatedir}/lib/mythweb/data
%config(noreplace) %{_sysconfdir}/httpd/conf/webapps.d/mythweb.conf

%files -n mythtv-plugin-video
%defattr(-,root,root,-)
%doc mythvideo/README*
%{_libdir}/mythtv/plugins/libmythvideo.so
%{_datadir}/mythtv/video_settings.xml
%{_datadir}/mythtv/videomenu.xml
%{_datadir}/mythtv/i18n/mythvideo_*.qm
%{_datadir}/mythtv/mythvideo/scripts
%{_datadir}/mythtv/themes/default*/mv*.png
%{_datadir}/mythtv/themes/default/md_*.png
%{_datadir}/mythtv/themes/default*/video*.xml
%{_localstatedir}/lib/mythvideo

%files -n mythtv-plugin-zoneminder
%defattr(-,root,root,-)
%doc mythzoneminder/README mythzoneminder/COPYING mythzoneminder/AUTHORS
%{_bindir}/mythzmserver
%{_libdir}/mythtv/plugins/libmythzoneminder.so
%{_datadir}/mythtv/zonemindermenu.xml
%{_datadir}/mythtv/themes/default*/zoneminder*.xml
%{_datadir}/mythtv/themes/default*/mz_*.png
%{_datadir}/mythtv/i18n/mythzoneminder_*.qm

%files -n mythtv-plugin-archive
%defattr(-,root,root)
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
