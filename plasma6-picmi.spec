#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		plasma6-picmi
Version:	25.04.0
Release:	%{?git:0.%{git}.}1
Summary:	A nonogram logic game for KDE
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		https://games.kde.org/game.php?game=picmi
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/picmi/-/archive/%{gitbranch}/picmi-%{gitbranchd}.tar.bz2#/picmi-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/picmi-%{version}.tar.xz
%endif
BuildRequires: 	cmake(KDEGames6)
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Test)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:  cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6CoreAddons)

%description
Picmi is a number logic game in which cells in a grid have to be colored or
left blank according to numbers given at the side of the grid to reveal a
hidden picture.

%files -f picmi.lang
%{_bindir}/picmi
%{_datadir}/applications/org.kde.picmi.desktop
%{_datadir}/picmi
%{_datadir}/metainfo/org.kde.picmi.appdata.xml
%{_iconsdir}/hicolor/*/apps/picmi.*
%{_datadir}/qlogging-categories6/picmi.renamecategories
%{_datadir}/qlogging-categories6/picmi.categories
#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n picmi-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang picmi --with-html
