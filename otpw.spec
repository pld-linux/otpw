Summary:	A one-time password login package
Summary(pl):	Pakiet logowania do systemu bazuj±cy na has³ach jednorazowego u¿ytku
Name:		otpw
Version:	1.3
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/System
Source0:	http://www.cl.cam.ac.uk/~mgk25/download/%{name}-%{version}.tar.gz
# Source0-md5:	8e72d23714b29e450aeb50c35be67b55
URL:		http://www.cl.cam.ac.uk/~mgk25/otpw.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	pam-devel

%description
OTPW is a one-time password authentication library and PAM module that
provides a number of advantages over other systems. OTPW uses license-free
RIPEMD-160 hash function to generate keys and keeps key-related information
in user's home directory so it's no-suid.

This package contains binary programs needed by OTPW to work.

%description -l pl
OTPW jest bibliotek± uwierzytelniaj±c± metod± hase³ jednorazowego u¿ytku,
wraz z opcjonalnym modu³em PAM, który pozwala prze¼roczy¶cie jej u¿ywaæ.
OTPW u¿ywa wolnej od ograniczeñ licencyjnych funkcji skrótu RIPEMD-160
do generowania kluczy, a tak¿e przechowuje informacje zwi±zane z kluczem
w katalogu u¿ytkownika, wiêc nie potrzebuje nigdzie ustawionego bitu suid.

Ten pakiet zawiera programy binarne potrzebne do dzia³ania OTWP.

%package examples
Summary:	OTPW - example programs
Summary(pl):	OTPW - programy przyk³adowe
Group:		Development/Libraries
License:	GPL
Requires:	%{name} = %{version}

%description examples
OTPW is a one-time password authentication library and PAM module that
provides a number of advantages over other systems. OTPW uses license-free
RIPEMD-160 hash function to generate keys and keeps key-related information
in user's home directory so it's no-suid.

This package contains example programs, which shows how to integrate
OTPW with own tools.

%description examples -l pl
OTPW jest bibliotek± uwierzytelniaj±c± metod± hase³ jednorazowego u¿ytku,
wraz z opcjonalnym modu³em PAM, który pozwala prze¼roczy¶cie jej u¿ywaæ.
OTPW u¿ywa wolnej od ograniczeñ licencyjnych funkcji skrótu RIPEMD-160
do generowania kluczy, a tak¿e przechowuje informacje zwi±zane z kluczem
w katalogu u¿ytkownika, wiêc nie potrzebuje nigdzie ustawionego bitu suid.

Ten pakiet zawiera przyk³adowe programy pokazuj±ce, jak integrowaæ OTPW
z w³asnymi narzêdziami.

%package -n pam_otpw
Summary:	PAM module for OTPW
Summary(pl):	Modu³ PAM dla OTPW
Group:		Base
License:	GPL
Requires:	%{name} = %{version}

%description -n pam_otpw
OTPW is a one-time password authentication library and PAM module that
provides a number of advantages over other systems. OTPW uses license-free
RIPEMD-160 hash function to generate keys and keeps key-related information
in user's home directory so it's no-suid.

This package contains PAM module for OTPW.

%description -n pam_otpw -l pl
OTPW jest bibliotek± uwierzytelniaj±c± metod± hase³ jednorazowego u¿ytku,
wraz z opcjonalnym modu³em PAM, który pozwala prze¼roczy¶cie jej u¿ywaæ.
OTPW u¿ywa wolnej od ograniczeñ licencyjnych funkcji skrótu RIPEMD-160
do generowania kluczy, a tak¿e przechowuje informacje zwi±zane z kluczem
w katalogu u¿ytkownika, wiêc nie potrzebuje nigdzie ustawionego bitu suid.

Ten pakiet zawiera modu³ PAM dla OTPW.

%prep
%setup -q -n %{name}

%build
%{__make} CFLAGS="%{rpmcflags} -Wall" DESTDIR="$RPM_BUILD_ROOT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/security}
install -d $RPM_BUILD_ROOT%{_mandir}/{man1,man8}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install %{name}-gen	$RPM_BUILD_ROOT%{_bindir}
install pam_%{name}.so	$RPM_BUILD_ROOT%{_libdir}/security
install *%{name}*.1	$RPM_BUILD_ROOT%{_mandir}/man1
install *%{name}*.8	$RPM_BUILD_ROOT%{_mandir}/man8
install demo*		$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES %{name}.html
%attr(0755,root,root) %{_bindir}/%{name}-gen
%{_mandir}/man1/*%{name}*.1*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files -n pam_otpw
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/security/pam_%{name}.so
%{_mandir}/man8/*pam*.8*
