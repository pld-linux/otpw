Summary:	A one-time password login package
Summary(pl.UTF-8):   Pakiet logowania do systemu bazujący na hasłach jednorazowego użytku
Name:		otpw
Version:	1.3
Release:	6
Epoch:		1
License:	GPL
Group:		Applications/System
Source0:	http://www.cl.cam.ac.uk/~mgk25/download/%{name}-%{version}.tar.gz
# Source0-md5:	8e72d23714b29e450aeb50c35be67b55
URL:		http://www.cl.cam.ac.uk/~mgk25/otpw.html
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OTPW is a one-time password authentication library and PAM module that
provides a number of advantages over other systems. OTPW uses patent-free
RIPEMD-160 hash function to generate keys and keeps key-related information
in user's home directory so it's no-suid.

This package contains binary programs needed by OTPW to work.

%description -l pl.UTF-8
OTPW jest biblioteką uwierzytelniającą metodą haseł jednorazowego użytku,
wraz z opcjonalnym modułem PAM, który pozwala przezroczyście jej używać.
OTPW używa wolnej od ograniczeń licencyjnych funkcji skrótu RIPEMD-160
do generowania kluczy, a także przechowuje informacje związane z kluczem
w katalogu użytkownika, więc nie potrzebuje nigdzie ustawionego bitu suid.

Ten pakiet zawiera programy binarne potrzebne do działania OTPW.

%package examples
Summary:	OTPW - example programs
Summary(pl.UTF-8):   OTPW - programy przykładowe
Group:		Development/Libraries
License:	GPL
Requires:	%{name} = %{epoch}:%{version}

%description examples
OTPW is a one-time password authentication library and PAM module that
provides a number of advantages over other systems. OTPW uses patent-free
RIPEMD-160 hash function to generate keys and keeps key-related information
in user's home directory so it's no-suid.

This package contains example programs, which shows how to integrate
OTPW with own tools.

%description examples -l pl.UTF-8
OTPW jest biblioteką uwierzytelniającą metodą haseł jednorazowego użytku,
wraz z opcjonalnym modułem PAM, który pozwala przezroczyście jej używać.
OTPW używa wolnej od ograniczeń licencyjnych funkcji skrótu RIPEMD-160
do generowania kluczy, a także przechowuje informacje związane z kluczem
w katalogu użytkownika, więc nie potrzebuje nigdzie ustawionego bitu suid.

Ten pakiet zawiera przykładowe programy pokazujące, jak integrować OTPW
z własnymi narzędziami.

%package -n pam-pam_otpw
Summary:	PAM module for OTPW
Summary(pl.UTF-8):   Moduł PAM dla OTPW
Group:		Base
License:	GPL
Requires:	%{name} = %{epoch}:%{version}
Obsoletes:	pam_otpw

%description -n pam-pam_otpw
OTPW is a one-time password authentication library and PAM module that
provides a number of advantages over other systems. OTPW uses patent-free
RIPEMD-160 hash function to generate keys and keeps key-related information
in user's home directory so it's no-suid.

This package contains PAM module for OTPW.

%description -n pam-pam_otpw -l pl.UTF-8
OTPW jest biblioteką uwierzytelniającą metodą haseł jednorazowego użytku,
wraz z opcjonalnym modułem PAM, który pozwala przezroczyście jej używać.
OTPW używa wolnej od ograniczeń licencyjnych funkcji skrótu RIPEMD-160
do generowania kluczy, a także przechowuje informacje związane z kluczem
w katalogu użytkownika, więc nie potrzebuje nigdzie ustawionego bitu suid.

Ten pakiet zawiera moduł PAM dla OTPW.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/%{_lib}/security}
install -d $RPM_BUILD_ROOT%{_mandir}/{man1,man8}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install %{name}-gen	$RPM_BUILD_ROOT%{_bindir}
install pam_%{name}.so	$RPM_BUILD_ROOT/%{_lib}/security
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

%files -n pam-pam_otpw
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/security/pam_%{name}.so
%{_mandir}/man8/*pam*.8*
