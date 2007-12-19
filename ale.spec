Summary:	Anti-Lamenessing Engine
Summary(pl.UTF-8):	Anti-Lamenessing Engine - silnik poprawiający zdjęcia
Name:		ale
Version:	0.8.11
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://auricle.dyndns.org/ALE/download/%{name}-%{version}.tar.gz
# Source0-md5:	ae852de09b1fcb86696e25df9ab9cb6a
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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS
%attr(755,root,root) %{_bindir}/*
