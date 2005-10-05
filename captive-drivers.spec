# the drivers that were supposed to work. didn't.
# so these drivers didn't work for me.
Summary:	NTFS Drivers
Name:		captive-drivers
Version:	0.1
Release:	0.1
License:	restricted, non-distributable
Group:		Applications/System
Source0:	http://download.microsoft.com/download/9/7/6/9763833d-bd58-41e2-9911-50f64c7252a3/xpsp1a_en_x86_CHK.exe
# NoSource0-md5:	52ea53ae2cf93247ca07c0cf257367b6
NoSource:	0
BuildRequires:	rpm-utils
BuildRequires:	unzip
BuildRequires:	mawk
BuildRequires:	cdrtools-utils
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Contains ntfs.sys and ntoskrnl.exe from XP SP1.

%prep
%setup -q -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/lib/captive

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/var/lib/captive/*
