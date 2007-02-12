Summary:	Anti-Lamenessing Engine
Summary(pl.UTF-8):	Anti-Lamenessing Engine - silnik poprawiający zdjęcia
Name:		ale
Version:	0.8.4
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://auricle.dyndns.org/ALE/download/%{name}-%{version}.tar.gz
# Source0-md5:	9a9270a8017da2bf8e68cdaf03a5e07c
URL:		http://auricle.dyndns.org/ALE/
BuildRequires:	ImageMagick-devel >= 1:6.2.4.0
BuildRequires:	fftw3-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALE is a free software program that renders high-fidelity images of
real scenes by aligning and combining many similar images from a
camera or scanner.

%description -l pl.UTF-8
ALE to wolnodostępny program tworzący wysokiej jakości obrazy
prawdziwych scen poprzez wyrównywanie i łączenie wielu podobnych
obrazów z aparatu lub skanera.

%prep
%setup -q

%build
%{__make} \
	FFTW=1 \
	IMAGEMAGICK=1 \
	OPT_CFLAGS="%{rpmcflags}" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ale $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/*
