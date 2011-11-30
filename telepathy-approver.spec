%define git git20110807

Summary:	KDE Channel Approver for Telepathy
Name:		telepathy-approver
Version:	0.1
Release:	%mkrel -c %{git} 1
Url:		https://projects.kde.org/projects/playground/network/telepathy/telepathy-approver
Source0:	telepathy-approver-%git.tar.bz2
License:	GPLv2+
Group:		Graphical desktop/KDE
BuildRequires:	kdelibs4-devel
BuildRequires:	telepathy-qt4-devel

%description
KDE Channel Approver for Telepathy.

%files
%{_kde_libdir}/kde4/kded_telepathy_kde_approver.so
%{_kde_configdir}/telepathy_kde_approverrc
%{_kde_services}/kded/telepathy_kde_approver.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}

%makeinstall_std -C build



