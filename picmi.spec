Name:		picmi
Version:	4.10.0
Release:	1
Summary:	A nonogram logic game for KDE
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://games.kde.org/game.php?game=picmi
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
Picmi is a number logic game in which cells in a grid have to be colored or
left blank according to numbers given at the side of the grid to reveal a
hidden picture.

%files
%{_kde_bindir}/picmi
%{_kde_applicationsdir}/picmi.desktop
%{_kde_appsdir}/picmi/
%{_kde_iconsdir}/hicolor/*/apps/picmi.*
%{_kde_docdir}/HTML/en/picmi

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build


%changelog
* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New package in KDE 4.10

