Summary:	GTK+ libmcal powered calendar
Summary(pl.UTF-8):   Oparty o libmcal kalendarz z interfejsem GTK+
Name:		gmcal
Version:	0.0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/libmcal/%{name}-%{version}.tar.gz
# Source0-md5:	9ed12226ec83512a0fe64af05eafd3d1
URL:		http://mcal.chek.com/
BuildRequires:	gtk+-devel
BuildRequires:	libmcal-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very early release of a GTK+ app that can display you
calendar and appointment either via mstore or ICAP protocol drivers.

%description -l pl.UTF-8
To jest wczesna wersja aplikacji GTK+ potrafiącej wyświetlając
kalendarz i terminy spotkań korzystając z protokołu mstore lub ICAP.

%prep
%setup -q -n %{name}

%build
%{__cc} -I/usr/include/mcal %{rpmcflags} %{rpmldflags} \
	gmcal.c -o gmcal -lmcal -lcrypt `gtk-config --cflags --libs`

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install gmcal $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
