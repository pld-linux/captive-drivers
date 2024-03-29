# the drivers that were supposed to work, didn't.
# so these drivers didn't work for me.
#
# Conditional build:
%bcond_with	license_agreement	# generates package
%define		source_url      http://download.microsoft.com/download/9/7/6/9763833d-bd58-41e2-9911-50f64c7252a3/
#
Summary:	NTFS Drivers
Summary(pl.UTF-8):	Sterowniki NTFS
%define		base_name	captive-drivers
%if %{with license_agreement}
Name:		%{base_name}
%else
Name:		%{base_name}-installer
%endif
Version:	0.2
%define		_rel	2
Release:	%{_rel}%{?with_license_agreement:wla}
Group:		Libraries
License:	restricted, non-distributable
%if %{with license_agreement}
# NB! This is 145M download.
Source0:	%{source_url}xpsp1a_en_x86_CHK.exe
# Source0-md5:	329c25f457fea66ec502b7ef70cb9ede
BuildRequires:	cabextract
Requires:	captive
%else
Source0:	http://svn.pld-linux.org/svn/license-installer/license-installer.sh
# Source0-md5:	329c25f457fea66ec502b7ef70cb9ede
Requires:	rpm-build-tools >= 4.4.37
Requires:	rpmbuild(macros) >= 1.544
Provides:	%{base_name}
%endif
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Contains ntfs.sys and ntoskrnl.exe from Windows XP SP1.
%if !%{with license_agreement}
License issues made us not to include inherent files into this package
by default. If you want to create full working package please build it
with the following command:

%{base_name}.install --with license_agreement %{_datadir}/%{base_name}/%{base_name}.spec
%endif

%description -l pl.UTF-8
Pakiet zawierający ntfs.sys i ntoskrnl.exe z Windows XP SP1.
%if !%{with license_agreement}
Kwestie licencji zmusiły nas do niedołączania do tego pakietu istotnych
plików. Jeśli chcesz stworzyć w pełni funkcjonalny pakiet, zbuduj go za
pomocą polecenia:

%{base_name}.install --with license_agreement %{_datadir}/%{base_name}/%{base_name}.spec
%endif

%prep
%setup -q -c -T
%if %{with license_agreement}
cabextract %{SOURCE0} -F ntfs.sys
cabextract %{SOURCE0} -F ntoskrnl.ex_
cabextract ntoskrnl.ex_
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if !%{with license_agreement}
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{base_name}}

sed -e '
	s/@BASE_NAME@/%{base_name}/g
	s/@TARGET_CPU@/%{_target_cpu}/g
	s-@VERSION@-%{version}-g
	s-@RELEASE@-%{release}-g
	s,@SPECFILE@,%{_datadir}/%{base_name}/%{base_name}.spec,g
	s,@DATADIR@,%{_datadir}/%{base_name},g
' %{SOURCE0} > $RPM_BUILD_ROOT%{_bindir}/%{base_name}.install

install %{_specdir}/%{base_name}.spec $RPM_BUILD_ROOT%{_datadir}/%{base_name}
%else
install -d $RPM_BUILD_ROOT/var/lib/captive
install ntfs.sys ntoskrnl.exe $RPM_BUILD_ROOT/var/lib/captive
%endif

%if !%{with license_agreement}
%post
%{_bindir}/%{base_name}.install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%if %{with license_agreement}
/var/lib/captive/*
%else
%attr(755,root,root) %{_bindir}/%{base_name}.install
%{_datadir}/%{base_name}
%endif
