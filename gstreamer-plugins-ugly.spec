# not built: a52dec, sid, twolame

%define		gstname		gst-plugins-ugly
%define		gst_major_ver	1.0
%define		gst_req_ver	1.4.5

Summary:	Ugly GStreamer Streaming-media framework plugins
Name:		gstreamer-plugins-ugly
Version:	1.4.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-ugly/%{gstname}-%{version}.tar.xz
# Source0-md5:	6954beed7bb9a93e426dee543ff46393
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gst_req_ver}
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	orc-devel >= 0.4.5
BuildRequires:	pkg-config
#
BuildRequires:	lame-libs-devel
BuildRequires:	libcdio-paranoia-devel
BuildRequires:	libdvdnav-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmpeg2-devel
BuildRequires:	libx264-devel
BuildRequires:	opencore-amr-devel
Requires:	gstreamer >= %{gst_req_ver}
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{gst_major_ver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%package apidocs
Summary:	gstreamer-plugins-ugly API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gstreamer-plugins-ugly API documentation.

%prep
%setup -qn %{gstname}-%{version}

%build
%{__autopoint}
patch -p0 < common/gettext.patch
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules		\
	--disable-static		\
	--with-html-dir=%{_gtkdocdir}	\
	--with-package-name="GStreamer (Freddix)"   \
	--with-package-origin="http://freddix.org/"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{gstlibdir}/*.la

%find_lang gst-plugins-ugly-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gst-plugins-ugly-1.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{gstlibdir}/libgstamrnb.so
%attr(755,root,root) %{gstlibdir}/libgstamrwbdec.so
%attr(755,root,root) %{gstlibdir}/libgstasf.so
%attr(755,root,root) %{gstlibdir}/libgstcdio.so
%attr(755,root,root) %{gstlibdir}/libgstdvdlpcmdec.so
%attr(755,root,root) %{gstlibdir}/libgstdvdread.so
%attr(755,root,root) %{gstlibdir}/libgstdvdsub.so
%attr(755,root,root) %{gstlibdir}/libgstlame.so
%attr(755,root,root) %{gstlibdir}/libgstmad.so
%attr(755,root,root) %{gstlibdir}/libgstmpeg2dec.so
%attr(755,root,root) %{gstlibdir}/libgstrmdemux.so
%attr(755,root,root) %{gstlibdir}/libgstx264.so
%attr(755,root,root) %{gstlibdir}/libgstxingmux.so

%{_datadir}/gstreamer-1.0/presets/GstAmrnbEnc.prs
%{_datadir}/gstreamer-1.0/presets/GstX264Enc.prs

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gst-plugins-ugly-plugins-*

