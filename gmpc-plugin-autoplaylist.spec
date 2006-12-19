%define		source_name gmpc-autoplaylist
Summary:	Autoplaylist plugin for Gnome Music Player Client
Summary(pl):	Wtyczka autoplaylist dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-autoplaylist
Version:	0.1.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
# http://sarine.nl/gmpc-plugins-downloads
Source0:	%{source_name}-%{version}.tar.gz
# Source0-md5:	046ed7e57fac849d3b33a5b37ff7540e
Patch0:		%{name}-plugins_path.patch
URL:		http://sarine.nl/gmpc-plugins-autoplaylist
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmpc-devel
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The plugin allows you to generate a playlist based on a set of rules,
f.e. "Genre contains 'jazz' and artist doesn't contain 'Jones'".

%description -l pl
Ta wtyczka pozwala generowa� playlisty w oparciu o zbi�r regu�, na
przyk�ad "Gatunek zawiera 'jazz' i wykonawca nie zawiera 'Jones'".

%prep
%setup -qn %{source_name}-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/gmpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/*.so
%{_libdir}/gmpc/apl